# -*- coding: utf-8 -*-

"""
yaspin.yaspin
~~~~~~~~~~~~~

A lightweight terminal spinner.
"""

from __future__ import absolute_import

import functools
import itertools
import sys
import threading
import time

from .base_spinner import default_spinner
from .compat import PY2, basestring, builtin_str, bytes, str
from .constants import ENCODING
from .helpers import to_unicode
from .termcolor import colored


class Yaspin(object):
    """Implements a context manager that spawns a thread
    to write spinner frames into a tty (stdout) during
    context execution.
    """

    # When Python finds its output attached to a terminal,
    # it sets the sys.stdout.encoding attribute to the terminal's encoding.
    # The print statement's handler will automatically encode unicode
    # arguments into bytes.
    #
    # In Py2 when piping or redirecting output, Python does not detect
    # the desired character set of the output, it sets sys.stdout.encoding
    # to None, and print will invoke the default "ascii" codec.
    #
    # Py3 invokes "UTF-8" codec by default.
    #
    # Thats why in Py2, output should be encoded manually with desired
    # encoding in order to support pipes and redirects.

    def __init__(self, spinner=None, text='',
                 color=None, right=False, reverse=False):
        self._spinner = self._set_spinner(spinner)
        self._frames = self._set_frames(self._spinner, reverse)
        self._interval = self._set_interval(self._spinner)
        self._cycle = self._set_cycle(self._frames)
        self._text = self._set_text(text)
        self._color = self._set_color(color) if color else color

        self._right = right
        self._reverse = reverse

        self._stop_spin = None
        self._hide_spin = None
        self._spin_thread = None
        self._last_frame = None

    #
    # Dunders
    #
    def __repr__(self):
        repr_ = u'<Yaspin frames={0!s}>'.format(self._frames)
        if PY2:
            return repr_.encode(ENCODING)
        return repr_

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        # Avoid stop() execution for the 2nd time
        if self._spin_thread.is_alive():
            self.stop()
        return False  # nothing is handled

    def __call__(self, fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            with self:
                return fn(*args, **kwargs)
        return inner

    #
    # Properties
    #
    @property
    def spinner(self):
        return self._spinner

    @spinner.setter
    def spinner(self, sp):
        self._spinner = self._set_spinner(sp)
        self._frames = self._set_frames(self._spinner, self._reverse)
        self._interval = self._set_interval(self._spinner)
        self._cycle = self._set_cycle(self._frames)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, txt):
        self._text = self._set_text(txt)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = self._set_color(value) if value else value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value

    @property
    def reverse(self):
        return self._reverse

    @reverse.setter
    def reverse(self, value):
        self._reverse = value
        self._frames = self._set_frames(self._spinner, self._reverse)
        self._cycle = self._set_cycle(self._frames)

    #
    # Public
    #
    def start(self):
        if sys.stdout.isatty():
            self._hide_cursor()

        self._stop_spin = threading.Event()
        self._hide_spin = threading.Event()
        self._spin_thread = threading.Thread(target=self._spin)
        self._spin_thread.start()

    def stop(self):
        if self._spin_thread:
            self._stop_spin.set()
            self._spin_thread.join()

        sys.stdout.write("\r")
        self._clear_line()

        if sys.stdout.isatty():
            self._show_cursor()

    def hide(self):
        """Hide the spinner to allow for custom writing to the terminal."""
        thr_is_alive = self._spin_thread and self._spin_thread.is_alive()

        if thr_is_alive and not self._hide_spin.is_set():
            # set the hidden spinner flag
            self._hide_spin.set()

            # clear the current line
            sys.stdout.write("\r")
            self._clear_line()

            # flush the stdout buffer so the current line can be rewritten to
            sys.stdout.flush()

    def show(self):
        """Show the hidden spinner."""
        thr_is_alive = self._spin_thread and self._spin_thread.is_alive()

        if thr_is_alive and self._hide_spin.is_set():
            # clear the hidden spinner flag
            self._hide_spin.clear()

            # clear the current line so the spinner is not appended to it
            sys.stdout.write("\r")
            self._clear_line()

    def write(self, text):
        """Write text in the terminal without breaking the spinner."""
        # similar to tqdm.write()
        # https://pypi.python.org/pypi/tqdm#writing-messages
        sys.stdout.write("\r")
        self._clear_line()

        _text = to_unicode(text)
        if PY2:
            _text = _text.encode(ENCODING)

        # Ensure output is bytes for Py2 and Unicode for Py3
        assert isinstance(_text, builtin_str)

        sys.stdout.write("{0}\n".format(_text))

    def ok(self, text="OK"):
        """Set Ok (success) finalizer to a spinner."""
        _text = text if text else "OK"
        self._freeze(_text)

    def fail(self, text="FAIL"):
        """Set fail finalizer to a spinner."""
        _text = text if text else "FAIL"
        self._freeze(_text)

    #
    # Protected
    #
    def _freeze(self, final_text):
        """Stop spinner, compose last frame and 'freeze' it."""
        text = to_unicode(final_text).strip()
        self._last_frame = self._compose_out(text, mode="last")

        # Should be stopped here, otherwise prints after
        # self._freeze call will mess up the spinner
        self.stop()
        sys.stdout.write(self._last_frame)

    def _spin(self):
        while not self._stop_spin.is_set():

            if self._hide_spin.is_set():
                # Wait a bit to avoid wasting cycles
                time.sleep(self._interval)
                continue

            # Compose output
            spin_phase = next(self._cycle)
            out = self._compose_out(spin_phase)

            # Write
            sys.stdout.write(out)
            self._clear_line()
            sys.stdout.flush()

            # Wait
            time.sleep(self._interval)
            sys.stdout.write('\b')

    def _compose_out(self, frame, mode=None):
        # Ensure Unicode input
        assert isinstance(frame, str)
        assert isinstance(self._text, str)

        frame = frame.encode(ENCODING) if PY2 else frame
        text = self._text.encode(ENCODING) if PY2 else self._text

        if self._color and callable(self._color):
            color_fn = self._color
            frame = color_fn(frame)
        if self._color and not callable(self._color):
            frame = colored(frame, self._color)

        if self._right:
            frame, text = text, frame

        if not mode:
            out = "\r{0} {1}".format(frame, text)
        else:
            out = "{0} {1}\n".format(frame, text)

        # Ensure output is bytes for Py2 and Unicode for Py3
        assert isinstance(out, builtin_str)

        return out

    #
    # Static
    #
    @staticmethod
    def _set_spinner(spinner):
        if not spinner:
            sp = default_spinner

        if hasattr(spinner, "frames") and hasattr(spinner, "interval"):
            if not spinner.frames or not spinner.interval:
                sp = default_spinner
            else:
                sp = spinner
        else:
            sp = default_spinner

        return sp

    @staticmethod
    def _set_frames(spinner, reverse):
        # type: (base_spinner.Spinner, bool) -> Union[str, List]
        uframes = None      # unicode frames
        uframes_seq = None  # sequence of unicode frames

        if isinstance(spinner.frames, basestring):
            uframes = to_unicode(spinner.frames) if PY2 else spinner.frames

        # TODO (pavdmyt): support any type that implements iterable
        if isinstance(spinner.frames, (list, tuple)):

            # Empty spinner.frames is handled by Yaspin._set_spinner
            if spinner.frames and isinstance(spinner.frames[0], bytes):
                uframes_seq = [to_unicode(frame) for frame in spinner.frames]
            else:
                uframes_seq = spinner.frames

        _frames = uframes or uframes_seq
        if not _frames:
            raise ValueError(
                "{0!r}: no frames found in spinner".format(spinner)
            )

        # Builtin reversed returns reverse iterator,
        # which adds unnecessary difficulty for returning
        # unicode value;
        # Hence using [::-1] syntax
        frames = _frames[::-1] if reverse else _frames

        return frames

    @staticmethod
    def _set_interval(spinner):
        # Milliseconds to Seconds
        return spinner.interval * 0.001

    @staticmethod
    def _set_cycle(frames):
        return itertools.cycle(frames)

    @staticmethod
    def _set_text(text):
        if PY2:
            return to_unicode(text)
        return text

    @staticmethod
    def _set_color(color):

        if callable(color):
            return color

        available_text_colors = (
            "red", "green", "yellow", "blue", "magenta", "cyan", "white",
        )

        c_lower = color.lower()

        if c_lower not in available_text_colors:
            raise ValueError(
                "{0}: unsupported text color. Use one of the: {1}"
                .format(c_lower, available_text_colors)
            )

        return c_lower

    @staticmethod
    def _hide_cursor():
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    @staticmethod
    def _show_cursor():
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

    @staticmethod
    def _clear_line():
        sys.stdout.write("\033[K")


def yaspin(spinner=None, text='', color=None, right=False, reverse=False):
    """Display spinner in stdout.

    Can be used as a context manager or as a function decorator.

    Arguments:
        spinner (yaspin.Spinner, optional): Spinner to use.
        text (str, optional): Text to show along with spinner.
        color (str, callable, optional): Color or color style of the spinner.
        right (bool, optional): Place spinner to the right end
            of the text string.
        reverse (bool, optional): Reverse spin direction.

    Returns:
        yaspin.Yaspin: instance of the Yaspin class.

    Raises:
        ValueError: If unsupported `color` is specified.

    Example::

        # Use as a context manager
        with yaspin():
            some_operations()

        # Context manager with text
        with yaspin(text="Processing..."):
            some_operations()

        # Context manager with custom sequence
        with yaspin(Spinner('-\\|/', 150)):
            some_operations()

        # As decorator
        @yaspin(text="Loading...")
        def foo():
            time.sleep(5)

        foo()

    """
    return Yaspin(
        spinner=spinner,
        text=text,
        color=color,
        right=right,
        reverse=reverse,
    )

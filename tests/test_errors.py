"""Test file for errors.py file of debsutil module."""
import pytest

import debsutil.errors as ET
from debsutil.errors import errorExit
from debsutil.errors import errorNotify
from debsutil.errors import errorRaise


class TheException(Exception):
    """A test Exception.

    Args:
        Exception:
    """

    pass


def test_formatter():
    """Arguments are concatenated."""
    fname = "test_formatter"
    msg = "This is the test exception."
    e = TheException(msg)
    expect = f"Error in {fname}: Exception: TheException: {msg}\n"
    got = ET.formatMsg(fname, e)
    assert got == expect


def test_raises():
    """It raises TheException Exception."""
    fname = "test_raises"
    msg = "This is the test exception."
    with pytest.raises(TheException):
        errorRaise(fname, TheException(msg))


def test_notify(capsys):
    """It writes the error to stderr.

    Args:
        capsys: pytest system handles capturing
    """
    fname = "test_notify"
    msg = "This is the test exception"
    e = TheException(msg)
    errorNotify(fname, e)
    captured = capsys.readouterr()
    assert captured.err == f"Error in {fname}: Exception: TheException: {msg}\n"


def test_exits():
    """It attempts sys.exit."""
    fname = "test_notify"
    msg = "This is the test exception"
    e = TheException(msg)
    with pytest.raises(SystemExit):
        errorExit(fname, e, 1)

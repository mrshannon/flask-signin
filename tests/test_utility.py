import pytest
from flask_signin.utility import true_function, false_function


def test_true_function():
    assert true_function()


def test_false_function():
    assert not false_function()

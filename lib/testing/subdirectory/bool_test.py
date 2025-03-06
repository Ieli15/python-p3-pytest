#!/usr/bin/env python3

from bool_functions import return_true

def test_return_true():
    """Test that return_true() returns True."""
    assert return_true() is True  # Using `is True` is more explicit.

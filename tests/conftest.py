"""Shared pytest fixtures available to all test modules."""

import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    """Return a fresh Calculator instance for each test."""
    return Calculator()

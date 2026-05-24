"""Tests for Calculator.add and Calculator.subtract.

How to run
----------
# All tests
pytest tests/ -v

# One operation only
pytest tests/ -v -k "add"
pytest tests/ -v -k "subtract"

# With coverage report
pytest tests/ -v --cov=calculator
"""

import pytest


# ── Add ───────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("a, b, expected", [
    (2,         3,         5),    # two positives
    (-4,        -6,        -10),  # two negatives
    (-1,        1,         0),    # cancels to zero
    (7,         0,         7),    # identity: add zero
    (0,         0,         0),    # both zero
    (1_000_000, 2_000_000, 3_000_000),  # large numbers
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


def test_add_floats(calc):
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)


# ── Subtract ──────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("a, b, expected", [
    (10, 4,  6),   # two positives
    (3,  10, -7),  # result goes negative
    (-5, -3, -2),  # both negative
    (9,  0,  9),   # identity: subtract zero
    (0,  5,  -5),  # zero minus positive
    (8,  8,  0),   # same numbers cancel
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


def test_subtract_floats(calc):
    assert calc.subtract(0.5, 0.2) == pytest.approx(0.3)

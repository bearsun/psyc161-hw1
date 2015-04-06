"""
Module for estimation of factorial (Homework #1)

This module includes a function for estimation of factorial
and another function for testing.

Arithmetic
----------
- 'factorial_recursive' -- calculate the factorial

Misc Functions
----------
- 'test_factorial' -- test the factorial_recursive function

"""

from nose.tools import assert_equal


def factorial_recursive(n):
    """
    Estimate factorial

    Parameters
    ----------
    n: positive integer

    Returns
    ----------
    product: positive integer
        The factorial
    """
    assert n > 0
    assert type(n) == int or type(n) == long

    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)


def test_factorial():
    """
    Test for factorial_recursive for nosetest
    """
    assert_equal(factorial_recursive(1), 1)
    assert_equal(factorial_recursive(2), 2)
    assert_equal(factorial_recursive(3), 6)
    assert_equal(factorial_recursive(4), 24)
    assert_equal(factorial_recursive(5), 120)


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    nconditions = long(raw_input("Please enter number of conditions: "))
    norders = factorial_recursive(nconditions)
    print("Number of possible trial orders: " + str(norders))

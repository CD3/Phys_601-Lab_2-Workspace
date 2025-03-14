import pytest

import Phys601.math


def simpsons_integral_1(f, xmin, xmax, N):
    # Each "step" in simpsons rule
    # includes two intervals
    #
    # ( h / 3 )* (f1 + 4*f2 + f3)
    #
    # The "left" interval goes from f1 -> f2,
    # the "right" inerval goes from f2 -> f3.
    # |    _______
    # |   /  |   |\
    # |  /   |   | \        /
    # |  | L | R |  \______/
    # |  |   |   |
    # +--------------------------
    #
    #
    # So if we want to evaluate the integral using
    # N intervals, it will take N/2 loop iterations
    # AND, we must have an even number of intervals...
    if N % 2 != 0:
        raise RuntimeError(
            f"simpsons rule requires an even number of intervals, {N} was given"
        )
    I = 0
    h = (xmax - xmin) / N  # h is used in the textbook
    i = 0  # we are going to manually increment loop var
    while i < N:
        x = xmin + i * h
        f1 = f(x)
        f2 = f(x + h)
        f3 = f(x + 2 * h)
        I += (h / 3) * (f1 + 4 * f2 + f3)

        i += 2

    return I


def func_to_integrate(x):
    return Phys601.math.exp(-0.3)







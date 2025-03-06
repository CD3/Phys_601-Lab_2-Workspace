import example_1
import pytest



def test_riemann():
    def f(x):
        return 2*x + 3

    def If(x):
        return x**2 + 3*x


    I = example_1.riemann_integral(f, 0, 2, 10)
    assert I == pytest.approx( If(2) - If(0), rel=0.05) # 5% error

    I = example_1.riemann_integral(f, 2, 4, 10)
    assert I == pytest.approx( If(4) - If(2), rel=0.05)


def test_trapezoid():
    def f(x):
        return 2*x + 3

    def If(x):
        return x**2 + 3*x


    I = example_1.trapezoid_integral_1(f, 0, 2, 10)
    assert I == pytest.approx( If(2) - If(0), rel=0.01) # 1% error

    I = example_1.trapezoid_integral_1(f, 2, 4, 10)
    assert I == pytest.approx( If(4) - If(2), rel=0.01)


    I = example_1.trapezoid_integral_2(f, 0, 2, 10)
    assert I == pytest.approx( If(2) - If(0), rel=0.01) # 1% error

    I = example_1.trapezoid_integral_2(f, 2, 4, 10)
    assert I == pytest.approx( If(4) - If(2), rel=0.01)

def test_simpsons():
    def f(x):
        return 2*x + 3

    def If(x):
        return x**2 + 3*x


    I = example_1.simpsons_integral_1(f, 0, 2, 10)
    assert I == pytest.approx( If(2) - If(0), rel=0.01) # 1% error

    I = example_1.simpsons_integral_1(f, 2, 4, 10)
    assert I == pytest.approx( If(4) - If(2), rel=0.01)



import math as m
import pint
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

def planks_law(a_wavelength, a_temperature):
    h = 6.626e-34  # J s
    c = 3e8  # m/s
    k = 1.380649e-23 # J / K
    pi = 3.14159
    l = a_wavelength
    T = a_temperature

    Term1 = 8 * pi * h * c**2 / a_wavelength**5
    Term2 = 1 / (m.exp(h * c / k / T / a_wavelength) - 1)

    return Term1 * Term2

def planks_law_with_units(a_wavelength, a_temperature):
    h = Q_(6.626e-34,'J s')
    c = Q_(3e8,'m/s')
    k = Q_(1.380649e-23,'J / K')
    pi = 3.14159
    l = a_wavelength.to("m")
    T = a_temperature.to("K")

    Term1 = 8 * pi * h * c**2 / a_wavelength**5
    Term2 = 1 / (m.exp(h * c / k / T / a_wavelength) - 1)

    return (Term1 * Term2).to("W/m**2/sr/m")


# time how long it takes these two functions. Is one faster than the other?
B1 = planks_law(532e-9, 310.9)
B2 = planks_law_with_units( Q_(532,'nm'), Q_(100,'degF'))


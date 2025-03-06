import Phys601.math as m


def planks_law(a_wavelength, a_temperature):
    h = 6.626e-34  # J s
    c = 3e8  # m/s
    k = 1.380649e-23 # J / k
    pi = 3.14159
    l = a_wavelength
    T = a_temperature

    Term1 = 8 * pi * h * c / a_wavelength**5
    Term2 = 1 / (m.exp(h * c / k / T / a_wavelength) - 1)

    return Term1 * Term2


print(planks_law(532e-9, 3000))


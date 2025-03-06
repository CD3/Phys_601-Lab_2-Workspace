import Phys601.math as m


def sin_squared_1(x):
    return m.sin(x) * m.sin(x)


def sin_squared_1(x):
    return m.sin(x) ** 2


N = 10
xmin = 0
xmax = 5
dx = (xmax - xmin) / N
integral = 0
for i in range(N):
    x = xmin + i * dx
    f = m.math.sin(x) * m.math.sin(x) + m.math.cos(x) * m.math.cos(x)
    integral += f * dx

print("I:", integral)



def binary_search(function, value, min_x, max_x):
    if function(x_min) < value and function(x_max) < value:
        raise RuntimeError("Function evaluated to ")

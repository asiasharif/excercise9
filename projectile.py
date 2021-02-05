from math import pi, tan, cos
y0 = 1
x = 0.5
θ = 80 * (pi / 180)
v0 = 44
g = 9.81**2

y = y0 + x * tan(0) - (g * x**2) / 2 * (v0 * cos(θ)) **2

print(y) #worked, declared variables, compied maths equation on exercise
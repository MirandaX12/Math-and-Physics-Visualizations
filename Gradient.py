import numpy as np
import sympy as sp #defines symbolic objects, allows user to enter functions
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x, y = sp.symbols('x y') #sets symbolic variables

f = sp.sympify(input("Input f(x,y) (use ** for ^): ",)) #user input is turned into function

x_min_input = input("x min (enter to skip): ",) #user input of xy min/max values
x_max_input = input("x max (enter to skip): ",)
y_min_input = input("y min (enter to skip): ",)
y_max_input = input("y max (enter to skip): ",)

ranges = [x_min_input, x_max_input, y_min_input, y_max_input]

for i in range(len(ranges)): #if user skipped, use default values (-20,20)
    if not ranges[i]:
        if i % 2 == 0:
            ranges[i] = -20
        else:
            ranges[i] = 20
    else:
        ranges[i] = int(ranges[i])

x_partial = sp.diff(f, x) #partial derivatives
y_partial = sp.diff(f, y)

f_num = sp.lambdify((x, y), f, 'numpy') #inputs f(x, y) with symbolic variables into numpy
fx_partial = sp.lambdify((x, y), x_partial, 'numpy') #partial derivatives to numpy
fy_partial = sp.lambdify((x, y), y_partial, 'numpy')

x = np.linspace(ranges[0],ranges[1],25) #array of evenly spaced numbers
y = np.linspace(ranges[2],ranges[3],25)
X, Y = np.meshgrid(x,y) #tuple
Z = f_num(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

x_comp = fx_partial(X, Y) #xy component of gradient vector
y_comp = fy_partial(X, Y)
vec_mag = np.sqrt(x_comp**2 + y_comp**2)
max_mag = np.max(vec_mag) #finds max grad vector magnitude to scale the field

ax.quiver(X, Y, 0, x_comp/max_mag*2, y_comp/max_mag*2, 0) #plots all gradient vectors

ax.set_xlabel('X') #labels axes
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Surface Plot and Gradient')

plt.show()
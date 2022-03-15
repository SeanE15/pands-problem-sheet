# This is a program that will plot f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Sean Elliott 

import numpy as np
import matplotlib.pyplot as plt

f = np.array([0,0])
g = np.array([1,1])
h = np.array([2,4])

plt.plot(f, g, h) 
plt.savefig("lecture1.png")
plt.show() 

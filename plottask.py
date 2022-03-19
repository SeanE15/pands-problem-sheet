# This is a program that will plot f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Sean Elliott 

import numpy as np
import matplotlib.pyplot as plt

# we start the program by importing numpy and matplotlib to the program so that they can be used to create the plot.

points = np.array(range (0,4))

# we then use numpy arrange the range within which the points thta we plot will fall into.
# The below equations are the 3 designated values that we will plot.

fpoints = points
# is our starting value as set out by the instructions for the program.
gpoints = points * points 
# in order to plot the second value we must get the answer for x squared. in order to get x squared - we multiply the original range by itsself.               
hpoints = points * points * points
# as with x squared - x cubed must be multiplied by itsself 3 times. This gives us our thrid and final value.

plt.plot(fpoints, label = "F(x) = x") 
plt.plot(gpoints, label = "G(x) = x2")
plt.plot(hpoints, label = "H(x) = x3")
# In order to make the plot look more presentable I have added the labels for each point - f,g and h above. This will also feed information to the legend. Each label also has a description
# of what value is being plotted.

plt.title("Plot Task")
# This line is the 'Title' of the program. 

plt.xlabel("X Axis") 
plt.ylabel("Y Axis")  
# The two lines above clearly label each axes - X and Y.  
                  
plt.legend()
# This will allow Matplotlib to print the legend - further clarifying which point is which - f,g and h.

plt.show()
# we run this finally to show the end product.



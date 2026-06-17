import numpy as np # import numpy
import matplotlib.pyplot as plt

def f(x, y):
    return -y + x + 1 #  Define the equation to use to calculate the slope

x0 = 0
y0 = 1

h = 0.1
xf = 4 # Declare the intial variables for X and y, the step size and final one for X

x = np.arange(x0, xf + h, h) # create an array for the range of values to be used for x i.e
# (start, stop, step)
y = np.zeros(len(x)) # create another array of zeros whose length is the same as the number of elements in x

y_heun = np.zeros(len(x))

y[0] = y0 # change the value of the initial Y (y0) to the given value
y_heun[0] = y0

for i in range(len(x)-1):
    y[i+1] = y[i] +  h*f(x[i],y[i]) # loop through the eulers formular using a range of the length of array x - 1


#print
print("x\t y")
print("-----------")

for i in range(len(x)):
    #euler
    print(f"{x[i]:.1f}\t{y[i]:.4f}")


    #Heun
for i in range(len(x) - 1):
    # predictor
    y_pred = y_heun[i] + h * f(x[i], y_heun[i])

    # corrector
    y_heun[i + 1] = y_heun[i] + (h / 2) * (
        f(x[i], y_heun[i]) + f(x[i + 1], y_pred)
    )


plt.plot(x, y)
plt.plot(x, y_heun)
plt.xlabel("Step sizes")
plt.ylabel("Euler and Heun steps")
plt.title("Graph of Euler and Heun methods")
plt.show()


")

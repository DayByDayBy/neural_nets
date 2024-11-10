import numpy as np
import matplotlib.pyplot as plt

def f1(x, n):
    return (x - n)**x

def f2(x, n):
    return (n - x)**n

def f3(x, n):
    return (x - n)**n

def f4(x, n):
    return (n - x)**x

n = 5
x_vals = np.linspace(-100, 100, 500)

y1_vals = f1(x_vals, n)
y2_vals = f2(x_vals, n)
y3_vals = f3(x_vals, n)
y4_vals = f4(x_vals, n)

plt.figure(figsize=(10, 10))
plt.plot(x_vals, y1_vals, label=r'$(x-n)^x$', color='blue')
plt.plot(x_vals, y2_vals, label=r'$(n-x)^n$', color='green')
plt.plot(x_vals, y3_vals, label=r'$(x-n)^n$', color='red')
plt.plot(x_vals, y4_vals, label=r'$(n-x)^x$', color='orange')

plt.title(r"Graphs of $(x-n)^x$, $(n-x)^n$, $(x-n)^n$, $(n-x)^x$ for n = {}".format(n))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.ylim(-200, 200)
plt.xlim(-20, 20)

plt.show()




# euelers

import numpy as np
import matplotlib.pyplot as plt
import math

# factorial function
def factorial(n):
    return np.math.factorial(n)

# partial sums for the series expansion of e
def partial_sums_of_e(terms):
    sums = []
    current_sum = 0
    for n in range(terms):
        current_sum += 1 / factorial(n)
        sums.append(current_sum)
    return sums

max_terms = 20


sums = partial_sums_of_e(max_terms)


true_e = math.e


plt.plot(range(1, max_terms + 1), sums, label='Partial Sums of e')
plt.axhline(y=true_e, color='r', linestyle='--', label=f'e = {true_e:.5f}')
plt.xlabel('Number of terms')
plt.ylabel('Approximation of e')
plt.title('Approximation of Euler\'s Constant e by Series')
plt.legend()
plt.grid(True)
plt.show()

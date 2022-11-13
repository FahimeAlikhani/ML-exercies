import numpy as np
import pandas as pa
import matplotlib.pyplot as plot
from scipy.optimize import curve_fit

df = pa.DataFrame({'x': [1,2,3,4,5],
                   'y': [6,4.5,7,8.5,12]})  

x = df['x']
y = df['y']

def func_powerlaw(x, m, c, c0):
    return c0 + x**m * c

target_func = func_powerlaw

popt, pcov = curve_fit(target_func, x, y)
print('PowerReg = ',pcov)

plot.scatter(x, y, label='Original data') 
plot.plot(x, target_func(x, *popt), '--', color='red', label='Power line')
plot.legend()
plot.show()
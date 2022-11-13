import matplotlib.pyplot as plot
import numpy as np
import pandas as pa

df = pa.DataFrame({'x': [1,2,3,4,5],
                   'y': [6,4.5,7,8.5,12]})  

x = df['x']
y = df['y']
XY = []
X2 = []
log_x = np.log(x)
log_y = np.log(y)    

X = log_x
Y = log_y
for i, row in df.iterrows():
    XY = X*Y
    df['XY'] = pa.Series(XY)
    
    X2 = X**2
    df['X^2'] = pa.Series(X2)
    
    df.loc['sum'] = df.sum()
    
# y=a*e^bx
p = np.polyfit(x, np.log(y), 1)

a = np.exp(p[1])
b = p[0]
x_fitted = np.linspace(np.min(x), np.max(x), 100)
y_fitted = a * np.exp(b * x_fitted)

print(df)
print(u'\u2500' * 40)
print('ExpReg = ',p)
plot.scatter(x, y,label='Original data')
plot.plot(x_fitted, y_fitted,'--', color='red', label='Fitted line')
plot.legend()
plot.show()


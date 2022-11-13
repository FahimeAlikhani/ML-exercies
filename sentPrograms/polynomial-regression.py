import numpy as np
import matplotlib.pyplot  as plot
import pandas as pa
from scipy import stats

df = pa.DataFrame({'x': [1,2,3,4,5],
                   'y': [6,4.5,7,8.5,12]})  

x = df['x']
y = df['y']
xy = [] 
x2 = []
x3 = []
x2y = []
e2 = []
ei2 = []
# *****************************************************************************
p = np.polyfit(x, y, 3)  # function with degree 3
model = np.poly1d(p)

line = np.linspace(1, 5, 12)

# ******************************************************************************      
for i, row in df.iterrows():
  
    resultXY = row['x'] * row['y']
    xy.append(resultXY)
    df['xy'] = pa.Series(xy)

    resultX2 = row['x'] **2
    x2.append(resultX2)
    df['x^2'] = pa.Series(x2)
    
    resultX3 = row['x'] **3
    x3.append(resultX3)
    df['x^3'] = pa.Series(x3)

    x2y = (x**2) * y 
    df['x^2y'] = pa.Series(x2y)
    
    #average x
    x_ave = np.mean(x)    
    #average y
    y_ave = np.mean(y) 
    
    # ei^2= انحراف معیار به توان 2
    resulte2 = (row['y'] -y_ave )**2 
    e2.append(resulte2)
    df['e^2'] = pa.Series(e2)
    
    
    # ei2 = (y - p)**2
    # df['ei^2'] = pa.Series(ei2)
    
    # sum of all columns in a Pandas Data frame
    df.loc['sum'] = df.sum()
    
    # r2 = (sum(e2)-sum(ei2))/sum(e2)
    # r = np.sqrt(r2)
    
print(df)
print(u'\u2500' * 40)
print('x_ave = ',x_ave)
print('y_ave = ',y_ave)
print("st= ",sum(e2))
print("sr= ",sum(ei2))
# print("r2= ",r2)
# print("r= ",r)
print ("polyReg = ", p)

plot.scatter(x,y,label='Original data')
plot.plot(line, model(line),'--', color='red', label='Fitted line')
plot.legend()
plot.show()
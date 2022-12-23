import numpy as np
import pandas as pd
import matplotlib.pyplot  as plot
import pandas as pa
from scipy import stats

data = pd.read_csv('datasetexample/heart_statlog_cleveland_hungary_final.csv')
df = pd.DataFrame(data)
x = df['cholesterol']
y = df['max heart rate']  


xy = []
xx = [] 
xxx = [] 
xxxx = [] 
xxxxx = [] 
e2 = []
ei2 = []  
lineY = []
e = []  # cost function result
# *****************************************************************************
# use stats library from scipy to calculate the linear regression
x4 = x**4
slope, intercept, r, p, std_err = stats.linregress(x4, y)
    
def lineFunc(x4):
  return slope * x4 + intercept   # Y = mx^4 + c

# ******************************************************************************      
for i, row in df.iterrows():
    resultXY = row['cholesterol'] * row['max heart rate']
    xy.append(resultXY)
    df['xy'] = pa.Series(xy)
    
    resultXX = row['cholesterol'] * row['cholesterol']
    xx.append(resultXX)
    df['x^2'] = pa.Series(xx)
    
    resultXXX = row['cholesterol'] * row['cholesterol'] * row['cholesterol']
    xxx.append(resultXXX)
    df['x^3'] = pa.Series(xxx)
    
    resultXXXX = row['cholesterol'] * row['cholesterol']* row['cholesterol']* row['cholesterol']
    xxxx.append(resultXXXX)
    df['x^4'] = pa.Series(xxxx)
    
    resultXXXXX = row['cholesterol'] * row['cholesterol']* row['cholesterol']* row['cholesterol']* row['cholesterol']
    xxxxx.append(resultXXXXX)
    df['x^5'] = pa.Series(xxxxx)
    
    #average x
    x_ave = np.mean(x)    
    #average y
    y_ave = np.mean(y)    
    
    # ei^2= انحراف معیار به توان 2
    resulte2 = (row['max heart rate'] -y_ave )**2 
    e2.append(resulte2)
    df['e^2'] = pa.Series(e2)
    
    # plot a line classifying our dataset
    # lineY.append(list(map(lineFunc, x)))
    # df['lineY'] = pa.Series(lineY)
    lineY = list(map(lineFunc, x))
    df['lineY'] = pa.Series(lineY)
    
    # cost function =>    ei^2 = ( y- lineY)^2 
    ei2 = (y - lineY)**2
    df['ei^2'] = pa.Series(ei2)

    # sum of all columns in a Pandas Data frame
    df.loc['sum'] = df.sum()
    
    r2 = (sum(e2)-sum(ei2))/sum(e2)
    r = np.sqrt(r2)
    
print(df)
print(u'\u2500' * 40)
print('x_ave = ',x_ave)
print('y_ave = ',y_ave)
#print('lineY = ',lineY)
print("st= ",sum(e2))
print("sr= ",sum(ei2))
print("r2= ",r2)
print("r= ",r)

plot.scatter(x,y,label='Original data') 
plot.scatter(x,lineY, color='green', label='Linear regression data')
plot.plot(x,lineY,'--', color='red', label='Fitted line')
plot.xlabel('cholesterol')  
plot.ylabel('max heart rate') 
#plot.plot(plot.scatter(x,y),plot.scatter(x,lineY), color='orange', label='Error line')
plot.legend()
plot.show()
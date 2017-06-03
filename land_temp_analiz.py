import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LinReg
plt.style.use('ggplot')


df = pd.read_csv('c:\GlobalTemperatures.csv')
df.head()

df = df.ix[:,:2]
df.head()
df.describe()

plt.figure(figsize=(20,5))
plt.plot(df['LandAverageTemperature'])
plt.title("Avarage Land Temprature 1750-2015")
plt.xlabel("Year")
plt.ylabel('Avarage Land Temprature')
plt.show()

times = pd.DatetimeIndex(df['dt'])
grouped = df.groupby([times.year]).mean()

plt.figure(figsize=(15,5))
plt.plot(grouped['LandAverageTemperature'])
plt.title("Yearly Average Temperature 1750-2015")
plt.xlabel("year")
plt.ylabel("yearly average land temrature")
plt.show()

df[times.year == 1752]

df[np.isnan(df['LandAverageTemperature'])]

df['LandAverageTemperature'] = df['LandAverageTemperature'].fillna(method = 'ffill')

grouped = df.groupby([times.year]).mean()
plt.figure(figsize=(15,5))
plt.plot(grouped['LandAverageTemperature'])
plt.show()

x = grouped.index.values.reshape(-1,1)
y = grouped['LandAverageTemperature'].values

reg = LinReg()
reg.fit(x,y)
y_preds = reg.predict(x)
print("Accuracy: "+str(reg.score(x,y)))

plt.figure(figsize=(15,4))
plt.title("Linear Reggession")
plt.scatter(x = x, y = y_preds)
plt.scatter(x = x, y = y, c = 'r')

reg.predict(2050)
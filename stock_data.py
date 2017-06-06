from datetime import date

import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

start = datetime.datetime(2016,5,25)
end  = datetime.datetime(2017,6,5)
f = web.DataReader(['KATMR'],'google',start,end)

print(f.keys())


dataFrame = DataFrame(f.ix['Close'])

dataFrame1 = DataFrame(f.ix['Volume'])

plt.figure(1)
plt.subplot(211)
plt.plot(dataFrame)
plt.subplot(212)
plt.plot(dataFrame1)
plt.show()
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
end  = datetime.datetime(2017,5,26)
f = web.DataReader(['OZKGY'],'google',start,end)
ls_key = 'Close'
print(f.keys())
cleanData = f.ix[ls_key]
dataFrame = DataFrame(cleanData)

#plt.figure()
dataFrame.plot()
plt.show()
#plt.plot(dataFrame)
#plt.show()
print(dataFrame)


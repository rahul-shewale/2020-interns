import matplotlib.pyplot as plt
import numpy as np
import requests
from datetime import datetime as d

first_day = '2019-01-01'
last_day = '2019-01-31'
url1='https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols=INR,GBP'.format(first_day,last_day)
url2='https://api.exchangeratesapi.io/latest?symbols=INR,GBP'

r1 = requests.get(url1)
data = r1.json()

r2 = requests.get(url2)
latest= r2.json()

values=sorted(data['rates'])
INR_rate = list()
GBP_rate = list()
date = list()

for i in values:    
    day = d.strptime(i,'%Y-%m-%d')
    INR_rate.append(data['rates'][i]['INR'])
    GBP_rate.append(data['rates'][i]['GBP'])
    date.append([day.day])
        
plt.plot(date, INR_rate, linewidth=2, linestyle='solid', label='INR')
plt.plot(date, GBP_rate, linewidth=2, linestyle='solid', label='GBP')

plt.xlabel('January 2019')
plt.xticks(np.arange(32),rotation=45)
plt.ylabel('Values wrt EUR')
plt.title('INR and GBP exchange rate against EUR')
l=plt.legend(loc="center right")
l.get_texts()[0].set_text("INR="+str(latest['rates']['INR']))
l.get_texts()[1].set_text("GBP="+str(latest['rates']['GBP']))
plt.show()
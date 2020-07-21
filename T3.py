import json
import matplotlib.pyplot as plt 
from datetime import datetime as d
import numpy as np
with open('data.json') as f:
    data = json.load(f)
    
with open('latest-rates.json') as f:
    latest_rates = json.load(f)

first_day = d(2019,1,1)
last_day = d(2019,1,31)
values = sorted(data["rates"])
INR_rate = list()
GBP_rate = list()
date = list()

for i in values:    
    day = d.strptime(i,'%Y-%m-%d')
    if day <= last_day and day >= first_day:
        INR_rate.append(data['rates'][i]['INR'])
        GBP_rate.append(data['rates'][i]['GBP'])
        date.append([day.day])
        
plt.plot(date, INR_rate, linewidth=2, linestyle='solid', label='INR')
plt.plot(date, GBP_rate, linewidth=2, linestyle='solid', label='GBP')

plt.xlabel('January 2019')
plt.xticks(np.arange(32))
plt.ylabel('Values wrt EUR')
plt.title('INR and GBP exchange rate against EUR')
l=plt.legend(loc="center right")
l.get_texts()[0].set_text("INR="+str(latest_rates['rates']['INR']))
l.get_texts()[1].set_text("GBP="+str(latest_rates['rates']['GBP']))
plt.show()
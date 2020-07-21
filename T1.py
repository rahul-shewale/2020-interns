import json
import matplotlib.pyplot as plt 
from datetime import datetime as d
import numpy as np

with open('/data.json') as f:
    data = json.load(f)

first_date = d(2019,1,1)
last_date = d(2019,1,31)
values = sorted(data["rates"])
rate = list()
date = list()

for i in values:    
    day = d.strptime(i,'%Y-%m-%d')
    if day <= last_date and day >= first_date:
        rate.append(data['rates'][i]['INR'])
        date.append([day.day])

plt.plot(date,rate,'go--', linewidth=2, linestyle='solid')
plt.xlabel('January 2019')
plt.xticks(np.arange(32),rotation=45)
plt.ylabel('Value of INR wrt EUR')
plt.title('INR exchange rate against EUR')
plt.show()
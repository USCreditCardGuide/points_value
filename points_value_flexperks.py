import numpy as np
import matplotlib.pyplot as plt

max_price_for_the_plot = 10000
air_price = np.arange(max_price_for_the_plot)
points_value = np.zeros_like(air_price,dtype='f')
for i in range(air_price.size):
    if air_price[i] < 400:
        points_value[i] = air_price[i]/200.00
    elif air_price[i] < 600:
        points_value[i] = air_price[i]/300.00       
    elif air_price[i] < 800:
        points_value[i] = air_price[i]/400.00 
    elif air_price[i] < 1000:
        points_value[i] = air_price[i]/500.00 
    elif air_price[i] < 1400:
        points_value[i] = air_price[i]/700.00 
    elif air_price[i] < 2000:
        points_value[i] = air_price[i]/1000.00 
    elif air_price[i] < 3000:
        points_value[i] = air_price[i]/1500.00
    elif air_price[i] < 4000:
        points_value[i] = air_price[i]/2000.00
    elif air_price[i] < 5000:
        points_value[i] = air_price[i]/2500.00
    elif air_price[i] < 6000:
        points_value[i] = air_price[i]/3000.00
    elif air_price[i] < 7000:
        points_value[i] = air_price[i]/3500.00
    elif air_price[i] < 8000:
        points_value[i] = air_price[i]/4000.00
    elif air_price[i] < 9000:
        points_value[i] = air_price[i]/4500.00       
    elif air_price[i] < 10000:
        points_value[i] = air_price[i]/5000.00                        
    else:
        points_value[i] = air_price[i]/(250.00+(air_price[i]-500))

plt.figure()
plt.plot(air_price,points_value)
plt.ylim(0,2.5)
plt.hlines(y=1.0,xmin=0.0,xmax=max_price_for_the_plot,color='red',linestyles='dashed')
plt.hlines(y=2.0,xmin=0.0,xmax=max_price_for_the_plot,color='red',linestyles='dashed')
plt.vlines(x=400,ymin=0.0,ymax=2.5,color='red',linestyles='dashed')
plt.vlines(x=600,ymin=0.0,ymax=2.5,color='red',linestyles='dashed')
plt.vlines(x=800,ymin=0.0,ymax=2.5,color='red',linestyles='dashed')
plt.vlines(x=1000,ymin=0.0,ymax=2.5,color='red',linestyles='dashed')
plt.xlabel('Air Price')
plt.ylabel('Points Value')
plt.savefig('points_value_flexperks.png')
plt.show()
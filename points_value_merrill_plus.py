import numpy as np
import matplotlib.pyplot as plt

max_price_for_the_plot = 1500
air_price = np.arange(max_price_for_the_plot)
points_value = np.zeros_like(air_price,dtype='f')
for i in range(air_price.size):
    if air_price[i] < 500:
        points_value[i] = air_price[i]/250.00
    else:
        points_value[i] = air_price[i]/(250.00+(air_price[i]-500))

plt.figure()
plt.plot(air_price,points_value)
plt.ylim(0,2.5)
plt.hlines(y=1.0,xmin=0.0,xmax=max_price_for_the_plot,color='red',linestyles='dashed')
plt.hlines(y=2.0,xmin=0.0,xmax=max_price_for_the_plot,color='red',linestyles='dashed')
plt.vlines(x=500,ymin=0.0,ymax=2.5,color='red',linestyles='dashed')
plt.xlabel('Air Price')
plt.ylabel('Points Value')
plt.savefig('points_value_merrill_plus.png')
plt.show()
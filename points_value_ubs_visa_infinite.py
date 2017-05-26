import numpy as np
import matplotlib.pyplot as plt

max_price_for_the_plot = 1500
air_price = np.arange(max_price_for_the_plot)
points_value = np.zeros_like(air_price,dtype='f')
for i in range(air_price.size):
    if air_price[i] < 350:
        points_value[i] = air_price[i]/250.00
    elif air_price[i] < 900:
        points1 = 250.00+np.ceil((air_price[i]-350)/50.0)*50.0
        points2 = 500.00
        points_value[i] = air_price[i]/(np.minimum(points1,points2))
    else:
        points_value[i] = air_price[i]/(500.00+np.ceil((air_price[i]-900)/50.0)*50.0)

plt.figure()
plt.plot(air_price,points_value)
plt.ylim(0,2.5)
plt.hlines(y=1.0,xmin=0.0,xmax=max_price_for_the_plot,color='red',linestyles='dashed')
plt.hlines(y=1.8,xmin=0.0,xmax=max_price_for_the_plot,color='red',linestyles='dashed')
plt.vlines(x=900,ymin=0.0,ymax=2.5,color='red',linestyles='dashed')
plt.xlabel('Air Price')
plt.ylabel('Points Value')
plt.savefig('points_value_ubs_visa_infinite.png')
plt.show()
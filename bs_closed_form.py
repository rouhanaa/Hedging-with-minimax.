import numpy as np
import scipy.stats as ss
import time 
import matplotlib.pyplot as plt


def argument_d1(S0, K, r, volatility, maturity):
    return (np.log(S0/K) + (r + volatility**2 / 2) * maturity)/(volatility * np.sqrt(maturity))
 
def argument_d2(S0, K, r, volatility, maturity):
    return (np.log(S0 / K) + (r - volatility**2 / 2) * maturity) / (volatility * np.sqrt(maturity))
 
def BS_Price(type,S0, K, r, volatility, maturity):
        return S0 * ss.norm.cdf(argument_d1(S0, K, r, volatility, maturity)) - K * np.exp(-r * maturity) * ss.norm.cdf(argument_d2(S0, K, r, volatility, maturity))


S0 = 5    
K = 4
r=0
maturity = float(100)/365
Otype='C' 
c=[]
#compute price versus volatility
for volatility in range(1,10):    
    volatility=float(volatility)/10
    c_BS = BS_Price(Otype,S0, K, r, volatility, maturity)
    c.append(c_BS)
#plot Black-Scholes price versus volatility
volatility=np.arange(0.1,1.,0.1)
plt.plot(volatility,c,'r',linewidth=2)
plt.title("Black-Scholes price versus Volatility")
plt.xlabel('Volatility')
plt.ylabel('Black-Scholes Price')
plt.show()   
   

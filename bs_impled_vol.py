from math import log, sqrt, exp
from scipy.stats import norm
import datetime


def implied_vol(target_value, S_0, strike, T, r):
    TOTAL_ITERATIONS = 1000
    error_allowed = 0.01

    volatility = 0.8
    for iter in xrange(0, TOTAL_ITERATIONS):
        price = bs_value(S_0, strike, T, r, volatility)
        Vega = vega( S_0, strike, T, r, volatility)

        price = price
        error = target_value - price  # our root
        if (abs(error) < error_allowed):
            return volatility
        volatility = volatility + error/Vega # f(x) / f'(x)
    return volatility


def bs_value(S_0,strike,maturity,r,p):
    cdf = norm.cdf
    d1 = (log(S_0/strike)+(r+p*p/2.)*maturity)/(p*sqrt(maturity))
    d2 = d1-p*sqrt(maturity)
    price = S_0*cdf(d1)-strike*exp(-r*maturity)*cdf(d2)
    return price

def vega(S_0,strike,maturity,r,p):
     pdf = norm.pdf
     d1 = (log(S_0/strike)+(r+p*p/2.)*maturity)/(p*sqrt(maturity))
     return S_0 * sqrt(maturity)*pdf(d1)

market_price= 1
strike =15
maturity = float(10) /365
S_0 = 16
r = 0
implied_vol = implied_vol(market_price, S_0, strike, maturity, r)
print 'Implied volatility:' +str(implied_vol)

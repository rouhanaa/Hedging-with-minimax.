#OPTION PROPERTIES
n_stocks = 1 #underlying quantity
stock_price = 5 #initial stock price in dollars
n_trading =50 #number of trading until maturity  
strike=4
initial_utility=max(0,stock_price-strike)
#NATURE CONSTRAINTS
var_budg =5#variance budget
zeta =2 #maximum jump
discretize_r =0.5
discretize_delta =0.5
#negative delta: this corresponds to selling stocks.
#positive delta: this corresponds to buying stocks.
n_jumps = zeta / discretize_r 
r=[] #r contains the possible variation in the stock price.
i=0
v1=0
while v1 < zeta:
        v1= -zeta +i* discretize_r
        #v1= +i* discretize_r
        if v1 != 0 and v1 !=-1:
            r.append( -zeta +i* discretize_r) 
        i=i+1

#Delta represents the initial set of possible investments.
n_delta = (n_stocks * stock_price) / discretize_delta 
delta=[]
j=0
v2=0
while v2 < stock_price:
    v2=-stock_price + j*discretize_delta
   # v2= j*discretize_delta
    if v2 != 0:
        #delta.append( j*discretize_delta)
        delta.append(- n_stocks * stock_price+ j*discretize_delta) 
    j=j+1

print "Number of trading periods: "+str(n_trading)
print "Possible stock values given by market " +str(r) 
print "Possible investment value by investor "+str(delta)



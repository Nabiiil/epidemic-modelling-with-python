from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


P=np.atleast_1d(
    [0,1/3,1/3,1/3,0,0,0,0,0,0,0,0],
    [1/3,0,1/3,0,0,0,0,1/3,0,0,0,0],
    [0.2,0.2,0,0.2,0.2,0,0,0.2,0,0,0,0],
    [0.25,0,0.25,0,0.25,0.25,0,0,0,0,0,0],
    [0,0,0.2,0.2,0,0.2,0.2,0.2,0,0,0,0],
    [0,0,0,1/3,1/3,0,1/3,0,0,0,0,0],
    [0,0,0,0,0.25,0.25,0,0.25,0.25,0,0,0],
    [0,0.2,0.2,0,0.2,0,0,0.2,0,0.2,0,0],
    [0,0,0,0,0,0,1/3,1/3,0,1/3,0,0],
    [0,0,0,0,0,0,0,0,0.5,0,0.5,0],
    [0,0,0,0,0,0,0,0,0,0.5,0,0.5],
    [0,0,0,0,0,0,0,0,0,0,1,0])
data=pd.read_csv('C:/Users/elhao/Desktop/Markov Chaine/data.csv')
datadf=pd.DataFrame(data)
n=datadf.loc[datadf['date']=='3/10/2020',"Tanger-Tétouan-Al Hoceïma":"Béni Mellal-Khénifra"]
c=[]
for i in list(n.columns): c.append(i[:8])
#Infected people distribution by region
a=datadf.loc[:,"Tanger-Tétouan-Al Hoceïma":"Béni Mellal-Khénifra"].div(datadf["Total"], axis=0)
b=np.asarray(a.loc[57])
for i in range(50):n=np.dot(n,P)
#Comparing with barplots the distribution
'''fig,ax = plt.subplots()
x = np.arange(len(c))
width=0.2
b1=ax.bar(x-width/2,n[0],width,label='model')
b2=ax.bar(x+width/2,b,width,label='real')
ax.set_xticks(x)
ax.set_xticklabels(c)
ax.legend()
plt.show()'''
#Comparing the infected funtction with real data
'''
def deriv(y, t):
    S, I, R= y
    dSdt = -a*S*I
    dIdt = a*S*I -b*I
    dRdt = b*I
    return dSdt, dIdt, dRdt
S0, I0, R0 = 1000000, 10, 0  # initial conditions: one exposed
t = np.linspace(0, 60, 100000) # Grid of time points (in days)
y0 = S0, I0, R0 # Initial conditions vector
a=0.0000002
b=0.1
ret = odeint(deriv, y0, t)
S, I, R = ret.T

f, ax = plt.subplots(1,1,figsize=(10,4))
ax.plot(t, I, 'g', alpha=0.7, linewidth=2, label='Real')
ax.plot(datadf["Total"], 'r', alpha=0.7, linewidth=2, label='Model')
plt.title("Infected people in the first 60 days")
plt.legend()
plt.show()
'''
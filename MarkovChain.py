import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Transition Matrix for the Markov Chain:
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
#COVID19 DATA MOROCCO
data=pd.read_csv('C:/Users/elhao/Desktop/Markov Chaine/data.csv')
datadf=pd.DataFrame(data)
#We will consider the date Mars 10th to be our initial starting point
n=datadf.loc[datadf['date']=='3/10/2020',"Tanger-Tétouan-Al Hoceïma":"Béni Mellal-Khénifra"]
c=[]
for i in list(n.columns): c.append(i[:8]) #Morocco's Region will the indexes of our data
print(c)
#Distribution in 1 days
for i in range(1):n=np.dot(n,P)
#Distribution in 100 days
m=n
for i in range(100):m=np.dot(m,P)
#Distribution in 300 days
k=m
for i in range(300):k=np.dot(k,P)
#Plotting the results

x = np.arange(len(c))
width=0.2
fig, ax = plt.subplots()

b1=ax.bar(x-width,n[0],width,label='Day1')
b2=ax.bar(x,m[0],width,label='Day100')
b3=ax.bar(x+width,k[0],width,label='Day300')

ax.set_xticks(x)
ax.set_xticklabels(c)
ax.legend()
plt.show()


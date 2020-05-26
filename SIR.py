from scipy.integrate import odeint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Building the differential equations system
def deriv(y, t):
    S, I, R= y
    dSdt = -a*S*I
    dIdt = a*S*I -b*I
    dRdt = b*I
    return dSdt, dIdt, dRdt
S0, I0, R0 = 3000000, 18, 0  # initial conditions: 18 infected people in 3/14/2020

t = np.linspace(0, 60, 100000) # Grid of time points (in days)
y0 = S0, I0, R0 # Initial conditions vector
a=0.004 #infection probability in Morocco
b=0.38  #Recovery Rate

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t)
S, I, R = ret.T

def plotseird(t, S, I, R):
  f, ax = plt.subplots(1,1,figsize=(10,4))
  ax.plot(t, S, 'r', alpha=0.7, linewidth=2, label='Suspected')
  ax.plot(t, I, 'g', alpha=0.7, linewidth=2, label='Infected')
  ax.plot(t, R, 'b', alpha=0.7, linewidth=2, label='Recovered')

  ax.set_xlabel('Time (days)')

  ax.yaxis.set_tick_params(length=0)
  ax.xaxis.set_tick_params(length=0)
  ax.grid(b=True, which='major', c='w', lw=2, ls='-')

  legend = ax.legend()
  legend.get_frame().set_alpha(0.5)
  for spine in ('top', 'right', 'bottom', 'left'):
      ax.spines[spine].set_visible(False)
  plt.show();

plotseird(t, S, I, R)

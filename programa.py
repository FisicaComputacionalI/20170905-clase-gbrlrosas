# lineplot.py
import numpy as np
import pylab as pl
#make an array of x values
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  
#make an array of y values for each x values
y= [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#use a pylab to plot x and y
pl.plot(x, y,'ro')
#show the plot on the screen
pl.savefig('temp1.png')


 

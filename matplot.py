import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.linspace(0,5,11)
y=x**2
plt.title("Hello")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.subplot(2,2,1) #subplot hota h quadrants type
plt.plot(y)
plt.subplot(2,2,2)
plt.plot(x)
plt.subplot(2,2,3)
plt.plot(y,x)
plt.subplot(2,2,4)
plt.plot(x,y)
plt.show()
fig=plt.figure(figsize=(12,8),dpi=100)
axis1=fig.add_axes([.1,.1,1,1]) # left,bottom,width
axis1.plot(x,y)
axis2=fig.add_axes([.3,.4,1,1]) # left,bottom,width
axis2.plot(x,y)
plt.scatter(x,y)
plt.show()
from random import sample
data=sample(range(1,1000),100)
plt.hist(data)
plt.show()
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y)
plt.savefig("Basic_fig.jpeg")
import matplotlib.image as mpimg
img=mpimg.imread('IMG_0294.JPG')
rotated = np.rot90(img)
plt.imshow(rotated)
plt.axis('off')
plt.show()
# optional designing
plt.plot(x,y,color='pink')
plt.show()
xaxis=np.linspace(0,5,11)
fig, ax = plt.subplots(figsize=(12,6))


ax.plot(xaxis, xaxis+1, color="red", linewidth=0.25)
ax.plot(xaxis, xaxis+2, color="red", linewidth=0.50)
ax.plot(xaxis, xaxis+3, color="red", linewidth=1.00)
ax.plot(xaxis, xaxis+4, color="red", linewidth=2.00)

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(xaxis, xaxis+5, color="green", lw=3, linestyle='-')
ax.plot(xaxis, xaxis+6, color="green", lw=3, ls='-.')
ax.plot(xaxis, xaxis+7, color="green", lw=3, ls=':')

# custom dash
line, = ax.plot(xaxis, xaxis+8, color="black", lw=1.50)
line.set_dashes([5, 50, 15, 50]) # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(xaxis, xaxis+ 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(xaxis, xaxis+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(xaxis, xaxis+11, color="blue", lw=3, ls='-', marker='s')
ax.plot(xaxis, xaxis+12, color="blue", lw=3, ls='--', marker='1')
ax.plot(xaxis, xaxis+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(xaxis, xaxis+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(xaxis, xaxis+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(xaxis, xaxis+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green");
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
print(df)
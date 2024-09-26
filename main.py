import numpy
import matplotlib.pyplot as plt

num=[1,10,50,100]
means=[]

for j in num:
    numpy.random.seed(1)
    x=[numpy.mean(numpy.random.randint(-40,40,j)) for _j in range(1000)]
    means.append(x)
k=0

fig,ax = plt.subplots(2,2,figsize = (6,6))
for i in range(0,2):
    for j in range(0,2):
        ax[i,j].hist(means[k], 10, density = True)
        ax[i,j].set_title(label = num[k])
        k=k+1
plt.show()
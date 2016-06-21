import numpy as np
import matplotlib.pyplot as plt


crumb = 0
crust = 0
circle_crumb = 0
circle_crust = 0
px = []
py = []

for i in range(1,1000000):
    x = np.random.random_sample()
    y = np.random.random_sample()
    
    
    max_c = max(x,y)
    dist_to_crust = 1 - max_c
    dist_to_center = np.sqrt( np.square(x) + np.square(y))


    if(dist_to_crust <= dist_to_center):
	# sample in crust
        crust = crust+1
    else:
	# sample in crumb
        crumb = crumb+1
	# add point for plotting
        px.append(x)
        py.append(y)

# results
total = crumb+crust
per = (crumb/total) * 100

print("crumb: "+str(crumb))
print("crust: "+str(crust))
print("answer: "+str(per))

# plot
plt.ylim(0, 1)
plt.xlim(0, 1)
plt.scatter(px,py)

plt.show()

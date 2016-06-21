import numpy as np
import matplotlib.pyplot as plt


crumb = 0
crust = 0
circle_crumb = 0
circle_crust = 0
px = []
py = []
cx1 = []
cy1 = []
cx2 = []
cy2 = []
for i in range(1,1000000):
    x = np.random.random_sample()
    y = np.random.random_sample()
    
    
    max_c = max(x,y)
    dist_to_crust = 1 - max_c
    dist_to_center = np.sqrt( np.square(x) + np.square(y))
    #in_circle = np.square(x) + np.square(y)

    #if(in_circle <= 1):
    #    if(dist_to_center <= 0.5):	
    #       circle_crumb = circle_crumb + 1
    #       cx2.append(x)
    #       cy2.append(y)
    #    else:
    #       circle_crust = circle_crust + 1
    #       cx1.append(x)
    #       cy1.append(y)


    if(dist_to_crust <= dist_to_center):
        crust = crust+1
#    print("CRUST")
    else:
        crumb = crumb+1
        px.append(x)
        py.append(y)
#    print("CRUMB")

print("crumb: "+str(crumb))
print("crust: "+str(crust))
total = crumb+crust

per = (crumb/total) * 100

#total_circle = circle_crust+circle_crumb
#per = (circle_crumb/total_circle) * 100

print("answer: "+str(per))

plt.ylim(0, 1)
plt.xlim(0, 1)
plt.scatter(px,py)
#plt.scatter(cx1,cy1,c="red")
#plt.scatter(cx2,cy2,c="blue")


plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

vec1 = np.array(input("3D Vector 1 (separated by spaces): ",).split(" ")).astype(int)
vec2 = np.array(input("3D Vector 2 (separated by spaces): ",).split(" ")).astype(int)
cross = np.cross(vec1,vec2)

all_vecs = np.array([vec1,vec2,cross,[0,0,0]])

max_range = np.abs(all_vecs).max() #max range across all dimensions

limit = max_range*1.2 #20% for visibility

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.set_xlim([-limit,limit]) #sets axes limits
ax.set_ylim([-limit,limit])
ax.set_zlim([-limit,limit])

ax.quiver(0,0,0,vec1[0], vec1[1], vec1[2],color='b',arrow_length_ratio=0.1) #plots vectors
ax.quiver(0,0,0,vec2[0], vec2[1], vec2[2],color='r',arrow_length_ratio=0.1)
ax.quiver(0,0,0,cross[0], cross[1], cross[2],color='black',arrow_length_ratio=0.1)

ax.text(vec1[0]+max_range*0.05,vec1[1],vec1[2], 'Vector 1', color='b',fontsize=8) #labels vectors
ax.text(vec2[0]+max_range*0.05,vec2[1],vec2[2], 'Vector 2', color='r',fontsize=8)
ax.text(cross[0]+max_range*0.05,cross[1],cross[2], 'Cross Product', color='black',fontsize=8)

ax.set_xlabel('X') #labels axes
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Section 11.4: Cross Products Visualization')

plt.show()

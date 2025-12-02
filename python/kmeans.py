import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


np.random.seed(0)
# There are 6 classes:
# X direction down => X = 1800, label = 0
# X direction up => X = 1200, label = 1
# etc.
data = np.zeros((600,4))
data[0:100,:] = np.array([1800,1500,1500,0])
data[100:200,:] = np.array([1200,1500,1500,1])
data[200:300,:] = np.array([1500,1800,1500,2])
data[300:400,:] = np.array([1500,1200,1500,3])
data[400:500,:] = np.array([1500,1500,1800,4])
data[500:600,:] = np.array([1500,1500,1200,5])
data[:,0:3] = data[:,0:3] + 70*np.random.rand(600, 3)

y_data = data[:,3]

X_data = data[:,0:3]

N=600

k = 6

clusters = {}
for idx in range(k):
    center = 1500+100*(np.random.random((X_data.shape[1],)))
    points = []
    cluster = {
        'center' : center,
        'points' : []
    }
    clusters[idx] = cluster

def calcDistance(p1, p2):
    return np.sqrt(np.sum((p1-p2)**2))

epochs = 10
for e in range(epochs):
    for d in range(X_data.shape[0]):
        distance = []
        currentPoint = X_data[d]
        for k in range(6):
            distance.append(calcDistance(clusters[k]['center'], currentPoint))
        winnerCluster = np.argmin(distance)
        clusters[winnerCluster]['points'].append(currentPoint)

#Update centers
    for k in range(6):
        currentCluster = clusters[k]
        points = np.array(currentCluster['points'])
        if points.shape[0] > 0:
            currentCluster['center'] = points.mean(axis=0)
            currentCluster['points'] = []
        else:
            currentCluster['center'] = 1500+200*(np.random.random((X_data.shape[1],)))



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(data[:,0], data[:,1], data[:,2],color='red')

for i in clusters:
    center = clusters[i]['center']
    ax.scatter(center[0], center[1], center[2], marker = '^', c = 'green', s=400)
    print(clusters[i]['center'])


# Akselien nimet
ax.set_xlabel('X-akseli')
ax.set_ylabel('Y-akseli')
ax.set_zlabel('Z-akseli')

plt.show()


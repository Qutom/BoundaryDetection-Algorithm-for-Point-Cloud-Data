#테스트용 파일
#points를 읽어와 resolution을 계산하고 circle을 그리는 것 까지 구현

import numpy as np
import matplotlib.pyplot as plt
import random
import Circle
from sklearn.neighbors import NearestNeighbors
from itertools import combinations
  
file_name = "points.txt"
points = np.loadtxt(file_name)

#knn
neighbors = NearestNeighbors(n_neighbors=30, algorithm='ball_tree').fit(points)
distances, indices = neighbors.kneighbors(points)

#랜덤한 점을 하나 잡음
point_index = random.randrange(0, points.shape[0])
p_neighbor, p_distance = indices[point_index], distances[point_index]

#resolution 계산 ( distance의 mean + 2*std)
p_mean = np.mean(p_distance)
p_std = np.std(p_distance)
local_resol = p_mean + 2*p_std

#랜덤한 두 이웃을 잡아 원을 생성
pairs = list(combinations(p_neighbor[1:], 2))
#for i in range(len(pairs)) :
p1 = points[point_index]
p2 = points[pairs[10][0]]
p3 = points[pairs[10][1]]
c = Circle(p1, p2, p3)


#implement radius >= resolution check

#plot
plt.axes(projection='3d')
plt.scatter((p1[0], p2[0], p3[0]), (p1[1], p2[1], p3[1]), (p1[2], p2[2], p3[2]))


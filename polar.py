import numpy as np
import matplotlib.pyplot as plt
import random
import Circle as C
import open3d as o3d
import alphashape
from sklearn.neighbors import NearestNeighbors
from itertools import combinations

class Polar :
    def __init__(self, center, points, normalize=False):
        self.r, self.theta = self.cart2pol(center, points)
        self.min_theta = np.min(self.theta)
        self.max_theta = np.max(self.theta)
        self.min_r = np.min(self.r)
        self.max_r = np.max(self.r)

        if normalize :
            self.polar_normalize()

        self.bis = np.min(self.theta) + np.max(self.theta) / 2

    def cart2pol(self, center, points, show=False):
        points -= center

        x = points[:, 0]
        y = points[:, 1]

        r = np.sqrt(x ** 2 + y ** 2)
        theta = np.arctan2(y, x)
        if show :
            print(r)
            print(theta)
        return r, theta

    def polar_normalize(self):

        self.r = (self.r - self.min_r) / (self.max_r - self.min_r)
        self.theta = (self.theta - self.min_theta) / (self.max_theta - self.min_theta)

    def plot(self):
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.scatter(self.theta, self.r)

        max_r = np.max(self.r)
        ax.set_rmax(max_r * 1.5)
        ax.grid(True)

        plt.show()

    def check(self):
        #set starting point
        theta_bis = np.max(self.max_theta) - np.min(self.min_theta)
        chr_param = self.r + np.abs(self.theta - self.theta_bis)

        





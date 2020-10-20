from typing import List
import matplotlib.pyplot as plt

from constants import COLORS
from models.Cluster import Cluster


def graph(clusters: List[Cluster]):

    for cluster_idx in range(0, len(clusters)):
        x_list = []
        y_list = []
        x_center_list = []
        y_center_list = []

        for point in clusters[cluster_idx].points:
            x_list.append(point.x)
            y_list.append(point.y)
            x_center_list.append(clusters[cluster_idx].centroid.x)
            y_center_list.append(clusters[cluster_idx].centroid.y)

        plt.plot(x_list, y_list, '-o', color=COLORS[cluster_idx], markersize=1, linewidth=0)
        plt.plot(x_center_list, y_center_list, '-o', color='black', markersize=5, linewidth=0)

    plt.show()

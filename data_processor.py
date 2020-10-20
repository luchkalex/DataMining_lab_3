import random
from math import sqrt
from typing import List

from models.Cluster import Cluster
from models.Point import Point


def get_clusters(centroid_quantity, points: List[Point]):
    clusters = []
    for x in range(0, int(centroid_quantity)):
        random_point = points.pop(int(random.random() * (len(points) - 1)))
        random_point.cluster_idx = x
        clusters.append(Cluster([random_point], random_point, random_point.x, random_point.y))
    return clusters


def recalculate_cluster_center(cluster: Cluster, point: Point, adding: bool):
    if adding:
        cluster.sum_x += point.x
        cluster.sum_y += point.y
    else:
        cluster.sum_x -= point.x
        cluster.sum_y -= point.y

    cluster.centroid.x = cluster.sum_x / len(cluster.points)
    cluster.centroid.y = cluster.sum_y / len(cluster.points)


def distribute_points(clusters: List[Cluster], points: List[Point]):
    for point_idx in range(0, len(points)):
        min_dist = 2147483647
        min_dist_cluster_index = 0
        for cluster_idx in range(0, len(clusters)):
            cur_dist = get_distance_between_points(points[point_idx], clusters[cluster_idx].centroid)
            if cur_dist < min_dist:
                min_dist = cur_dist
                min_dist_cluster_index = cluster_idx
        clusters[min_dist_cluster_index].points.append(points[point_idx])
        points[point_idx].cluster_idx = min_dist_cluster_index
        recalculate_cluster_center(clusters[min_dist_cluster_index], points[point_idx], True)

    for i in range(0, 10):
        for point_idx in range(0, len(points)):
            min_dist = 2147483647
            min_dist_cluster_index = 0
            for cluster_idx in range(0, len(clusters)):
                cur_dist = get_distance_between_points(points[point_idx], clusters[cluster_idx].centroid)
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    min_dist_cluster_index = cluster_idx

            clusters[points[point_idx].cluster_idx].points.remove(points[point_idx])
            recalculate_cluster_center(clusters[points[point_idx].cluster_idx], points[point_idx], False)
            clusters[min_dist_cluster_index].points.append(points[point_idx])
            points[point_idx].cluster_idx = min_dist_cluster_index
            recalculate_cluster_center(clusters[min_dist_cluster_index], points[point_idx], True)


def get_distance_between_points(point1: Point, point2: Point):
    return sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

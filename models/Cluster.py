from typing import List
from models.Point import Point


class Cluster:
    def __init__(self, points: List[Point], centroid: Point, sum_x: int, sum_y: int):
        self.points = points
        self.centroid = centroid
        self.sum_x = sum_x
        self.sum_y = sum_y

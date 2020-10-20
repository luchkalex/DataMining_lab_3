from re import *
from models.Point import Point


def get_list_of_lines_from_file(src_filename):
    src_file = open(src_filename, "r")
    result_list = []

    for line in src_file:
        result_list.append(sub("\n", "", line))

    return result_list


def get_point_from_string(src_str):
    return Point(
        int(sub("\\d+\\s*$", "", src_str)),
        int(sub("^\\s+\\d+", "", src_str)),
        -1
    )


def get_points_from_string_list(src_list):
    points = []

    for line in src_list:
        points.append(get_point_from_string(line))

    return points

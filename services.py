from re import *

from constants import OUTPUT_DIR


def get_list_of_lines_from_file(src_filename):
    src_file = open(OUTPUT_DIR + "/" + src_filename, "r")
    result_list = []

    for line in src_file:
        result_list.append(sub("\n", "", line))

    return result_list


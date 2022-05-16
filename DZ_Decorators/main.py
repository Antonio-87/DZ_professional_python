from math_utils import FlatIterator
from input_date.date import nested_list


if __name__ == '__main__':

    for item in FlatIterator(nested_list):
        print(item)
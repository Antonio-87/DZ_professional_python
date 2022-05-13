from input_data.date import *
from iter_class import *
from generator import *

if __name__ == '__main__':
    # for item in FlatIterator(nested_list):
    #     print(item)
    # flat_list = [item for item in FlatIterator(nested_list)]
    for item in FlatIterator_any(nested_list_any):
        print(item)
    # print(flat_list)
    # for item in  flat_generator(nested_list):
	    # print(item)
    # for item in  flat_generator_any(nested_list_any):
    #         print(item)
    
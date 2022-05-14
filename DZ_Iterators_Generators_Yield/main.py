from input_data.date import *
from iter_class import *
from generator import *

if __name__ == '__main__':
    print('Задание №1')
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)    
    print('Задание №2')
    for item in flat_generator(nested_list):
        print(item)
    print('Задание №3 - не получается')
    for item in FlatIterator_any(nested_list_any):
        print(item)
    print('Задание №4')
    for item in flat_generator_any(nested_list_any):
        print(item)
    
    
        
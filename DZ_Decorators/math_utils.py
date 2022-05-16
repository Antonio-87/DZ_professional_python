import os
from logger_params import logger

file_path = os.path.join(os.getcwd(),"logs/log2.txt")

@logger(path=file_path)
class FlatIterator:
    def __init__(self, nested_list):
        self.flat_list = sum(nested_list, [])
        
        
    def __iter__(self):
        self.start = -1
        self.end = len(self.flat_list)
        return self


    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration       
        return self.flat_list[self.start]
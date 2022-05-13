from matplotlib.cbook import flatten
from generator import flat_generator


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


class FlatIterator_any:
    def __init__(self, nested_list):
        self.flat_list = sum(nested_list, [])
        
          
    def __iter__(self):
        self.start = -1
        self.end = len(self.flat_list)
        return self

    def flattan(self, nested_list):
        for l in nested_list:
            for i in l:
                yield i

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        if self.flat_list[self.start] != list:
            return self.flat_list[self.start]
        for i in self.flat_list[self.start]:
            for x in i:
                if x == 'bool':
                    return x
            return x     
        return self.flat_list[self.start]
    
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
        self.flat_list = self.flatten(nested_list)
        
          
    def __iter__(self):
        self.start = -1
        self.end = len(self.flat_list)
        return self

    
    def flatten(self, nested_list):
        if isinstance(nested_list, list):   
            return sum(map(self.flatten, nested_list), [])
        else:
            return [nested_list]  


    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.flat_list[self.start]
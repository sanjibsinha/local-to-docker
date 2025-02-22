class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
        

    def __iter__(self): # Iterator returns itself
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
        
# Using custom iterator
my_range = MyRange(1, 10)
for number in my_range:
    print(number) # 1, 2, 3, 4, 5, 6, 7, 8, 9
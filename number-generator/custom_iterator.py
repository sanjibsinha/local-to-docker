# custom iterator
class CustomIterator:
    def __init__(self, start, step, count):
        self.current = start
        self.step = step
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        current = self.current
        self.current += self.step
        self.count -= 1
        return current
    
# use the iterator
iterator = CustomIterator(1, 2, 5)
for number in iterator:
    print(number)
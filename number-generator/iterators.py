my_numbers = [1, 2, 3]

# Get an iterator from the list
iterator = iter(my_numbers)

# Get the first item from the iterator
item = next(iterator) # 1

# Get the next item from the iterator
item = next(iterator) # 2

# Get the next item from the iterator
item = next(iterator) # 3

# Get the next item from the iterator
# item = next(iterator) # StopIteration

for item in my_numbers:
    print(item) # 1, 2, 3

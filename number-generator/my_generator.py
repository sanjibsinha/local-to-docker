def my_generator(n):
    for i in range(n):
        yield i

# Create a generator object
generator = my_generator(10)

# Get values from the generator
print(next(generator))  # 0
print(next(generator))  # 1
print(next(generator))  # 2

# You can also use a for loop to iterate over the generator
for value in generator:
    print(value) #  3, 4, 5, 6, 7, 8, 9

print("============")

for item in my_generator(3):
    print(item) # 0, 1, 2
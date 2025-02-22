# A simple number generator

def number_generator(start, step, count):
    current = start
    for _ in range(count):
        yield current
        current += step

# Get input from the user
start = int(input("Enter the starting number: "))
step = int(input("Enter the step value: "))
count = int(input("Enter the number of numbers to generate: "))

# Create the generator
generator = number_generator(start, step, count)

# Print the generated numbers
for number in generator:
    print(number)
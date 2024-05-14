import random

num_min = 0
num_max = 4999
total_numbers = 1000

numbers = [random.randint(num_min, num_max) for _ in range(total_numbers)]

# Write requests to a text file
with open("numbers.txt", "w") as file:
    for i in numbers:
        file.write(str(i) + "\n")

print("File 'numbers.txt' has been created.")
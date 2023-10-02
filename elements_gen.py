import numpy as np

# Specify the file path
file_path = 'random_elements.txt'

# Generate random integers and write them to the file
with open(file_path, 'w') as file:
    # Change the range and size as needed
    random_integers = np.random.randint(1, 1000, size=1000)
    for num in random_integers:
        file.write(str(num) + '\n')

print(f"File '{file_path}' generated.")

# Group Members:
# Caleb Mabuka: CIT-227-030/2021
# Joram Kariuki: CIT-227-009/2021
# JohnMark Wanjugu: CIT-227-008/2021
# Thorne Musau: CIT-227-029/2021


import numpy as np
import time
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
        
def measure_time(n):
    # Generate a random array of size n
    elements = np.random.randint(1, 1000, size=n)

    # Measure the time taken to sort the array using quicksort
    start_time = time.time()
    sorted_elements = quicksort(elements)
    end_time = time.time()

    return end_time - start_time

# # Read elements from a file
# file_path = 'random_elements.txt'  # Replace with the actual path
# with open(file_path, 'r') as file:
#     lines = file.readlines()
#     elements = [int(line.strip()) for line in lines]

n_values = np.random.randint(1, 100, size=10)
times_taken = []

for n in n_values:
    time_taken = measure_time(n)
    times_taken.append(time_taken)
    print(f"Time taken for n={n}: {time_taken:.6f} seconds")

# Plotting the graph
plt.plot(n_values, times_taken, marker='o')
plt.title('Quicksort Performance')
plt.xlabel('Number of Elements (n)')
plt.ylabel('Time Taken (seconds)')
plt.show()
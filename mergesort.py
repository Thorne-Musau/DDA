import numpy as np
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure_time(arr):
    start_time = time.time()
    sorted_arr = merge_sort(arr)
    end_time = time.time()
    return end_time - start_time

# Read elements from a file
file_path = 'random_elements.txt'  # Replace with the actual path
with open(file_path, 'r') as file:
    elements = [int(line.strip()) for line in file]

# Experiment for different values of n
n_values = np.random.randint(1, 100, size=10)
times_taken = []

for n in n_values:
    # Use a subset of elements with size n
    subset_elements = elements[:n]

    time_taken = measure_time(subset_elements)
    times_taken.append(time_taken)
    print(f"Time taken for n={n}: {time_taken:.6f} seconds")

# Plotting the graph
plt.plot(n_values, times_taken, marker='o')
plt.title('Merge Sort Performance')
plt.xlabel('Number of Elements (n)')
plt.ylabel('Time Taken (seconds)')
plt.show()

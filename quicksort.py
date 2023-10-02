import numpy as np
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
        
# Random number generator using numpy
random_array = np.random.randint(1, 100, size=10) 

start = time.time()

x = quicksort(random_array)
print(x)

end = time.time()
print(end-start)
import numpy as np
from concurrent.futures import ThreadPoolExecutor

# Define the two vectors as NumPy arrays
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# Function to compute partial dot product
def partial_dot(start, end):
    return np.dot(vector_a[start:end], vector_b[start:end])

# Use multiple threads for parallel computation  ooye ooye
def parallel_dot(a, b, num_threads=2):
    chunk_size = len(a) // num_threads
    futures = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            start = i * chunk_size
            end = len(a) if i == num_threads - 1 else (i + 1) * chunk_size
            futures.append(executor.submit(np.dot, a[start:end], b[start:end]))
        results = [f.result() for f in futures]
    return sum(results)

# Calculate the dot product using parallelism
dot_product = parallel_dot(vector_a, vector_b, num_threads=2)

print(f"The parallel dot product of vector_a and vector_b is: {dot_product}")

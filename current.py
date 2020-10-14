import tracemalloc
tracemalloc.start()
import time
startTime = time.time()

prin

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
current, peak = tracemalloc.get_traced_memory()
print(f"Max Memory usage was {peak / 10**6}MB")
tracemalloc.stop()
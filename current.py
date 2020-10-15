import tracemalloc
tracemalloc.start()
import timeit
print('Your Output Here :')
codetotest="""
print('yogessh')
"""
print()
elapsed_time = timeit.timeit(codetotest, number=1)/1
print()
# executionTime = (int(time.time() *1000) - startTime)
# print(int(time.time() *1000))
print('Execution time in seconds: ',end ="")
print(elapsed_time)
current, peak = tracemalloc.get_traced_memory()
print(f"Max Memory usage was {peak / 10**6}MB")
tracemalloc.stop()
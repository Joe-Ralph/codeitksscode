
print()
elapsed_time = timeit.timeit(codetotest, number=1)/1
print()
# executionTime = (int(time.time() *1000) - startTime)
# print(int(time.time() *1000))
print('Execution time in seconds: ',end ="")
print(elapsed_time)
current, peak = tracemalloc.get_traced_memory()
print("Max Memory usage was "+ str(peak / 10**6)+ " MB")
tracemalloc.stop()
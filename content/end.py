
print()
elapsed_time = timeit.timeit(codetotest, number=1)/1
print()
# executionTime = (int(time.time() *1000) - startTime)
# print(int(time.time() *1000))
print('Execution time in seconds: '+str(elapsed_time)+" seconds")
current, peak = tracemalloc.get_traced_memory()
print("Max Memory usage was "+ str(peak)+ " Bytes")
tracemalloc.stop()
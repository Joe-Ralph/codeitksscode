import tracemalloc
tracemalloc.start()
import timeit
print('Your Output Here :')
codetotest="""
def getNthFibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return getNthFibonacci(n-1) + getNthFibonacci(n-2)

def getNthFibonacciMemoized(n, memo = {0:0,1:1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = getNthFibonacciMemoized(n-1,memo)+getNthFibonacciMemoized(n-2,memo)
    return memo[n]


print(getNthFibonacci(8))
"""
print()
elapsed_time = timeit.timeit(codetotest, number=1)/1
print()
# executionTime = (int(time.time() *1000) - startTime)
# print(int(time.time() *1000))
print('Execution time in seconds: '+str(elapsed_time)+" seconds")
current, peak = tracemalloc.get_traced_memory()
print("Max Memory usage was "+ str(peak)+ " Bytes")
tracemalloc.stop()
import tracemalloc
tracemalloc.start()
import timeit
print('Your Output Here :')
codetotest="""
def search(mat,key):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==key:
                return (i,j)
    return (-1,-1)

mat =[[1,2,3],[4,5,6],[7,8,9]]
search(mat,9)
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
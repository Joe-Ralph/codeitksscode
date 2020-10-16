import tracemalloc
tracemalloc.start()
import timeit
print('Your Output Here :')
codetotest="""
# UNDO REDO PROBLEM
inputList = ['WRITE A', 'WRITE B', 'WRITE C', 'UNDO', 'READ', 'REDO', 'READ']

def solution(inputList):
    stack=[]
    anslist=[]
    for i in inputList:
        if i == "UNDO":
            x = anslist.pop()
            stack.append(x)
        elif i == "REDO":
            x = stack.pop()
            anslist.append(x)
        elif i == "READ":
            print("".join(anslist),end=" ")
        else:
            anslist.append(i.split(' ')[1])
    print()

solution(inputList)

#ans AB ABC
"""
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
import tracemalloc
tracemalloc.start()
import timeit
print('Your Output Here :')
codetotest="""
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [4, 5, 6]
m = 3
n = 3


def mergeTwoLists(arr1,arr2,m,n):
    while m>0 and n>0:
        if arr1[m-1] > arr2[n-1]:
            arr1[m+n-1] = arr1[m-1]
            m-=1
        else:
            arr1[m+n-1] = arr2[n-1]
            n-=1

    while n>0:
        arr1[m+n-1] = arr2[n-1]
        n-=1

    return arr1

print(mergeTwoLists(nums1,nums2,m,n))
            

'''
Concept need to be revised: ARRAY, POINTERS
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]

Constraints:
-109 <= nums1[i], nums2[i] <= 109
nums1.length == m + n
nums2.length == n

'''
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
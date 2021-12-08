# n개의 수가 주어졌을 때, 이를 오름 차 순으로 정렬하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i,j,k = 0,0,0

    while i<len(left) and j <len(right):
        if left[i]<right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j +=1
        k+=1
    
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
    return arr

""" 퀵정렬 : 시간초과
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return
        
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)
    
    def partition(low,high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0,len(arr)-1) 
"""

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

merge_sort(nums)
print("\n".join(map(str,nums)))
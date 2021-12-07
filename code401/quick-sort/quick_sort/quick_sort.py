
def quick_sort(arr,left,right):
    if left < right:
        position = partition(arr,left, right)
        quick_sort(arr,left,position -1)
        quick_sort(arr,position +1,right) 

def partition(arr,left,right):
    # the last element is the pivot
    pivot = arr[right]
    low = left -1

    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            swap(arr,i,low)
    swap(arr,right,low +1)
    return low + 1

def swap(arr,i,low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
    return temp


      
a = [68, 13, 1, 49, 58]  
print("Before sorting array elements are - ")  
print(a)  
quick_sort(a, 0, len(a)-1)  
print("\nAfter sorting array elements are - ")  
print(a)  
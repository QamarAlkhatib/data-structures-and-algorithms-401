
def insertion_sort(arr):

    if len(arr) ==0:
        return Exception
        
    for i in range(len(arr)):
        key = arr[i]

        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key


# arr = [8,4,23,42,16,15]
arr = [5,12,7,5,5,7]
insertion_sort(arr)
for i in range(len(arr)):
    print(arr[i])
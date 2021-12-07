# Quick Sort

Merge Sort is a sorting algorithm and its a Divide and Conquer. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves.

## Pseudocode

```Pseudocode
ALGORITHM QuickSort(arr, left, right)
        if left < right
            // Partition the array by setting the position of the pivot value
            DEFINE position <-- Partition(arr, left, right)
            // Sort the left
            QuickSort(arr, left, position - 1)
            // Sort the right
            QuickSort(arr, position + 1, right)

    ALGORITHM Partition(arr, left, right)
        // set a pivot value as a point of reference
        DEFINE pivot <-- arr[right]
        // create a variable to track the largest index of numbers lower than the defined pivot
        DEFINE low <-- left - 1
        for i <- left to right do
            if arr[i] <= pivot
                low++
                Swap(arr, i, low)

        // place the value of the pivot location in the middle.
        // all numbers smaller than the pivot are on the left, larger on the right.
        Swap(arr, right, low + 1)
        // return the pivot index point
        return low + 1

    ALGORITHM Swap(arr, i, low)
        DEFINE temp;
        temp <-- arr[i]
        arr[i] <-- arr[low]
        arr[low] <-- temp
```

## Trace

- Sample Array: [8,4,23,42,16,15]

- Case 1: Sorting
![sorting](/code401/quick-sort/quick_sort_viso.png)

## Efficiency

- ```Time: average O(n*log n)``` it occurs when the array elements are in jumbled order that is not properly ascending and not properly descending
- ```Space: O(n)```  as we are not creating any container other then given array therefore Space complexity will be in order of N

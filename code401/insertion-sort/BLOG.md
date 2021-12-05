# Insertion Sort

insertion sort is an algorithm that sorts an array, it's efficient alternative to the preceding bubble sort algorithm. The principle of the insertion sort algorithm is based on the deck of cards, where we sort the cards according to a specific card. It has a lot of benefits, but the data structure also has a lot of efficient methods.

## Pseudocode

```

InsertionSort(int[] arr)

    FOR i = 1 to arr.length

    int j <-- i - 1
    int temp <-- arr[i]

    WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

    arr[j + 1] <-- temp
```

## Trace

- Sample Array: [8,4,23,42,16,15]

- Case 1: Sorting
![sorting](/code401/insertion-sort/sorting_case.png)

each line is an iteration, it checks first 2 element and then compare the result with the next element. in the final iteration, when its checks the elements and find that nothing to move that means that the array is sorted and exit the program.


## Efficency

- ```Time: o(n*2)```

- ```Space: o(1)```

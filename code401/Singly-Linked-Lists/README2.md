# Challenge Summary

Write the following methods for the Linked List class:

- append

        arguments: new value
        adds a new node with the given value to the end of the list  
- insert before

        arguments: value, new value
        adds a new node with the given new value immediately before the first node that has the value specified
- insert after

        arguments: value, new value
        adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process

- append:

![append](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/append.png?raw=true)

- insert before:

![insert before](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/insert_before.png?raw=true)

- insert after

![insert after](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/insert_after.png?raw=true)

## Approach & Efficiency

- Append:

```
the Approach was loop through the list to get the tail.
Big O : O(n), since we will be having a loop to go through from head to tail and add the value after last value
```

- insert before:
```
The approach was searching for the value then assign the value after it.
Big O: O(1), since i checked for the value without looping.
```
- insert After:
```
The approach was searching for the value with while loop.
Big O: O(n), since my condition in while loop is while self.head is true (is not none) do traversing. there is another way to do it as o(1) but i did not did it.
```
## Solution

1. clone this repo using ```git clone```
2. inside of it run ```python poetry install```
3. then ```python poetry shell```
4. if you want to run the test the cases run ```python pytest```

## Code Implementation

[Linked List](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/single-linked-list/single_linked_list/linked_list.py)

[Tests Implementation](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/single-linked-list/tests/test_single_linked_list.py)


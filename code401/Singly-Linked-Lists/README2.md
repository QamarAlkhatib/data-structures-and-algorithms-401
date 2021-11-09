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
        
- kth from end

        argument: a number, k, as a parameter.
        Return the node’s value that is k places from the tail of the linked list.
        You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous               challenges.


- zip lists
    
        Arguments: 2 linked lists
        Return: Linked List, zipped as noted below
        Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
        Try and keep additional space down to O(1)
        You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process

- append:

![append](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/append.png?raw=true)

- insert before:

![insert before](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/insert_before.png?raw=true)

- insert after

![insert after](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/insert_after.png?raw=true)

- kth from end

![kth from end](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/kth_from_end.png?raw=true)

- zip lists
    
![zipLists](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/ll_zip.png?raw=true)


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

- kth from end
```
O(n) where n is the num of nodes

````

- zip lists

```
the approach to while loop through the 2 linked list as long as they are True and then make the next of the list2 to list1 and the updating the pointer 
O(n)
```

## Solution

1. clone this repo using ```git clone```
2. inside of it run ```python poetry install```
3. then ```python poetry shell```
4. if you want to run the test the cases run ```python pytest```

## Code Implementation

[Linked List](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/single-linked-list/single_linked_list/linked_list.py)

[Tests Implementation](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/single-linked-list/tests/test_single_linked_list.py)


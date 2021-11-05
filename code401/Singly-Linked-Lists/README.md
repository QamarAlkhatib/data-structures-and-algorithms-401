# Singly Linked List

linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer

## Challenge

Node

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

Linked List

    Create a Linked List class
    Within your Linked List class, include a head property.
        Upon instantiation, an empty Linked List should be created.
    The class should contain the following methods
        insert
            Arguments: value
            Returns: nothing
            Adds a new node with that value to the head of the list with an O(1) Time performance.
        includes
            Arguments: value
            Returns: Boolean
                Indicates whether that value exists as a Node’s value somewhere within the list.
        to string
            Arguments: none
            Returns: a string representing all the values in the Linked List, formatted as:
            "{ a } -> { b } -> { c } -> NULL"

## Structure and Testing

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

    Can successfully instantiate an empty linked list
    Can properly insert into the linked list
    The head property will properly point to the first node in the linked list
    Can properly insert multiple nodes into the linked list
    Will return true when finding a value within the linked list that exists
    Will return false when searching for a value in the linked list that does not exist
    Can properly return a collection of all the values that exist in the linked list

## Code Implementation

[Linked List](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/single-linked-list/single_linked_list/linked_list.py)

[Tests Implementation](https://github.com/QamarAlkhatib/data-structures-and-algorithms-401/blob/main/code401/Singly-Linked-Lists/single-linked-list/tests/test_single_linked_list.py)

## Approach & Efficiency

So the approach was some of functions were O(n) and O(1) and the total is O(n)

## API

- Insert to the head with O(1) time complexity, This function inserts the value to the first position of the linked list

- Includes a function that checks if the value exists in the linked list or not, its returns True or False. The time complexity is O(n) since it goes through the linked list index by index to check for the value.

- Printing function, thus function print the output of the linked list, also the time complexity is O(n) since it goes through the list to print its elements.

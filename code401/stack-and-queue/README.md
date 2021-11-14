# Stacks and Queues
<!-- Short summary or background information -->

## Challenge
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue
Node

    Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

Stack

    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
        This object should be aware of a default empty value assigned to top when the stack is created.
        The class should contain the following methods:
        push
            Arguments: value
            adds a new node with that value to the top of the stack with an O(1) Time performance.
        pop
            Arguments: none
            Returns: the value from node from the top of the stack
            Removes the node from the top of the stack
            Should raise exception when called on empty stack
        peek
            Arguments: none
            Returns: Value of the node located at the top of the stack
            Should raise exception when called on empty stack
        is empty
            Arguments: none
            Returns: Boolean indicating whether or not the stack is empty.

Queue

    Create a Queue class that has a front property. It creates an empty Queue when instantiated.
        This object should be aware of a default empty value assigned to front when the queue is created.
        The class should contain the following methods:
        enqueue
            Arguments: value
            adds a new node with that value to the back of the queue with an O(1) Time performance.
        dequeue
            Arguments: none
            Returns: the value from node from the front of the queue
            Removes the node from the front of the queue
            Should raise exception when called on empty queue
        peek
            Arguments: none
            Returns: Value of the node located at the front of the queue
            Should raise exception when called on empty stack
        is empty
            Arguments: none
            Returns: Boolean indicating whether or not the queue is empty


## Approach & Efficiency

The approach was to reduce time complicity as much as possible.
 
- for stack, the time complexity is o(1) for each method
- for queue, the time complexity is o(1) for each method


## API
<!-- Description of each method publicly available to your Stack and Queue-->
- Stack:
    the methods were:
    1. pop: which removes an element from the top of stack with an O(1) Time performance.
    2. push: which adds an element to the top of stack with an O(1) Time performance.
    3. peek: which returns the top value of the stack with an O(1) Time performance.
    4.isempty: which returns boolean is the stack is empty or not with an O(1) Time performance.

- Queue
    the methods were:
    1. dequeue: which removes an element from the front of queue with an O(1) Time performance.
    2. enqueue: which adds an element to the rear of queue with an O(1) Time performance.
    3. peek: which returns the front value of the queue with an O(1) Time performance.
    4.isempty: which returns boolean is the queue is empty or not with an O(1) Time performance.

### Code implementation:

Queue: 

- [Queue code](/code401/stack-and-queue/stack_and_queue/queue.py)

- [Test queue](/code401/stack-and-queue/tests/test_queue.py)

Stack:

- [Stack code](/code401/stack-and-queue/stack_and_queue/stack.py)

- [Test Stack](/code401/stack-and-queue/tests/test_stack.py)

Pseudo Queue:

- [code](/code401/stack-and-queue/stack_and_queue/pseudo_queue.py)

- [Test](/code401/stack-and-queue/tests/test_pseudo_queue.py)

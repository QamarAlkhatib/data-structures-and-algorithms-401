from stack_and_queue.node import Node


class Stack:
    """
    A class that implement the stack data structure
    """

    def __init__(self):
        """
        Constructors of the Stack
        """
        self.top = None
        self.stack_size = 0

    def push(self,new_value):
        """
        a method that adds new Value to the stack.
        """
        new_node = Node(new_value)
        new_node.next = self.top
        self.top = new_node
        self.stack_size += 1
    

    def pop(self):
        """
        a method that removes a value from the stack.
        """
        if self.top is None:
            return Exception
    
        temp = self.top
        top = self.top.next
        temp.next = None
        self.stack_size -= 1
        return temp.data

       


    def is_empty(self):
        return self.top == None


    def peek(self):

        if self.top is None:
            return Exception
        
        return self.top.data
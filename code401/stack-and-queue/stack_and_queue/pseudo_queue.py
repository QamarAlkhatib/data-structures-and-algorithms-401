import re
from stack_and_queue.stack import Stack
from stack_and_queue.node import Node
class PseudoQueue:


    def __init__(self):
        self.stack1 = Stack() #head
        self.stack2 = Stack() #tail
        self.front = self.stack1.top
        self.rear = self.stack2.top

    
    def enqueue(self,value):
        """
        inserts value into the PseudoQueue, using a first-in, first-out approach.
        insert to the front/top
        """

        new_node = Node(value)
        new_node.next = self.front
        self.front = new_node
        self.stack1.push(new_node)


    def dequeue(self):

        """
        Extracts a value from the PseudoQueue, using a first-in, first-out approach.
        remove from the rear
        """
        if self.front is None:
            return Exception
        
        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.data
        
            

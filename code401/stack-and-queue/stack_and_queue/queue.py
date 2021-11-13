from stack_and_queue.node import Node

class Queue:
    """
    A class that implement the Queue data structure
    """

    def __init__(self):
        self.front = None
        self.rear = None
        self.queue_size = 0

    def enqueue(self,new_value):
        new_node = Node(new_value)
        if not self.rear:
            self.front =  new_node
            self.rear =  new_node
        else:
            self.rear.next =  new_node
            self.rear =  new_node
        self.queue_size += 1

    
    def dequeue(self):

        if self.front is None:
            return Exception
        temp = self.front
        self.front = self.front.next
        temp.next =  None
        self.queue_size -= 1
        return temp.data

    
    def peek(self):

        if self.front is None:
            return Exception

        return self.front.data

    def is_empty(self):
        return self.front == None
    

    
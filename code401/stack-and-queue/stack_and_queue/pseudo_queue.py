from stack_and_queue.stack import Stack
from stack_and_queue.node import Node

class  PseudoQueue():
  
    def __init__(self):

        self.stack1 = Stack()
        self.stack2 = Stack()
        self.front = self.stack1.top
        self.rear = self.stack2.top

    def enqueue(self, value):

        new_node = Node(value)

        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):

        if self.front is None:
             raise Exception

        temp = self.front.data
        self.front = self.front.next
        return temp
        
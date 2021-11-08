
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        


class LinkedList():

    def __init__(self):
        self.head = None
        

    # insert a value to the end of the linked list
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # checks is the value is exists in the linked list
    def includes(self, data):

        if self.head is None:
            return False
        else:
            currentValue = self.head
            while (currentValue is not None):
                if currentValue.data == data:
                    return True
                currentValue = currentValue.next
        return False
    
    # Add a new value to the tail of the linked list
    def append(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            return
        
        last_node = self.head
        while(last_node.next):
            last_node = last_node.next
        last_node.next = new_node
                            
    def insert_before(self, target_value, value):
        newNode = Node(value)
         
        if self.head is None:
         print("There aren't any nodes to insert before")

        else:
            if self.head.data == target_value:
              newNode.next = self.head
              self.head = newNode

        
            if self.head.next.data == target_value:
                
                newNode.next = self.head.next
                self.head.next = newNode
             
    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
         
        if current is None:
         print("There aren't any nodes to insert before")

        while current:
            if current.data == value:
                value = current.next
                current.next = new_node
                current.next.next = value
                break
            current = current.next

    def kth_from_end(self,k):
        count =0
        current = self.head
        last = self.head
        if k < count:
            return "Exception Error"

        if k > count:
            return "Exception Error"

        while current:
            if count == k+1:
                break
            count +=1
            current=current.next
        
        return current.data
    

    def __str__(self):
        output =""
        if self.head is None:
            output += 'None'
        else:
            currentValue = self.head
            while (currentValue):
                output += '{ '+ f"{currentValue.data}" + ' } -> '
                currentValue = currentValue.next
            output += "NULL"
            return output


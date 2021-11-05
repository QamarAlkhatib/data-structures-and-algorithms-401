
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

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


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(5)
    ll.insert('Hi')
    print(ll.includes(5))
    print(ll.includes(7))
    print(ll.includes(7))
    print(ll.__str__())
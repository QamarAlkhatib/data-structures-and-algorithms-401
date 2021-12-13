# from linked_list import LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self,value):
        """
        adds new value to the linked list
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
            
class HashTable(object):
    def __init__(self,size=1024):
        self.num_elements = 0
        self.size = size
        self.map = [None] * size
        

    def hash(self,key):
        sum_of_ascii = 0
        for ch in key:
            ascii_of_ch = ord(ch)
            sum_of_ascii += ascii_of_ch
        temp_value = sum_of_ascii*19 #19 here is the prime number
        hashed_key = temp_value%self.size
        return hashed_key

    def add(self,key,value):
        """
        This method adds a key/value pair to the Table
        """
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        new_value = [key,value]
        self.map[hashed_key].add(new_value)
        self.num_elements +=1
        


    def get(self,key):
        """
        return the data key 
        """
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
       
            linked_list = self.map[hashed_key]
            current = linked_list.head
            while current:
      
                if current.data[0] == key: 
                    return current.data[1]
                current = current.next
        
        return "KeyError"
        
    def contains(self,key):
        """
        return boolean if the key already exists in the table
        """
        hashed_key = self.hash(key)
        return True if self.map[hashed_key] else False
    
    def print_hash(hash_table):

        for index,key in enumerate(hash_table.map):
             if key:
                 print("index is = ",index, "  key is = ",key,end=" ")

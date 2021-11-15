# Animal here is the Node 
class Animal:
    def __init__(self,next=None):
        self.dog = 'dog'
        self.cat = 'cat'
        self.next = next

class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self,val):
        
        animal = Animal(val)

        if self.front is None:
            self.front = self.rear = animal
        else:
            self.rear.next =  animal
            self.rear =  animal


    def dequeue(self,pref):
        if self.front is not None:
            if pref == self.dog or pref == self.cat:
                
                while self.front.data != pref:

                    current_animal = self.front
                    self.front = self.front.next
                    current_animal.data = None
                    self.enqueue(current_animal.data)
                
                current_animal = self.front
                self.front = self.front.next
                current_animal.data = None
                return current_animal.data
            else:
                return None
        else:
            return Exception

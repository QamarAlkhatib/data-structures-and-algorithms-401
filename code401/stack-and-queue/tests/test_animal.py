from stack_and_queue.animal import Animal

def enqueue():
    animal = Animal(dog=Animal)
    animal.enqueue('dog')
    expected = 'dog'
    actual = animal.front.data
    assert actual == expected


# pytest is not working, i will re test once i solve the problem.
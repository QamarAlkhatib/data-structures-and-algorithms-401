from stack_and_queue.pseudo_queue import PseudoQueue
import pytest


def test_pseudo_enqueue(queue):
    queue.enqueue(5)
    actual = queue.rear.data
    expected = 5
    assert actual == expected

def test_pseudo_dequeue(queue):
    actual = queue.dequeue()
    expected =  10
    assert actual == expected


@pytest.fixture
def queue():
    queue = PseudoQueue()
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    return queue
from stack_and_queue.queue import Queue
import pytest


def test_enqueue(en_queue):
    actual = en_queue.rear.data
    expected = 'Hi'
    assert actual == expected


def test_multi_enqueue(en_queue):
    en_queue.enqueue('test')
    en_queue.enqueue('multi')
    en_queue.enqueue('enqueue')
    actual = en_queue.rear.data
    expected = 'enqueue'
    assert actual == expected


def test_size_of_queue(en_queue):
    actual = en_queue.queue_size
    expected = 2
    assert actual == expected

def test_dequeue_to_clear_queue(de_queue):
    de_queue.dequeue()
    actual= de_queue.queue_size
    expected = 0
    assert actual == expected

def test_dequeue(de_queue):
    actual = de_queue.dequeue()
    expected = 100
    assert actual == expected

def test_dequeue_from_empty(empty_queue):
    actual = empty_queue.dequeue()
    expected = Exception
    assert actual == expected

def test_peek(en_queue):
    actual = en_queue.peek()
    expected = 1
    assert actual == expected

def test_empty_peek(empty_queue):
    actual = empty_queue.peek()
    expected = Exception
    assert actual == expected

def test_is_not_empty(en_queue):
    actual = en_queue.is_empty()
    expected = False
    assert actual == expected

def test_is_empty(empty_queue):
    actual = empty_queue.is_empty()
    expected = True
    assert actual == expected

@pytest.fixture
def en_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue('Hi')
    return queue

@pytest.fixture
def de_queue():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(100)
    queue.dequeue()
    return queue

@pytest.fixture
def empty_queue():
    queue = Queue()
    queue.dequeue()
    return queue
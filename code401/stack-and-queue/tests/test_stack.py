from stack_and_queue.stack import Stack
from stack_and_queue.node import Node
import pytest


def test_push_stack(push_stack):
   actual = push_stack.top.data
   expected = 3
   assert expected == actual

def test_multi_push_stack(push_stack):
    push_stack.push('Hello')
    push_stack.push('From')
    push_stack.push('Stack')
    actual = push_stack.top.data
    expected = 'Stack'
    assert expected == actual

def test_size_of_stack(push_stack):
    actual = push_stack.stack_size
    expected = 3
    assert expected == actual

def test_pop_from_stack(pop_stack):
    actual = pop_stack.pop()
    expected = 2
    assert expected == actual

def test_pop_to_clear_stack(pop_stack):
    actual = pop_stack.stack_size
    expected = 0
    assert expected == actual

def test_pop_from_empty_stack(empty_stack):
    actual = empty_stack.pop()
    expected = Exception
    assert expected == actual

def test_is_empty(empty_stack):
    actual = empty_stack.is_empty()
    expected = True
    assert expected == actual

def test_is_not_empty(push_stack):
    actual = push_stack.is_empty()
    expected = False
    assert expected == actual
    
def test_peek(push_stack):
    actual = push_stack.peek()
    expected = 3
    assert expected == actual

def test_empty_peek(empty_stack):
    actual = empty_stack.peek()
    expected = Exception
    assert expected == actual

@pytest.fixture
def push_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack

@pytest.fixture
def pop_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    return stack

@pytest.fixture
def empty_stack():
    stack = Stack()
    return stack


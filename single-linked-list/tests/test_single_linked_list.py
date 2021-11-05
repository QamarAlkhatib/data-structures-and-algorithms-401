from single_linked_list import __version__
from single_linked_list.linked_list import LinkedList, Node
import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_empty_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual

def test_insert_Hi(ll):
    expected = '{ Hi } -> { 5 } -> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_insert_to_existing(ll):
    ll.insert(787)
    expected = '{ 787 } -> { Hi } -> { 5 } -> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_is_includes(ll):
    ll = LinkedList()
    ll.includes('Hi')
    expected = True
    actual = ll.__eq__(ll)
    assert expected == actual

# Plus I don't know how these tests passed =) (includes)'

def test_is_not_includes(ll):
    expected = False
    actual = ll.includes(10)
    assert expected == actual

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(5)
    ll.insert('Hi')
    # ll.includes(8)
    # ll.includes("Hi")
    return ll
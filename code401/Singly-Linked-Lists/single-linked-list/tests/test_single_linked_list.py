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

def test_add_to_tail(ll):
    ll = LinkedList()
    ll.append(88)
    ll.append(20)
    expected ='{ 88 } -> { 20 } -> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_insert_before(ll):
    ll.insert_before(5,200)
    expected ='{ Hi } -> { 200 } -> { 5 } -> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_insert_after(ll):
    ll.append('World')
    ll.insert_after(5,700)
    expected ='{ Hi } -> { 5 } -> { 700 } -> { World } -> NULL'
    actual = ll.__str__()
    assert expected == actual

def kth_from_end(ll):
    ll.insert(5)
    ll.insert(4)
    ll.insert(0)
    ll.insert(7)
    ll.kth_from_end(1)
    expected = '4'
    actual= ll.__str__()
    assert expected == actual


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(5)
    ll.insert('Hi')   
    return ll
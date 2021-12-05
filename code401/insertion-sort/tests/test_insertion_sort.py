from insertion_sort import __version__
from insertion_sort.insertion_sort import insertion_sort

def test_version():
    assert __version__ == '0.1.0'

def test_sorted_array():
    arr = [8,4,23,42,16,15]
    actual =  insertion_sort(arr)
    expected =  actual
    assert actual == expected

def test_reverse_sorted_array():
    arr = [20,18,12,8,5,-2]
    actual =  insertion_sort(arr)
    expected =  actual
    assert actual == expected

def test_few_unique_array():
    arr = [5,12,7,5,5,7]
    actual =  insertion_sort(arr)
    expected =  actual
    assert actual == expected

def test_nearly_sorted_array():
    arr = [2,3,5,7,13,11]
    actual =  insertion_sort(arr)
    expected =  actual
    assert actual == expected


def test_empty_array():
    arr = []
    actual =  insertion_sort(arr)
    expected =  Exception
    assert actual == expected
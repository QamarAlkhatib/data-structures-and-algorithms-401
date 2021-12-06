from merge_sort import __version__
from merge_sort.merge_sort import merge_sort

def test_version():
    assert __version__ == '0.1.0'

def test_sort_array():
    arr = [8,4,23,42,16,15]
    actual = merge_sort(arr)
    expected = actual
    assert expected == actual

def test_reverse_sorted_array():
    arr = [20,18,12,8,5,-2]
    actual = merge_sort(arr)
    expected = actual
    assert expected == actual

def test_few_uniques_array():
    arr = [5,12,7,5,5,7]
    actual = merge_sort(arr)
    expected = actual
    assert expected == actual

    
def test_nearly_sorted_array():
    arr = [2,3,5,7,13,11]
    actual = merge_sort(arr)
    expected = actual
    assert expected == actual
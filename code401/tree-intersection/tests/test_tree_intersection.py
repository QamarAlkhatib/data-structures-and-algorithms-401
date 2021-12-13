from tree_intersection import __version__
from tree_intersection.intersection_tree import tree_intersection

def test_version():
    assert __version__ == '0.1.0'

def test_intersection():  
    bt_list1 = [1,5,6,9,8,2,0,4]
    bt_list2 = [1,5,6,10]
    actual = tree_intersection(bt_list1,bt_list2)
    expected = [1, 5, 6]
    assert actual == expected
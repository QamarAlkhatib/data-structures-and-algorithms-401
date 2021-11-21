import pytest
from tree_bts.binary_tree import BinaryTree,Node,BinarySearchTree

def test_pre_order(tree):
    traverse = tree.pre_order(tree.root)
    actual = traverse(tree.root)
    excepted = [10, 20, 30, 50, 70,100]
    assert actual == excepted

def test_empty_in_order(empty_tree):
    traverse = empty_tree.in_order(empty_tree.root)
    actual = traverse(empty_tree.root)
    excepted =  "root tree is empty"
    assert actual == excepted

def test_pre_order_one_root(one_root):
    traverse = one_root.pre_order(one_root.root)
    actual = traverse(one_root.root)
    excepted = [10]
    assert actual == excepted

def test_pre_order_one_root_one_right_one_left(one_root_one_right_one_left):
    traverse = one_root_one_right_one_left.pre_order(one_root_one_right_one_left.root)
    actual = traverse(one_root_one_right_one_left.root)
    excepted = [10, 20, 70]
    assert actual == excepted

def test_post_order(tree):
    traverse = tree.post_order(tree.root)
    actual = traverse(tree.root)
    excepted = [30, 50, 20, 100, 70, 10]
    assert actual == excepted

def test_empty_post_order(empty_tree):
    traverse = empty_tree.post_order(empty_tree.root)
    actual = traverse(empty_tree.root)
    excepted =  "root tree is empty"
    assert actual == excepted

def test_pre_order(tree):
    traverse = tree.pre_order(tree.root)
    actual = traverse(tree.root)
    excepted = [10, 20, 30, 50, 70,100]
    assert actual == excepted

def test_empty_pre_order(empty_tree):
    traverse = empty_tree.pre_order(empty_tree.root)
    actual = traverse(empty_tree.root)
    excepted =  "root tree is empty"
    assert actual == excepted

def text_max_value(tree):
    actual = tree.find_max(tree.root)
    expected = 100
    assert actual == expected

def text_empty_max_value(empty_tree):
    actual = empty_tree.find_max()
    expected = ValueError
    assert actual == expected

@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(20)
    tree.root.right = Node(70)
    tree.root.left.left = Node(30)
    tree.root.left.right = Node(50)
    tree.root.right.left = Node(100)
    return tree

@pytest.fixture
def empty_tree():
    tree = BinaryTree()
    return tree

@pytest.fixture
def one_root():
    tree = BinaryTree()
    tree.root = Node(10)
    return tree

@pytest.fixture
def one_root_one_right_one_left():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(20)
    tree.root.right = Node(70)
    return tree

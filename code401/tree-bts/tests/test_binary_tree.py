import pytest
from tree_bts.binary_tree import BinaryTree,Node,BinarySearchTree

def test_pre_order(tree):
    traverse = tree.pre_order(tree.root)
    actual = traverse(tree.root)
    excepted = ["A", "B", "D", "E", "C", "F"]
    assert actual == excepted

def test_empty_in_order(empty_tree):
    traverse = empty_tree.in_order(empty_tree.root)
    actual = traverse(empty_tree.root)
    excepted =  "root tree is empty"
    assert actual == excepted

def test_pre_order_one_root(one_root):
    traverse = one_root.pre_order(one_root.root)
    actual = traverse(one_root.root)
    excepted = ["A"]
    assert actual == excepted

def test_pre_order_one_root_one_right_one_left(one_root_one_right_one_left):
    traverse = one_root_one_right_one_left.pre_order(one_root_one_right_one_left.root)
    actual = traverse(one_root_one_right_one_left.root)
    excepted = ["A", "B", "C"]
    assert actual == excepted

def test_post_order(tree):
    traverse = tree.post_order(tree.root)
    actual = traverse(tree.root)
    excepted = ['D', 'E', 'B', 'F', 'C', 'A']
    assert actual == excepted

def test_empty_post_order(empty_tree):
    traverse = empty_tree.post_order(empty_tree.root)
    actual = traverse(empty_tree.root)
    excepted =  "root tree is empty"
    assert actual == excepted

def test_pre_order(tree):
    traverse = tree.pre_order(tree.root)
    actual = traverse(tree.root)
    excepted = ["A", "B", "D", "E", "C", "F"]
    assert actual == excepted

def test_empty_pre_order(empty_tree):
    traverse = empty_tree.pre_order(empty_tree.root)
    actual = traverse(empty_tree.root)
    excepted =  "root tree is empty"
    assert actual == excepted

@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    return tree

@pytest.fixture
def empty_tree():
    tree = BinaryTree()
    return tree

@pytest.fixture
def one_root():
    tree = BinaryTree()
    tree.root = Node("A")
    return tree

@pytest.fixture
def one_root_one_right_one_left():
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    return tree

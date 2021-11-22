# Trees

implement trees with pre/post/in order travers and implement a binary search tree as a sub-class of trees with add and contains methods.

## Challenge

Features
Node

    Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Binary Tree

    Create a Binary Tree class
        Define a method for each of the depth first traversals:
            pre order
            in order
            post order which returns an array of the values, ordered appropriately.
    Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

Binary Search Tree

    Create a Binary Search Tree class
        This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
        Add
            Arguments: value
            Return: nothing
            Adds a new node with that value in the correct location in the binary search tree.
        Contains
            Argument: value
            Returns: boolean indicating whether or not the value is in the tree at least once.

Structure and Testing

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

    Can successfully instantiate an empty tree
    Can successfully instantiate a tree with a single root node
    Can successfully add a left child and right child to a single root node
    Can successfully return a collection from a preorder traversal
    Can successfully return a collection from an inorder traversal
    Can successfully return a collection from a postorder traversal

## Approach & Efficiency

Add method: O(n)
contains: o(log n)
pre-order: o(n)
post-order: o(n)
in-order:o(n)

## API

Depth First
Pre-order:root >> left >> right
In-order: left >> root >> right
Post-order: left >> right >> root
Add: add value to its right place in binary search tree
contains: return true if value is exists, otherwise false.

### There is no whiteboard since the assignment does not asked for it. also, there is no tests for the binary search tree


Solution: 

[Code implementation](/code401/tree-bts/tree_bts/binary_tree.py)

[Test implementation](/code401/tree-bts/tests/test_binary_tree.py)



Tree max method:

[Readme](/code401/tree-bts/TREEMAX.md)


Tree breadth first function:

[Readme](/code401/tree-bts/tree_breadth_first.md)
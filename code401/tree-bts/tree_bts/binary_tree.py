class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self,root):
        '''
        Pre-order: root >> left >> right
        '''
        output = []
        # closure function, private function.
        def _traverse(_root):
            if _root is None: 
                return ("root tree is empty")

            output.append(_root.value)
            if _root.left is not None:
                _traverse(_root.left)
            if _root.right is not None:
                _traverse(_root.right)
            return output
        return _traverse
      
    def in_order(self,root):
        '''
        left >> root >> right
        '''
        output = []
        # closure function, private function.
        def _traverse(_root):
           if _root is None: 
                return ("root tree is empty")


           if _root.left is not None:
               _traverse(_root.left)
        
           output.append(_root.value)

           if _root.right is not None:
               _traverse(_root.right)
           return output
        return _traverse
        
    def post_order(self,root):
        '''
        left >> right >> root
        '''
        output = []
        # closure function, private function.
        def _traverse(_root):
           if _root is None: 
                return ("root tree is empty")
           if _root.left is not None:
               _traverse(_root.left)

           if _root.right is not None:
               _traverse(_root.right)
           output.append(_root.value)
           return output
        return _traverse

    def find_max(self):
        
       if self.root is None:
           return ValueError
       _max = self.root.value
        # define a closure function
       def _traverse(node):
            nonlocal _max
            _max = node.value if node.value > _max else _max
            if node.left:
                _traverse(node.left)
            if node.right:
                _traverse(node.right)

       _traverse(self.root)

       return _max

    #    maximum = self.root.value
       
    #    if self.root.left is not None:
    #        left_max = self.find_max(self.root.left)
    #        maximum = max(maximum, left_max)

    #    if self.root.right is not None:
    #        right_max = self.find_max(self.root.right)
    #        maximum = max(maximum, right_max)
       
    #    return maximum

class BinarySearchTree(BinaryTree):

    def __init__(self):
        super().__init__()


    def add(self,value):
        if self.root is None:
          self.root = Node(value)
          return self.root
        if value < self.root.value:
            self.root.left = self.add(self.root.left,value)
        else:
            self.root.right = self.add(self.root.right,value)
        return self.root

    def contains(self,value):

        while self.root:
            if self.root == value:
                return True
            if self.root.value > value:
                self.root = self.root.left
            else:
                self.root = self.root.right
        return False


def breadth_first(root):
    list = [root]
    values = []
    
    while len(list)!=0:
        currentNode = list.pop(0)

        values.append(currentNode.value)

        if currentNode.left!=None:

            list.append(currentNode.left)
        if currentNode.right!=None:

            list.append(currentNode.right)
    return values

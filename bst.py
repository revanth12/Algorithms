# create the class of Binary Search tree
class BSTNode(object):

    """
    What the fuck is   a node in a "vanilla" BST TREE
    """

    def __init__(self,parent,k):
        """

        :param parent: Parent of the node
        :param k: key of the node
        """
        self.left = None
        self.key = k
        self.right = None
        self.parent = parent
    def _str(self):
        """ Internal method for ASCII art."""
        label = str(self.key)
        if self.left


    def __str__(self):
        return '\n'.join(self._str()[0])

    def find(self,k):
        """ Finds and returns the node with key k from the subtree rooted
        at this node.

        Args:
            k: The node with key k.

        Returns:
              The node with key k.
        """

    def insert(self,node):
        """ Inserts a node into the subtree rooted at this node"""
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent  =self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right  = node
            else:
                self.right.insert(node)

    def delete(self,node):
        if node is None:
            return
        if node.key < self.key:
            if self.left is None or self.right is None:
                if self is self.parent.left:
                    self.parent.left = self.left or self.right
                    if self.
                print("there is no node with that key")
            elif self.left:







class BST(object):
    """ A binary search Tree """
    def __init__(self, klass = BSTNode):
        """ Creates an empty BST.
        Args:
            klass (optional): The class of the node in the BST.
            Default to BSTNode.
        """
        self.root = None
        self.klass = klass

    def __str__(self):
        if self.root is None: return '<empty tree>'
        return str(self.root)

    def find(self, k):
        """
        Finds @nd returns the node with key k from the subtree rooted @t this node
        :param k:
        :return:
        """
        return self.root and self.root.find(k)

    def find_min(self):
        return self.root and self.root.find_min()

    def insert(self, k):
        """

        :param k: key of the node to be inserted
        :return: the node inserted (or) the whole tree after the insertion
        """
        node = self.klass(None, k)
        if self.root is None:
            #the root's parent is None.
            self.root = node
        else:
            self.root.insert(node)
        return node
    def delete(self,k):
        """

        :param k: key that we want to delete
        :return: the deleted node with key k
        """
        node = self.find(k)
        if node is None:
            return None

        if node is self.root:
            pseudoroot = self.root
            pseudoroot.left =



















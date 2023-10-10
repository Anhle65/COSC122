import doctest
import os

# --------------------------------------------------------------------------


def load_file(file_name):
    """ The file should contain one integer value per line.
    A list of integers is returned.
    """
    nums = [
        int(line)
        for line in open(file_name, encoding='utf-8').read().splitlines()]
    return nums


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
class Node(object):

    """Represents a node in a binary tree."""

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return str(self)

    def __str__(self):
        val = repr(self.value)
        left = repr(self.left)
        right = repr(self.right)
        return f'[{val}, l:{left}, r:{right}]'


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------


class BinarySearchTree(object):

    """Implements the operations for a Binary Search Tree."""
    # -------------------------------------------

    def __init__(self):
        self.root = None

    # -------------------------------------------
    def insert(self, value):
        """
        Inserts a new item into the tree.

        >>> b = BinarySearchTree()
        >>> b.insert(5)
        >>> b.insert(3)
        >>> b.root.left.value
        3
        >>> b.insert(4)
        >>> repr(b.root.left.right.value)
        '4'
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    # -------------------------------------------
    def _insert(self, subtree_root, value):
        """
        Recursively locates the correct position in the subtree starting
        at 'subtree_root' to insert the given 'value',
        and attaches a Node containing the 'value' to the tree.
        NOTE: _ before a method name indicates that it is a private method and
        should only be called by other methods within the class.
        Most of these private methods are recursive in this class.
        """
        if value < subtree_root.value:
            # Insert to the left
            if subtree_root.left is None:
                subtree_root.left = Node(value)
            else:
                self._insert(subtree_root.left, value)
        else:
            # Insert to the right
            if subtree_root.right is None:
                subtree_root.right = Node(value)
            else:
                self._insert(subtree_root.right, value)

    # -------------------------------------------
    def in_order_items(self):
        """
        Returns a sorted list of all items in the tree using in-order traversal.

        >>> b = BinarySearchTree()
        >>> b.insert(5)
        >>> b.insert(3)
        >>> b.insert(4)
        >>> b.in_order_items()
        [3, 4, 5]
        >>> b.insert(7)
        >>> b.in_order_items()
        [3, 4, 5, 7]
        """
        out_list = []
        # out_list will be built up as we recurse through the tree
        # out_list is change in-place so no answer is returned from _in_order_items
        self._in_order_items(self.root, out_list)
        return out_list

    # -------------------------------------------
    def _in_order_items(self, subtree_root, out_list):
        """Performs a in-order traversal of the subtree with the
        given subtree_root, adding values from visited nodes to
        out_list. Note: out_list is mutable and updated in-place so
        no answer is returned.
        """
        # ---start student section---
        if subtree_root is None:
            # return out_list
            pass
        else:
            subtree_rootl = subtree_root.left
            subtree_rootr = subtree_root.right
            if subtree_rootl != None:
                out_list.append(subtree_rootl.value) 
                self._in_order_items(subtree_rootl, out_list)
                out_list.append(subtree_root.value)
                # return subtree_root.value
            if subtree_rootr != None:
                self._in_order_items(subtree_rootr, out_list)
                out_list.append(subtree_rootr.value)
            

# if __name__ == '__main__':
#     # os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h
#     # doctest.testmod()
#     my = load_file("list0.txt")
#     minimum = []
#     my_favourite = BinarySearchTree()
#     for each in my:
#         my_favourite.insert(each)
    
#     value = my_favourite.in_order_items()
#     print(type(value))
#     value.remove(108661)
#     for num in value[888:]:
#         minimum.append(num - 108661)
#     print(min(minimum))
#     print(191 + 108661)
#     #108661

def probability_of_party_time(num_slots, num_items):
    """return a single float of probability"""
    proportion = 1/num_slots
    return float(proportion ** (num_items - 1))
def pinga(items):
    if len(items) == 0:
        print('ping', end=' ')
        return
    else:
        x = items.pop()
        print(x, end=' ')
        pinga(items)
        print(x, end=' ')
def number_of_edges(n):
    if n == 1:
        return 0
    else:
        return number_of_edges(n - 1) + 1
print(number_of_edges(5))
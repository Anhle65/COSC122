"""
Author: Anh Le :)

This is a module that implements a GeneBst and various supporting functions.

You should count each `Gene` comparison that is made.
See the handout for how to do this.
"""
import sys
from classes2 import Gene, GeneBstNode, bst_nested_repr

sys.setrecursionlimit(10**6)

# note you might want to import other things here for testing
# but your submission should only include the import line above.



class GeneBst:
    """A Gene Binary Search Tree stores Gene objects for efficient
    matching of genes to diseases, meaning faster diagnosis for
    patients.
    """

    def __init__(self, root=None):
        self.root = root
        self.comparisons = 0

    def insert(self, gene, disease):
        """
        Stores the gene, disease pair in the BST tree.
        This function updates an existing tree so:
        - If self.root is None set self.root to be a new GeneBstNode.
        - Returns Nothing
        - Assumes the gene is unlikely to already be in the tree and shouldn't check
          for the gene being in the current node first, in a similar fashion to the
          binary search from assignment 1. You must figure out which gene comparison
          is done first. The simple BST tests will help you figure it out.
        - If the gene already exists then the disease in that node should be updated
          to the given disease. This means that genes in the bst will be unique.
        NOTE: You shouldn't use recursion here as it will eventually cause
        Python to blow-up when testing large, worst case, data sets.
        """
        # ---start student section---
        if self.root is None:
            self.root = GeneBstNode(gene,disease)
        else:
            prev_node = self.root
            current = self.root
            # self.comparisons += 1
            if self.root.key > gene:
                prev_node = self.root.left
                self.comparisons += 1
                next_gene = prev_node
                if prev_node == None:
                    self.root.left = GeneBstNode(gene,disease)
                else:
                    while prev_node is not None:
                        next_gene = prev_node
                        self.comparisons += 1
                        if gene < prev_node.key:
                            prev_node = prev_node.left
                            self.comparisons += 1
                        else:
                            prev_node = prev_node.right
                            self.comparisons += 1
                    self.comparisons += 1
                    if next_gene.key == gene:
                        next_gene.value = disease
                    elif next_gene.key < gene:
                        next_gene.right = GeneBstNode(gene,disease)
                    else:
                        next_gene.left = GeneBstNode(gene,disease)
            elif self.root.key < gene:
                self.comparisons += 1
                current = self.root.right
                next_gene = current
                if current == None:
                    self.root.right = GeneBstNode(gene,disease)
                else:
                    while current is not None:
                        next_gene = current
                        self.comparisons += 1
                        if gene < current.key:
                            current = current.left
                            self.comparisons += 1
                        else:
                            current = current.right
                            self.comparisons += 1
                    self.comparisons += 1
                    if next_gene.key == gene:
                        next_gene.value = disease
                    elif next_gene.key < gene:
                        next_gene.right = GeneBstNode(gene,disease)
                    else:
                        next_gene.left = GeneBstNode(gene,disease)
            else:
                # self.comparisons += 1
                self.root.value = disease
            


        # ===end student section===

    def __getitem__(self, gene):
        """Returns the value associated with the given gene,
        or None if the gene is not present in the tree.
        - Your search should only check that the root contains the gene
          after ruling out that the gene can't be in a sub tree.
        - That is check if you need to search one of the sub trees first.
          The tests expect a specific comparison to be first, you will
          need to figure out which one it is :)
        - Returns the value/None and the number of gene comparisons used.
        NOTE: You shouldn't use recursion here as it will eventually cause
        Python to blow-up when testing large, worst case, data sets.
        """
        value = None
        # ---start student section---
        found = False
        if self.root is None:
            self.comparisons += 1
            return None
        else:
            # self.comparisons += 1
            prev_node = self.root
            current = self.root
            if self.root.key ==  gene:
                self.comparisons += 1
                value = self.root.value
            elif self.root.key < gene:
                current = self.root.right
                while current is not None and not found:
                    self.comparisons += 1
                    if current.key == gene:
                        value = current.value
                        found = True
                    elif current.key < gene:
                        current = current.right
                    else:
                        current = current.left
                self.comparisons += 1
                if not found:
                    return None
            else:
                prev_node = self.root.left
                while prev_node is not None and not found:
                    self.comparisons += 1
                    if prev_node.key == gene:
                        value = prev_node.value
                        found = True
                    elif prev_node.key < gene:
                        prev_node = prev_node.right
                    else:
                        prev_node = prev_node.left
                self.comparisons += 1
                
                if not found:
                    return None

        # ===end student section===
        return value

    def __len__(self):
        return num_nodes_in_tree(self.root)

    def __repr__(self):
        return bst_nested_repr(self.root)


def num_nodes_in_tree(root):
    """Returns the number of nodes in the tree starting at root.
    If the root is None then the number of nodes is zero.
    NOTE: recursion recommended here.
    """
    num_nodes = 0
    # ---start student section---
    if root == None:
        pass
    else:
        num_nodes_in_tree(root.left) + 1
        num_nodes_in_tree(root.right) + 1
    # ===end student section===
    return num_nodes


def bst_depth(root):
    """The level of a node is the number of edges from the root to the node
    The depth is the maximum level of nodes in a tree.
    Remember, the level of a node is how many edges there are on a path
    from the root to the node.
    So, the depth of a tree starting at the root is:
    - zero if the root is None
    - zero if the root has no children
    - 1 + the max depth of the trees starting at the left and right child
    NOTE: recursion recommended here.
    """
    depth = 0
    # ---start student section---
    if root is not None:
        rroot = root.right
        lroot = root.left
        # return bst_depth(lroot) + 1
        if lroot is not None:
            left_branch = bst_depth(lroot) + 1
            if rroot is not None:
                left_branch += 1
        elif rroot is not None:
            # if rroot is not None:
            right_branch = bst_depth(rroot) + 1
            if lroot is not None:
                right_branch += 1
        if right_branch > left_branch:
            depth = right_branch

            
    # ===end student section===
    return depth


def bst_in_order(root, result_list=None):
    """Returns a list containing (key, value) tuples
    from the bst, in the order of the keys.
    Basically does an in order traversal of the tree
    collecting (key, value) pairs as each node is visited.
    Returns an empty list if the root is None.
    This function shouldn't use any key comparisons!
    NOTE: recursion recommended here.
    """
    if result_list is None:
        result_list = []
    # ---start student section---
    else:
        bst_in_order(root.left, result_list)
        if root is not None:
            result_list.append((root.key,root.value))
        bst_in_order(root.right, result_list)
    return result_list


if __name__ == "__main__":
    # put your own simple tests here
    # you don't need to submit this code
    bst = GeneBst(root=GeneBstNode(Gene("ggt"), "Alkaptonuria"))
    gene_to_add = Gene("cat")
    value_to_add = "Crohn's disease"
    bst.insert(gene_to_add, value_to_add)
    print(bst.comparisons)
    print(bst)
    bst.comparisons = 0  # Reset comparisons.
    gene_to_add = Gene("tgt")
    value_to_add = "PCT"
    bst.insert(gene_to_add, value_to_add)
    print(bst[gene_to_add])
    print(bst)
    print(bst.comparisons)
    print("Add some tests here...")
    gene0 = Gene("ggt")
    value0 = 1234
    bst1 = GeneBst(root=GeneBstNode(gene0, value0))
    gene1 = Gene("tgt")
    value1 = "Crohn's disease"
    value2 = "Stickler syndrome"
    value3 = "Another test"
    gene2 = Gene("ttt")
    bst1.insert(gene1, value1)
    print(bst1)
    bst1.insert(gene1, value2)
    print(bst1)
    bst1.insert(gene2, value3)
    print(bst1)
    print(bst1.root.right.key, gene1)
    print(bst1.root.right.value, value2)

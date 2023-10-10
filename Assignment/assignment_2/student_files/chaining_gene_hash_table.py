"""
Author = Anh Le

This is a fun module that implements a ChainingGeneHashTable.

The table uses closed addressing.

A GeneLinkedList in each table slot is used to store
all the items that hash to a given slot.

You should count each gene comparison and each hash that is made.
"""

from classes2 import GeneLinkedList, GeneLink

# Uncomment the following line to be able to make your own testing Genes
from classes2 import Gene


class ChainingGeneHashTable:
    """A Chaining Gene Hash Table stores Gene objects for efficient
    matching of genes to diseases, meaning faster diagnosis for
    patients. This particular variation makes use of linked lists
    to handle gene hash collisions.
    """

    def __init__(self, table_size):
        """Create a hash table of the correct size, reset counters.
        Be sure to use GeneLinkedList objects in your hash table.
        """
        self.table_size = table_size
        self.comparisons = 0
        self.hashes = 0
        self.hash_table = [GeneLinkedList() for _ in range(table_size)]

    def __str__(self):
        results = []
        for i, row in enumerate(self.hash_table):
            results.append(f"  {i}: {row}")
        results = [self.__class__.__name__ + "["] + results + ["]"]
        return "\n".join(results)

    def __getitem__(self, gene):
        """Look for the given gene in the hash table.
        If the gene is present, return its disease.
        If it is not, return None.
        """
        # ---start student section---
        position = gene.__hash__() % self.table_size
        self.hashes += 1
        if self.hash_table[position].head is None:
            return None
        else:
            item = self.hash_table[position].head
            while item is not None:
                self.comparisons += 1
                prev_item = item
                item = item.next_node
                name, diease = prev_item.data
                if name == gene:
                    return diease
        # return None
        # ===end student section===


    def insert(self, gene, disease):
        """Insert the given gene and disease into the hash table
        as a gene-disease pair (tuple).
        You may assume the gene has not been previously inserted
        into the table.
        """
        # ---start student section---
        position = gene.__hash__() % self.table_size
        self.hashes += 1
        new_node = GeneLink((gene, disease))
        if self.hash_table[position].head is not None:
            last_node = self.hash_table[position].head
            prev_last = last_node
            while last_node is not None:
                prev_last = last_node
                last_node = last_node.next_node
            prev_last.next_node = new_node
        else:
            self.hash_table[position].head = new_node
        # ===end student section===


if __name__ == "__main__":
    table = ChainingGeneHashTable(5)
    table.insert(Gene('atcg'), 'Asthma')
    table.insert(Gene('tcga'), 'Leukemia')
    table.insert(Gene('gtca'), 'kemia')
    table.insert(Gene('tgca'), 'a')
    table.insert(Gene('tgac'), 'b')
    table.insert(Gene('ctag'), 'c')
    table.insert(Gene('tacg'), 'd')
    table.insert(Gene('actg'), 'e')
    table.insert(Gene('gatc'), 'f')
    table.insert(Gene('gcta'), 'g')
    table.insert(Gene('atgc'), 'h')
    table.insert(Gene('ctga'), 'ia')
    print(table)
    print("Add some tests here...")
    print(table[Gene('atcc')])
    print(table[Gene('tgca')])

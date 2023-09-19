"""
Author: your name should probably go here :)

This is a module that implements a LinearProbingGeneHashTable.

The table uses open addressing, ie, collisions are resolved by
using linear probing.

You should count each gene comparison and each hash that is made.
See the handout for how to do this.
"""


# Uncomment the following line to be able to make your own testing Genes
from classes2 import Gene
import doctest

class LinearProbingGeneHashTable:
    """A Linear Probing Gene Hash Table stores Gene objects for efficient
    matching of genes to diseases, meaning faster diagnosis for
    patients. This particular variation uses linear probing
    to handle collisions.
    >>> table = LinearProbingGeneHashTable(5)
    >>> table.insert(Gene('atcg'), 'Asthma')
    >>> table.insert(Gene('tcga'), 'Leukemia')
    >>> table.insert(Gene('gtca'), 'kemia')
    >>> table.insert(Gene('tgca'), 'a')
    >>> table.insert(Gene('tcag'), 'b')
    >>> table.insert(Gene('ctga'), 'ia')
    >>> print(table)
    LinearProbingGeneHashTable[
    0: None
    1: None
    2: (('tcga', 'Leukemia')) -> None
    3: None
    4: (('atcg', 'Asthma')) -> None
    ]
    >>> print(table[Gene('atcg')])
    Asthma
    >>> print(table[Gene('cgta')])
    None
    """

    def __init__(self, table_size):
        """Create a hash table of the correct size, reset counters."""
        self.table_size = table_size
        self.comparisons = 0
        self.hashes = 0
        self.hash_table = [None] * table_size

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
        if self.hash_table[position] == None:
            return None
        else:
            name, disease = self.hash_table[position]
            self.comparisons += 1
            if name == gene:
                return disease
        check = position + 1
        check = check % self.table_size
        while check != position:
            if self.hash_table[check] == None:
                return None
            else:
                n_name, n_disease = self.hash_table[check]
                self.comparisons += 1
                if n_name == gene:
                    return n_disease
            check = (check + 1) % self.table_size
        return None
            
        # ===end student section===

    def insert(self, gene, disease):
        """Insert the given gene and disease into the hash table
        as a gene-disease pair (tuple). If the table is full,
        raise IndexError("The table is now full.").
        You may assume the gene has not been previously inserted
        into the table.
        """
        # ---start student section---
        condition = True
        position = gene.__hash__() % self.table_size
        check = position
        if self.hash_table[check] == None:
            self.hashes += 1
            self.hash_table[check] = (gene,disease)
        else:
            check += 1
            while check != position and condition:
                check = check % self.table_size
                if self.hash_table[check] == None:
                    self.hashes += 1
                    self.hash_table[check]=(gene,disease)
                    condition = False
                check += 1
            if condition:
                raise IndexError("The table is full.")

        # ===end student section===


if __name__ == "__main__":
    # put your own simple tests here
    # you don't need to submit this code
    # table = LinearProbingGeneHashTable(5)
    # table.insert(Gene('atcg'), 'Asthma')
    # table.insert(Gene('tcga'), 'Leukemia')
    # table.insert(Gene('gtca'), 'kemia')
    # table.insert(Gene('tgca'), 'a')
    # # table.insert(Gene('tcag'), 'b')
    # print(table[Gene('atcg')])
    # table.insert(Gene('ctga'), 'ia')
    # print(table)
    # # doctest.testmod()
    # print("Add some tests here...")
    print("gtg" > "cgt")

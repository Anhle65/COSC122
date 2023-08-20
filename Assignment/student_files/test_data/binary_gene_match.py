""" Filename: binary_gene_match.py
    Author: your name should potentially go here

A module for finding the genetic similarity between 
two genomes using a binary search.
"""
from classes import GeneList, Gene, Genome


# Uncomment the following line to be able to make your own testing Genes
# from classes import Gene, Genome

def binary_gene_match(first_genome, second_genome):
    """ This function takes two Genome objects, and returns a GeneList
        and an integer.
        The second_genome will be in alphabetical/lexicographic order.
        The GeneList is of all genes that are common
        between first_genome and second_genome,
        while the integer is how many comparisons it took to find all 
        the similar genes.
        The Genes in the result GeneList should be in the same order as 
        they appear in first_genome.
        HINT: a helper function will be helpful :)
    """
    comparisons = 0
    common_genes = GeneList()
    # ---start student section---
    for gene1 in first_genome._genes:
        lower_bound = 0
        upper_bound = len(second_genome._genes) - 1
        while lower_bound <= upper_bound:
            index = (lower_bound + upper_bound) // 2
            middle = second_genome._genes[index]
            comparisons += 1
            if gene1.__lt__(middle):
                upper_bound = index - 1
            else:
                lower_bound = index + 1
        index = (lower_bound + upper_bound) // 2
        middle = second_genome._genes[index]
        comparisons += 1
        if gene1.__eq__(middle):
            common_genes.append(gene1)
        print(comparisons)


    # ===end student section===
    return common_genes, comparisons
genome1 = Genome([Gene('atcg'), Gene('ctga'), Gene('gtcg'), Gene('gtgg')])
genome2 = Genome([Gene('atcg'), Gene('ctga'), Gene('gtcg'), Gene('gtgg')])
print(binary_gene_match(genome1, genome2))
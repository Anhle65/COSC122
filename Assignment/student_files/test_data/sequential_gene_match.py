""" Filename: sequential_gene_match.py
    Author: Anh Le

A module for finding the genetic similarity between 
two genomes using a linear search.
"""
 # rom classes import Genome, Gene
from classes import GeneList, Gene, Genome

# Uncomment the following line to be able to make your own testing Genes


def sequential_gene_match(first_genome, second_genome):
    """ This function takes two Genome objects, and returns a GeneList
        and an integer. The GeneList is of all genes that are common
        between first_genome and second_genome, while the integer is how many
        comparisons it took to find all the similar genes.
        The Genes in the result GeneList should be in the same order as 
        they appear in first_genome.
    """
    common_genes = GeneList()
    comparisons = 0
    # ---start student section---
    for gene_1 in first_genome._genes:
        for gene_2 in second_genome._genes:
            comparisons += 1
            if gene_1.__eq__(gene_2):
                common_genes.append(gene_2)
                break
    # ===end student section===
    return common_genes, comparisons


# Add your small tests here, e.g:
genome1 = Genome([Gene('atcg'), Gene('ctga')])
genome2 = Genome([ Gene('atcg'),Gene('ctga'),Gene('gtcg'), ])
print(sequential_gene_match(genome1, genome2))
# ...

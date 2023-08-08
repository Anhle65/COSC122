
class Gene():
    def __init__(self, gene = None):
        self.comparisons = 0
        self.gene = gene
    def __str__(self):
        return f"{self.gene}"

class Genome(Gene):
    def __init__(self, genes):
        super().__init__(gene = None)
        self.genes = genes
        # self.string = ''
        # self.lists_gene = []
        # for gene in self.genes:
        #     gene = Gene(gene)
        #     self.lists_gene.append(gene.gene)

    def __str__(self, index = None):
        self.lists_gene = []
        for gene in self.genes:
            gene = Gene(gene)
            self.lists_gene.append(gene.gene)
        if index == None:
            # for gene in self.genes:
            #     self.string += gene + ' '
            return ' '.join(self.lists_gene)
        else:
            return self.lists_gene[index]


class GeneList(Genome):
    def __init__(self, genes = []):
        super().__init__(genes = None)
        self.common = genes
        # self.comparison(gene_2)
    # def comparison(self, other):
    #     gene_1 = Gene()
    #     gene_2 = Gene()
    #     for i in self.genes:
    #         self.gene_1.gene = i
    #         for j in other.genes:
    #             self.gene_2.gene = j
    #             self.comparisons += 1
    #             if self.gene_1.gene == self.gene_2.gene:
    #                 self.common.append(self.gene_1.gene)
                # # if i == j:
                # #     self.common.append(i)
                #     break
        # return self.comparisons, self.common
    def __str__(self):
        return f"{' '.join(self.common)}"



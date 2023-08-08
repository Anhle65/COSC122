from classes import *
a = Genome(('asfdsgdsgdg', 'afafageag', 'rtuii'))
b = Genome(('asfdsgdsgdg', 'sdfcvrfgf', 'wegreddfgreg', 'afafageag'))
c = GeneList()
def comparison():
    gene_1 = Gene()
    gene_2 = Gene()
    for i in a.genes:
        gene_1.gene = i
        for j in b.genes:
            gene_2.gene = j
            c.comparisons += 1
            if gene_1.gene == gene_2.gene:
                c.common.append(gene_1.gene)
                break
    return c.common, c.comparisons
def main ():
    result, count = comparison()
    print(c)
    print(type(c))
    # print(a.seperated_gene())
    print(a)
    print(b)
    print(count)
    print(type(a))
    print(a[0])
    
main()

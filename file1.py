def DNA_strand(dna):
    list_dna = list(dna)
    for i in range(len(list_dna)):
        a = list_dna[i]
        if a == 'A':
            list_dna[i] = 'T'
        elif a == 'T':
            list_dna[i] = 'A'
        elif a == 'G':
            list_dna[i] = 'C'
        else:
            list_dna[i] = 'G'
    return ''.join(list_dna)

print(DNA_strand('AAAA'))
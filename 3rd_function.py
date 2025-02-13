def DNA_strand(dna):
    str01 = ''
    info0 = {'A':'T','T':'A','G':'C','C':'G'}
    info01 = ' '.join(dna).split(' ')
    for i in info01:
        if i in info0:
            str01 = str01 + info0[i]
        else:
            break
    return str01
print(DNA_strand("ATTGC"))
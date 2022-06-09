
#########MATRIX PARAMETERS

### This function check if adn is correct
def is_adn(dna):
    bn = ['A', 'T', 'C', 'G']
    for i in range(len(dna)):
        for j in range(len(dna)):
            if dna[i][j] not in bn:
                return {f"Error {dna[i][j]} isn't a valid value!!"}
    return True

### This function validates array size
def array_size(dna):
    for i in range(len(dna)):
        if len(dna[i]) == len(dna):
            return is_adn(dna)


def horizontal_validation(dna, sequence):
    counter = 1
    for i in range(len(dna)):
        for j in range(len(dna)-1):
            if dna[i][j] == dna[i][j+1]:
                counter += 1
                if counter == 4:
                    sequence += 1
                    counter = 1
            else:
                counter = 1
    return sequence

def vertical_validation(dna, sequence):
    counter = 1
    for i in range(len(dna)):
        for j in range(len(dna)-1):
            if dna[j][i] == dna[j+1][i]:
                counter += 1
            else:
                counter = 1
            if counter == 4:
                sequence += 1
                counter = 1
    return sequence


def oblique_validation(dna, sequence):
    counter = 1;
    for i in range(len(dna)):
        for j in range(len(dna)):
            if i == j:
                valor = f"{dna[i-1][j-1]}"
                if dna[i][j] == valor:
                    counter += 1
                else:
                    counter = 1
                if counter == 4:
                    sequence += 1
    return sequence


def is_mutant(dna):
    if array_size(dna) == True:
        sequence = 0
        va_1 = horizontal_validation(dna, sequence)
        va_2 = vertical_validation(dna, sequence)
        va_3 = oblique_validation(dna, sequence)
        if (va_1 + va_2 + va_3) >= 2:
            return True
        elif (va_1 + va_2 + va_3) < 2:
            return False

dna =["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
humano = ["ATGCGA","CCGTGC","TTATAT","ATAAGG","CCTCTA","TCACTC"]
con_falla = ["ATGCGA","CGTGC","TPATAT","ATAAGG","CCTCTA","TCACTC"]

is_mutant(dna)



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
        if len(dna[i]) != len(dna):
            return {"Error array size!!"}
    return is_adn(dna)

def horizontal_validation(dna):
    counter = 1
    for i in range(len(dna)):
        for j in range(len(dna)-1):
            if dna[i][j] == dna[i][j+1]:
                counter += 1
                if counter == 4:
                    return True
            else:
                counter = 1
    return False

def vertical_validation(dna):
    counter = 1
    for i in range(len(dna)):
        for j in range(len(dna)-1):
            if dna[j][i] == dna[j+1][i]:
                counter += 1
            else:
                counter = 1
            if counter == 4:
                return True
    return False


def oblique_validation(dna):
    counter = 1;
    valor = None
    for i in range(len(dna)):
        for j in range(len(dna)):
            if i == j:
                valor = f"{dna[i-1][j-1]}"
                if dna[i][j] == valor:
                    counter += 1
                else:
                    counter = 1
                if counter == 4:
                    return True


def is_mutant(dna):
    if array_size(dna) == True:
        va_1 = horizontal_validation(dna)
        va_2 = vertical_validation(dna)
        va_3 = oblique_validation(dna)
        if va_1 or va_2 or va_3:
            return {"Is a Mutant"}



dna =["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]

print(is_mutant(dna))



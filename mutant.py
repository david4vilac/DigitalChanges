### This function check if adn is correct
def is_adn(dna):
    bn = ['A', 'T', 'C', 'G']
    for elemento in dna:
        for i in range(0, len(elemento)):
            if elemento[i] != bn:
                return False
            else:
                return True

### This function validates array size
def array_size(dna):
    for elemento in dna:
        if len(elemento) == len(dna):
            return True
        else:
            return False

def validacion_horizontal(dna):
    contador = 1
    for i in range(len(dna)):
        for j in range(len(dna)-1):
            if dna[i][j] == dna[i][j+1]:
                contador += 1
                if contador == 4:
                    print(f'En la fila: {dna[i]} tiene dna mutante')
                    return True
            else:
                contador = 1
    return False



def validacion_vertical(dna):
    contador = 1
    for i in range(len(dna)):
        for j in range(len(dna)-1):
            if dna[j][i] == dna[j+1][i]:
                contador += 1
            else:
                contador = 1
            if contador == 4:
                print(f'En la columna: {i+1} tiene dna mutante')
                return True

    return False



def validacion_oblicua(dna):
    contador = 1;
    valor = None
    for i in range(len(dna)):
        for j in range(len(dna)):
            if i == j:
                valor = f"{dna[i-1][j-1]}"
                if dna[i][j] == valor:
                    contador += 1
                else:
                    contador = 1
                if contador == 4:

                    print("mutante")




dna =  ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]




validacion_vertical(dna)
validacion_oblicua(dna)
#print(is_adn(dna))
#print(array_size(dna))


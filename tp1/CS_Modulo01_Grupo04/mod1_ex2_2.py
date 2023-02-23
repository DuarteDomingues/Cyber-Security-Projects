"""
Exercício 2.2 - Comparação de cifras de substituição em bytes
Realizado pelo Grupo 04:
Tiago Martins, 45240
Carlos Costa, 45231
Duarte Domingues, 45140
Miguel Távora, 45102
"""

"""
A função split_sequence divide uma sequência binária
em conjuntos de n bits
"""
def split_sequence(sequence, n):
    return [sequence[i:i+n] for i in range(0, len(sequence), n)]

"""
A função cifras_sustituicao_bytes permite realizar, a partir de uma chave K, 
4 tipos de substituições diferentes
"""
def cifras_sustituicao_bytes(byte, n):
    m = byte
    k = "11010101"

    m = split_sequence(m,n)   # divisão do byte em blocos de n bits
    k = split_sequence(k,n)   # divisão da chave em blocos de n bits

    cifra_byte = ""

    for i in range(0, len(m)):
        a = m[i]
        a = int(a,2)        # bloco de bits convertido para número inteiro (decimal)
        b = k[i]
        b = int(b,2)        # bloco de bits convertido para número inteiro (decimal)
        c = (a+b)%(2**n)    # soma dos números em módulo de 2^n
        c = "{0:0{n}b}".format(c, n=n)  # conversão de volta para bits
        cifra_byte += str(c)    # concatenação dos vários blocos de bits

    #print(cifra_byte)
    return cifra_byte



if __name__ == '__main__':

    byte = input("Insira uma sequência de 8 bits:\n")
    n = input("Indique a operação a realizar (valor de n):\n")
    n = int(n)

    cifra_byte = cifras_sustituicao_bytes(byte, n)

    print("A sequência de bits obtida é: " + cifra_byte)

    




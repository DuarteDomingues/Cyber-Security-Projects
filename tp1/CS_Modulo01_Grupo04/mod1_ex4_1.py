"""
Testes do Exercício 4.1 - Construção de Merkle-Damgård
Realizado pelo Grupo 04:
Tiago Martins, 45240
Carlos Costa, 45231
Duarte Domingues, 45140
Miguel Távora, 45102
"""

import numpy as np
s = 16
n = 4

"""
A função hash_MD_funcaof calcula o hash de uma
sequencia de bits
"""
def hash_MD_funcaof(m, H0):

    mArr = splitToBlocks(m)

    hashM = H0
    H = [hashM]

    for m in mArr:
        hashM = hashProcess(m,hashM)
        H.append(hashM)

    return H


"""
A função splitToBlocks divide uma sequencia
de bits em blocos de l bits 
"""
def splitToBlocks(m):

    isLast = False

    i = 0
    l = s-n
    space = 0
    mList = []

    while(isLast==False):
        
        mi = m[space:l+space]
        space= space + l
        if (len(mi) < l):
            
            #padding oneZeros
            mi = oneZerosPadding(mi,l)
            isLast = True

        mList.append(mi)
    
    mList.append(fillLengthBlock(l))
    return mList
    
"""
A função oneZerosPadding realiza o padding
a uma sequencia de bits
"""
def oneZerosPadding(mi, l):
    c=0
    while (len(mi) < l):

        if ( c==0):
            mi = mi + '1'
        
        else :
            mi = mi + '0'
        
        c=c+1
    return mi

"""
A função fillLengthBlock preenche um bloco de
tamanho l com esse mesmo tamanho em binário
"""
def fillLengthBlock(l):

    lengthBlock = ''
    
    #length of block to binary
    blockSize = np.binary_repr(l)
    
    while (len(lengthBlock) < (l - len(blockSize))):
        lengthBlock = lengthBlock + '0'
    
    lengthBlock = lengthBlock + blockSize
    return lengthBlock

"""
A função hashProcess aplica o hash H à mensagem m
"""
def hashProcess(m, H):

    hashM = int(H, 2)

    numBlocks =  len(m)/n + 1
    numBlocks = int(numBlocks)
    space = 0
    for i in range (numBlocks-1):

        hashM  = hashM + int(m[space : n+space], 2)
        space = space + n

    hashM = np.binary_repr(hashM % s)
    while(len(hashM) < 4):
        hashM = '0' + hashM
    
    return hashM


if __name__ == '__main__':
    print(hash_MD_funcaof('010101010101010000', '1111'))






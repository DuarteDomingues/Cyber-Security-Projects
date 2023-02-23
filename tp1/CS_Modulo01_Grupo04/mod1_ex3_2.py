"""
Exercício 3.2 - Parâmetros e cifra RSA
Realizado pelo Grupo 04:
Tiago Martins, 45240
Carlos Costa, 45231
Duarte Domingues, 45140
Miguel Távora, 45102
"""

"""
A função gcd calcula o máximo divisor comum
entre dois números inteiros
"""
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

"""
A função keys_rsa gera as chaves pública e privada
para a cifra RSA
"""
def keys_rsa(p,q):

    n = p*q     
    phi = (p-1)*(q-1)
    e = 2
    while ( e < phi):   # loop para encontrar um valor de e que seja invertível
        if(gcd(e, phi) ==1):
            break
        else:
            e=e+1

    d=0
    
    while (True):   # loop que calcula o inverso de e
        if(d * e % phi == 1):
            break
        else:
            d=d+1

    kPub = (n,e)    # chave pública
    kPriv = (n,d)   # chave privada

    print("n: ",n)
    print("phi: ",phi)
    print("e: ",e)
    print("d:",d)

    return kPub, kPriv

"""
Na função main é testada a cifra RSA e a respetiva decifragem
"""
if __name__ == '__main__':
    pub,priv = keys_rsa(5,11)

    n = pub[0]
    e = pub[1]
    d = priv[1]

    # ORIGINAL MESSAGE
    M = 10
    print("ORIGINAL MESSAGE:", M)
    M = int(str(M),2)   # conversão para inteiro

    # MESSAGE ENCRIPTION
    C = (M**e)%n
    C_bits = "{0:0{n}b}".format(C, n=2)  # conversão de volta para bits
    print("ENCRIPTED MESSAGE:", C_bits)

    # MESSAGE DECRIPTION
    M_DEC = (C**d) % n
    M_DEC_bits = "{0:0{n}b}".format(M_DEC, n=2)  # conversão de volta para bits
    print("DECRIPTED MESSAGE:", M_DEC_bits)





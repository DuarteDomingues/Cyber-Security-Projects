"""
Exercício 1.4 - A cifra de Belaso-Vigènere
Realizado pelo Grupo 04:
Tiago Martins, 45240
Carlos Costa, 45231
Duarte Domingues, 45140
Miguel Távora, 45102
"""

import math

"""
A função letra_para_numero converte uma letra do alfabeto (minuscula) no seu número correspondente,
correspondendo ao "a" o 0, ao "b" o 1, etc...
"""
def letra_para_numero(letra):
    numero = ord(letra) - 97 # a função ord() retorna o inteiro que representa o unicode de um certo carater
    #print(numero)
    return numero

"""
A função numero_para_letra converte um número inteiro na letra do alfabeto (maiuscula) correspondente,
correspondendo ao 0 o A, ao 1 o B, etc...
"""
def numero_para_letra(numero):
    letra = (chr(ord('@')+numero+1))
    #print(letra)
    return letra

"""
A função belaso_vigenere obtém o texto cifrado a partir do texto em claro e da palavra-chave designada
"""
def belaso_vigenere(texto_claro, palavra_chave):
    K = palavra_chave
    texto_cifrado = ""

    tamanho = len(texto_claro)
    K_tamanho = len(K)
    a = math.ceil(tamanho/K_tamanho)
    K = K*a
    K = K[0:tamanho]    # coloca a palavra-chave com o mesmo número de carateres que o texto em claro
    K = K.lower()

    for i in range(0,tamanho):  
        letra_texto = texto_claro[i]
        letra_K = K[i]

        numero_texto = letra_para_numero(letra_texto)   # obtém número correspondente à letra do texto em claro
        numero_K = letra_para_numero(letra_K)           # obtém número correspondente à letra da palavra-chave

        novo_numero = (numero_texto + numero_K)%26      # obtém o novo número realizando a soma em módulo 26 
        #print(novo_numero)
        nova_letra = numero_para_letra(novo_numero)     # converte de volta para uma letra
        #print(nova_letra)
        texto_cifrado += nova_letra

    #print(texto_cifrado)
    return texto_cifrado


if __name__ == '__main__':

    texto_claro = input("Insira o texto a cifrar (em minusculas e sem espaços):\n")
    chave = input("Insira a chave (em maiusculas):\n")

    texto_cifrado = belaso_vigenere(texto_claro, chave)
    print("O texto cifrado é: " + texto_cifrado)
    
import nltk


listaPalavras=[]
f = open('/Users/Patrick F/Desktop/projeto/ambienteVirtual/Corretor/dicionario.txt', 'r', encoding='utf8')
tokens = nltk.tokenize.word_tokenize(f.read())
for token in tokens:
    if token.isalpha():
        listaPalavras.append(token.lower())


def principal(texto):
    lista = tratamento(texto)
    listaPalavras = []
    palavra_certa = []
    for palavra in lista:
        listaPalavras += geradorPalavras(palavra)
        palavra_certa.append(max(listaPalavras,key=probabilidade))
        listaPalavras = []
    return palavra_certa

def tratamento(texto):
    listaPalavras=[]
    tokens = nltk.tokenize.word_tokenize(texto)
    for token in tokens:
        if token.isalpha():
            listaPalavras.append(token.lower())
    return listaPalavras

def geradorPalavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    possibilidades = inserirLetra(fatias)
    possibilidades += deletandoLetra(fatias)
    possibilidades += trocaLetra(fatias)
    possibilidades += inverteLetra(fatias)
        
    return possibilidades

def inserirLetra(palavras):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in palavras:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras

def deletandoLetra(palavras):
    novas_palavras = []
    for E, D in palavras:
        novas_palavras.append(E + D[1:])
    return novas_palavras

def trocaLetra(palavras):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzáâàãéêèẽíîìĩóôõòúûùũç'
    for E, D in palavras:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])
    return novas_palavras

def inverteLetra(palavras):
    novas_palavras = []
    for E, D in palavras:
        if len(D) > 1:
            novas_palavras.append(E + D[1] + D[0] + D[2:])
    return novas_palavras

def probabilidade(palavras_gerada):
    total_palavras = len(listaPalavras)
    frequencia = nltk.FreqDist(listaPalavras)
    return frequencia[palavras_gerada]/total_palavras

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a
      ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
        #Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    ttr = float(input("Entre a relação Type-Token:"))
        #Relação Type-Token: Número de palavras diferentes utilizadas em 
        # um texto divididas pelo total de palavras.
    hlr = float(input("Entre a Razão Hapax Legomana:"))
        #Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido
        #  pelo número total de palavras.
    sal = float(input("Entre o tamanho médio de sentença:"))
        #Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    sac = float(input("Entre a complexidade média da sentença:"))
        #Complexidade de sentença: Média simples do número de frases por sentença.
    pal = float(input("Entre o tamanho medio de frase:"))
        #Tamanho médio de frase: Média simples do número de caracteres por frase.

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada
    texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras 
    que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras 
    diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver 
    o grau de similaridade nas assinaturas.'''

    as1  = as_a
    as2  = as_b
    dift = 0 
    
    for i in range (6):
        dif = abs (as1[i] - as2[i])
        dift += dif

    similaridade = dift / 6
    return similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    assinatura = [media_caract(texto), type_token (texto), Hapax (texto), med_sentenca(texto), 
                  med_comple(texto), med_frase(texto)]
    return assinatura

def caracteres_t (texto):
    '''Essa função recebe um texto e retorna a quantidade total de caracteres'''

    total_caracteres = 0
    sentenças = separa_sentencas (texto)
    for sentença in sentenças:
        frases = separa_frases (sentença)
        for frase in frases:
            palavras = separa_palavras (frase)
            for palavra in palavras:
                total_caracteres += len(palavra)
    return total_caracteres

def palavras_t (texto):
    '''Essa função recebe um texto e retorna a quantidade total de palavras'''

    total_palavras = 0
    sentenças = separa_sentencas (texto)

    for sentença in sentenças:
        frases = separa_frases (sentença)
        for frase in frases:
            palavras = separa_palavras (frase)
            total_palavras += len (palavras)
    return total_palavras

def media_caract (texto):
    '''Recebe a quantidade total de caracteres de um texto e 
    retorna a média aritimética de caracteres por palavra'''

    walt = caracteres_t(texto) / palavras_t(texto)
    return walt

def type_token (texto):
    '''Retorna a média entre o número de palavras diferentes em comparação com 
    o número total de palavras'''    

    ttrt = 0
    palavras_d = 0
    total_palavras = []
    sentenças = separa_sentencas (texto)

    for sentença in sentenças:
        frases = separa_frases (sentença)
        for frase in frases:
            palavras = separa_palavras (frase)
            total_palavras.extend (palavras)

    palavras_d += n_palavras_diferentes (total_palavras)
    ttrt = palavras_d / palavras_t(texto)
    return ttrt

def Hapax (texto):
    '''retorna a proporção entre o número de palavras utilizado uma única vez 
    e a quantidade total de palavras'''

    hlrt = 0
    palavras_u = 0
    total_palavras = []
    sentenças = separa_sentencas (texto)

    for sentença in sentenças:
        frases = separa_frases (sentença)
        for frase in frases:
            palavras = separa_palavras (frase)
            total_palavras.extend (palavras)
            
    palavras_u = n_palavras_unicas(total_palavras)
    hlrt = palavras_u / palavras_t(texto)
    return hlrt

def med_sentenca (texto):
    '''Retorna a média aritmética do número de caracteres por sentença'''

    salt = 0
    nsentenças = len (separa_sentencas (texto))
    scaracteres = 0
    sentenças = separa_sentencas (texto)
        
    for sentença in sentenças:
        scaracteres += len (sentença)
            
    salt = scaracteres / nsentenças
    return salt

def med_comple (texto):
    '''Retorna a média aritmética do número de frases por sentença'''

    sact = 0
    nsentenças = len (separa_sentencas (texto))
    sentenças = separa_sentencas (texto)
    nfrases = 0

    for sentença in sentenças:
        frases = separa_frases (sentença)
        for frase in frases:
            nfrases += 1
    
    sact = nfrases / nsentenças 
    return sact 

def med_frase (texto):
    '''Retorna a média artmética do número de caracteres por frase'''

    palt = 0
    ncaracteres = 0
    nfrases = 0 
    sentenças = separa_sentencas (texto)

    for sentença in sentenças:
        frases = separa_frases (sentença)
        for frase in frases:
            nfrases += 1
            ncaracteres += len (frase)

    palt = ncaracteres / nfrases
    return palt 


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp 
    e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido 
    infectado por COH-PIAH.'''
    
    simi = 0
    suspeitos = textos
    comparados = []

    for texto in suspeitos:
        as_t = calcula_assinatura (texto)
        simi = compara_assinatura (as_t, ass_cp)
        comparados.append (simi)
    maior_prob = min (comparados)
            
    return comparados.index (maior_prob) + 1

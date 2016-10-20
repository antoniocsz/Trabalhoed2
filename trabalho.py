from string import ascii_lowercase


def is_tamanho(tamanho, istring):
    if len(istring) > tamanho:
        return False
    return True


def trata_texto(tamanho, texto):
    texto = texto.rstrip()
    if len(texto) > tamanho:
        texto = texto[:tamanho-1]
    return texto


def buscar_padrao(texto, transicoes):
    '''busca o padrao no texto'''
    tamanho = len(transicoes)
    estado = 0
    ocorrencias = []
    for count, char in enumerate(texto):
        estado = transicoes[estado][char]
        if estado == tamanho:
            ocorrencias.append(count - tamanho +1)
            estado = 0
    return ocorrencias


def gerar_tabela(padrao):
    alfabeto = ascii_lowercase + ' .,'
    TAM = len(padrao)
    transicoes = [ {caracter : 0 for caracter in alfabeto} for i in range(TAM) ]
    for count in range(TAM):
        for caracter in alfabeto:
            k = min(TAM, count+1)
            while (padrao[:count]+caracter)[-k:] != padrao[:k]:
                k-=1
            transicoes[count][caracter]=k
    return transicoes


def imprimir_tabela(texto, padrao):
    tabela = gerar_tabela(padrao)
    print ('Tabela Delta:')
    estado = 0
    for count, char in enumerate(texto):
        estado = tabela[estado][char]
        print ("[{},'{}']:{}".format(estado, char, count+1))


def main(texto, padrao):
    opcao = input()
    while opcao != 'e':
        if opcao == 's':
            ocorrencias = buscar_padrao(texto, gerar_tabela(padrao))
            for ocorrencia in ocorrencias:
                print (ocorrencia)
        if opcao == 'u':
            imprimir_tabela(texto, padrao)
        opcao = input()
    exit()


if __name__ == '__main__':
    quantidade = int(input())
    texto = input()
    padrao = input()

    if not is_tamanho(quantidade, texto):
        texto = trata_texto(quantidade, texto)
    if not is_tamanho(quantidade, padrao):
        padrao = trata_texto(quantidade, padrao)

    main(texto, padrao)

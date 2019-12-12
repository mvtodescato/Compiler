erroSem = 0
def duplica(nome,j):
    while j<len(TS):
        if TS[j][3] == 'decl':
            if TS[j+1][2] == nome:
                return 1
        j = j+1
    return 0

def verifica(nome,local,linha):
    global erroSem
    erro = 1  #Erro 1: atribuição não encontrada, Erro 2: duas atribuições, Erro 3: atribuição dentro de escopo inapropriado, Erro 4: Atribuição depois de utilizar a variavel
    for j in range(len(TS)):
        if TS[j][3] == 'decl':
            if TS[j+1][2] == nome:
                if TS[j][4] == local or TS[j][4] == 'all':
                    if duplica(nome,j+1) == 0:
                        if TS[j][1] > linha:
                            erro = 4
                            erroSem = 1
                            break
                        else:
                            erro = 0
                            break
                    else:
                        erro = 2
                        erroSem = 1
                        break
                else:
                    erroSem = 1
                    erro = 3
                    break
    if erro == 1:
        erroSem = 1
        print("ERRO!!! Declaração para varivel " + nome + " não encontrada!")
        print("Linha: " + linha)
    elif erro == 2:
        print("ERRO!!! Duas declarações encontradas para a variavel " + nome)
        print("Linha: " + linha)
    elif erro == 3:
        print("ERRO!!! Declaração dentro de escopo inapropriado para a váriavel " + nome)
        print("Linha: " + linha)
    elif erro == 4:
        print("ERRO!!! Declaração depois de utilizar a váriavel " + nome)
        print("Linha: " + linha)


TS = []
arquivo = open('TS.txt','r')
for linha in arquivo:
    linha = linha.rstrip('\n')
    aux = linha.split(' ')
    TS.append(aux)
arquivo.close()
for i in range(len(TS)):
    if TS[i][3] == 'oplvar' or TS[i][3] == 'opvar':
        verifica(TS[i][2],TS[i][4],TS[i][1])
if erroSem == 1:
    print("Erro Semantico!!!")
else:
    print("Sem erros semanticos")
    import cod_int
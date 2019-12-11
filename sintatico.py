import xml.etree.ElementTree as ET
dic = {'$':'0','j':'20','D':'22','K' :'10','Q':'23','I':'5','g':'15','B':'17','J':'6','W':'18','X':'11','e':'9','Y':'12','^':'21','H':'19','c':'14','_':'13','b':'4','l':'7','k':'8','`':'3','d':'16'}
fita = []
pilha = ['0']
arquivo = "parser.xml"
tree =  ET.parse(arquivo)
root = tree.getroot()
filtro = "*"
in_state = 0
acpt = 0
rt = 0
TS = []

def empilha(estado):
    pilha.append(fita[0])
    pilha.append(estado)
    del(fita[0])

def salto(estado):
    pilha.append(estado)

def reduz(prod):
    global rt
    in_state = 0
    tam = len(pilha)
    for child in root.iter(filtro):
        if child.tag == "Production" and child.attrib["Index"] == prod:
            for i in range(int(child.attrib["SymbolCount"]) * 2):
                if (int(child.attrib["SymbolCount"])*2) >= tam:
                    rt = 0
                    break
                del(pilha[tam-i-1])
            pilha.append(child.attrib["NonTerminalIndex"])
            value = child.attrib["NonTerminalIndex"]
        if child.tag == "LALRState":
            if child.attrib["Index"] == pilha[len(pilha)-2]:
                in_state=1
        if child.tag == "LALRAction" and in_state == 1:
            if child.attrib["SymbolIndex"] == pilha[len(pilha)-1]:
                pilha.append(child.attrib["Value"])
                break


def percorre():
    in_state = 0
    global acpt
    global rt
    for child in root.iter(filtro):
        if child.tag == "LALRState":
            if child.attrib["Index"] == pilha[len(pilha)-1] :
                in_state = 1
        if child.tag == "LALRAction" and in_state == 1:
            if child.attrib["SymbolIndex"] == fita[0]:
                if child.attrib["Action"]=='1':
                    rt = 1
                    empilha(child.attrib["Value"])
                    break
                if child.attrib["Action"]=='2':
                    rt = 1
                    reduz(child.attrib["Value"])
                    break
                if child.attrib["Action"]=='3':
                    rt = 1
                    salto(child.attrib["Value"])
                    break
                if child.attrib["Action"] == '4':
                    acpt = 1
                    rt = 1
                    break

def translate():
    for i in range(len(fita)):
        fita[i] = dic[fita[i]]

def infos():
    #mudar para lista o where para melhor controle
    #arrumar tab no lexico
    index = 0
    cont = 0
    where = 'all'
    while index<len(TS):
        if cont == 0:
            where = 'all'
        if TS[index][0] == 'j':
            #atribuiçao
            TS[index][3] = 'atrib'
            TS[index].append(where)
            index = index + 1
            TS[index][3]= 'var'
            TS[index].append(where)
            index = index + 1
            TS[index][3] = 'N'
            TS[index].append('N')
        elif TS[index][0] == 'Q':
            TS[index][3] = 'cond'
            TS[index].append(where)
            where = 'cond'
            cont = cont + 1
            #if
        elif TS[index][0] == '^':
            cont = cont + 1
            TS[index][3] = 'N'
            TS[index].append('N')
            where = 'cond'
        elif TS[index][0] == 'Y':
            cont = cont - 1
            TS[index][3] = 'N'
            TS[index].append('N')
        elif TS[index][0] == 'I':
            TS[index][3] = 'N'
            TS[index].append('N')        
        elif TS[index][0] == 'X':
            TS[index][3] = 'N'
            TS[index].append('N')
        elif TS[index][0] == 'D':
            index = index + 1
            if TS[index][0] == 'e':
                TS[index-1][3] = 'opvar'
                TS[index-1].append(where)
                TS[index][3] = 'N'
                TS[index].append('N')
                index = index + 1
                while(TS[index][0] != 'K'):
                    if TS[index][0] == 'D':
                        TS[index][3] = 'opvar'
                        TS[index].append(where)
                    else:
                        TS[index][3] = 'N'
                        TS[index].append('N')
                    index = index + 1
                TS[index][3] = 'N'
                TS[index].append('N')
            else:
                TS[index-1][3] = 'oplvar'
                TS[index-1].append(where)
                TS[index][3] = 'N'
                TS[index].append('N')
                index = index + 1
                if TS[index][0] == 'e':
                    TS[index][3] = 'oplvar'
                    TS[index].append(where)
                else:
                    TS[index][3] = 'N'
                    TS[index].append('N')
                index = index + 1
                TS[index][3] = 'N'
                TS[index].append('N')                  
            #opl ou op
        elif TS[index][0] == 'H':
            TS[index][3] = 'rep'
            TS[index].append(where)
            where = 'rep'
            cont = cont + 1
            #while/fon
        index = index + 1
    print('Tabela de Simbolos com informações')
    print(TS)  


def sintatico():
    translate()
    global rt
    while acpt == 0:
        percorre()
        #print(pilha)
        #print(fita)
        if acpt == 1:
            print("Nenhum erro sintatico localizado")
            infos()
        elif rt == 0:
            print("Erro sintatico!!!")
            break
        rt = 0

arquivo = open('fita_saida.txt','r')
for linha in arquivo:
    for caractere in linha:
        fita.append(caractere)
arquivo.close()

arquivo = open('TS.txt','r')
for linha in arquivo:
    linha = linha.rstrip('\n')
    aux = linha.split(' ')
    TS.append(aux)
arquivo.close()
        
sintatico()
if acpt == 1:
    with open('TS.txt', 'w') as arquivo:
            for valor in TS:
                for v in valor:
                    arquivo.write(str(v) + ' ')
                arquivo.write('\n')
    arquivo.close()
    import semantico
            
            
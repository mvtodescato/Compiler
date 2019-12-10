codigo = []
asm = []
TS = []

def geracod(i):
    cont = 0
    var = i
    i = i + 2
    while 1:
        if TS[i][2] == '*' or TS[i][2] == '/':
            print("KKKKK1")
            #verificar se é variavel ou constante e guardar em uma temporaria + count (tira os dois valores da tabela e o operador e deixa apenas 1 com a informação sobre a variavel temporaria)
        elif TS[i][2] == ';':
            break
        i = i+1
    i = var + 2
    while 1:
        if TS[i][2] == '+' or TS[i][2] == '-':
            print("KKKKK2")
            #verificar se é variavel ou constante e guardar em uma temporaria + count (tira os dois valores da tabela e o operador e deixa apenas 1 com a informação sobre a variavel temporaria)
        elif TS[i][2] == ';':
            break
        i = i+1
    if cont == 0:
        print("KKKKK3")
        #isso quer dizer que é apenas um var = 2 ou var = var














arquivo = open('TS.txt','r')
for linha in arquivo:
    linha = linha.rstrip('\n')
    aux = linha.split(' ')
    TS.append(aux)
arquivo.close()
for i in range(len(TS)):
    if TS[i][3] == 'opvar':
        geracod(i)
        break
codigo = []
asm = []
TS = []

def geracod(i):
    cont = 0
    var = i
    i = i + 2
    while 1:
        if TS[i][2] == '*' or TS[i][2] == '/':
            codigo.append(['T'+str(cont),'=',TS[i-1][2],TS[i][2],TS[i+1][2]])
            del(TS[i-1])
            del(TS[i-1])
            TS[i-1][2] = 'T'+str(cont)
            cont = cont + 1
            i = var + 1
        elif TS[i][2] == ';':
            break
        i = i+1
    i = var + 2
    while 1:
        if TS[i][2] == '+' or TS[i][2] == '-':
            codigo.append(['T'+str(cont),'=',TS[i-1][2],TS[i][2],TS[i+1][2]])
            del(TS[i-1])
            del(TS[i-1])
            TS[i-1][2] = 'T'+str(cont)
            cont= cont + 1
            i = var + 1
        elif TS[i][2] == ';':
            break
        i = i+1
    if cont == 0:
        codigo.append([TS[var][2],'=',TS[var+2][2]])
    else:
        codigo.append([TS[var][2],'=',codigo[len(codigo)-1][0]])
    print("Código:")
    print(codigo)

def geraASM():
    for i in range(len(codigo)):
        asm.append(['LOAD',codigo[i][2]])
        if len(codigo[i]) > 3:
            if codigo[i][3] == '*':
                asm.append(['MULT',codigo[i][4]])
            elif codigo[i][3] == '/':
                asm.append(['DIV',codigo[i][4]])
            elif codigo[i][3] == '+':
                asm.append(['ADD',codigo[i][4]])
            elif codigo[i][3] == '-':
                asm.append(['SUB',codigo[i][4]])
        asm.append(['STR',codigo[i][0]])
    print("Código de maquina:")
    print(asm)
    with open('Cod_intermediario.txt', 'w') as arquivo:
            for valor in asm:
                for v in valor:
                    arquivo.write(v + ' ')
                arquivo.write('\n')
    arquivo.close()











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
geraASM()
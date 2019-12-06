import xml.etree.ElementTree as ET

fita = ['21','13','16','8','0']
pilha = ['0']
arquivo = "teste.xml"
tree =  ET.parse(arquivo)
root = tree.getroot()
filtro = "*"
in_state = 0
acpt = 0

def empilha(estado):
    pilha.append(fita[0])
    pilha.append(estado)
    del(fita[0])

def salto(estado):
    pilha.append(estado)

def reduz(prod):
    in_state = 0
    tam = len(pilha)
    for child in root.iter(filtro):
        if child.tag == "Production" and child.attrib["Index"] == prod:
            for i in range(int(child.attrib["SymbolCount"]) * 2):
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
    for child in root.iter(filtro):
        if child.tag == "LALRState":
            if child.attrib["Index"] == pilha[len(pilha)-1] :
                in_state = 1
        if child.tag == "LALRAction" and in_state == 1:
            if child.attrib["SymbolIndex"] == fita[0]:
                if child.attrib["Action"]=='1':
                    empilha(child.attrib["Value"])
                    break
                if child.attrib["Action"]=='2':
                    reduz(child.attrib["Value"])
                    break
                if child.attrib["Action"]=='3':
                    salto(child.attrib["Value"])
                    break
                if child.attrib["Action"] == '4':
                    acpt = 1
                    break


def main():
    while acpt == 0:
        percorre()
        print(pilha)
        print(fita)



main()
            
            
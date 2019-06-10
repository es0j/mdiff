import sys
import pdb
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BGBLUE = '\33[44m'

def criarMatriz(nome):
    m=[]
    try:
        with open(nome,"r") as arq:
            for linha in arq:
                
                if linha[-1]=="\n":
                    linha=linha[:-1]
                m.append(linha)
    
        return m
    except:
        print("nao foi possivel abrir o arquivo %s"%nome)
        sys.exit(-1)

def converter(texto,cor,cor2=""):
    return cor + texto + bcolors.ENDC

def usage():
    print("Uso: python3 mdiff.py <arq1> <arq2> <arq3> ....")

def inserir(string,posicaoInicial,posFinal,texto1,texto2):
    return string[:posicaoInicial]+texto1+string[posicaoInicial:posFinal]+texto2+string[posFinal:]

def linhaIgual(listaLinhas):
    igual=True
    for i in range(len(listaLinhas)-1):
        if listaLinhas[i]!=listaLinhas[i+1]:
            igual=False
            break

    return igual


def addInList(lista,caractere):
    for i in range(len(lista)):
        lista[i]=lista[i]+caractere
    return lista
def confLinhas(linhas):
    INICIO=bcolors.WARNING
    FIM=bcolors.ENDC
    
    novasLinhas=[""]*len(linhas)
    indiceNovasInicio=0
    colorido=False
    tamanho=min([len(k) for k in linhas])
    for caractereIndice in range(tamanho):
        if (not linhaIgual([x[caractereIndice] for x in linhas]) and colorido==False):
            novasLinhas=addInList(novasLinhas,INICIO)
            colorido=True

        if linhaIgual([x[caractereIndice] for x in linhas]) and colorido==True:
            novasLinhas=addInList(novasLinhas,FIM)
            colorido=False
    
        for i in range(len(linhas)):
            novasLinhas[i]+=linhas[i][caractereIndice]
    if colorido==True:
        novasLinhas=addInList(novasLinhas,FIM)


    return novasLinhas 


def checar(lista):
    planilhas=[]
    inicio="nomes:"
    for i in lista:
        inicio+="%s|"%i
    print(inicio)
    for i in lista:
        planilhas.append(criarMatriz(i))
    #planilhas=[["119D8000262000080007300001E88202"],["119D6240702000080007300004EC4101"]] 
    #achamos o arquivo com mais linhas
    tamanho=[len(i) for i in planilhas]
    #maiorIndice = tamanho.find(max(tamanho))
    #maior=planilhas[maiorIndice]

    for linhaIndice in range(max(tamanho)):
        linhas=[i[linhaIndice] for i in planilhas]
        igual=linhaIgual(linhas)
        strIndice="%03d"%linhaIndice
        print(strIndice,end="")
        if igual:

            y=converter("==|",bcolors.OKGREEN)
            print(y,end="")
            x="|".join(linhas)
            print(x,end="")


        else:
            y=converter("!=|",bcolors.FAIL)
            print(y,end="")
            linhas=confLinhas(linhas)
            x="|".join(linhas)
            print(x,end="")
        print("")
    return 0


def main():
    args=sys.argv[1:]
    if args==[]:
        usage()
    else:
        checar(args)


main()


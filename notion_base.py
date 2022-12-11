from math import pi ; 
def nomPrenom():
    prenom = input("entrez votre prenom : ")
    nom = input("entrez votre nom : ")             # nom et prenom  2.1

    print("votre nom est : ",nom," ",prenom) 


def aireCercle():
    rayon = int(input("entrez le rayon du crecle : "))
    aire = rayon *rayon * pi                                         # aire du crecle 2.2

    print("l'aire du cercle est : ",aire)  


def contienCaractere(chain,e):

    if(e in chain):                                                   # caractere dans le chain 2.3
        print("le caracte est dans le chain ")
    else:
        print("le caratere est ne pas dans le chain")


def Bonjour32():
    for i in range(33):
        print("Bonjour ")                                           # bonjour 32 fois et aurevoir une seul fois 2.4
        if(i == 32):
            print("Au revoir")



def fetchDate(date):
    arr  = []
    d = ""
    for i in range(len(date)):
        if date[i] == "," :
            arr.append(int(d))
            d = ""
            continue                                                            # fonction retuourner le date sous form list
        d += date[i]
        if len(date)-1 == i :
            arr.append(int(d))
    return arr


def nombre_jour():
    date1 = fetchDate(input("entrez le 1er date avec format a/m/j :  "))
    date2 = fetchDate(input("entrez le 2eme date avec format a/m/j : "))
    d = []
    for i in range(len(date1)):
        if date1[i] > date2[i]:
            d.append(date1[i] - date2[i]) 
        elif date1[i] < date2[i]:
            d.append(date2[i] - date1[i])                                       # le nombre de jour entre deux deux date different 2.5
        else:
            d.append(0)  

    nj = d[0]* 365 + d[1]*30 + d[2]
    print("le nomber de jour est ",nj)


def rectangle_de_chiffer():                                                     # 123456789
    n = int(input("entrez un nomber : "))                                       # 123456789       2.6
    for i in range(5):                                                          # 123456789
        for e in range(n+1):
            print(e,end=" ")
        print()


def tableMulti():
    for i in range(1,21):
        result  = 7*i
        if result%3 == 0:
            print(result," *")
        else:
            print(result)

def triangleIso():
    n = int(input("enter n :"))
    b = n
    for i in range(1,n):
        print(" "*b,end="")
        print("*"*(2*i -1))
        b = b-1



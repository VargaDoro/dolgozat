import random

def elso():
    szam:int=int(input("Adj meg egy páros számot: "))
    while(szam%2 != 0):
        print("Páros számot adj meg!")
        szam:int=int(input("Adj meg egy páros számot: "))
    print("A megadott szám: ",szam)


'''Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot.
Hány 3-mal osztható van közöttük? A kiírás formátuma: „A számok között X db 3-mal osztható van!'''
def masodik():
    lista=[]
    for i in range(0,13,1):
        szam:int=int(random.random()*141+10)
        lista.append(szam)
    return lista

def masodik_harommal(lista):
    osszeg:int=0
    db:int=0
    for i in range(len(lista)):
        if(osszeg%3==0):
            osszeg+=lista[i]
            db+=1
            print(f"A számok között {db} db 3-mal osztható van!")


'''Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot. 
 Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!”
Ha hosszabb, akkor a text szövegnek az N. karakterét írjuk ki csupa nagybetűvel 3-szor! '''
def harom(text:str, N:int):
    if(len(text)<N):
        print("Nincs N. karakter!")
    else:
        print(f"A szöveg {N} karaktere: ",text[N].upper()*3)

'''Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja.
Hány nevet adott meg a felhasználó? 
A kiírás formája: „A felhasználó 12 nevet adott meg.'''
def negy():
    


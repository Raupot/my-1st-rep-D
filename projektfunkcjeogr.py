 def mnozenie(lista1, lista2):
     if len(lista1) == len(lista2):
         if len(lista1) > 0:
             przemnozone = lista1[0] * lista2[0]
             return przemnozone, mnozenie(lista1[1:], lista2[1:])
         else:
             return
     else:
         return "LISTY POWINNY BYĆ RÓWNEJ DŁUGOŚCI!"


 pierwszaLista = [1,2,3,4]
 drugaLista = [2,4,6,8]

 wynik = mnozenie(pierwszaLista, drugaLista)
 print (wynik)

# ----------

 def binegacja(zmiennaP, zmiennaQ):
     if zmiennaP == zmiennaQ:
         if zmiennaP == "False":
             return "True"
         else:
             return "False"
     else:
         return "False"

 def poprawnaBinegacja(zmiennaP, zmiennaQ):
     if zmiennaP == "True" or zmiennaP == "False":
         if zmiennaQ == "True" or zmiennaQ == "False":
             return binegacja(zmiennaP, zmiennaQ)
         else:
             return "ZmiennaQ musi przyjmować wartość True or False"
     else:
         return "ZmiennaP musi przyjmować wartość True or False"

 zmienna1a = "False"
 zmienna1b = "False"

 zmienna2a = "False"
 zmienna2b = "True"

 zmienna3a = "True"
 zmienna3b = "False"

 zmienna4a = "True"
 zmienna4b = "True"

 print (poprawnaBinegacja(zmienna1a, zmienna1b))
 print (poprawnaBinegacja(zmienna2a, zmienna2b))
 print (poprawnaBinegacja(zmienna3a, zmienna3b))
 print (poprawnaBinegacja(zmienna4a, zmienna4b))

import random

def funkcja(liczbaKolumn, liczbaWierszy, wylosowana = random.randint (0,5)):
    lista = []
    for i in range (liczbaWierszy):
        for j in range (liczbaKolumn):
            lista.append(wylosowana)
    return lista



wynik1 = funkcja(2,3)
 wynik2 = funkcja(4,5)
 wynik3 = funkcja(1,1)

print(wynik1)
 print(wynik2)
 print(wynik3)

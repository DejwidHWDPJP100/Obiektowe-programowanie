#zad 1
def pole_prostokata(wiek,cena_podstawowa=30):
  return dlugosc * szerokosc
print (pole_prostokata(5,3))

#zad 2
def uczen(imie, wiek=18):
  return f"uczen {imie} ma {wiek} lat"
print(uczen("Jan",17))
print(uczen("Marek",19))

#zad 3
def dodaj(a,b):
  return a+b
def odejmij(a,b):
  return a-b
def pomnoz(a,b):
  return a*b
def podziel(a,b):
  return a/b
print(dodaj(10,5))
print(odejmij(10,5))
print(pomnoz(10,5))
print(podziel(10,5))

#zad 4
def cena_biletu(wiek,cena_podstawowa=30):
  if wiek <13:
    return 15
  elif wiek<18:
    return 20
  else:
    return cena_podstawowa
print(cena_biletu(10))
print(cena_biletu(17))
print(cena_biletu(50))

#zad 5
def produkt(nazwa,cena,sztuk):
  wartosc = cena*sztuk
  return f"{nazwa} : {wartosc} zl"
print(produkt("laptok",3500,2))
print(produkt("klawiatura",150,5))
print(produkt("ajfon",2500,4))
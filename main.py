from funtzioak import *
from Gehiketa import *



def menu():
	#MENU DE OPCIONES
	print("** ::::::::::::::::::::::::::::::::::::::::::::::**")
	print(":: Aukeratu bi zenbakiren arteko eragiketa bat ::")
	print("** :::::::::::::::::::::::::::::::::::::::::::::: **")
	print("-------------------------------")
	print("| Gehiketa:              ->  1     |")
	print("| Kenketa:               ->  2     |")
	print("| Biderketa:             ->  3     |")
	print("| Zatiketa:              ->  4     |")
	print("| Berreketa:             ->  5     |")
	print("| Erroa:                 ->  6     |")
	print("| Ezabatu:               ->  e     |")
	print("| Irten:                 ->  i     |")
	print("-------------------------------")
	print("** ::::::::::::::::::::::::: **")
	print("\n")

def aukerak(auk=0):
	aukera = int(input("Aukeratu funtzio bat "))
	return aukera
menu()
auk=aukerak(auk=0)


if(auk==1):
	print(Gehiketa())
elif(auk==2):
	print(Kenketa())
elif(auk==3):
	print(Biderketa())
elif(auk==4):
	print(Zatiketa())
elif(auk==5):
	print(Berreketa())
else:
	print("Eskerrik asko kalkulagailua erabiltzeagatik!!")




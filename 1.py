#Egilea: Alvaro Viguera
#Data: 03-02-2020
#Idatzi zenbaki oso positibo bat jaso eta bere faktoriala itzultzen duen programa


def lehen_funtzioa():
    num = int (input("Sartu zenbaki bat: "))
    resultado=1
    for i in range(1,num):
        resultado=resultado*i
    print(resultado)
lehen_funtzioa()

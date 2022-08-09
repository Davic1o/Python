#Importamos la libreria random para tener nuemro al azar
import random

def run():
    #asignamos el numero randomico a una varaible
    numero_aleatorio = random.randint(1, 2)
    #creamos el condicional 
    numero_elegido = int(input("Elije un numero del 1 al 10 :"))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un numero mas grande ")
        else:
            print("Busca un numero mas pequeño ")
        numero_elegido = int(input("Elije otro numero  :"))
    print("Ganaste!")


if __name__ == "__main__":
    run()
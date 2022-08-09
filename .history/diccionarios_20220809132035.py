def run():
    #declaramos los objetos con los valores que tiene en formato Json
    mi_diccionario ={
      'llave1' : 1,
      'llave2' : 2,
      'llave3' : 3,      
    }
    #nos permite imprimir el valor que este gurdado en cualquier objeto
    print(mi_diccionario['llave1'])

for llave in mi_diccionario.keys():
        print(llave)
if __name__ == "__main__":
    run()
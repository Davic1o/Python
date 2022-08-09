def run():
    # Defino el diccionario, agrego los valores.
    mi_diccionario = {
      'llave1' : 1,
      'llave2' : 2,
      'llave3' : 3,
    }
    for llave in mi_diccionario.keys():
        print(llave)
    for valores in mi_diccionario.values():
        print(valores)
    
    if __name__ == '__main__':
        run()
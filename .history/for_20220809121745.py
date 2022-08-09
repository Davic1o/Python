def imprimir_numero(inicio, fin):
    for inicio in range(fin+1):
        print(f'Numero: {inicio}')


def imprimir_numero_while(inicio, fin):
    while inicio <= fin:
        print(f'Numero: {inicio}')
        inicio += 1

def run():


    while True:
        print('')
        print('*********************************************************')
        print('*******************N U M E R O S**********************')
        print('')
        inicio = int(input('Digite el número inicial para la secuencial:  '))
        print('')
        fin = int(input('Digite el número final para la secuencial: '))
        print('')

        if inicio < fin:
            imprimir_numero(inicio,fin)
        else:
            print(f'El numero inicial {inicio} debe ser ser menor al numero final {fin}.')



if __name__ == "__main__":
    run()
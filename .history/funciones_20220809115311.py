def conversacion(opcion):
    print('Hola')
    print('Cómo estás')
    print('Elegiste la opcion: ' + str(opcion))
    print('Adiós')

opcion = int(input('Ingrese una opción (1, 2, 3): '))

if opcion == 1:
    conversacion(opcion)

elif opcion == 2:
    conversacion(opcion)

elif opcion == 3:
    conversacion(opcion)

else:
    print('Escribe una opción correcta.')

def suma(a, b):
    print('definimos una funcion que nos retorna un resultado')
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)
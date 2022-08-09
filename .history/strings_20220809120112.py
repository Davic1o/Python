# variable.strip(): El método strip eliminará todos los caracteres vacíos que pueda contener la variable

# variable.lower(): El método lower convertirá a las letras en minúsculas.

# variable.upper(): El método upper convertirá a las letras en mayúsculas.

# variable.capitalize(): El método capitalize convertirá a la primera letra de la cadena de caracteres en mayúscula.

# variable.replace (‘o’, ‘a’): El método replace remplazará un caracterer por otro. En este caso remplazará todas las ‘o’ por el caracter ‘a’.

# # len(variable): Te indica la longitud de la cadena de texto dentro de la variable en ese momento.
# Índices:
# Se escriben entre corchetes al lado de la variable y son apuntadores numéricos a cada caracter. Por ejemplo, para el nombre Facundo, cuando utilizamos la variable nombre[1], aparece la letra ‘a’, dado que dicha variable tiene almacenada en ese momento la cadena de caracteres ‘Facundo’ donde la ‘a’ es el segundo caracterer.

# Aclaración: se comienza a contar caracteres desde el 0 (que es el primer número en informática). Siguiendo el ejemplo, la letra ‘F’ de ‘Facundo’ es el caracter número 0. Por ende, nombre[0], nos devolvería una F.
nombre = "Francisco"
nombre[0 : 3]
#imprime las letras desde la la posicion 1 hasta la 3
nombre[: 3]
#imprime las tres primeras letras
nombre[3: ]
#NO imprime las tres primeras letras

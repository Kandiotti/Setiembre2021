nombre = input('Escribe tu nombre: ')
saludo = f'Hola, {nombre} esta cadena tiene '
len(saludo)
print(f'{saludo}{str(int(len(saludo))+13)} caracteres')
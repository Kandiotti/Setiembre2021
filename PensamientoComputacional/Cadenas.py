def main():
    nombre = input('Escribe tu nombre: ')
    saludo = f'Hola, {nombre} esta cadena tiene '
    print(f'{saludo}{str(int(len(saludo))+13)} caracteres')


if __name__ == '__main__':
    main()
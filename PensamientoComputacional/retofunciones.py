def Enumeracion_Exhaustiva(num):
    respuesta = 0

    while respuesta**2 < num:
        respuesta += 1

    if respuesta**2 == num:
        print(f'La raíz cuadrada de {num} es {respuesta}')
    else:
        print(f'El {num} no tiene una raiz cuadrada exacta')

def Aproximacion(num):
    respuesta = 0
    epsilon = float(
        input('Elige el nivel de confianza para hallar la raiz cuadrada: '))
    paso = epsilon**2

    while abs(respuesta**2 - num) >= epsilon and respuesta < num:
        respuesta += paso

    if abs(respuesta**2 - num) >= epsilon:
        print(f'{num} no tiene una raiz cuadrada')
    else:
        print(f'La raiz cuadrada de {num} es {respuesta}')

def Busqueda_Binaria(num):
    epsilon = float(
        input('Elige el nivel de confianza para hallar la raiz cuadrada: '))
    li = 0.0
    ls = max(1.0, num)
    respuesta = (ls + li)/2

    while abs(respuesta**2 - num) >= epsilon:
        print(f'inferior: {li}, superior: {ls}, raiz: {respuesta}')

        if respuesta ** 2 < num:
            li = respuesta
        else:
            ls = respuesta

        respuesta = (li+ls)/2

    print(f'La raiz cuadrada de {num} es {respuesta}')


def main():
    num = int(input('Elige un número: '))
    print('''
          Menú 😁:
          
          1. Algoritmo de Enumeración Exhaustiva
          2. Algoritmo de Aproximación de Soluciones
          3. Algoritmo de Búsqueda Binaria
          ''')
    opcion = int(input(
        'Elige el tipo de algoritmo que prefieres usar para la siguiente operación:'))
    if opcion == 1:
        Enumeracion_Exhaustiva(num)
    elif opcion == 2:
        Aproximacion(num)
    elif opcion == 3:
        Busqueda_Binaria(num)
    else:
        print(f'La opción {opcion} no está dentro de las opciones del menu')


if __name__ == '__main__':
    main()
def main():
    objetivo = int(input('Ingrese un número entero: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    contador = 0
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo),respuesta, contador)
        contador += 1
        respuesta += paso
        
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se logró encontrar la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


if __name__ == '__main__':
    main()
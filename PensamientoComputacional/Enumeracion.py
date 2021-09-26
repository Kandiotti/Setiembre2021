def main():
    objetivo = int(input('Escoge un entero: '))
    respuesta = 0
    
    while respuesta**2 < objetivo:
        # print(respuesta)
        # para saber que arroja en cada iteración 
        respuesta += 1
        
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')


if __name__ == '__main__':
    main()
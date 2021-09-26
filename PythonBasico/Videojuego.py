import random as rnd


def main():
    numero_aleatorio = rnd.randint(1,100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige un número nuevo: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    main()
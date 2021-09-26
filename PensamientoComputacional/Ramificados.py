def main():
    # num_1 = int(input('Escoge un entero: '))
    # num_2 = int(input('Escoge otro entero: '))
    # if num_1 > num_2:
    #     print(f'El número {num_1} es mayor que {num_2}')
    # elif num_1 < num_2:
    #     print(f'El  número {num_1} es menor que {num_2}')
    # else:
    #     print('Los números son iguales')
    
    name_1 = input('Escribe el nombre de la primera persona: ')
    edad_1 = int(input(f'Escribe la edad de {name_1}: '))
    name_2 = input('Escribe el nombre de la segunda persona: ')
    edad_2 = int(input(f'Escribe la edad de {name_2}: '))
    
    if edad_1 > edad_2:
        print(f'{name_1} es el mayor')
    elif edad_1 < edad_2:
        print(f'{name_2} es el mayor')
    else:
        print(f'tanto {name_1} como {name_2} tienen la misma edad')


if __name__ == '__main__':
    main()
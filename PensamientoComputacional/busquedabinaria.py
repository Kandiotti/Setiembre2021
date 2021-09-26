def main():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.00001
    li = 0.0
    ls = max(1.0, objetivo)
    respuesta = (ls + li)/2
    
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'inferior = {li}, superior = {ls}, respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            li = respuesta
        else:
            ls = respuesta
            
        respuesta = (ls + li)/2
        
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')


if __name__ == '__main__':
    main()
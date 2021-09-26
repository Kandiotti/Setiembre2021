import random as rnd


def generar_contrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
             '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = MAYUS + MINUS + NUMS + CHARS

    contrasena = []
    
    for i in range(15):
        caracter_random = rnd.choice(caracteres)
        # con rnd.choice elijo un caracter al azar de toda la lista de caracteres 
        # y lo guardo en una variable caracter_random
        contrasena.append(caracter_random)
    
    contrasena = "".join(contrasena)
    # para convertir una lista a un string se utiliza el join
    # '' simboliza un string vacio, genero un string de la lista original
    # Si en la lista tenia [A,B,C,D,E] lo que devuelve es ABCDE
    return contrasena


def main():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    main()

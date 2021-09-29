import sys as ss

print(ss.getrecursionlimit())

ss.setrecursionlimit(1500)


def factorial(n):
    """[Calcula el factorial de n]

    Args:
        n ([int]): [n > 0]

        returns n!
    """
    print(n)
    if n == 1:
        return 1

    return n*factorial(n-1)


def main():
    n = int(input('Escribe un entero positivo: '))

    if n <= 0:
        print(f'{n} no es una entrada correcta')
        main()
    else:
        print(factorial(n))


if __name__ == '__main__':
    main()

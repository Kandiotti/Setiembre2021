def funcion1 (arg, func):
    def funcion2(arg):
        return arg * 2
    
    valor = funcion2(arg)
    return func(valor)

def funcion_random(arg):
    return arg * 5


def main():
    argumento = 2
    print(funcion1 (argumento, funcion_random))
    

if __name__ == '__main__':
    main()    
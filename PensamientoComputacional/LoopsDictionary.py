def main():
    estudiantes = {
        'mexico': 10,
        'colombia': 15,
        'peru': 13,
        'alemania': 5,
        'bolivia': 10
    }

    for pais in estudiantes:
        print (pais)

    for pais in estudiantes.keys():
        print (pais)
        
    for num_est in estudiantes.values():
        print(num_est)

    for pais, num_est in estudiantes.items():
        print(f'En el establecimiento hay {num_est} estudiantes del pais {pais}')
    

if __name__ == '__main__':
    main()
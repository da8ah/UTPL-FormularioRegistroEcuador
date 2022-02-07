def validar_cedula(cedula: str) -> str:

    nums_1 = ['0'+str(i) for i in range(1, 10)]
    nums_2 = [str(i) for i in range(10, 25)]
    nums = nums_1 + nums_2

    provinces = ['Azuay',
                 'Bolivar',
                 'Canar',
                 'Carchi',
                 'Cotopaxi',
                 'Chimborazo',
                 'El Oro',
                 'Esmeraldas',
                 'Guayas',
                 'Imbabura',
                 'Loja',
                 'Los Rios',
                 'Manabi',
                 'Morona Santiago',
                 'Napo',
                 'Pastaza',
                 'Pichincha',
                 'Tungurahua',
                 'Zamora Chinchipe',
                 'Galapagos',
                 'Sucumbios',
                 'Orellana',
                 'Santo Domingo de los Tsachilas',
                 'Santa Elena']

    zip_iterator = zip(nums, provinces)
    ced_dict = dict(zip_iterator)

    what_province = ced_dict.get(cedula[:2])
    return what_province


# To validate uncomment and run the script
# def main():
#    valid = input('>> ')
#    print(validar_cedula(valid))


# if __name__ == '__main__':
#    main()

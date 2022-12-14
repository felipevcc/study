# LISTAS Y DICCIONARIOS ANIDADOS    

def run():
    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Rodriguez"},
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "Fernandez"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43]
    }

    for key, value in super_dict.items():
        print(key, ">", value)
    
    print('\n')

    for elements in super_list:
        print(elements)


if __name__ == '__main__':
    run()
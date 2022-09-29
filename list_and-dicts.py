def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firsname": "Daniel", "lastname": "Vilca"}

    super_list = [
        {"firsname": "Daniel", "lastname": "Vilca"},
        {"firsname": "Josue", "lastname": "Jaramillo"},
        {"firsname": "Genesis", "lastname": "Vilca"},
        {"firsname": "Yamile", "lastname": "Vilca"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.2, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if (__name__ == "__main__"):
    run()

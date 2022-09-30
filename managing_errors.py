def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    num = (input("Numero ingresado: "))
    # assert num.isnumeric(), "El valor ingresado no es un numero"
    assert int(num) > 0, "El valor debe ser positivo"
    print(divisors(int(num)))


if (__name__ == "__main__"):
    run()
    print("Hello, world!")

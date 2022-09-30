def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    try:
        num = int(input("Numero ingresado: "))
        print(divisors(num))
    except:
        print("ERROR: Invalid number")


if (__name__ == "__main__"):
    run()
    print("Hello, world!")

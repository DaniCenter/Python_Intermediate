from functools import reduce


def start():
    listNumbers = [i for i in range(1, 11)]
    listNumbers2 = list(filter(lambda x: x % 2 == 0, listNumbers))
    listNumbers3 = list(map(lambda x: x ** 2, listNumbers))
    listNumbers4 = reduce(lambda a, b: a + b, listNumbers)
    print(listNumbers2)
    print(listNumbers3)
    print(listNumbers4)


if (__name__ == "__main__"):
    start()

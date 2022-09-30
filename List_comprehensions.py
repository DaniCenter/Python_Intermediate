def run():
    listNumbers = [i for i in range(1, 10000) if i % 36 == 0]
    print(listNumbers)
    diccionary = {i: round(i**0.5, 2) for i in range(1, 1000)}
    print(diccionary)


if (__name__ == '__main__'):
    run()

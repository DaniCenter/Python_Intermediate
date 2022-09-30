# r => Lectura
# w => Escritura (sobrescribir)
# a => Escritura (agregar al final)
def create_file():
    names = ["Daniel", "Josúe", "Vilca", "Jaramillo"]
    with open("./archivos/prueba.txt", "w", encoding="utf-8") as f:
        for i in names:
            f.write(i)
            f.write("\n")
        f.close()


def read():
    namesReading = []
    with open("./archivos/prueba.txt", "r", encoding="utf-8") as f:
        for i in f:
            namesReading.append(i)
        f.close()
    print(namesReading)


def run():
    create_file()
    read()


if (__name__ == "__main__"):
    run()

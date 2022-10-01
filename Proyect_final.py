import os
from random import randint
import time
bienvenida = '''
     ___       __    __    ______   .______        ______      ___       _______    ______
    /   \     |  |  |  |  /  __  \  |   _  \      /      |    /   \     |       \  /  __   |
   /  ^  \    |  |__|  | |  |  |  | |  |_)  |    |  ,----'   /  ^  \    |  .--.  ||  |  |  |
  /  /_\  \   |   __   | |  |  |  | |      /     |  |       /  /_\  \   |  |  |  ||  |  |  |
 /  _____  \  |  |  |  | |  `--'  | |  |\  \----.|  `----. /  _____  \  |  '--'  ||  `--'  |
/__/     \__\ |__|  |__|  \______/  | _| `._____| \______|/__/     \__\ |_______/  \______/

                                      by: Daniel Vilca
Hello, welcome to the hangman game :V, this is the first "serious" python project,
I hope you like it.

DON'T BREAK THE CODE >:l
'''
ahorcado = [
    '''
  +---+
  |   |
      |
      |
      |
      |
==========
  ''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
==========
  ''',
    '''
  +---+
  |   |
  O   |
  |   |
  |   |
      |
==========
  ''',
    '''
  +---+
  |   |
  O   |
  |   |
  |   |
 / \  |
==========
  ''',
    '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
==========
  '''
]
a, b = 'áéíóúü', 'aeiouu'
trans = str.maketrans(a, b)
with open("./data.txt", "r", encoding="utf-8") as f:
    words = [i.replace("\n", "") for i in f]
    f.close()


def run():
    escena = 0
    secret_word = words[randint(0, len(words)-1)]
    secret_word = secret_word.translate(trans)
    secret_word_list = list(secret_word)
    test = []
    for i in range(0, len(secret_word)):
        test.append(" _ ")
    print(bienvenida)
    time.sleep(2)

    while True:
        os.system("cls")
        print(ahorcado[escena])
        print("".join(test))
        word_input = input("Ingrese letra: ")
        input_letter = False
        temp = 0
        if len(word_input) == 1:
            for i in secret_word_list:
                if word_input == i:
                    test[secret_word_list.index(i, temp)] = word_input
                    input_letter = True
                temp += 1
            if (not input_letter):
                if escena < 4:
                    escena += 1
                else:
                    print("Perdiste :c")
                    print("La palabra secreta era: ", secret_word)
                    reload = input("Reiniciar?: (y/n)")
                    if reload == "y":
                        escena = 0
                        secret_word = ""
                        run()
                    else:
                        break
        else:
            print("Escribe una letra")
            time.sleep(1)


if (__name__ == "__main__"):
    run()

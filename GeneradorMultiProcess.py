from multiprocessing import Pool

import time

n = 100
p = [2, 3, 5, 7]
r = 0


def encontrarprimos(n):
    p = [2] + [x for x in range(3, n + 1, 2) if
               not [y for y in range(3, int(x ** 0.5) + 1, 2) if (float(x) / y).is_integer()]]
    print(p)
    print("suma de la lista : ", sum(p))


def encontrar_primos_threads(n):
    aux = n
    global p
    if not(dividir(aux)):
        p.append(aux)
        return aux



def dividir(x):
    for y in range(3, int(x ** 0.5) + 1, 2):
        if (float(x) / y).is_integer():
            return True

if __name__ == "__main__":
    v = "y"
    while v == "y":

        n = raw_input("Que numero deseas calcular")
        try:
            n = int(n)
            print("Calculando.....")
            t = time.time()

            proc = Pool()

            result = [2] + proc.map(encontrar_primos_threads, range(3, n + 1, 2))

            proc.close()

            proc.join()

            result = filter(None, result)

            print(result)

            print("trabajo terminado con multiprocesamiento : ", time.time() - t)

            # Aqui empieza el metodo normal sin ningun Thread

            t = time.time()

            encontrarprimos(n)

            print("trabajo terminado sin multiprocesamiento en : ", time.time() - t)

            v = raw_input("Deseas colocar otro numero y/n")
            a = True
            while a:
                if v == "y" or v == "n":
                    a = False
                else:
                    print("No entiendo lo que dices")
                    v = raw_input("Deseas colocar otro numero y/n")

        except ValueError:
            print("Debes colocar un numero =(")

    print("Gracias por participar")

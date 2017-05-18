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
    while True:

        if not(dividir(aux)):
            return aux
        else:
            aux += 1


def dividir(x):
    for y in range(3, int(x ** 0.5) + 1, 2):
        if (float(x) / y).is_integer():
            return True

if __name__ == "__main__":

    n = 1000

    t = time.time()

    proc = Pool()

    result = proc.map(encontrar_primos_threads, range(3, n + 1, 2))

    proc.close()

    proc.join()

    print(result)

    print("trabajo terminado con threads : ", time.time()-t)

    #Aqui empieza el metodo normal sin ningun Thread

    t = time.time()

    encontrarprimos(n)

    print("trabajo terminado sin threads en : ", time.time()-t)
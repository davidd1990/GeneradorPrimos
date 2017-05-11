import threading

import time

n = 100
p = [2, 3, 5, 7]
r = 0
lock = threading.Lock()


def imprimirmensaje(mensaje):
    while True:
        print(mensaje)
        time.sleep(1)


def encontrarprimos(n):
    p = [2] + [x for x in range(3, n + 1, 2) if
               not [y for y in range(3, int(x ** 0.5) + 1, 2) if (float(x) / y).is_integer()]]
    print(p)
    print("suma de la lista : ", sum(p))


def encontrar_primos_threads(n, z):
    global p
    for x in range(z + 1, n + 1, 2):
             lock.acquire()
             if not(dividir(x)):
                 p.append(x)

             lock.release()


def dividir(x):
    for y in range(3, int(x ** 0.5) + 1, 2):
        if (float(x) / y).is_integer():
            return True


#Este es el metodo principal donde corren los Threads y el metodo sin Threads
def main():
    n = 100
    global p
    #funcion que empieza ha  llevar el tiempo en que se ejecuta el metodo
    t = time.time()


    #Aqui pueden crear los Threads que necesitan simplemente copien y peguen
    #como pueden ver el numero que desean encontrar los primos toca partirlo de acuerdo a sus neceidades
    # el metedo encontrar_primos_threads tiene dos argumentos el primero es la cantidad final y segundo es de donde
    #empezar. Por ejemplo si quiero 100 como cantidad final puedo empezar desde 10 o desde 50 depende de lo que ustedes
    #deseen.Por ultimo, el valor minimo es 8 no 0
    t1 = threading.Thread(target=encontrar_primos_threads, args=(50000, 8,))
    t2 = threading.Thread(target=encontrar_primos_threads, args=(100000, 50000,))
    t3 = threading.Thread(target=encontrar_primos_threads, args=(150000, 100000,))
    t4 = threading.Thread(target=encontrar_primos_threads, args=(200000, 150000,))


    #Cada vez que creen un thread tiene que inicializarlo de la forma que se muestra abajo
    t1.start()
    t2.start()
    t3.start()
    t4.start()


    #Despues de inicializarlo deben colocar el metodo join para que se aseguren que el thread se termine
    t1.join()
    t2.join()
    t3.join()
    t4.join()


    #Como son varios Threads la lista resultante queda en desorden por lo que hay q ordenarla
    p.sort()

    print(p)

    print("suma de la lista : ", sum(p))
    print("trabajo terminado con threads : ", time.time()-t)

    #Aqui empieza el metodo normal sin ningun Thread
    t = time.time()
    encontrarprimos(200000)

    print("trabajo terminado sin threads en : ", time.time()-t)

main()

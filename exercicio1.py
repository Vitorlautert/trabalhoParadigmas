import threading
import time

contador = 0

def incrementar_contador_sem_protecao():
    global contador
    for _ in range(1000):
        contador += 1

def incrementar_contador_com_protecao(lock):
    global contador
    for _ in range(1000):
        lock.acquire()
        try:
            contador += 1
        finally:
            lock.release()

def executar_sem_protecao():
    global contador
    contador = 0 
    print("\nExecutando sem proteção (desprotegido)")
    thread1 = threading.Thread(target=incrementar_contador_sem_protecao)
    thread2 = threading.Thread(target=incrementar_contador_sem_protecao)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"Valor final do contador (desprotegido): {contador}")

def executar_com_protecao():
    global contador
    contador = 0 
    print("\nExecutando com proteção (travado)")
    lock = threading.Lock()
    thread1 = threading.Thread(target=incrementar_contador_com_protecao, args=(lock,))
    thread2 = threading.Thread(target=incrementar_contador_com_protecao, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"Valor final do contador (protegido): {contador}")

executar_sem_protecao()
executar_com_protecao()

# Comparação dos Resultados
# Ao executar sem proteção (desprotegido), o valor final do contador é frequentemente menor que 2000.
# Isso ocorre devido a condições de corrida: ambas as threads tentam ler, 
# incrementar e escrever na variável 'contador' concorrentemente. Se uma thread lê o valor, 
# outra o incrementa, e então a primeira thread escreve seu valor antigo incrementado de volta, 
# uma atualização é perdida. Com proteção (travado), um `threading.Lock` garante que 
# apenas uma thread possa acessar e modificar o `contador` por vez. 
# Isso previne condições de corrida, garantindo que cada incremento seja aplicado corretamente, 
# resultando no valor final correto de 2000.
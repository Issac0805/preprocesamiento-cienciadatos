import time

def num_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

inicio = time.time()

primos = []
for numero in range(1, 100000):
    if num_primo(numero):
        primos.append(numero)

fin = time.time()

print("Tiempo de ejecución:", fin - inicio, "segundos")

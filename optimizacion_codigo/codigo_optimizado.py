import time
import numpy as np
import math

def primo (n):
    if n < 2:
        return False
    limite = int(math.sqrt(n)) + 1
    divisores = np.arange(2, limite)
    return not np.any(n % divisores == 0)

inicio=time.time()

primos=[num for num in range(1, 100000) if primo (num)]

fin=time.time()

print("Tiempo ejecución NumPy:", fin - inicio, "segundos")


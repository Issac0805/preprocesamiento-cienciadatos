import matplotlib.pyplot as plt

tiempo_original = 24.60
tiempo_optimizado = 0.65

plt.figure(figsize=(7,4))
plt.bar(["Original", "Optimizado"], [tiempo_original, tiempo_optimizado])
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación del tiempo de ejecución")
plt.savefig("comparacion_tiempos.png")
plt.close()

plt.figure(figsize=(7,4))
plt.plot(["Original", "Optimizado"], [tiempo_original, tiempo_optimizado], marker="o")
plt.ylabel("Tiempo (segundos)")
plt.title("Distribución de tiempos de ejecución")
plt.savefig("distribucion_tiempos.png")
plt.close()

print("Gráficos generados.")

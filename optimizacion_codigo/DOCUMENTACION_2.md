Optimización de Código y Medición de Tiempos — Actividad Autónoma
## 1. Introducción

En esta actividad se trabajó con un programa en Python que busca números primos desde el 1 a 100.000.
Primero se analizó el código original, que era poco eficiente porque revisaba todos los posibles divisores de cada número y no aprovechaba librerías como NumPy, que permiten hacer operaciones mucho más rápidas, después se aplicaron varias técnicas de optimización para mejorar el tiempo de ejecución, junto con mediciones usando la biblioteca time y un análisis de rendimiento con cProfile.

El objetivo principal fue comparar el antes y después de optimizar el código y entender cómo cambios simples pueden mejorar mucho la velocidad de un programa.

## 2. Código original y problemas detectados

El código original verificaba si un número era primo probando todos los divisores desde 2 hasta el mismo número, lo cual genera muchísimas operaciones innecesarias, esto hace que el programa tarde más tiempo cuando trabaja con rangos grandes.

El tiempo promedio del código original fue aproximadamente:

24.60 segundos

Los principales problemas identificados fueron:

- Uso de un bucle demasiado largo para cada número.

- Falta de optimización matemática.

- Construcción de la lista de primos con bucles tradicionales en vez de list comprehensions.

- Falta de uso de librerías más eficientes como NumPy.

## 3. Código optimizado

Para mejorar el rendimiento del código se aplicaron estas técnicas:

a) Iterar solo hasta la raíz cuadrada del número

No es necesario revisar todos los divisores, solo hasta la raíz de n (√n), porque si un número tuviera un divisor mayor, el otro sería menor y ya habría sido detectado.

b) Uso de list comprehensions

Esto permite crear listas de forma más rápida y sólida que con bucles normales.

c) Uso de NumPy

NumPy permite aplicar operaciones de manera vectorizada, lo que reduce el tiempo de cálculo comparado con un bucle de Python.

Después de optimizar el programa, el tiempo de ejecución bajó aproximadamente a:

0.65 segundos

Esto representa una mejora enorme frente al código original.

## 4. Resultados

Para comparar ambas versiones se midieron los tiempos con:

- time.time() y cProfile para ver dónde se invierte el tiempo realmente

### Tiempos obtenidos:
|Versión|Tiempo aproximado|
|----|----|
|Original|22–25 segundos|
|Optimizada (NumPy)|0.4–0.6 segundos|

La optimización redujo el tiempo más de un 98%.

### Resultados de cProfile

cProfile mostró que:

En el código original, en la función primo() consumía casi todo el tiempo del programa.

En el código optimizado, NumPy realiza las divisiones en un solo bloque, reduciendo miles de llamadas repetidas.

Esto confirma que el problema del código original era la cantidad de operaciones internas, y que NumPy resolvió eso con operaciones vectorizadas.

## 6. Gráficos generados

Se generaron dos gráficos usando Matplotlib:

- Comparación del tiempo de ejecución entre el código original y el optimizado. 

![Gráfico de comparación de tiempos](optimizacion_codigo/comparacion_tiempos.png)


- Distribución de los tiempos, mostrando visualmente la diferencia entre ambas versiones.

![Distribución de tiempos](optimizacion_codigo/distribucion_tiempos.png)


Estos gráficos permiten apreciar claramente el impacto de las mejoras aplicadas.

## 7. Conclusiones

Optimizar un código puede reducir los tiempos de ejecución de manera significativa.

Técnicas simples como limitar el rango del bucle y usar list comprehensions generan mejoras importantes.

El uso de librerías especializadas como NumPy aporta un rendimiento mucho mayor gracias a la vectorización.

El análisis con cProfile ayuda a identificar qué partes del programa consumen más tiempo.

La optimización final redujo el tiempo de ejecución de 24 segundos a menos de 1 segundo, logrando una mejora notable en eficiencia.


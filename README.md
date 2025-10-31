# 🎮 Proyecto: Análisis Básico de Tienda de Videojuegos

Este es un proyecto introductorio a Python que simula el análisis de datos de una tienda de videojuegos. El objetivo principal es aplicar las estructuras de datos fundamentales (diccionarios, tuplas, conjuntos) y la lógica de programación básica (funciones, condicionales).

## 📂 Contenido del Repositorio

* `tienda_videojuegos.py` (o el nombre de tu script): Contiene todo el código fuente, incluyendo las estructuras de datos, las funciones de análisis y la ejecución principal.
* `README.md`: Esta documentación que estás leyendo.

## ✨ Características Principales

* **Modelado de Datos:** Utiliza diccionarios para mapear juegos a sus géneros, métricas de ventas/stock y listas de clientes.
* **Reportes Individuales:** Una función (`resumen_juego`) genera un resumen formateado para cualquier juego.
* **Filtrado de Datos:** Una función (`mostrar_resumenes`) recorre los datos y aplica un condicional para mostrar solo los juegos "TOP" (con ventas superiores a 500 unidades).
* **Cálculo Agregado:** Emplea una función `lambda` para calcular rápidamente la suma total de ventas de los juegos que cumplen el criterio de filtro.

## 🛠️ Estructuras de Datos

El script se articula sobre tres diccionarios principales:

1.  **`generos`**: Un `dict` que asocia el nombre del juego (str) con su categoría (str).
2.  **`ventas_stock`**: Un `dict` que asocia el nombre del juego (str) con una `tupla` de enteros `(ventas, stock)`.
3.  **`clientes`**: Un `dict` que asocia el nombre del juego (str) con un `set` (conjunto) de clientes (str). Se usa un conjunto para evitar nombres duplicados.

## 🚀 Cómo Empezar

# Prerrequisitos

* Se necesita [Python 3](https://www.python.org/downloads/) (cualquier versión reciente funcionará).

### Ejecución

Al ejecutar el script, la salida mostrará un resumen de los juegos más vendidos y el total de ventas de esos juegos:


    =============================================
    === MOSTRANDO JUEGOS TOP (Ventas > 500) ===
    =============================================
    --- Resumen de: Left 4 Dead ---
    Género: Cooperativo
    Ventas: 800 unidades
    Stock:  400 unidades
    Clientes: Diego, Rossy, Kevin
    ----------------------------
    --- Resumen de: Mortal Kombat ---
    Género: Lucha
    Ventas: 877 unidades
    Stock:  322 unidades
    Clientes: Alonso, Sandra, Luis, Cesar
    ------------------------------

    =============================================
    Total de ventas de juegos TOP: 1677
    =============================================
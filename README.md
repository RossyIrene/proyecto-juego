## Proyecto: Análisis de Ventas y Clientes – Tienda de Videojuegos

Este proyecto simula el análisis de ventas y clientes para una tienda de videojuegos. Todo el código se encuentra en un único archivo: `tienda_videojuegos.py`.

### Estructura del proyecto
```text
Proyecto-analisis-cliente/
├─ tienda_videojuegos.py   # Código principal con estructuras, funciones y ejecución
└─ README.md               # Documentación del proyecto
```

### Objetivos
- **Estructuras de datos**: definición de `generos`, `ventas_stock` y `clientes`.
- **Función base**: `resumen_juego(juego)` imprime el resumen de un juego.
- **Lógica y condicionales**: listado `juegos`, filtrado por ventas > 500 e impresión de resúmenes.
- **Función lambda**: cálculo del total de ventas por encima de un límite.
- **Ejecución principal**: muestra juegos TOP e imprime el total de ventas con límite 500.

### Requisitos previos
- Python 3.9 o superior.

### Estructuras de datos
- **generos**: `dict[str, str]` que mapea nombre del juego a su género (por ejemplo: "Aventura", "Rol").
- **ventas_stock**: `dict[str, tuple[int, int]]` donde el valor es `(ventas, stock)`.
- **clientes**: `dict[str, set[str]]` donde cada juego tiene el conjunto de clientes (nombres) asociados.

### Función base
- **resumen_juego(juego)**: imprime de forma clara el género, ventas, stock y la lista de clientes.
  - La lista de clientes se muestra con `", ".join(...)` (sin llaves ni formato de conjunto).

### Lógica de análisis
- **Lista de juegos**: `juegos` contiene todos los nombres de juegos.
- **Filtrado**: `mostrar_resumenes_filtrados()` recorre `juegos` y muestra resúmenes solo si las ventas son `> 500`.

### Función lambda solicitada
La expresión utilizada (idéntica a la especificada) es:

```python
ventas_totales = lambda data, limite: sum(
    ventas for juego, (ventas, _) in data.items() if ventas > limite
)
```

Se emplea para calcular el total de ventas de los juegos con más de `limite` unidades vendidas.

### Ejecución principal
Al ejecutar el script:
1. Se listan los juegos TOP con ventas > 500 usando `mostrar_resumenes_filtrados()`.
2. Se imprime el resultado de `ventas_totales(ventas_stock, 500)`.

### Cómo ejecutar
Desde PowerShell (Windows):

```bash
python tienda_videojuegos.py
```

### Salida esperada (ejemplo abreviado)
```
=== Juegos TOP (ventas > 500) ===
--------------------------------------------------
Juego: The Witcher 3
Género: Rol
Ventas: 1250 | Stock disponible: 60
Clientes: Ana, Carla, Luis, Mateo
--------------------------------------------------
Juego: Speed Rush
Género: Carreras
Ventas: 730 | Stock disponible: 35
Clientes: Iván, Nora, Tomás
...

=== Total de ventas de juegos con más de 500 unidades ===
3435
```

Nota: Los nombres de clientes pueden aparecer en distinto orden si no se ordenan; el script los imprime ordenados para una salida estable.



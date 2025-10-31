# Día 1
#1.Actividad principal
generos = {
"Left 4 Dead": "Cooperativo",
"Resident Evil": "Aventura",
"GTA V": "Rol",
"Mortal Kombat": "Lucha"
}

# tupla (ventas, stock) 
ventas_stock = {
"Left 4 Dead": (800, 400),
"Resident Evil": (499, 250),
"GTA V": (353, 125),
"Mortal Kombat": (877, 322)
}

clientes = {
"Left 4 Dead": {"Diego", "Rossy", "Kevin"},
"Resident Evil": {"Sandra", "Alonso", "Luis"},
"GTA V": {"Diego", "Cesar"},
"Mortal Kombat": {"Cesar", "Sandra", "Alonso", "Luis"}
}



#2. Subtarea en equipo
def resumen_juego(juego):
    """
    Imprime un resumen formateado de un juego específico.
    """
    print(f"--- Resumen de: {juego} ---")
    
    # Acceder a los datos usando la clave 'juego'
    genero = generos[juego]
    ventas, stock = ventas_stock[juego]
    lista_clientes = clientes[juego]
    
    # Imprimir la información
    print(f"  Género: {genero}")
    print(f"  Ventas: {ventas} unidades")
    print(f"  Stock:  {stock} unidades")
    
    # Convertir el conjunto a una cadena separada por comas
    clientes_str = ", ".join(lista_clientes)
    print(f"  Clientes: {clientes_str}")
    print("-" * (17 + len(juego)))


#Día 2

# 1. Desafío 1
# Obtenemos los nombres de los juegos desde las claves de un diccionario
juegos = list(generos.keys())

# 2. Desafío 1 y 2
def mostrar_resumenes():
    """
    Recorre todos los juegos y muestra el resumen solo de los que
    tienen más de 500 ventas. 
    """
    print("=============================================")
    print("=== MOSTRANDO JUEGOS TOP (Ventas > 500) ===")
    print("=============================================")
    
    for juego in juegos:
        # Obtenemos las ventas para el condicional
        # Accedemos al primer ítem (índice 0) de la tupla (ventas, stock)
        ventas = ventas_stock[juego][0]
        
        # Condicional del Desafío 2 
        if ventas > 500:
            resumen_juego(juego)

# 3. Desafío 3
# Definimos la lambda tal como se indica en el PDF
ventas_totales = lambda data, limite: sum(
    ventas for juego, (ventas, _) in data.items() if ventas > limite
)

# --- Ejecución Principal del Programa ---
if __name__ == "__main__":
    
    # 1. Ejecutar la función de resúmenes filtrados (Día 2)
    mostrar_resumenes()
    
    # 2. Calcular y mostrar el total de ventas TOP (Día 2)
    total_top = ventas_totales(ventas_stock, 500)
    
    print("\n=============================================")
    print(f"Total de ventas de juegos TOP: {total_top}")
    print("=============================================")
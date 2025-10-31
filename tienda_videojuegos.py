
import sys
import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# 1. Definición de Estructuras
# -----------------------------
# Nota: Los nombres de juegos son consistentes en las tres estructuras

generos = {
    "The Witcher 3": "Rol",
    "Grand Theft Auto V": "Aventura",
    "Speed Rush": "Carreras",
    "League of Legends (LoL)": "Estrategia",
    "Plants vs. Zombies Fusion": "Estrategia",
    "Los Sims 4": "Simulación",
}

ventas_stock = {
    # juego: (ventas, stock)
    "The Witcher 3": (1250, 60),
    "Grand Theft Auto V": (480, 120),
    "Speed Rush": (730, 35),
    "League of Legends (LoL)": (515, 80),
    "Plants vs. Zombies Fusion": (290, 200),
    "Los Sims 4": (940, 15),
}

clientes = {
    "The Witcher 3": {"Ana", "Luis", "Carla", "Mateo"},
    "Grand Theft Auto V": {"Sofía", "Pedro"},
    "Speed Rush": {"Nora", "Tomás", "Iván"},
    "League of Legends (LoL)": {"Lucía", "Elena"},
    "Plants vs. Zombies Fusion": {"Marcos"},
    "Los Sims 4": {"Raúl", "Julia", "Ana"},
}

# 2. Implementación de la Función Base (Subtare

def resumen_juego(juego: str) -> None:
    """Imprime la información de un juego: género, ventas/stock y clientes.

    - El listado de clientes se muestra con ".join()" para evitar el formato de set.
    - Se realizan comprobaciones mínimas para asegurar que el juego exista en las
      estructuras. Si falta en alguna, se indica claramente.
    """
    print("-" * 50)
    print(f"Juego: {juego}")

    # Género
    genero = generos.get(juego)
    if genero is None:
        print("Género: (no encontrado)")
    else:
        print(f"Género: {genero}")

    # Ventas y stock
    ventas_stock_tuple = ventas_stock.get(juego)
    if ventas_stock_tuple is None:
        print("Ventas/Stock: (no disponible)")
    else:
        ventas, stock = ventas_stock_tuple
        print(f"Ventas: {ventas} | Stock disponible: {stock}")

    # Clientes
    clientes_set = clientes.get(juego, set())
    if not clientes_set:
        print("Clientes: (sin registros)")
    else:
        # Se ordenan para una salida estable
        clientes_lista_ordenada = sorted(clientes_set)
        print("Clientes: " + ", ".join(clientes_lista_ordenada))


def generar_resumen_texto(juego: str) -> str:
    """Genera un texto con el resumen del juego (sin imprimir)."""
    lineas = ["-" * 50, f"Juego: {juego}"]
    genero = generos.get(juego)
    lineas.append(f"Género: {genero}" if genero is not None else "Género: (no encontrado)")

    ventas_stock_tuple = ventas_stock.get(juego)
    if ventas_stock_tuple is None:
        lineas.append("Ventas/Stock: (no disponible)")
    else:
        ventas, stock = ventas_stock_tuple
        lineas.append(f"Ventas: {ventas} | Stock disponible: {stock}")

    clientes_set = clientes.get(juego, set())
    if not clientes_set:
        lineas.append("Clientes: (sin registros)")
    else:
        clientes_lista_ordenada = sorted(clientes_set)
        lineas.append("Clientes: " + ", ".join(clientes_lista_ordenada))
    return "\n".join(lineas)



# 3. Lógica de análisis y condicionales (Día 2)

# Lista de todos los juegos (se toma de la estructura base de géneros)
juegos = list(generos.keys())


def mostrar_resumenes_filtrados() -> None:
    """Muestra resúmenes solo de juegos con más de 500 ventas."""
    print("\n=== Juegos TOP (ventas > 500) ===")
    for juego in juegos:
        datos = ventas_stock.get(juego)
        if datos is None:
            continue
        ventas, _ = datos
        if ventas > 500:
            resumen_juego(juego)


# Función Lambda (expresión exacta solicitada)
ventas_totales = lambda data, limite: sum(
    ventas for juego, (ventas, _) in data.items() if ventas > limite
)


def launch_gui() -> None:
    """Lanza una interfaz simple para explorar los datos."""
    root = tk.Tk()
    root.title("Tienda de Videojuegos - Análisis")
    root.geometry("900x600")

    # Paleta y estilos
    bg = "#0f172a"          # fondo ventana
    panel_bg = "#111827"    # paneles
    text_fg = "#e5e7eb"     # texto claro
    accent = "#8b5cf6"      # acento

    style = ttk.Style()
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    root.configure(bg=bg)
    style.configure("App.TFrame", background=panel_bg)
    style.configure("App.TLabel", background=panel_bg, foreground=text_fg)
    style.configure("App.TButton", background=panel_bg, foreground=text_fg)
    style.map("App.TButton",
              background=[("active", "#7c3aed")],
              foreground=[("active", "#ffffff")])

    frame_left = ttk.Frame(root, padding=10, style="App.TFrame")
    frame_left.pack(side=tk.LEFT, fill=tk.Y)

    frame_right = ttk.Frame(root, padding=10, style="App.TFrame")
    frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    ttk.Label(frame_left, text="Juegos", style="App.TLabel").pack(anchor=tk.W)
    listbox = tk.Listbox(frame_left, height=20, exportselection=False,
                         bg=panel_bg, fg=text_fg, selectbackground=accent,
                         selectforeground="#ffffff", highlightthickness=0,
                         relief=tk.FLAT)
    listbox.pack(fill=tk.Y)
    for j in sorted(juegos):
        listbox.insert(tk.END, j)

    controls = ttk.Frame(frame_left, style="App.TFrame")
    controls.pack(fill=tk.X, pady=(10, 0))

    def append_output(msg: str) -> None:
        text.insert(tk.END, msg + "\n")
        text.see(tk.END)

    def clear_output() -> None:
        text.delete("1.0", tk.END)

    def get_selected_game() -> str | None:
        sel = listbox.curselection()
        if not sel:
            return None
        return listbox.get(sel[0])

    def on_mostrar_resumen() -> None:
        juego = get_selected_game()
        if not juego:
            messagebox.showinfo("Información", "Selecciona un juego de la lista.")
            return
        clear_output()
        append_output(generar_resumen_texto(juego))

    def on_mostrar_top() -> None:
        clear_output()
        append_output("=== Juegos TOP (ventas > 500) ===")
        for j in sorted(juegos):
            datos = ventas_stock.get(j)
            if not datos:
                continue
            ventas, _ = datos
            if ventas > 500:
                append_output(generar_resumen_texto(j))

    ttk.Button(controls, text="Mostrar resumen", command=on_mostrar_resumen, style="App.TButton").pack(fill=tk.X)
    ttk.Button(controls, text="Mostrar TOP (>500)", command=on_mostrar_top, style="App.TButton").pack(fill=tk.X, pady=5)

    limite_frame = ttk.Frame(frame_left, style="App.TFrame")
    limite_frame.pack(fill=tk.X, pady=(10, 0))
    ttk.Label(limite_frame, text="Límite ventas:", style="App.TLabel").pack(side=tk.LEFT)
    limite_var = tk.StringVar(value="500")
    limite_entry = ttk.Entry(limite_frame, textvariable=limite_var, width=10)
    limite_entry.pack(side=tk.LEFT, padx=5)

    def on_total() -> None:
        try:
            limite_val = int(limite_var.get())
        except ValueError:
            messagebox.showerror("Error", "El límite debe ser un número entero.")
            return
        total = ventas_totales(ventas_stock, limite_val)
        append_output(f"\n=== Total de ventas de juegos con más de {limite_val} unidades ===\n{total}")

    ttk.Button(frame_left, text="Calcular ventas_totales", command=on_total, style="App.TButton").pack(fill=tk.X, pady=5)

    ttk.Label(frame_right, text="Salida", style="App.TLabel").pack(anchor=tk.W)
    text = tk.Text(frame_right, wrap=tk.WORD, bg=panel_bg, fg=text_fg,
                   insertbackground=text_fg, relief=tk.FLAT, highlightthickness=0)
    text.pack(fill=tk.BOTH, expand=True)

    root.mainloop()


# --------------------
# 4. Ejecución principal
# --------------------
if __name__ == "__main__":
    if "--gui" in sys.argv:
        launch_gui()
    else:
        # Mostrar juegos TOP
        mostrar_resumenes_filtrados()

        # Imprimir total de ventas con límite 500
        limite = 500
        total_top = ventas_totales(ventas_stock, limite)
        print("\n=== Total de ventas de juegos con más de", limite, "unidades ===")
        print(total_top)






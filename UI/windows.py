import tkinter as tk
from Texts import *

def create_window(root, titulo="", ancho=400, alto=300, bg="lightblue"):
    """Crea una ventana centrada con parámetros personalizables"""
    ventana = tk.Toplevel(root)  # Usar Toplevel para ventanas secundarias
    ventana.title(titulo)
    ventana.geometry(f"{ancho}x{alto}")
    ventana.configure(bg=bg)

    # Centrar ventana
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width // 2) - (ancho // 2)
    y = (screen_height // 2) - (alto // 2)
    ventana.geometry(f"+{x}+{y}")

    return ventana
def create_label(parent, text, font,bg, fg, padx=0, pady=0, wraplength=0, justify="center"):
    label = tk.Label(
        parent,
        text=text,
        font=font,
        bg=bg,
        fg=fg,
        padx=padx,
        pady=pady,
        wraplength=wraplength,
        justify=justify
    )
    return label

# about
def about_window(root):
    about = create_window(root, titulo=senseTitle, ancho=800, alto=800)
    about_title = create_label(
            about,
            text=favoriteOsText,
            font=("Arial", 34, "bold"),
            bg=lightblue,  # Usamos el color directamente para mayor claridad
            fg=black,
    )
    about_title.pack(expand=True)
    mision = create_label(
        about,
        text=ourMission,
        font=("Arial", 30, "bold"),
        bg=lightblue,
        fg=grey
    )
    mision.pack(expand=True)
    mision_text = create_label(
        about,
        text=ourMissionText,
        font=("Arial", 25),
        bg=lightblue,
        fg=green,
        wraplength=600,
        justify="center",
        pady=30
    )
    mision_text.pack(expand=True)
    choose_sense = tk.Label(
        about,
        text=whyChooseSense,
        font=("Arial", 30, "bold"),
        bg=lightblue,
        fg=grey
    )
    choose_sense.pack(expand=True)
    choose_sense_text = create_label(
        about,
        text=whyChooseSenseText,
        font=("Arial", 25),
        bg=lightblue,
        fg=green,
        wraplength=600,
        justify="center",
        pady=30
    )
    choose_sense_text.pack(expand=True)
    return about


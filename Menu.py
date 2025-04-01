from UI.windows import *


def create_menu(root):
    """Función que crea y devuelve la barra de menú completa"""
    menu_bar = tk.Menu(root)

    # Menú About
    about_menu = tk.Menu(menu_bar, tearoff=0)
    about_menu.add_command(label=about, command=lambda: about_window(root))
    menu_bar.add_cascade(label=about, menu=about_menu)

    # Menú Help
    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=help, menu=help_menu)

    # Menú Contact
    contact_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=contct, menu=contact_menu)

    # Menú Future
    future_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=future, menu=future_menu)

    return menu_bar

menu_bar = tk.Menu()

"""
home_menu = tk.Menu(menu_bar, tearoff=0)
home_menu.add_command(label=home, command=root)
menu_bar.add_cascade(label=home, menu=home_menu)
"""

about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label=about, command=lambda: about_window(tk))
menu_bar.add_cascade(label=about, menu=about_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label=help, menu=help_menu)

contact_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label=contct, menu=contact_menu)

future_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label=future, menu=future_menu)


def setup_menu(self):
    # Menú minimalista solo con About
    menu_bar = tk.Menu(self.root)

    about_menu = tk.Menu(menu_bar, tearoff=0)
    about_menu.add_command(label=about, command=lambda: about_window(self.root))
    menu_bar.add_cascade(label=about, menu=about_menu)

    self.root.config(menu=menu_bar)
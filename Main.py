from PIL import Image, ImageTk

from IAConversationWindow import IAConversationWindow
from UI.windows import *
from Texts import *
from Images import *


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_main_window()
        self.load_images()
        self.create_widgets()
        self.setup_menu()
        self.root.mainloop()
        self.root.create_button()

    def setup_main_window(self):
        self.root.title(mainWindowTitle)
        self.root.geometry("1400x1000")
        self.root.resizable(True, True)
        self.root.configure(bg=lightblue)

    def load_images(self):
        # Mantener referencia como atributo de clase
        try:
            imagen = Image.open(logo)
            imagen = imagen.resize((150, 150), Image.LANCZOS)
            self.imagen_tk = ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"{imageLoadingError}: {str(e)}")
            self.imagen_tk = ImageTk.PhotoImage(Image.new('RGB', (200, 200), color=red))

    def create_widgets(self):
        # Título
        title = create_label(
            self.root,
            text=senseTitle,
            font=("Arial", 45, "bold"),
            bg=lightblue,
            fg=teal,
            pady=45
        )
        title.pack()

        # Botón con imagen
        self.imageButton = tk.Button(
            self.root,
            image=self.imagen_tk,
            command=lambda: about_window(self.root),
            borderwidth=0,
            bg="lightblue"
        )
        self.imageButton.image = self.imagen_tk  # Referencia adicional
        self.imageButton.place(relx=1.0, rely=0, anchor="ne")

        # Botón del asistente virtual
        self.assistant_button = tk.Button(
            self.root,
            text="Asistente Virtual",
            font=("Arial", 14),
            bg=grey,
            fg=black,
            padx=20,
            borderwidth=0,
            pady=10,
            command=lambda: IAConversationWindow(self.root)
        )
        self.assistant_button.pack(pady=20)


    def setup_menu(self):
        # Menú minimalista solo con About
        menu_bar = tk.Menu(self.root)
        """
        home_menu = tk.Menu(menu_bar, tearoff=0)
        home_menu.add_command(label=home, command=root)
        menu_bar.add_cascade(label=home, menu=home_menu)
        """

        ia_menu = tk.Menu(menu_bar, tearoff=0)
        ia_menu.add_command(
            label=asistenteVirtualChat,
            command=lambda: IAConversationWindow(self.root)
        )
        menu_bar.add_cascade(label="Asistente", menu=ia_menu)

        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label=about, command=lambda: about_window(self.root))
        menu_bar.add_cascade(label=about, menu=about_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=help, menu=help_menu)

        contact_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=contct, menu=contact_menu)

        future_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=future, menu=future_menu)

        self.root.config(menu=menu_bar)

if __name__ == "__main__":
    app = App()
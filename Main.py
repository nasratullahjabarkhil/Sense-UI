import os
import tkinter as tk
import webbrowser
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
from IAConversationWindow import IAConversationWindow
from Texts import *
from Images import *
from windows import about_window, help_window, contact_window, future_window


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_main_window()
        self.load_images()
        self.create_widgets()
        self.setup_menu()
        self.root.mainloop()

    def setup_main_window(self):
        self.root.title(mainWindowTitle)
        self.root.geometry("1500x1000")
        self.root.resizable(True, True)
        self.root.configure(bg=lightblue)

    def load_images(self):
        try:
            imagen = Image.open(logo)
            imagen = imagen.resize((150, 150), Image.LANCZOS)
            self.imagen_tk = ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"{imageLoadingError}: {str(e)}")
            self.imagen_tk = ImageTk.PhotoImage(Image.new('RGB', (200, 200), color=red))

    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg=lightblue)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Barra superior con título y controles
        header_frame = tk.Frame(main_frame, bg=lightblue)
        header_frame.pack(fill="x", pady=(0, 20))

        # Configurar grid en el header_frame
        header_frame.grid_columnconfigure(0, weight=1)  # Columna izquierda (expansión)
        header_frame.grid_columnconfigure(1, weight=1)  # Columna central (título)
        header_frame.grid_columnconfigure(2, weight=1)  # Columna derecha (botones)

        # Título CENTRADO
        title = tk.Label(
            header_frame,
            text=senseTitle,
            font=("Arial", 45, "bold"),
            bg=lightblue,
            fg=teal
        )
        title.grid(row=0, column=1, sticky="nsew")  # Centrado en columna 1

        # Botones a la derecha (en columna 2)
        header_buttons = tk.Frame(header_frame, bg=lightblue)
        header_buttons.grid(row=0, column=2, sticky="e")

        # Botón de información (About)
        self.imageButton = tk.Button(
            header_buttons,
            image=self.imagen_tk,
            command=lambda: about_window(self.root),
            borderwidth=0,
            bg="lightblue",
            relief="flat"
        )
        self.imageButton.image = self.imagen_tk
        self.imageButton.pack(side="right", padx=(10, 0))

        # Contenedor principal para contenido
        content_frame = tk.Frame(main_frame, bg=lightblue)
        content_frame.pack(fill="both", expand=True)

        # Frame para el chatbot (75% del ancho)
        chatbot_frame = tk.Frame(content_frame, bg=lightblue)
        chatbot_frame.pack(side="left", fill="both", expand=True, padx=(0, 15))

        # Frame para controles laterales (25% del ancho)
        controls_frame = tk.Frame(content_frame, bg=lightblue, width=300)
        controls_frame.pack(side="right", fill="y")

        # Integración del chatbot
        try:
            self.assistant_ui = IAConversationWindow(
                self.root,
                embed=True,
                parent_frame=chatbot_frame
            )
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el asistente: {str(e)}")
            chatbot_frame.destroy()

        # Botón para abrir terminal
        terminal_btn = tk.Button(
            controls_frame,
            text="Abrir Terminal",
            font=("Arial", 12),
            bg=grey,
            fg=black,
            padx=15,
            pady=10,
            command=self.execute_sense_shell,
            width=18,
            relief="groove"
        )
        terminal_btn.pack(pady=(20, 30), fill="x")

        # Botón desplegable de noticias
        self.create_news_dropdown(controls_frame)

        # Botón para abrir terminal
        music_btn = tk.Button(
            controls_frame,
            text="Musica",
            font=("Arial", 12),
            bg=grey,
            fg=black,
            padx=15,
            pady=10,
            command=self.open_music_url,
            width=18,
            relief="groove"
        )
        music_btn.pack(pady=(20, 30), fill="x")

        # Botón para abrir terminal
        calculator_btn = tk.Button(
            controls_frame,
            text="Calculadora",
            font=("Arial", 12),
            bg=grey,
            fg=black,
            padx=15,
            pady=10,
            command=self.open_calculator,
            width=18,
            relief="groove"
        )
        calculator_btn.pack( fill="x")

    def open_music_url(self):
        try:
            webbrowser.open_new("https://www.youtube.com/watch?v=z4j2WZq9hsA&list=PLJGEY7ccQ7V0InCyUYCUT5sIENWx34cA5")  # O cualquier otra URL de servicio musical
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el reproductor de música: {str(e)}")

    def open_calculator(self):
        try:
            subprocess.run(["open", "-a", "Calculator"])
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir la Calculadora: {str(e)}")

    def execute_sense_shell(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(current_dir, "script.sh")

            if not os.path.exists(script_path):
                messagebox.showerror("Error", "script.sh no encontrado")
                return
            if not os.access(script_path, os.X_OK):
                os.chmod(script_path, 0o755)
            try:
                subprocess.run(["xattr", "-d", "com.apple.quarantine", script_path],
                             check=False, stderr=subprocess.DEVNULL)
            except:
                pass
            subprocess.run([
                "osascript",
                "-e",
                f'tell app "Terminal" to do script "cd \'{current_dir}\' && /bin/bash ./script.sh"'
            ], check=True)

        except Exception as e:
            error_msg = f"""
            Error al ejecutar script.sh:
            {str(e)}

            Solución manual:
            1. Abre Terminal
            2. Ejecuta estos comandos:
               cd "{current_dir}"
               chmod +x script.sh
               ./script.sh
            """
            messagebox.showerror("Error", error_msg)

    def create_news_dropdown(self, parent):
        # Frame contenedor
        dropdown_frame = tk.Frame(parent, bg=lightblue)
        dropdown_frame.pack(fill="x", pady=(0, 10))

        # Botón principal
        self.news_dropdown_btn = tk.Button(
            dropdown_frame,
            text="Noticias ▼",
            font=("Arial", 12),
            bg="#4a7a8c",
            fg=black,
            padx=10,
            pady=8,
            relief="flat",
            command=self.toggle_news_dropdown,
            width=25
        )
        self.news_dropdown_btn.pack(fill="x")

        # Menú desplegable (inicialmente oculto)
        self.news_dropdown_menu = tk.Frame(
            dropdown_frame,
            bg="white",
            bd=1,
            relief="solid"
        )

        # Opciones de noticias
        news_sources = [
            ("El País", "https://elpais.com"),
            ("BBC Mundo", "https://www.bbc.com/mundo"),
            ("CNN Español", "https://cnnespanol.cnn.com"),
            ("Reuters", "https://www.reuters.com"),
            ("Google", "https://www.google.com")  # Reemplaza con tu fuente local
        ]

        for name, url in news_sources:
            btn = tk.Button(
                self.news_dropdown_menu,
                text=name,
                font=("Arial", 10),
                bg="white",
                fg="black",
                padx=15,
                pady=5,
                relief="flat",
                command=lambda u=url: self.open_news_url(u),
                anchor="w",
                width=16
            )
            btn.pack(fill="x", pady=1)

        self.news_dropdown_shown = False

    def toggle_news_dropdown(self):
        if self.news_dropdown_shown:
            self.news_dropdown_menu.pack_forget()
            self.news_dropdown_btn.config(text="Noticias ▼")
        else:
            self.news_dropdown_menu.pack(fill="x", pady=(5, 0))
            self.news_dropdown_btn.config(text="Noticias ▲")
        self.news_dropdown_shown = not self.news_dropdown_shown

    def open_news_url(self, url):
        try:
            import webbrowser
            webbrowser.open_new_tab(url)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el navegador:\n{str(e)}")

    def setup_menu(self):
        # Menú minimalista solo con About
        menu_bar = tk.Menu(self.root)
        """
        home_menu = tk.Menu(menu_bar, tearoff=0)
        home_menu.add_command(label=home, command=root)
        menu_bar.add_cascade(label=home, menu=home_menu)
        """
        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label=about, command=lambda: about_window(self.root))
        menu_bar.add_cascade(label=about, menu=about_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label=help, command=lambda: help_window(self.root))
        menu_bar.add_cascade(label=help, menu=help_menu)

        contact_menu = tk.Menu(menu_bar, tearoff=0)
        contact_menu.add_command(label=contct, command=lambda: contact_window(self.root))
        menu_bar.add_cascade(label=contct, menu=contact_menu)

        future_menu = tk.Menu(menu_bar, tearoff=0)
        future_menu.add_command(label=future, command=lambda: future_window(self.root))
        menu_bar.add_cascade(label=future, menu=future_menu)

        self.root.config(menu=menu_bar)


if __name__ == "__main__":
    app = App()

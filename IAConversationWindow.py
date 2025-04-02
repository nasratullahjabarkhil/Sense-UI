import threading
from tkinter import messagebox
import tkinter as tk

from Texts import *
from ai_assistant import *


class IAConversationWindow:
    def __init__(self, parent, model_name: str = "mistral"):
        self.window = tk.Toplevel(parent)
        self.window.title(f"Asistente Virtual ({model_name.capitalize()})")

        try:
            self.assistant = AIAssistant(model_name)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.window.destroy()
            return

        # Configuración inicial
        self.setup_window()
        self.create_widgets()
        self.setup_conversation()

        # Variables de control
        self.thinking_msg_id = None

    def setup_window(self):
        """Configura la ventana principal"""
        self.window.geometry("1000x700")
        self.window.configure(bg=lightblue)

        # Centrar ventana
        window_width = 1000
        window_height = 700
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Fuentes accesibles
        self.large_font = ("Arial", 16)
        self.extra_large_font = ("Arial", 20)
        self.high_contrast = False

    def create_widgets(self):
        """Crea todos los elementos de la interfaz"""
        # Frame principal
        main_frame = tk.Frame(self.window, bg=lightblue)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Área de conversación con estilos
        self.conversation_text = tk.Text(
            main_frame,
            wrap="word",
            font=self.extra_large_font,
            bg="white",
            fg="black",
            padx=15,
            pady=15,
            state="normal",
            height=20
        )
        self.conversation_text.pack(fill="both", expand=True)

        # Configurar tags de estilo
        self.conversation_text.tag_config("thinking", foreground="gray", font=("Arial", 18, "italic"))
        self.conversation_text.tag_config("assistant", foreground="blue", font=("Arial", 20))
        self.conversation_text.tag_config("user", foreground="darkgreen", font=("Arial", 20))
        self.conversation_text.tag_config("error", foreground="red", font=("Arial", 18, "bold"))

        # Scrollbar
        scrollbar = tk.Scrollbar(self.conversation_text)
        scrollbar.pack(side="right", fill="y")
        self.conversation_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.conversation_text.yview)

        # Frame de entrada
        input_frame = tk.Frame(main_frame, bg=lightblue)
        input_frame.pack(fill="x", pady=(10, 0))

        # Campo de entrada
        self.user_input = tk.Entry(
            input_frame,
            font=self.large_font,
            width=60,
        )
        self.user_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", lambda e: self.send_message())

        # Botón de enviar
        self.send_button = tk.Button(
            input_frame,
            text="Enviar",
            font=self.large_font,
            command=self.send_message,
            bg=teal,
            fg=black,
            padx=20,
            state="normal"

        )
        self.send_button.pack(side="right")

        # Controles de accesibilidad
        self.setup_accessibility_controls(main_frame)

        # Inicialmente deshabilitar el Text widget después de configurarlo
        self.conversation_text.config(state="disabled")

        # Configurar tags de estilo para el Asistente (azul)
        self.conversation_text.tag_config(
            "asistente",  # Tag para el asistente
            foreground="#3498DB",  # Azul claro
            font=("Arial", 18, "bold"),
            lmargin1=20,  # Margen izquierdo
            spacing2=5  # Espacio entre párrafos
        )

        # Configurar tags de estilo para el Usuario (verde)
        self.conversation_text.tag_config(
            "tú",  # Tag para el usuario
            foreground="#2ECC71",  # Verde claro
            font=("Arial", 18),
            rmargin=20,  # Margen derecho
            spacing2=5
        )

        # Mantén los otros tags (thinking, error)
        self.conversation_text.tag_config("thinking", foreground="#7F8C8D", font=("Arial", 16, "italic"))
        self.conversation_text.tag_config("error", foreground="#E74C3C", font=("Arial", 16, "bold"))


    def setup_accessibility_controls(self, parent):
        """Botones para ajustes de accesibilidad"""
        control_frame = tk.Frame(parent, bg=lightblue)
        control_frame.pack(fill="x", pady=(10, 0))

        # Controles de tamaño de fuente
        tk.Button(
            control_frame,
            text="A+",
            font=("Arial", 14, "bold"),
            command=self.increase_font_size,
            bg="white",
            width=3
        ).pack(side="left", padx=(0, 5))

        tk.Button(
            control_frame,
            text="A-",
            font=("Arial", 14, "bold"),
            command=self.decrease_font_size,
            bg="white",
            width=3
        ).pack(side="left")

        # Control de contraste
        self.contrast_button = tk.Button(
            control_frame,
            text="Alto Contraste",
            font=("Arial", 12),
            command=self.toggle_contrast,
            bg="white"
        )
        self.contrast_button.pack(side="right")

    def setup_conversation(self):
        """Inicia la conversación con mensaje de bienvenida"""
        welcome_message = (
            "¡Hola! Soy tu asistente virtual. "
            "Puedes preguntarme lo que necesites.\n\n"
        )
        self.display_message("Asistente", welcome_message)

    def send_message(self):
        """Procesa el mensaje del usuario"""
        user_text = self.user_input.get().strip()
        if user_text:
            # Mostrar mensaje del usuario
            self.display_message("Tú", user_text)
            self.user_input.delete(0, "end")

            # Deshabilitar entrada durante el procesamiento
            self.user_input.config(state="disabled")
            self.send_button.config(state="disabled", text="Enviando...")

            # Procesar respuesta
            self.process_ai_response(user_text)

    def process_ai_response(self, user_input: str):
        """Maneja la obtención de la respuesta de la IA"""
        # Mostrar indicador de "Pensando..."
        self.conversation_text.config(state="normal")
        self.thinking_msg_id = self.conversation_text.index("end-1c")
        self.conversation_text.insert("end", "Asistente: Pensando...\n\n", "thinking")
        self.conversation_text.config(state="disabled")
        self.window.update()

        # Hilo para no bloquear la interfaz
        def generate_response():
            try:
                ai_response = self.assistant.get_response(user_input)
                self.window.after(0, lambda: self.show_final_response(ai_response))
            except Exception as e:
                self.window.after(0, lambda: self.show_error(str(e)))
            finally:
                self.window.after(0, lambda: [
                    self.user_input.config(state="normal"),
                    self.send_button.config(state="normal", text="Enviar"),
                    self.user_input.focus()
                ])

        threading.Thread(target=generate_response, daemon=True).start()

    def show_final_response(self, response: str):
        """Muestra la respuesta final reemplazando el mensaje temporal"""
        self.conversation_text.config(state="normal")

        # Eliminar mensaje "Pensando..."
        if self.thinking_msg_id:
            self.conversation_text.delete(self.thinking_msg_id, "end")
            self.thinking_msg_id = None

        # Insertar respuesta formateada
        self.conversation_text.insert("end", "Asistente: ", "assistant")
        self.conversation_text.insert("end", f"{response}\n\n")

        self.conversation_text.config(state="disabled")
        self.conversation_text.see("end")

    def show_error(self, error_msg: str):
        """Muestra mensajes de error"""
        self.conversation_text.config(state="normal")

        # Eliminar mensaje "Pensando..." si existe
        if self.thinking_msg_id:
            self.conversation_text.delete(self.thinking_msg_id, "end")
            self.thinking_msg_id = None

        self.conversation_text.insert("end", f"Error: {error_msg}\n\n", "error")
        self.conversation_text.config(state="disabled")
        self.conversation_text.see("end")

    def display_message(self, sender: str, message: str):
        """Muestra mensajes normales en la conversación"""
        self.conversation_text.config(state="normal")
        tag = sender.lower()
        self.conversation_text.insert("end", f"{sender}: ", (tag,))
        self.conversation_text.insert("end", f"{message}\n\n")
        self.conversation_text.config(state="disabled")
        self.conversation_text.see("end")

    # Métodos de accesibilidad
    def increase_font_size(self):
        """Aumenta el tamaño de fuente"""
        current_size = self.large_font[1]
        new_size = min(current_size + 2, 28)
        self.large_font = (self.large_font[0], new_size)
        self.extra_large_font = (self.extra_large_font[0], new_size + 4)
        self.update_fonts()

    def decrease_font_size(self):
        """Reduce el tamaño de fuente"""
        current_size = self.large_font[1]
        new_size = max(current_size - 2, 14)
        self.large_font = (self.large_font[0], new_size)
        self.extra_large_font = (self.extra_large_font[0], new_size + 4)
        self.update_fonts()

    def toggle_contrast(self):
        """Alterna el modo de alto contraste"""
        self.high_contrast = not self.high_contrast
        if self.high_contrast:
            self.conversation_text.config(bg="black", fg="white")
            self.contrast_button.config(bg="black", fg=blue)

        else:
            self.conversation_text.config(bg="white", fg="black")
            self.contrast_button.config(bg="white", fg="black")

    def update_fonts(self):
        """Actualiza todas las fuentes en la interfaz"""
        self.conversation_text.config(font=self.extra_large_font)
        self.user_input.config(font=self.large_font)
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


def help_window(root):
    help_win = create_window(root, titulo="SENSE Help", ancho=700, alto=800)

    # Main container with scrollbar
    main_frame = tk.Frame(help_win, bg=lightblue)
    main_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(main_frame, bg=lightblue)
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=lightblue)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Title
    help_title = create_label(
        scrollable_frame,
        text="Help & Support",
        font=("Arial", 34, "bold"),
        bg=lightblue,
        fg=black
    )
    help_title.pack(pady=20, anchor="center")

    # Getting Started section
    section1 = create_label(
        scrollable_frame,
        text="Getting Started with SENSE OS",
        font=("Arial", 30, "bold"),
        bg=lightblue,
        fg=grey
    )
    section1.pack(pady=10, anchor="center")

    desc1 = create_label(
        scrollable_frame,
        text="Welcome to SENSE OS! To help you get started, here are a few\n"
             "steps to familiarize yourself with the system and its features:",
        font=("Arial", 25),
        bg=lightblue,
        fg=green,
        wraplength=600,
        justify="center",
        pady=30
    )
    desc1.pack(pady=10, anchor="center")

    # Features list
    features_text = create_label(
        scrollable_frame,
        text="\n".join([
            "- Voice Commands: Enable the voice assistant to control various features of the system.",
            "- Screen Reader: Turn on the screen reader to hear descriptions of your actions.",
            "- Braille Support: Connect a Braille display to interact with SENSE OS more efficiently.",
            "- Adjusting Settings: Customize font size, contrast, and other accessibility features."
        ]),
        font=("Arial", 20),
        bg=lightblue,
        fg=black,
        wraplength=600,
        justify="center",
        pady=20
    )
    features_text.pack(pady=10, anchor="center")

    # Commands section
    section2 = create_label(
        scrollable_frame,
        text="SENSE Shell Commands",
        font=("Arial", 30, "bold"),
        bg=lightblue,
        fg=grey
    )
    section2.pack(pady=10, anchor="center")

    commands_text = create_label(
        scrollable_frame,
        text="\n".join([
            "- SENSE: Used to access our shell",
            "- uninstall-sense: Removes the folder structure and commands themselves",
            "- space: Show disk space",
            "- memory: Shows the free memory",
            "- services: Shows the services that are running",
            "- cpu: Shows the use of the cpu",
            "- find-file name: Returns the path to the file passed as parameter",
            "- processes: Displays the running processes created by the user",
            "- order-66 pid: Stops the process whose pid coincides with the past",
            "- system-run: Sample the time the system has been in operation",
            "- active-connections: Shows you the active network connections",
            "- processes-memory: Shows you the processes that consume the most memory",
            "- processes-cpu: Shows you the most cpu-consuming processes",
            "- help-sense: Opens the help documentation",
            "- bye: Turns off the system",
            "- miguel: Display an ASCII artwork",
            "- example: Creates and executes a sample script",
            "- no-example: Removes the example script and folder"
        ]),
        font=("Arial", 20),
        bg=lightblue,
        fg=black,
        wraplength=600,
        justify="left",
        pady=20
    )
    commands_text.pack(pady=10,padx=50, anchor="center")

    # Common Issues section
    section3 = create_label(
        scrollable_frame,
        text="Common Issues & Solutions",
        font=("Arial", 30, "bold"),
        bg=lightblue,
        fg=grey
    )
    section3.pack(pady=10, anchor="center")

    issues_text = create_label(
        scrollable_frame,
        text="\n".join([
            "- Voice Assistant Not Responding: Ensure the microphone is enabled in your settings",
            "- Screen Reader Lag: Adjust the speed in the accessibility settings",
            "- Connection Issues: Check your internet connection or restart your device"
        ]),
        font=("Arial", 20),
        bg=lightblue,
        fg=black,
        wraplength=600,
        justify="left",
        pady=20
    )
    issues_text.pack(pady=10, anchor="center")

    # Contact section
    section4 = create_label(
        scrollable_frame,
        text="Contact Support",
        font=("Arial", 30, "bold"),
        bg=lightblue,
        fg=grey
    )
    section4.pack(pady=10, anchor="center")

    contact_text = create_label(
        scrollable_frame,
        text="If you need further assistance, please contact our support team tlf:XXXXXXXXXXXX.",
        font=("Arial", 25),
        bg=lightblue,
        fg=green,
        wraplength=600,
        justify="center",
        pady=30
    )
    contact_text.pack(pady=10, anchor="center")

    return help_win


def contact_window(root):
    contact = create_window(root, titulo="Contact - SENSE OS", ancho=800, alto=800)
    title1 = create_label(
        contact,
        text="Do you need help?",
        font=("Arial", 34, "bold"),
        bg=lightblue,
        fg=black
    )
    title1.pack(expand=True)

    title2 = create_label(
        contact,
        text="We are here for you!",
        font=("Arial", 34, "bold"),
        bg=lightblue,
        fg=black
    )
    title2.pack(expand=True)

    contact_text = ("At Sense OS, we want your experience to be simple and accessible. "
                    "If you have any questions, need technical support, or want to send us suggestions, "
                    "you can contact us in the following ways:\n\n"
                    "Phone: 111222333\n"
                    "Email: Ejemplo@gmail.com\n"
                    "Website: DenseOS.com\n\n"
                    "Our support team is available Monday to Friday from 10:00 a.m. to 6:00 p.m. "
                    "to help you with any problems or queries.\n\n"
                    "Your comfort and accessibility are our priority!")

    contact_info = create_label(
        contact,
        text=contact_text,
        font=("Arial", 20),
        bg=lightblue,
        fg=darkblue,
        wraplength=600,
        justify="center",
        pady=30
    )
    contact_info.pack(expand=True)

    return contact


def future_window(root):
    future = create_window(root, titulo="Future - SENSE OS", ancho=800, alto=800)

    title = create_label(
        future,
        text="Future of Sense",
        font=("Arial", 34, "bold"),
        bg=lightblue,
        fg=black
    )
    title.pack(pady=50)

    future_text = (
        "Welcome to Sense, a Unix-based operating system designed specifically for blind and elderly people.\n\n"
        "In this section, we explore the directions and visions that guide the continued development of this platform.\n\n"
        "Our goal is clear: create an operating system that not only meets the current needs of our users "
        "but also evolves to adapt to the challenges and opportunities of the future.")

    future_description = create_label(
        future,
        text=future_text,
        font=("Arial", 20),
        bg=lightblue,
        fg=black,
        wraplength=600,
        justify="center",
        pady=30
    )
    future_description.pack()

    objectives_title = create_label(
        future,
        text="Our Objectives",
        font=("Arial", 30, "bold"),
        bg=lightblue,
        fg=black
    )
    objectives_title.pack(pady=20)

    objectives_text = ("1. Accessibility without limits\n"
                       "2. Simplicity and ease of use\n"
                       "3. Security and privacy\n"
                       "4. Sustainability and compatibility")

    objectives = create_label(
        future,
        text=objectives_text,
        font=("Arial", 20),
        bg=lightblue,
        fg=black,
        wraplength=600,
        justify="left",
        pady=30
    )
    objectives.pack()

    return future

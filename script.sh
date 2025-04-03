#!/bin/bash

# Configuración inicial para macOS
export PS1="Sense@$(whoami)> "
HISTFILE="$HOME/SENSE/Program_Files/SHELL_HISTORY"
HISTSIZE=1000
SAVEHIST=1000

# Crear directorios necesarios
if [ ! -d "$HOME/SENSE/Program_Files" ]; then
    mkdir -p "$HOME/SENSE/Program_Files"
fi

if [ ! -f "$HISTFILE" ]; then
    touch "$HISTFILE"
fi

history -r "$HISTFILE"
echo "Welcome to SENSE (macOS Edition)"
trap 'echo " Process interrupted"; continue' SIGINT

# Funciones adaptadas para macOS
space() {
    echo "Available disk space:"
    df -h
}

memory() {
    echo "Memory usage:"
    vm_stat | perl -ne '/page size of (\d+)/ and $size=$1; /Pages\s+([^:]+)[^\d]+(\d+)/ and printf("%-16s % 16.2f MB\n", "$1:", $2 * $size / 1048576)'
}

services() {
    echo "Running services:"
    launchctl list | grep -v "\-\t0"
}

cpu() {
    echo "CPU usage:"
    top -l 1 -s 0 | grep -E "^CPU"
}

find-file() {
    echo "Enter the name of the file to search for:"
    read archivo
    resultados=$(mdfind -name "$archivo")
    if [ -z "$resultados" ]; then
        echo "Error: File not found '$archivo'."
    else
        echo "File(s) found:"
        echo "$resultados"
    fi
}

processes() {
    echo "Running processes for user $(whoami):"
    ps aux | grep "^$(whoami)" | awk '{print $2, $11}'
}

order-66() {
    pid=$1
    if [ -z "$pid" ]; then
        echo "Error: PID not provided."
        return 1
    fi
    if kill -0 $pid 2>/dev/null; then
        sudo kill -9 $pid
        echo "Process $pid eliminated."
    else
        echo "Error: The PID $pid does not exist."
    fi
}

system-run() {
    echo "System uptime:"
    uptime
}

active-connections() {
    echo "Active network connections:"
    lsof -i -P | grep -i "established"
}

processes-memory() {
    echo "Top memory-consuming processes:"
    ps aux -r | head -n 11
}

processes-cpu() {
    echo "Top CPU-consuming processes:"
    ps aux -S | head -n 11
}

help-sense() {
    open "https://example.com/sense-help"  # Reemplaza con tu URL de ayuda
}

bye() {
    sudo shutdown -h now
}

miguel() {
    echo "                                                        "
    echo "███    ███  █████╗ ████████╗ █████╗ ███╗   ███╗███████╗ "
    echo "████  ████ ██╔══██╗╚══██╔══╝██╔══██╗████╗ ████║██╔════╝ "
    echo "██╔████╔██║███████║   ██║   ███████║██╔████╔██║█████╗   "
    echo "██║╚██╔╝██║██╔══██║   ██║   ██╔══██║██║╚██╔╝██║██╔══╝   "
    echo "██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║ ╚═╝ ██║███████╗ "
    echo "╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ "
    echo "════════════════════════════════════════════════════════"
    echo "    ██████╗ █████╗ ███╗   ███╗██╗ ██████╗ ███╗   ██╗   "
    echo "   ██╔════╝██╔══██╗████╗ ████║██║██╔═══██╗████╗  ██║   "
    echo "   ██║     ███████║██╔████╔██║██║██║   ██║██╔██╗ ██║   "
    echo "   ██║     ██╔══██║██║╚██╔╝██║██║██║   ██║██║╚██╗██║   "
    echo "   ╚██████╗██║  ██║██║ ╚═╝ ██║██║╚██████╔╝██║ ╚████║   "
    echo "    ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝   "
    echo "═══════════════════════════════════════════════════════"
}

example() {
    DIR="$HOME/SENSE/example"
    mkdir -p "$DIR"
    
    cat > "$DIR/example.sh" <<EOF
#!/bin/bash
while true; do
    sleep 1
done
EOF
    
    chmod +x "$DIR/example.sh"
    "$DIR/example.sh" &
    
    sleep 1
    pid=$(pgrep -o -f "$DIR/example.sh")
    echo "The PID of the process created by running example.sh is: $pid"
}

no-example() {
    DIR="$HOME/SENSE/example"
    if [ -d "$DIR" ]; then
        rm -rf "$DIR"
        echo "Example was removed"
    else
        echo "Error: example has not been created previously."
    fi
}

# Procesamiento de comandos
if [[ $# -gt 0 ]]; then
    cmd="$1"
    shift
    case "$cmd" in
        "space") space ;;
        "memory") memory ;;
        "services") services ;;
        "cpu") cpu ;;
        "find-file") find-file ;;
        "processes") processes ;;
        "order-66")
            [[ -n "$1" ]] && order-66 "$1" || echo "Error: PID required for 'order-66'"
            ;;
        "system-run") system-run ;;
        "active-connections") active-connections ;;
        "processes-memory") processes-memory ;;
        "processes-cpu") processes-cpu ;;
        "help-sense") help-sense ;;
        "bye") bye ;;
        "miguel") miguel ;;
        "example") example ;;
        "no-example") no-example ;;
        "exit") exit 0 ;;
        *)
            echo "$cmd $*" >> "$HISTFILE"
            history -s "$cmd $*"
            eval "$cmd $*"
            ;;
    esac
fi

# Shell interactivo
while true; do
    read -e -p "$PS1" cmd
    case "$cmd" in
        "space") space ;;
        "memory") memory ;;
        "services") services ;;
        "cpu") cpu ;;
        "find-file") find-file ;;
        "processes") processes ;;
        "order-66"*)
            pid=$(echo $cmd | awk '{print $2}')
            order-66 $pid
            ;;
        "system-run") system-run ;;
        "active-connections") active-connections ;;
        "processes-memory") processes-memory ;;
        "processes-cpu") processes-cpu ;;
        "help-sense") help-sense ;;
        "bye") bye ;;
        "miguel") miguel ;;
        "example") example ;;
        "no-example") no-example ;;
        "exit") break ;;
        *)
            echo "$cmd" >> "$HISTFILE"
            history -s "$cmd"
            eval "$cmd"
            ;;
    esac
done

export PS1="\u@\h:\w$ "
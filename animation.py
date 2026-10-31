# -*- coding: utf-8 -*-
import sys
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def typewriter(text: str, delay: float = 0.015, color=Fore.CYAN):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def play_intro():
    clear()
    banner = r"""
   ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗
   ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║
   ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║
   ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║
   ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗
   ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
    """
    for line in banner.splitlines():
        print(Fore.MAGENTA + line)
        time.sleep(0.01)
    
    print()
    typewriter("  [SYS] Chargement des modules de destruction...", 0.015, Fore.RED)
    time.sleep(0.2)
    typewriter("  [SYS] Contournement des sécurités...", 0.015, Fore.YELLOW)
    time.sleep(0.2)
    typewriter("  [SYS] Accès accordé. Bienvenue, Opérateur.", 0.015, Fore.GREEN)
    time.sleep(0.3)
    print()
    
    # Barre de chargement
    sys.stdout.write(Fore.CYAN + "  ╔══════════════════════════════════════════╗\n")
    sys.stdout.write(Fore.CYAN + "  ║ [")
    for _ in range(40):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("] 100% ║\n")
    sys.stdout.write(Fore.CYAN + "  ╚══════════════════════════════════════════╝\n\n")
    time.sleep(0.4)

def fake_window_transition(text="Chargement"):
    clear()
    print(Fore.MAGENTA + "\n\n" + " "*15 + "╔" + "═"*54 + "╗")
    print(" "*15 + "║ " + Fore.WHITE + Style.BRIGHT + f"NOUVELLE FENÊTRE : {text.upper()}".center(52) + Style.RESET_ALL + Fore.MAGENTA + " ║")
    print(" "*15 + "╠" + "═"*54 + "╣")
    
    sys.stdout.write(Fore.CYAN + " "*15 + "║ [")
    for _ in range(40):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.01)
    sys.stdout.write("] Prêt ! ║\n")
    print(" "*15 + "╚" + "═"*54 + "╝")
    time.sleep(0.2)
    clear()

# -*- coding: utf-8 -*-
import asyncio
import sys
import time
from colorama import Fore, init

from animation import play_intro, clear, fake_window_transition
from menu import (
    print_main_menu, print_action_mode_menu, 
    print_channel_menu, print_role_menu, get_choice
)
from config import load_config, save_config, ask_quick_target
from actions import execute_action

init(autoreset=True)

def select_mode_and_cfg(kind: str, base_cfg: dict):
    print_action_mode_menu()
    mode = None
    while True:
        c = get_choice()
        if c == "1": mode = "bot"; break
        elif c == "2": mode = "selfbot"; break
        elif c == "3": mode = "webhook"; break
        elif c == "0": return None
        else: print(Fore.RED + "  [!] Choix invalide")

    fake_window_transition("Paramètres")
    cfg = ask_quick_target(base_cfg, mode, action=kind)
    cfg["mode"] = mode
    save_config(cfg)
    return cfg

def run_channel_menu(cfg):
    while True:
        print_channel_menu()
        c = get_choice()
        if c == "1":
            n = input(Fore.WHITE + "  Combien de salons créer ? (défaut 10) : " + Fore.RESET).strip()
            n = int(n) if n.isdigit() else 10
            prefix = input(Fore.WHITE + "  Nom des salons : " + Fore.RESET).strip()
            prefix = prefix if prefix else "nuked"
            
            fake_window_transition("Création des salons")
            asyncio.run(execute_action(cfg, "create_channels", n, prefix))
            input(Fore.YELLOW + "\n  Appuie sur Entrée pour continuer...")
        elif c == "2":
            fake_window_transition("Suppression des salons")
            asyncio.run(execute_action(cfg, "delete_channels"))
            input(Fore.YELLOW + "\n  Appuie sur Entrée pour continuer...")
        elif c == "0":
            break

def run_role_menu(cfg):
    while True:
        print_role_menu()
        c = get_choice()
        if c == "1":
            n = input(Fore.WHITE + "  Combien de rôles créer ? (défaut 10) : " + Fore.RESET).strip()
            n = int(n) if n.isdigit() else 10
            prefix = input(Fore.WHITE + "  Nom des rôles : " + Fore.RESET).strip()
            prefix = prefix if prefix else "nuked"
            
            fake_window_transition("Création des rôles")
            asyncio.run(execute_action(cfg, "create_roles", n, prefix))
            input(Fore.YELLOW + "\n  Appuie sur Entrée pour continuer...")
        elif c == "2":
            fake_window_transition("Suppression des rôles")
            asyncio.run(execute_action(cfg, "delete_roles"))
            input(Fore.YELLOW + "\n  Appuie sur Entrée pour continuer...")
        elif c == "0":
            break

def main():
    play_intro()
    cfg = load_config()

    while True:
        print_main_menu()
        choice = get_choice()
        
        if choice == "1":
            cfg_act = select_mode_and_cfg("raid", cfg)
            if cfg_act:
                fake_window_transition("Lancement du RAID")
                asyncio.run(execute_action(cfg_act, "raid"))
                input(Fore.YELLOW + "\n  Appuie sur Entrée pour revenir...")
                
        elif choice == "2":
            cfg_act = select_mode_and_cfg("nuke", cfg)
            if cfg_act:
                fake_window_transition("Lancement du NUKE")
                asyncio.run(execute_action(cfg_act, "nuke"))
                input(Fore.YELLOW + "\n  Appuie sur Entrée pour revenir...")
                
        elif choice == "3":
            cfg_act = select_mode_and_cfg("spam", cfg)
            if cfg_act:
                fake_window_transition("Envoi du SPAM")
                asyncio.run(execute_action(cfg_act, "spam"))
                input(Fore.YELLOW + "\n  Appuie sur Entrée pour revenir...")
                
        elif choice == "4":
            cfg_act = select_mode_and_cfg("dm_all", cfg)
            if cfg_act:
                fake_window_transition("Envoi des DM")
                asyncio.run(execute_action(cfg_act, "dm_all"))
                input(Fore.YELLOW + "\n  Appuie sur Entrée pour revenir...")
                
        elif choice == "5":
            cfg_act = select_mode_and_cfg("ban_all", cfg)
            if cfg_act:
                fake_window_transition("Bannissement de masse")
                asyncio.run(execute_action(cfg_act, "ban_all"))
                input(Fore.YELLOW + "\n  Appuie sur Entrée pour revenir...")
                
        elif choice == "6":
            cfg_act = select_mode_and_cfg("manage_channels", cfg)
            if cfg_act:
                run_channel_menu(cfg_act)
                
        elif choice == "7":
            cfg_act = select_mode_and_cfg("manage_roles", cfg)
            if cfg_act:
                run_role_menu(cfg_act)
                
        elif choice == "8":
            cfg_act = select_mode_and_cfg("webhook_mass", cfg)
            if cfg_act:
                fake_window_transition("Webhook Massif")
                asyncio.run(execute_action(cfg_act, "webhook_mass"))
                input(Fore.YELLOW + "\n  Appuie sur Entrée pour revenir...")
                
        elif choice == "9":
            cfg_act = select_mode_and_cfg("voice_kick", cfg)
            if cfg_act:
                fake_window_transition("Voice Kick")
                asyncio.run(execute_action(cfg_act, "voice_kick"))
                input(Fore.YELLOW + "\n  Appuie sur Entrée pour revenir...")
                
        elif choice == "0":
            clear()
            print(Fore.CYAN + "\n  Fermeture de Sentinel...\n")
            time.sleep(0.5)
            sys.exit(0)
        else:
            print(Fore.RED + "  [!] Choix invalide")
            time.sleep(1)

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: 
        print(Fore.RED + "\n\n  [X] Processus interrompu par l'utilisateur.")
        sys.exit(0)

# -*- coding: utf-8 -*-
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear(): os.system("cls" if os.name == "nt" else "clear")

def print_header(title):
    clear()
    # Double trait en haut et en bas du titre (Rouge)
    print(Fore.RED + f"\n  ╔══════════════════════════════════════════════════════════╗")
    print(Fore.RED + f"  ║ " + Fore.WHITE + Style.BRIGHT + f"{title.center(56)}" + Style.RESET_ALL + Fore.RED + " ║")
    print(Fore.RED + f"  ╚══════════════════════════════════════════════════════════╝\n")

def print_main_menu():
    print_header("S E N T I N E L   —   M E N U   P R I N C I P A L")
    
    print(Fore.RED + "  ╔══════════════╦══════════════════════════════════════════╗")
    print(Fore.RED + "  ║ " + Fore.RED + Style.BRIGHT + "DESTRUCTION  " + Style.RESET_ALL + Fore.RED + "║ " + Fore.WHITE + "Attaques massives                        " + Fore.RED + "║")
    print(Fore.RED + "  ╠══════════════╬══════════════════════════════════════════╣")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[1] RAID     " + Fore.RED + "║ " + Fore.WHITE + "Attaque modérée du serveur               " + Fore.RED + "║")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[2] NUKE     " + Fore.RED + "║ " + Fore.WHITE + "Destruction totale (Nom, Icône, Spam)    " + Fore.RED + "║")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[3] SPAM     " + Fore.RED + "║ " + Fore.WHITE + "Spam de messages (Salons/Webhook)        " + Fore.RED + "║")
    print(Fore.RED + "  ╠══════════════╬══════════════════════════════════════════╣")
    print(Fore.RED + "  ║ " + Fore.RED + Style.BRIGHT + "MEMBRES      " + Style.RESET_ALL + Fore.RED + "║ " + Fore.WHITE + "Actions sur les utilisateurs             " + Fore.RED + "║")
    print(Fore.RED + "  ╠══════════════╬══════════════════════════════════════════╣")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[4] DM ALL   " + Fore.RED + "║ " + Fore.WHITE + "Message privé à tous les membres         " + Fore.RED + "║")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[5] BAN ALL  " + Fore.RED + "║ " + Fore.WHITE + "Bannissement de masse                    " + Fore.RED + "║")
    print(Fore.RED + "  ╠══════════════╬══════════════════════════════════════════╣")
    print(Fore.RED + "  ║ " + Fore.RED + Style.BRIGHT + "GESTION      " + Style.RESET_ALL + Fore.RED + "║ " + Fore.WHITE + "Contrôle des éléments du serveur         " + Fore.RED + "║")
    print(Fore.RED + "  ╠══════════════╬══════════════════════════════════════════╣")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[6] SALONS   " + Fore.RED + "║ " + Fore.WHITE + "Créer / Supprimer des salons             " + Fore.RED + "║")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[7] RÔLES    " + Fore.RED + "║ " + Fore.WHITE + "Créer / Supprimer des rôles              " + Fore.RED + "║")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[8] WEBHOOK  " + Fore.RED + "║ " + Fore.WHITE + "Créer & spammer via webhooks             " + Fore.RED + "║")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[9] VOICE    " + Fore.RED + "║ " + Fore.WHITE + "Déconnecter les membres des vocaux       " + Fore.RED + "║")
    print(Fore.RED + "  ╠══════════════╬══════════════════════════════════════════╣")
    print(Fore.RED + "  ║ " + Fore.RED + "[0] QUITTER  " + Fore.RED + "║ " + Fore.WHITE + "Fermer Sentinel                          " + Fore.RED + "║")
    print(Fore.RED + "  ╚══════════════╩══════════════════════════════════════════╝\n")

def print_action_mode_menu():
    print_header("M O D E   D ' E X É C U T I O N")
    print(Fore.RED + "  ╔══════════════════════════════════════════════════════════╗")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[1] BOT DISCORD   " + Fore.RED + "║ " + Fore.WHITE + "Token de bot officiel" + " "*20 + Fore.RED + "║")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[2] SELF-BOT      " + Fore.RED + "║ " + Fore.WHITE + "Token d'utilisateur" + " "*21 + Fore.RED + "║")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[3] WEBHOOK       " + Fore.RED + "║ " + Fore.WHITE + "URL Webhook uniquement" + " "*18 + Fore.RED + "║")
    print(Fore.RED + "  ╠══════════════════════════════════════════════════════════╣")
    print(Fore.RED + "  ║ " + Fore.RED + "[0] ANNULER       " + Fore.RED + "║ " + Fore.WHITE + "Retour au menu principal" + " "*17 + Fore.RED + "║")
    print(Fore.RED + "  ╚══════════════════════════════════════════════════════════╝\n")

def print_channel_menu():
    print_header("G E S T I O N   D E S   S A L O N S")
    print(Fore.RED + "  ╔══════════════════════════════════════════════════════════╗")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[1] Créer des salons de masse                            " + Fore.RED + "║")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[2] Supprimer tous les salons                            " + Fore.RED + "║")
    print(Fore.RED + "  ╠══════════════════════════════════════════════════════════╣")
    print(Fore.RED + "  ║ " + Fore.RED + "[0] Retour au menu principal                             " + Fore.RED + "║")
    print(Fore.RED + "  ╚══════════════════════════════════════════════════════════╝\n")

def print_role_menu():
    print_header("G E S T I O N   D E S   R Ô L E S")
    print(Fore.RED + "  ╔══════════════════════════════════════════════════════════╗")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[1] Créer des rôles de masse                             " + Fore.RED + "║")
    print(Fore.RED + "  ║ " + Fore.WHITE + "[2] Supprimer tous les rôles                             " + Fore.RED + "║")
    print(Fore.RED + "  ╠══════════════════════════════════════════════════════════╣")
    print(Fore.RED + "  ║ " + Fore.RED + "[0] Retour au menu principal                             " + Fore.RED + "║")
    print(Fore.RED + "  ╚══════════════════════════════════════════════════════════╝\n")

def get_choice(prompt="  >> Votre choix : "):
    return input(Fore.RED + Style.BRIGHT + prompt + Fore.WHITE).strip()

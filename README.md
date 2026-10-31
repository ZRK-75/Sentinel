# 🛡️ Sentinel — Ultimate Server Management Tool

**Sentinel** est un outil d'administration et de gestion pour serveurs Discord. Il propose une interface en ligne de commande (CLI) animée avec de multiples fonctionnalités d'optimisation, de gestion des membres et d'automatisation.

> ⚠️ **AVERTISSEMENT** : Cet outil est fourni à des fins **strictement éducatives et personnelles**. L'utiliser sur des serveurs que vous ne possédez pas est contraire aux CGU de Discord. L'auteur décline toute responsabilité en cas de mauvaise utilisation.

---

## 🚀 Installation

L'installation se fait directement depuis GitHub. 

### 1. Cloner le dépôt
Ouvre **Termux** (ou ton terminal) et tape :
```bash
git clone https://github.com/ZRK-75/Sentinel.git
cd Sentinel
pkg update -y && pkg upgrade -y
pkg install -y python git
pip install discord.py aiohttp colorama
python main.py


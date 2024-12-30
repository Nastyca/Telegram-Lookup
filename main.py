import os
import requests

from pystyle import *
from bs4 import BeautifulSoup
from colorama import Fore, init

#-

def cls():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear') 

#-

e = Fore.RESET
g = Fore.GREEN
r = Fore.RED
b = Fore.WHITE

#-

cls()

Write.Print(f"""
 _______   _                                  _                 _                
|__   __| | |                                | |               | |               
   | | ___| | ___  __ _ _ __ __ _ _ __ ___   | |     ___   ___ | | __ _   _ _ __  
   | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \  | |    / _ \ / _ \| |/ /| | | | '_ \ 
   | |  __/ |  __/ (_| | | | (_| | | | | | | | |___| (_) | (_) |   < | |_| | |_) |
   |_|\___|_|\___|\__, |_|  \__,_|_| |_| |_| |______\___/ \___/|_|\_\ \__,_| .__/ 
                   __/ |                                                 | |    
                  |___/                                                  |_|    \n""", Colors.blue_to_purple, interval=0)

recherche = input(f"\n{Fore.LIGHTMAGENTA_EX}Entrez votre recherche ->{Fore.RESET} ")
print(f"")

#-

try:
    requete = requests.get(f"https://t.me/{recherche}")
    soup = BeautifulSoup(requete.text, 'html.parser')

    nom = soup.find('meta', {'property': 'og:title'})['content'] if soup.find('meta', {'property': 'og:title'}) else "N/A"
    logo = soup.find('meta', {'property': 'og:image'})['content'] if soup.find('meta', {'property': 'og:image'}) else "N/A"
    description = soup.find('meta', {'property': 'og:description'})['content'] if soup.find('meta', {'property': 'og:description'}) else "N/A"
    abos = soup.find('div', {'class': 'tgme_page_extra'}).text.strip() if soup.find('div', {'class': 'tgme_page_extra'}) else "N/A"

    if "subscriber" in abos:
        extra = f"Abonnés : {abos.replace('subscribers', '').replace('members', '').replace(',', '(').replace('online', 'en ligne )')}"
    elif "member" in abos:
        extra = f"Membres : {abos.replace('subscribers', '').replace('members', '').replace(',', '(').replace('online', 'en ligne )')}"
    else:
        extra = f"Nom d'utilisateur : {abos}"

    print(f"""{g}Nom : {b}{nom}
{g}{extra}
{g}Lien : {b}t.me/{recherche}
{g}Description : {b}{description}""")
    
except Exception as erreur:
    print(f"{r}[-] Erreur : {erreur}")

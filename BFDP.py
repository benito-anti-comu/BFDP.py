#*****************************
#
# Ciao, questo e un brute force dei siti wb per scoprire dei path nei URL, e una piccola casa creata da me
# Spero che vi piacia.
#
#******************************

import argparse
import requests # type: ignore
import os
from time import sleep
from colorama import Fore, init # type: ignore

init()

argomenti = argparse.ArgumentParser(description="questo e un brute force dei siti web per scoprire path")

argomenti.add_argument("-u", "--url", action="store_true", help="mettere dominio del sito")
argomenti.add_argument("URL", type=str, help="deminio del sito web")
argomenti.add_argument("-w", "--wordlist", action="store_true", help="mettere percorso wordlist")
argomenti.add_argument("WORDLIST", type=str, help="percoso wordlist")

args = argomenti.parse_args()

percosso_wordlist = args.WORDLIST

array = []
if os.path.exists(percosso_wordlist):
    with open(f"{percosso_wordlist}", "r") as file:
        for righa in file:
            array.append(righa.strip())
else:
    print("il percosso del file non esiste o e errato")
    quit()

andare = True

print("creato da: benito-GRANDE")

while andare:
    for numero, sottodominio in enumerate(array):
        try:
            URL = requests.get(f"{args.URL}/{sottodominio}")

            if URL.ok:
                print(Fore.GREEN + f"Tutto bene {URL}/{sottodominio}")

            if URL.status_code == 404:
                print(Fore.RED + f"errore {URL}/{sottodominio}")
            
            sleep(2)

        except requests.exceptions.RequestException as e:
            print(f"Errore durante la richiesta: {e}")
    
    print(Fore.WHITE + f"\nTutte le righe della wordlist: {percosso_wordlist} sono state lette.")
    andare = False
#Imports

from pathlib import Path
import subprocess

#Funções

def limpar_apt():
    limpar = subprocess.run(
        ['sudo', 'apt', 'clean']
    )

def limpar_temp():
    caminho = Path.home() / '.cache'
    limpar = subprocess.run(
        ['rm', '-rf', str(caminho)]
    )

def limpar_log():
    limpar = subprocess.run(
        ['sudo', 'journalctl', '--vacuum-time=7d']
    )

def limpar_orfaos():
    pacotes = subprocess.run(
        ['deborphan'],
        capture_output=True,
        text=True
        ).stdout.splitlines()
    
    if pacotes:
        subprocess.run(['sudo', 'apt', 'remove', '--purge'] + pacotes)
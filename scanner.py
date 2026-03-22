#Imports

from pathlib import Path
import subprocess

#Funções

def scan_apt_cache():
    resultado = subprocess.run(
        ['du', '-sh', '/var/cache/apt/archives/'],
        capture_output=True,
        text=True
        )
    tamanho = resultado.stdout.split()[0]
    return {'nome': 'Cache do apt', 'Caminho': '/var/cache/apt/archives/', 'tamanho': tamanho}

def scan_temp_cache():
    caminho = Path.home() / '.cache'
    resultado = subprocess.run(
        ['du', '-sh', str(caminho)],
        capture_output=True,
        text=True
        )
    tamanho = resultado.stdout.split()[0]
    return{'nome': 'Cache do temp', 'caminho': caminho, 'tamanho': tamanho}

def scan_logs():
    resultado = subprocess.run(
        ['du', '-sh', '/var/log'],
        capture_output=True,
        text=True
        )
    tamanho = resultado.stdout.split()[0]
    return{'nome': 'Cache do Log', 'caminho': '/var/log', 'tamanho': tamanho}

def scan_orphans():
    resultado = subprocess.run(
        ['deborphan'],
        capture_output=True,
        text=True
    )
    caminho = resultado.stdout.splitlines()
    return{'nome': 'Pacotes Orfãos', 'caminho': caminho, 'quantidade': len(caminho) }
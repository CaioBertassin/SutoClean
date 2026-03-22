# Imports

from scanner import scan_apt_cache, scan_logs, scan_orphans, scan_temp_cache

from cleaner import limpar_apt, limpar_log, limpar_orfaos, limpar_temp

from datetime import datetime

import json

import questionary

# variavel

relatorio = []

hora = datetime.now().hour

# Funções

def criar():
    nome = input('Digite seu nome de usuário: ').strip()

    profile = {
        'nome': nome
    }
    with open('profile.json', 'w') as i:
        json.dump(profile, i)

def carregar():
    with open('profile.json', 'r') as i:
        return json.load(i)
    
# Usuário Carregamento

try:
    profile = carregar()
except FileNotFoundError:
    criar()
    profile = carregar()

if hora < 4:
    print(f"O que faremos nessa madrugada {profile['nome']}?")

elif hora < 12:
    print('Bom dia', profile['nome'])

elif hora < 18:
    print('Boa tarde', profile['nome'])

else:
    print('Boa noite', profile['nome'])

#Programa principal

escolhas = questionary.checkbox(
    'O que deseja organizar?',
    choices=['Cache do apt', 'Arquivos temporários', 'Logs antigos', 'Pacotes órfãos', 'Limpeza geral']
).ask()

print(escolhas)

if 'Cache do apt' in escolhas:
    relatorio.append(scan_apt_cache())

if 'Arquivos temporários' in escolhas:
    relatorio.append(scan_temp_cache())

if 'Logs antigos' in escolhas:
    relatorio.append(scan_logs())

if 'Pacotes órfãos' in escolhas:
    relatorio.append(scan_orphans())

if 'Limpeza geral' in escolhas:
    relatorio.append(scan_apt_cache())
    relatorio.append(scan_logs())
    relatorio.append(scan_orphans())
    relatorio.append(scan_temp_cache())

for i in relatorio:
    print(f"{i['nome']} > {i['caminho']} ({i['tamanho']})")

confirmar = questionary.confirm(f"{profile['nome']}, deseja prosseguir?").ask()

if confirmar:
    if 'Cache do apt' in escolhas:
        limpar_apt()

    if 'Arquivos temporários' in escolhas:
        limpar_temp()

    if 'Logs antigos' in escolhas:
        limpar_log()
    
    if 'Pacotes órfãos' in escolhas:
        limpar_orfaos()

    if 'Limpeza geral' in escolhas:
        limpar_orfaos()
        limpar_apt()
        limpar_log()
        limpar_temp()
import subprocess
import os

# caminho = r"C:\Users\Python\Desktop\Mover e Renomear Arquivos com Python"
lista_arquivos = os.listdir()

for arquivo in lista_arquivos:
    if ".xlsx" in arquivo:
        if "Varredura" in arquivo:
            # jogar pra pasta de janeiro
            os.rename(f"{arquivo}", f"Varreduras/{arquivo}")


subprocess.Popen(r'explorer /open,"C:\Users\Giovani\OneDrive - SESISENAISP - Corporativo\Área de Trabalho\IST-Projetos\legrand\Drone_le\Varreduras"')
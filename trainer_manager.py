import subprocess
import admin
import time

def get_running_processes():
    cmd = 'WMIC PROCESS get Caption'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        print(line)

game = input("What game are you playing: ")
if game == 'sekiro':
        subprocess.Popen('X:/Games/TRAINERS/Sekiro Shadows Die Twice v1.02-v1.05 Plus 24 Trainer.exe', shell=True)
        time.sleep(3)
        subprocess.Popen('X:/Games/Sekiro/sekiro.exe', cwd='X:\Games\Sekiro', shell=True)
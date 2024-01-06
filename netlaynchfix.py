import psutil
import socket
from art import tprint
import time
tprint('NetFix for Launcher V1.0')
print('Created by ErkinKraft')
print('GitHub > https://github.com/ErkinKraft')



def is_process_using_internet(process):
    connections = process.connections()
    for conn in connections:
        if conn.status == psutil.CONN_ESTABLISHED:
            return True
    return False
























def general():
    launcher_choice = input("Select launcher (1 - Epic Games, 2 - Steam)> ")
    if launcher_choice == "1":
        # Завершаем все процессы, кроме EpicGamesLauncher и системных процессов
        for proc in psutil.process_iter(['name']):
            try:
                process_name = proc.info['name']
                if process_name != "EpicGamesLauncher.exe" and is_process_using_internet(proc):
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    elif launcher_choice == "2":
        # Завершаем все процессы, кроме Steam и системных процессов
        for proc in psutil.process_iter(['name']):
            try:
                process_name = proc.info['name']
                if process_name != "Steam.exe" and is_process_using_internet(proc):
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    else:
        print("Некорректный выбор лаунчера. Пожалуйста, выберите 1 или 2.")


    if launcher_choice == "help":
        langchos = input('Select lang (1 - ru , 2 - en)> ')
        if langchos == '1':
            print(
                'Эта программа (возможно) поможет ускорить загрузку игр или файлов в таких лаунчерах как Epic Games и Steam \n'
                'Программа закроет все процессы использующие интернет')
            print()
            general()

        if langchos == '2':
            print(
                'This program will (probably) help speed up the download of games or files in such launchers as Epic Games and Steam \n'
                'The program will close all processes using the Internet')
            print()
            general()


general()

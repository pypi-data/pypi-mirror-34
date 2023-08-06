import subprocess
import sys
import time
import pandas as pd
"""
All the quick utility functions, frequently called in other libraries
"""

_version = "0.0.2.22"

def reset_data():

    print("[x] Reset data needs to be done manually now.")

def clean_data(string_data):
    clean_data = string_data.replace(',', '')
    clean_data = clean_data.lstrip()
    clean_data = clean_data.replace('(', '').replace(')', '')
    return clean_data

def _merge_and_align_columns(file_a, file_b):f
    df_main = pd.read_csv(file_a)
    print(df_main.loc['lat'])
    df_short = pd.read_csv(file_b)
    return 0

def _data_banner():
    """
    Displays just before stream data is shown on the node screen.
    """
    print("|=========================================================================================================|")
    print("| CANVASS Co-Sim Module 0.0.1                                                                             |")
    print("|---------------------------------------------------------------------------------------------------------|")
    print("| Starting Time: {} seconds, since Jan 1, 1970.".format(time.time()))
    print("| Questions? Ask: Sayonsom Chanda, Email: sayon@ieee.org                                                  |")
    print("|====================|============|====================|==========|=======================================|")
    print("|TIME STAMP          | Direction  | DEVICE IP          | PORT     | DATA RECEIVED                         |")
    print("|====================|============|====================|==========|=======================================|")


def _hide_terminal_output():
    """
    Configure subprocess to hide the console window
    """
    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE


def _update_progress(progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

def _banner():

    print("")
    print("  /$$$$$$                                                            ")
    print(" /$$__  $$                                                           ")
    print("| $$  \__/  /$$$$$$  /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$$ /$$$$$$$")
    print("| $$       |____  $$| $$__  $$|  $$  /$$/|____  $$ /$$_____//$$_____/")
    print("| $$        /$$$$$$$| $$  \ $$ \  $$/$$/  /$$$$$$$|  $$$$$$|  $$$$$$ ")
    print("| $$    $$ /$$__  $$| $$  | $$  \  $$$/  /$$__  $$ \____  $$\____  $$")
    print("|  $$$$$$/|  $$$$$$$| $$  | $$   \  $/  |  $$$$$$$ /$$$$$$$//$$$$$$$/")
    print(" \______/  \_______/|__/  |__/    \_/    \_______/|_______/|_______/ ")
    print("                                                                     ")
    print("")
    print("Cyber Attack & Network Vulnerability Analytics Software for Smartgrids")
    print("----------------------------------------------------------------------")
    print("Version           :	   {}".format(_version))
    print("Author            :     Sayonsom Chanda")
    print("License           :     GNU v2")
    print("Help & How to     :     sayon@ieee.org")
    print("----------------------------------------------------------------------")          

def _banner_2(): 
    print("\n" * 100)
    print("|----------------------------------------------|")
    print("| pyCanvass: {}                          |".format(_version))
    print("|----------------------------------------------|")
    print("| Resiliency computation tool for Smart Grids  |")
    print("|                                              |")
    print("| Author: Sayonsom Chanda                      |")
    print("| License: GNU Public License, v2: 2016-18     |")
    print("| Support: sayon@ieee.org                      |")
    print("|----------------------------------------------|")

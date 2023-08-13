import os
import pyautogui
from time import sleep

accept = input("[¡] Desea Activar el SpamBot (y/n): ")

if accept=="y":
    os.system("cls")
    msgint = int(input("Ingrese el numero de mensajes a enviar: "))
    msgText = input("Ingrese el mensaje: ")
    print("[¡ ATENCION !]")
    print("Tienes 10 segundos para ir al chat de Whastapp")
    sleep(10)

    for numero in range(msgint):
        pyautogui.typewrite(msgText)
        sleep(0.2)
        pyautogui.press("enter")

else:
    os.system("cls")
    print("[x] Saliendo del Spam Bot ...")
    sleep(2)
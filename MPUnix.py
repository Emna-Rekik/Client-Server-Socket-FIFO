#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import subprocess
import os

def FIFO():
    closeButtonsInterface()
    os.system('python3 Programme_FIFO.py')
    
def Socket():
    closeButtonsInterface()
    os.system('python3 Programme_Socket.py')
    
def Retour():
    closeButtonsInterface()
    welcomeInterface1()
    
def Step():
    closeWelcomeInterface()
    buttonsInterface1()
    
    
welcomeInterface = 1
memoryFunction = 1
serverInterface = 1
clientInterface = 1
buttonsInterface = 1

def buttonsInterface1():
    global buttonsInterface
    buttonsInterface= Tk()
    buttonsInterface.title("buttonsInterface")
    buttonsInterface.geometry("925x600")
    buttonsInterface.configure(bg = "#ffffff")
    
    # Création d'une interface vide
    canvas = Canvas(
        buttonsInterface,
        bg = "#ffffff",
        height = 600,
        width = 925,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    # Ajouter une photo d'arrière-plan
    background_img = PhotoImage(file = f"images/principale1.png")
    background = canvas.create_image(
        462, 280,
        image=background_img)
    
    # Ajouter le bouton de démarrage
    img0 = PhotoImage(file = f"images/FIFO1.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = FIFO,
        relief = "flat")

    b0.place(x = 70, y = 328, height = 80, width = 229)
    
    # Ajouter le bouton de démarrage
    img1 = PhotoImage(file = f"images/Socket1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = Socket,
        relief = "flat")

    b1.place(x = 595, y = 330, height = 81, width = 227)
    
    img2 = PhotoImage(file = f"images/back1.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = Retour,
        relief = "flat")

    b2.place(x = 19, y = 530,width = 96,height = 57)
    
    buttonsInterface.resizable(False, False)
    buttonsInterface.mainloop()

def welcomeInterface1():
    global welcomeInterface
    welcomeInterface= Tk()
    welcomeInterface.title("Projet Unix")
    welcomeInterface.geometry("925x600")
    welcomeInterface.configure(bg = "#ffffff")
    
    subprocess.run(["make","main"]);
    
    # Création d'une interface vide
    canvas = Canvas(
        welcomeInterface,
        bg = "#ffffff",
        height = 600,
        width = 925,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    # Ajouter une photo d'arrière-plan
    background_img = PhotoImage(file = f"images/welcome.png")
    background = canvas.create_image(
        462, 300,
        image=background_img)
    
    # Ajouter le bouton de démarrage
    img0 = PhotoImage(file = f"images/start3.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = Step,
        relief = "flat")

    b0.place(x = 330, y = 410, height = 92, width = 201)
    
    welcomeInterface.resizable(False, False)
    welcomeInterface.mainloop()
    

def closeWelcomeInterface():
    global welcomeInterface
    welcomeInterface.destroy()
    
def closeButtonsInterface():
    global buttonsInterface
    buttonsInterface.destroy()

    
try:
    welcomeInterface1()
except KeyboardInterrupt:
    display.clear_output()
    print("\nArret du programme ...\n")

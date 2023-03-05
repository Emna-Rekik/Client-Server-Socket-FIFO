#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import subprocess

def serveur_with_Socket():
    subprocess.call("./serveur_socket"); 
    
def client_with_Socket():
    result = subprocess.run(["./client_socket","127.0.0.1","54154"], stdout=subprocess.PIPE, text=True)
    return result.stdout

def serveur_with_FIFO():
    subprocess.call("./serveur");   

def client_with_FIFO():
    result = subprocess.run(["./client"], stdout=subprocess.PIPE, text=True)
    
    return result.stdout
    
serverInterface = 1
clientInterface = 1
clientInterfaceInit = 1
buttonsInterface = 1
serverInterfaceSocket1 = 1
clientInterfaceSocket1 = 1

def stepInit():
    global clientCount1, clientCountStr1
    global clientInterface1
    closeClientInterfaceInit()
    clientCount1 = 2
    clientCountStr1 = "Client" + str(clientCount1)
    clientInterface1= Tk()
    clientInterface(clientInterface1, clientCountStr1)

def step():
    global clientCount1, clientCountStr1
    global clientInterface1
    closeClientInterface()
    clientCount1 = clientCount1 + 1
    clientCountStr1 = "Client" + str(clientCount1)
    clientInterface1= Tk()
    clientInterface(clientInterface1, clientCountStr1)
    
def stepInit2():
    global clientCount1, clientCountStr1
    global clientInterfaceSocket1
    closeClientInterfaceSocketInit()
    clientCount1 = 2
    clientCountStr1 = "Client" + str(clientCount1)
    clientInterfaceSocket1= Tk()
    clientInterfaceSocket(clientInterfaceSocket1, clientCountStr1)

def step2():
    global clientCount1, clientCountStr1
    global clientInterfaceSocket1
    closeClientInterfaceSocket()
    clientCount1 = clientCount1 + 1
    clientCountStr1 = "Client" + str(clientCount1)
    clientInterfaceSocket1= Tk()
    clientInterfaceSocket(clientInterfaceSocket1, clientCountStr1)

def serverInterfaceSocket():
    global serverInterfaceSocket1
    serverInterfaceSocket1= Tk()
    serverInterfaceSocket1.title("Serveur")
    serverInterfaceSocket1.geometry("925x600")
    serverInterfaceSocket1.configure(bg = "#ffffff")
    
    # Création d'une interface vide
    canvas = Canvas(
        serverInterfaceSocket1,
        bg = "#ffffff",
        height = 600,
        width = 925,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    # Ajouter une photo d'arrière-plan
    background_img = PhotoImage(file = f"images/background.png")
    background = canvas.create_image(
        462, 300,
        image=background_img)
        
    result = serveur_with_Socket()
    
    canvas.create_text(
        353.0, 60.0,
        text = result,
        fill = "#FFFFFF",
        font = ("Comfortaa-Regular", int(24.0)))

    serverInterfaceSocket1.resizable(False, False)
    serverInterfaceSocket1.mainloop()

    
def serverInterface():
    global serverInterface
    serverInterface= Tk()
    serverInterface.title("Serveur")
    serverInterface.geometry("925x600")
    serverInterface.configure(bg = "#ffffff")
    
    # Création d'une interface vide
    canvas = Canvas(
        serverInterface,
        bg = "#ffffff",
        height = 600,
        width = 925,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    # Ajouter une photo d'arrière-plan
    background_img = PhotoImage(file = f"images/background.png")
    background = canvas.create_image(
        462, 300,
        image=background_img)
        
    result = serveur_with_FIFO()
    
    canvas.create_text(
        353.0, 60.0,
        text = result,
        fill = "#FFFFFF",
        font = ("Comfortaa-Regular", int(24.0)))

    serverInterface.resizable(False, False)
    serverInterface.mainloop()
    
def clientInterfaceSocketInit():
    global clientInterfaceSocketInit1
    clientInterfaceSocketInit1= Tk()
    clientInterfaceSocketInit1.title("Client1")
    clientInterfaceSocketInit1.geometry("485x647")
    clientInterfaceSocketInit1.configure(bg = "#ffffff")
    
    
    # Création d'une interface vide
    canvas = Canvas(
        clientInterfaceSocketInit1,
        bg = "#FFFFFF",
        height = 647,
        width = 485,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    # Ajouter une photo d'arrière-plan
    background_img = PhotoImage(file = f"images/clientInterface2.png")
    background = canvas.create_image(
        242, 323,
        image=background_img)
        
    result = client_with_Socket()
    
    canvas.create_text(
        200.0, 200.0,
        text = result,
        fill = "#FFFFFF",
        font = ("Comfortaa-Regular", int(18.0)))
        
    # Ajouter le bouton de démarrage
    img0 = PhotoImage(file = f"images/anotherClient1.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = stepInit2,
        relief = "flat")

    b0.place(x = 29, y = 575, height = 60, width = 430)
    
    clientInterfaceSocketInit1.resizable(False, False)
    clientInterfaceSocketInit1.mainloop()
    
def clientInterfaceSocket(clientInterfaceSocket1,clientCountStr1):
    clientInterfaceSocket1.title(clientCountStr1)
    clientInterfaceSocket1.geometry("485x647")
    clientInterfaceSocket1.configure(bg = "#ffffff")
    
    
    # Création d'une interface vide
    canvas = Canvas(
        clientInterfaceSocket1,
        bg = "#FFFFFF",
        height = 647,
        width = 485,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    # Ajouter une photo d'arrière-plan
    background_img = PhotoImage(file = f"images/clientInterface2.png")
    background = canvas.create_image(
        242, 323,
        image=background_img)
        
    result = client_with_Socket()
    
    canvas.create_text(
        200.0, 200.0,
        text = result,
        fill = "#FFFFFF",
        font = ("Comfortaa-Regular", int(18.0)))
        
    # Ajouter le bouton de démarrage
    img0 = PhotoImage(file = f"images/anotherClient1.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = step2,
        relief = "flat")

    b0.place(x = 29, y = 575, height = 60, width = 430)
    
    clientInterfaceSocket1.resizable(False, False)
    clientInterfaceSocket1.mainloop()

def clientInterface(clientInterface1, clientCountStr1):
    clientInterface1.title(clientCountStr1)
    clientInterface1.geometry("485x647")
    clientInterface1.configure(bg = "#ffffff")
    
    # Création d'une interface vide
    canvas = Canvas(
        clientInterface1,
        bg = "#FFFFFF",
        height = 647,
        width = 485,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    # Ajouter une photo d'arrière-plan
    background_img = PhotoImage(file = f"images/clientInterface2.png")
    background = canvas.create_image(
        242, 323,
        image=background_img)
        
    result = client_with_FIFO()
    
    canvas.create_text(
        200.0, 200.0,
        text = result,
        fill = "#FFFFFF",
        font = ("Comfortaa-Regular", int(18.0)))
        
    # Ajouter le bouton de démarrage
    img0 = PhotoImage(file = f"images/anotherClient1.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = step,
        relief = "flat")

    b0.place(x = 29, y = 575, height = 60, width = 430)

    clientInterface1.resizable(False, False)
    clientInterface1.mainloop()
    
def clientInterfaceInit():
    global clientInterfaceInit
    clientInterfaceInit= Tk()
    clientInterfaceInit.title("Client1")
    clientInterfaceInit.geometry("485x647")
    clientInterfaceInit.configure(bg = "#ffffff")
    
    # Création d'une interface vide
    canvas = Canvas(
        clientInterfaceInit,
        bg = "#FFFFFF",
        height = 647,
        width = 485,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    # Ajouter une photo d'arrière-plan
    background_img = PhotoImage(file = f"images/clientInterface2.png")
    background = canvas.create_image(
        242, 323,
        image=background_img)
        
    result = client_with_FIFO()
    
    canvas.create_text(
        200.0, 200.0,
        text = result,
        fill = "#FFFFFF",
        font = ("Comfortaa-Regular", int(18.0)))
        
    # Ajouter le bouton de démarrage
    img0 = PhotoImage(file = f"images/anotherClient1.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = stepInit,
        relief = "flat")

    b0.place(x = 29, y = 575, height = 60, width = 430)

    clientInterfaceInit.resizable(False, False)
    clientInterfaceInit.mainloop()


def closeServerInterface():
    global serverInterface
    serverInterface.destroy()
    
def closeClientInterface():
    global clientInterface1
    clientInterface1.destroy()
    
def closeClientInterfaceInit():
    global clientInterfaceInit
    clientInterfaceInit.destroy()
    
def closeClientInterfaceSocket():
    global clientInterfaceSocket1
    clientInterfaceSocket1.destroy()
    
def closeClientInterfaceSocketInit():
    global clientInterfaceSocketInit1
    clientInterfaceSocketInit1.destroy()

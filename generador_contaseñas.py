'''******************************************************|
| Un Simple Generador de Contraseñas con Interfaz Grafica|
| * Guarda la Contraseña en un archvo .pckl              |
| * Vizualizacion de todas las contraseñas               |
|               Ricardo - Inusui                         |  
|******************************************************'''

from sys import maxsize
from tkinter import *
from tkinter import messagebox
import random
import pickle
from turtle import bgcolor

root = Tk()
root.title("Generador de Contraseñas")
root.iconbitmap("res/password.ico")

#******************** Funciones
#Funciones 
def GeneradorPassword():
    mensaje.set("Generarando Contraseña")
    lower ="qwertyuiopasdfghjklzxcvbnm"
    mayus = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    numbers = "0123456789"
    symbols = "~!@#$%^&*()_+=/*-|\}{[];:?.>,<"

    
    if int(lenPassword.get()) == 0:
        print("entro`")
        messagebox.showerror("Error","Debe introducir algún numero")
    elif int(lenPassword.get()) != 0 :
        lenght = int ( int(lenPassword.get()))

        all = lower + mayus + numbers + symbols
        password = "".join(random.sample(all, lenght))
        newpassword.set(password)

def Guardar():
    guardarpwd = newpassword.get()
    if guardarpwd != "":
        mensaje.set("Guardar Contraseña")
        
        file = open("passwords.pckl","rb")
        passwordlist = pickle.load(file)
        file.close()

        guardarlista = str(passwordlist) + "\n" + str(guardarpwd)

        file = open("passwords.pckl","wb")
        pickle.dump(guardarlista, file)
        file.close()
        messagebox.showinfo("Contraseña Guardada","Contraseña ["+guardarpwd+"] Guardada")
    else:
        messagebox.showerror("Error","Debe Generar Alguna Contraseña antes")
        mensaje.set("Genere alguna Contraseña")

def Mostrar():
    file = open("passwords.pckl","rb")
    passwordlist = pickle.load(file)
    file.close()
    print(passwordlist)
    if passwordlist != None:
        newwindows = Toplevel(root)
        newwindows.title("Contraseñas Generadas")
        texto = Text(newwindows)
        texto.insert('insert', passwordlist)
        texto.configure(state='disable', bg='silver')
        texto.grid()
    else:
        messagebox.showinfo("Fichero Vacio", "No Tiene Contraseñas Guardadas")

def Salir():
    alt = messagebox.askquestion("Salir","¿Seguro de salir?")
    if alt =="yes":
        root.destroy()      
        
def Borrar():
    messagebox.showwarning("Borrar todas las Contraseñas", "Esta accion es Irreversible")
    alt = messagebox.askyesnocancel("Borrar Todas las Contraseñas", "¿Esta completamente seguro que desea borrar todas las contraseñas?")
    
    if (alt):
        file = open("passwords.pckl","wb")
        pickle.dump(None, file)
        file.close()
        messagebox.showinfo("Contraseñas Borradas", "Contraseñas Borradas con exito")
    elif(alt == False):
        Mostrar()        

#*************Inicializacion de variables
newpassword = StringVar()
newpassword.set("")


#****************** Interfaz Grafica
txtlenPassword = Label(root, text="¿De cuantos caracteres\nquiere su contraseña?")
txtlenPassword.grid(row=1, column=0, sticky="e", padx=5, pady=5)

lenPassword = Entry(root)
lenPassword.grid(row=1, column=1, sticky="w",padx=5, pady=5 )
lenPassword.config(justify="left")
lenPassword.insert(END,"0")

txtpassword = Label(root, text="Su nueva contraseña=>")
txtpassword.grid(row=2, column=0, sticky="e", padx=5,pady=5)

outputpassword = Label(root, textvar=newpassword, justify="right")
outputpassword.grid(row=2, column=1, padx=5,pady=5, sticky="w")

botonGenerar = Button(root, text="Generar Contraseña", command = GeneradorPassword)
botonGenerar.grid(row=3,column=0, padx=5,pady=5)

botonGuardar = Button(root,text="Guardar Contraseña", command=Guardar)
botonGuardar.grid(row=3,column=1,padx=5,pady=5)

botonMostrar = Button(root,text="Mostrar Contraseñas", command=Mostrar)
botonMostrar.grid(row=3,column=2,padx=5,pady=5)

botonBorrar = Button(root,text="Borrar Todas\nLas Contraseñas Guardadas", command=Borrar)
botonBorrar.grid(row=4,column=1,padx=5,pady=5)

botonSalir = Button(root,text="Salir", command=Salir)
botonSalir.grid(row=3,column=3,padx=5,pady=5)



#************************* Footer y botones para Guardar
mensaje = StringVar()
mensaje.set("Generador de Contraseñas")
footer = Label(root, textvar=mensaje, justify="right")
footer.grid(row=5, column=0, sticky='w')
Label(root, text="By: Inusui", justify="right").grid(row=5, column=2, sticky="e")
imagen = PhotoImage(file="res/dog.png")
Label(root, image=imagen, justify="right").grid(row=5, column=3,sticky="e")

#************************  Ciclo para mantener la ventana abierta durante la ejecucion
root.mainloop()
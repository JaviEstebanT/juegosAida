from tkinter import *
from tkinter import messagebox

def salir():
	valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")
	if valor==True:
		raiz.destroy()

raiz=Tk()
raiz.title("Juegos reunidos Aida")
raiz.iconbitmap("imagenes\patio-de-recreo.ico")

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

menuIncio=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Inicio", menu=menuIncio)
menuIncio.add_command(label="Salir", command=salir)

menuJuegos=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Juegos", menu=menuJuegos)
menuJuegos.add_command(label="Sonido vs Imagen")
menuJuegos.add_command(label="Imagen vs Sonido")
menuJuegos.add_command(label="Sombras")

menuAyuda=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de...")
menuAyuda.add_command(label="Instrucciones")
menuAyuda.add_command(label="Licencia")


raiz.mainloop()
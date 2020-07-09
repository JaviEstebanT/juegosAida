from tkinter import *
from tkinter import messagebox


def sonidoImagen():

	def salir():
		valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")
		if valor==True:
			raizSonidoImagen.destroy()

	raizSonidoImagen=Tk()
	raizSonidoImagen.title("Sonido vs Imagen")
	raizSonidoImagen.iconbitmap("imagenes\ltavoz.ico")

	barraMenu=Menu(raizSonidoImagen)
	raizSonidoImagen.config(menu=barraMenu, width=300, height=300)

	menuAcciones=Menu(barraMenu, tearoff=0)
	barraMenu.add_cascade(label="Acciones", menu=menuAcciones)
	menuAcciones.add_command(label="Salir", command=salir)

	raizSonidoImagen.mainloop()
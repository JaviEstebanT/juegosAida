from tkinter import *
from tkinter import messagebox
from sonidoImagen import *

def salir():
	valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")
	if valor==True:
		raizMarcoPincipal.destroy()

def licencia():
	licencia=Label(raizMarcoPincipal, text='MITlincese\n' + 
		'\n'+
		'Copyright 2020 Javi Esteban\n'+
		'\n'+
		'Icon made by Pixel perfect from www.flaticon.com\n'+
		'\n'+
		'Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\n'+
		'documentation files (the "Software"), to deal in the Software without restriction, including without limitation\n'+
		'the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,\n'+
		'and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n'+
		'The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n' +
		'\n'+
	 	'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO\n'+
	 	'THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.\n' +
	 	'IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,\n'+
	 	'WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE\n' +
	 	'OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.')
	licencia.pack()

def acerca():
	acerca=Label(raizMarcoPincipal, text='Vesión 0.2\n'+
		'\n'+
		'Programa con juegos infantiles educativos')

	acerca.pack()

raizMarcoPincipal=Tk()
raizMarcoPincipal.title("Juegos reunidos Aida")
raizMarcoPincipal.iconbitmap("imagenes\patio-de-recreo.ico")

barraMenu=Menu(raizMarcoPincipal)
raizMarcoPincipal.config(menu=barraMenu, width=300, height=300)

menuIncio=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Inicio", menu=menuIncio)
menuIncio.add_command(label="Salir", command=salir)

menuJuegos=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Juegos", menu=menuJuegos)
menuJuegos.add_command(label="Sonido vs Imagen", command=sonidoImagen)
menuJuegos.add_command(label="Imagen vs Sonido")
menuJuegos.add_command(label="Sombras")

menuAyuda=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de...", command=acerca)
menuAyuda.add_command(label="Licencia", command=licencia)


raizMarcoPincipal.mainloop()
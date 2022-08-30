from operator import truediv
from tkinter import *

programa = Tk()
programa.title("Calculadora")
programa.iconbitmap("Calc.ico")
programa.config(bg="blue")


ventana = Frame(programa, width=300, height=300, padx=2, pady=1)
ventana.pack()
ventana.config(bg="black")

##-------------------- Variables Globales

numeroPantalla = StringVar()
resultado = 0
operacion = False
ultima_op = ""


##--------------------- Funciones


def igual(num):
    global resultado, operacion, ultima_op

    if ultima_op == "suma":
        resultado += float(num)
        numeroPantalla.set(resultado)
        operacion = True
    elif ultima_op == "resta":
        resultado -= float(num)
        numeroPantalla.set(resultado)
        operacion = True
    elif ultima_op == "multi":
        resultado = resultado * float(num)
        numeroPantalla.set(resultado)
        operacion = True
    elif ultima_op == "div":
        resultado = resultado / float(num)
        numeroPantalla.set(resultado)
        operacion = True

    ultima_op = ""
    return resultado


def pulsacionnum(num):
    global resultado, operacion

    if operacion == True:
        numeroPantalla.set("")
        operacion = False

    numeroPantalla.set(numeroPantalla.get() + num)


def suma(num):
    global resultado, operacion, ultima_op
    if ultima_op == "":
        resultado = float(num)
        operacion = True
    elif ultima_op == "suma":
        resultado += float(num)
        numeroPantalla.set(resultado)
        operacion = True
    elif ultima_op != "suma" and ultima_op != "":
        igual(numeroPantalla.get())

    ultima_op = "suma"


def resta(num):
    global resultado, operacion, ultima_op
    if ultima_op == "":
        resultado = float(num)
        operacion = True
    elif ultima_op == "resta":
        resultado -= float(num)
        numeroPantalla.set(resultado)
        operacion = True
    elif ultima_op != "resta" and ultima_op != "":
        igual(numeroPantalla.get())

    ultima_op = "resta"


def multi(num):
    global resultado, operacion, ultima_op
    if ultima_op == "":
        resultado = float(num)
        operacion = True
    elif ultima_op == "multi":
        resultado = resultado * float(num)
        numeroPantalla.set(resultado)
        operacion = True
    elif ultima_op != "multi" and ultima_op != "":
        igual(numeroPantalla.get())

    ultima_op = "multi"


def div(num):
    global resultado, operacion, ultima_op
    if ultima_op == "":
        resultado = float(num)
        operacion = True
    elif ultima_op == "div":
        resultado = resultado / float(num)
        numeroPantalla.set(resultado)
        operacion = True
    elif ultima_op != "div" and ultima_op != "":
        igual(numeroPantalla.get())

    ultima_op = "div"


def softreset():
    numeroPantalla.set("")


def hardreset():
    global resultado, operacion, ultima_op
    numeroPantalla.set("")
    resultado = 0
    operacion = False
    ultima_op = ""


##--------------------- PANTALLA
pantalla = Entry(ventana, textvariable=numeroPantalla)
pantalla.grid(row=0, column=0, padx=2, pady=(5, 2), columnspan="4")


##-------------------- Botones Fila 1

cbutton = Button(ventana, text="C", width=7, command=lambda: hardreset())
cbutton.grid(row=1, column=0, columnspan=2, padx=(2, 0), pady=(3, 3))

cebutton = Button(ventana, text="CE", width=7, command=lambda: softreset())
cebutton.grid(row=1, column=2, columnspan=2, padx=(0, 2), pady=(3, 3))


##-------------------- Botones Fila 2

sietebutton = Button(ventana, text="7", width=3, command=lambda: pulsacionnum("7"))
sietebutton.grid(row=2, column=0, padx=(2, 0))

ochobutton = Button(ventana, text="8", width=3, command=lambda: pulsacionnum("8"))
ochobutton.grid(row=2, column=1)

nuevebutton = Button(ventana, text="9", width=3, command=lambda: pulsacionnum("9"))
nuevebutton.grid(row=2, column=2)

divbutton = Button(
    ventana, text="/", width=3, command=lambda: div(numeroPantalla.get())
)
divbutton.grid(row=2, column=3, padx=(0, 2))

##-------------------- Botones Fila 3

cuatrobutton = Button(ventana, text="4", width=3, command=lambda: pulsacionnum("4"))
cuatrobutton.grid(row=3, column=0, padx=(2, 0))

cincobutton = Button(ventana, text="5", width=3, command=lambda: pulsacionnum("5"))
cincobutton.grid(row=3, column=1)

seisbutton = Button(ventana, text="6", width=3, command=lambda: pulsacionnum("6"))
seisbutton.grid(row=3, column=2)

multbutton = Button(
    ventana, text="*", width=3, command=lambda: multi(numeroPantalla.get())
)
multbutton.grid(row=3, column=3, padx=(0, 2))

##-------------------- Botones Fila 4

unobutton = Button(ventana, text="1", width=3, command=lambda: pulsacionnum("1"))
unobutton.grid(row=4, column=0, padx=(2, 0))

dosbutton = Button(ventana, text="2", width=3, command=lambda: pulsacionnum("2"))
dosbutton.grid(row=4, column=1)

tresbutton = Button(ventana, text="3", width=3, command=lambda: pulsacionnum("3"))
tresbutton.grid(row=4, column=2)

restabutton = Button(
    ventana, text="-", width=3, command=lambda: resta(numeroPantalla.get())
)
restabutton.grid(row=4, column=3, padx=(0, 2))

##-------------------- Botones Fila 5

comabutton = Button(ventana, text=",", width=3, command=lambda: pulsacionnum("."))
comabutton.grid(row=5, column=0, padx=(2, 0), pady=(0, 5))

cerobutton = Button(ventana, text="0", width=3, command=lambda: pulsacionnum("0"))
cerobutton.grid(row=5, column=1, pady=(0, 5))

igualbutton = Button(
    ventana, text="=", width=3, command=lambda: igual(numeroPantalla.get())
)
igualbutton.grid(row=5, column=2, pady=(0, 5))

masbutton = Button(
    ventana, text="+", width=3, command=lambda: suma(numeroPantalla.get())
)
masbutton.grid(row=5, column=3, padx=(0, 2), pady=(0, 5))

##----------------

programa.mainloop()

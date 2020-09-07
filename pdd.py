from tkinter import *
from tkinter import messagebox
import random
#configuracion de la ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.resizable(0,0)
ventana.title("Algoritmos de Ordenacion")


#variables generales
opcion_ord = IntVar()
#configuracion de botones
titul_label = Label(ventana, text="ALGORITMOS DE ORDENACION",font="Helvetica 12 bold",bg="red")
titul_label.pack()
f = Entry(ventana,width=25)
f.place(x=60,y=100)

Label(ventana,text="Ordenar por:",font="Helvetica 12 bold",bg="skyblue").place(x=200,y=140)

#####################################################
def xD():
    print(opcion_ord.get())
    global arr
    print(arr)

def carg():
    global arr
    f = open("bdPalabras.txt",'r')
    arr = f.readlines()
    return arr

Button(ventana, text="Cargar Archivo...",command=carg,width=14).place(x=250,y=100)
#####################################################
#opciones de ordenamiento
rb_shellSort = Radiobutton(ventana, text="Shell Sort",variable=opcion_ord, value=1).place(x=90,y=175)
rb_insertSort = Radiobutton(ventana, text="Insert Sort",variable=opcion_ord, value=2).place(x=90,y=195)
rb_bubbleSort = Radiobutton(ventana, text="Bubble Sort",variable=opcion_ord, value=3).place(x=90,y=215)
rb_mergeSort = Radiobutton(ventana, text="Merge Sort",variable=opcion_ord, value=4).place(x=90,y=235)
rb_quickSort = Radiobutton(ventana, text="Quick Sort",variable=opcion_ord, value=5).place(x=90,y=255)
rb_bucketSort = Radiobutton(ventana, text="Bucket Sort",variable=opcion_ord, value=6).place(x=90,y=275)
rb_radixSort = Radiobutton(ventana, text="Radix Sort",variable=opcion_ord, value=7).place(x=325,y=175)
rb_heapSort = Radiobutton(ventana, text="Heap Sort",variable=opcion_ord, value=8).place(x=325,y=195)
rb_countSort = Radiobutton(ventana, text="Count Sort",variable=opcion_ord, value=9).place(x=325,y=215)
rb_binSort = Radiobutton(ventana, text="Bin Sort",variable=opcion_ord, value=10).place(x=325,y=235)
rb_rselectSort = Radiobutton(ventana, text="Random Select Sort",variable=opcion_ord, value=11).place(x=325,y=255)
rb_stoogeSort = Radiobutton(ventana, text="Stooge Sort",variable=opcion_ord, value=12).place(x=325,y=275)

Button(ventana, text="Run...!!!",command=xD).place(x=225,y=310)

ventana.mainloop()
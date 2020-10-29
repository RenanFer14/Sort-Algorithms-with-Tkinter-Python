# -*- coding: utf-8 -*-
# ···················Requerimientos de la aplicacion·················
# 
#   VERSION DE PYTHON ----> Python 3.8.5
#   
#   Version de las librerias usadas propias de la 
#   version de Python

#
#
# ----------------- SOPORTE GENERAL ---------------------------
#
# · SOPORTE GRAFICO DE LA APLICACION
#   - Libreria Tkinter
# 
# · SOPORTE PARA EL DESARROLLO DE LOS ALGORITMOS  
#   - Libreria Random
#   
# · SOPORTE PARA EL CALCULO DEL TIEMPO
#   - Libreria Time


import tkinter as tk
from tkinter import messagebox
from time import time
import tkinter.scrolledtext as st
from tkinter import filedialog
import random
import copy
import sys

import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline

# Si el error que se genera es de tipo:
# RecursionError: maximum recursion depth exceeded in comparison
# ejecutar lo siguiente
# sys.setrecursionlimit(10^6)

# una vez terminado el programa ejecute esta linea
# sys.setrecursionlimit(1000)
texto = "Tiempo de ejecucion..."


# programa que implementa los metodos de ordenacion
#   Insert Sort --> insert(arr)
#   Shell Sort --> shell(arr)
#   Bubble Sort --> bubble(arr)
#   Merge Sort --> merge(arr)
#   Quick Sort --> quick(arr)
#   Bucket Sort --> bucket(arr)
#   Radix Sort  --> radix(arr)
#   Heap Sort --> heap(arr,0,n)
#   Count Sort --> count(arr)
#   Bin Sort --> bin(arr)
#   Randomized Select Sort --> rselect(arr,0,n,0)
#   Stooge Sort --> stooge(arr,0,n)

#################### REGION ALGORITMOS ##########################

#  1. Insert Sort

def insert_sort(array):
    # se itera desde el segundo elemento asumiendo que el primero ya esta ordenado
    for i in range(1, len(array)):
        # elemento para el cual se debe "buscar su posicion"
        key_item = array[i]
        # inicializar la variable que sera usada para unicar la posicion correcta
        j = i - 1
        # analizar la parte izq del arreglo y buscar la pos correcta de key_item
        # Hacerlo solo cuando key_item sea menor qie los valores adyacentes        
        while j >= 0 and array[j] > key_item:
            # intercambiar los valores del arreglo analizando de izq a der
            array[j + 1] = array[j]
            j -= 1
        # al terminar de cambiar posicones se ubica el elemento actual
        array[j + 1] = key_item
    return array


#  2. Shell Sort
def shell_sort(arr):
    # comenzamos con un gap grande y luego lo reducimos
    n = len(arr)
    gap = n // 2

    # se hace un gap < insert_sort para este tamaño del gap. el primer elemento del gap es
    # a[0..gap-1] son casi en orden del gap, se sigue agregando un elemento más 
    # hasta que toda la matriz esté ordenada
    while gap > 0:
        for i in range(gap, n):
            # agregar arr[i] a los elementos que han sido ordenados
            # guardar a[i] en temp y hacer espacio en la posicion i 
            temp = arr[i]
            # cambiar los elementos ordenados antes de gap  hasta hallar la ubicacion para arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                # poner temp (el original arr[i]) en su posicion correcta
            arr[j] = temp
        gap //= 2


#   3. Bubble Sort
def bubble_sort(arr):
    # hallar la longitud de arr
    n = len(arr)
    # recorrer todos los elementos de arr 
    for i in range(n):
        # los ultimos i elementos estan casi ordenados 
        for j in range(0, n - i - 1):
            # recorrer el arr desde 0 hasta n-i-1 
            # cambiar si el elemento encontrado es mayor que el siguiente elemento 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


#   4. Merge Sort
def merge_sort(A, p, r):
    if (p < r):
        q = int((p + r) / 2)
        # recursion para el lado izq
        merge_sort(A, p, q)
        # recursion para el lado der
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return A


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    # arrays para las particiones derecha e izquierda
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    i = 1
    j = 1
    # verificar si algun elemento queda por asignar
    while i <= n1:
        L[i - 1] = A[p + i - 1]
        i = i + 1
    while j <= n2:
        R[j - 1] = A[q + j]
        j = j + 1
    # asignar valores maximos
    L[n1] = float("inf")
    R[n2] = float("inf")
    i = 0
    j = 0
    # copiar datos a los arrays der e izq
    for k in range(p, r + 1):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    return A


#   5. Quick Sort
def partition(arr, low, high):
    # indice del elemento mas pequeño 
    i = (low - 1)
    # pivote
    pivot = arr[high]
    for j in range(low, high):
        # si el elemento actual es menor que el pivote 
        if arr[j] < pivot:
            # incrementar el indice del elemento pequeño 
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            # intercambiar elementos
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quick_sort(arr, low, high):
    if low < high:
        # pi es indice de la particion, arr[p] esta en la posicion correcta
        pi = partition(arr, low, high)
        # ordenar elementos de forma separada antes y despues del pivot
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    #   6. Heap Sort


def heapify(arr, n, i):
    # incilizar largest como la raiz
    largest = i
    # izq = 2*i + 1 
    l = 2 * i + 1
    # der = 2*i + 2
    r = 2 * i + 2
    # ver si el hijo izq de la raiz existe y es mayor que la raiz
    if l < n and arr[i] < arr[l]:
        largest = l
        # ver si el hijo der de la raiz existe y es mayor que la raiz
    if r < n and arr[largest] < arr[r]:
        largest = r
        # cambiar la raiz si se necesita
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # poner la raiz en el heap. 
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # construir un maxheap. 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        # extraer los elementos uno a uno
    for i in range(n - 1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    #   7. Bucket Sort


def bucket_sort(lista):
    k = len(lista) - 1
    # crear buckets/cajas para ir almacenando
    buckets = [[] for i in range(k)]
    maxValue = max(lista)
    # distribuir los elementos de manera uniforme
    for i in range(k, -1, -1):
        buckets[lista[i] * k // (maxValue + 1)].insert(0, lista[i])
    # usar insert_sort para ordenar cada bucket
    for i in range(0, k):
        insert_sort(buckets[i])
    returnList = []
    # concatenar las listas ordenadas
    for bucket in buckets:
        returnList.extend(bucket)
    return returnList


#   8. Count Sort
def count_sort(list):
    # crear una lista de 0's de tamaño igual al maximo valor de la lista dada + 1
    c = [0] * (max(list) + 1)
    # el arr final ordenado sera devuelto del mismo tamaño que el dado
    b = [0] * len(list)
    # para cada elemento en la lista, el numero de ocurrencias se guarda en su respectivo indice en la lista C
    for i in list:
        c[i] = c[i] + 1
        # cada elemento en C incluye el valor de su elemento previo
    for k in range(1, len(c)):
        c[k] = c[k] + c[k - 1]
        # iterando la lista en reversa
    for l in list[::-1]:
        # modificamos cada valor en la lista al idnice daod por C, restadole 1
        b[c[l] - 1] = l
        c[l] = c[l] - 1
    return b


#   9. Radix Sort
def radix_sort(array):
    # determinar el maximo valor del array para saber el numero digitos
    m = max(array)
    # aplicar counting sort para cada digito
    i = 1
    while (m / i > 0):
        count_sort(array)
        i *= 10


#   10. Bin Sort
#### BIN SORT = BUCKET SORT
def bin_sort(lista):
    k = len(lista) - 1
    buckets = [[] for i in range(k)]
    maxValue = max(lista)
    for i in range(k, -1, -1):
        buckets[lista[i] * k // (maxValue + 1)].insert(0, lista[i])
    for i in range(0, k):
        insert_sort(buckets[i])
    returnList = []
    for bucket in buckets:
        returnList.extend(bucket)
    return returnList


#   11. Randomized Select Sort
def partition_(A, p, r):
    x = A[r]
    i = p - 1
    j = p
    while j < r:
        if A[j] <= x:
            i = i + 1
            k = A[j]
            A[j] = A[i]
            A[i] = k
        j = j + 1
    h = A[i + 1]
    A[i + 1] = A[r]
    A[r] = h
    return i + 1


def randomized_partition(A, p, r):
    q = random.randint(p, r)
    k = A[q]
    A[q] = A[r]
    A[r] = k
    return partition_(A, p, r)


def random_select(A, p, r, i):
    if p == r:
        return A[p]

    q = randomized_partition(A, p, r)
    k = q - p + 1

    if i == k:
        return A[q]
    else:
        if i < k:
            return random_select(A, p, q - 1, i)
        else:
            return random_select(A, q + 1, r, i - k)


#   12. Stooge Sort
def stooge_sort(arr, l, h):
    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t

    # si hay mas de dos elementos en el arra
    if h - l + 1 > 2:
        t = (int)((h - l + 1) / 3)
        # ordenar recursivamente los primeros 2 / 3 elementos 
        stooge_sort(arr, l, (h - t))
        # ordenar recursivamente los ultimos 2 / 3 elementos 
        stooge_sort(arr, l + t, (h))
        # # ordenar recursivamente los primeros 2 / 3 elementos OTRA VEZ para confirmar
        stooge_sort(arr, l, (h - t))
    return arr


#################### END REGION ALGORITMOS ########################## 
# ··························································································· 
#################### REGION VENTANA DE INTERFAZ ##########################
# configuracion de la ventana
ventana = tk.Tk()
ventana.geometry("1020x500")
ventana.resizable(0, 0)
ventana.title("Algoritmos de Ordenacion")
ventana.configure(background="royalblue")

# imagenes a usar
img_load = tk.PhotoImage(file="img/ext_dat.png")
img_btn_run = tk.PhotoImage(file="img/start.png")
img_exit = tk.PhotoImage(file="img/exit.png")

# variables generales
opcion_ord = tk.IntVar()
textMostrar = tk.StringVar()
textMostrar.set("0.00")

# titulo de ventana
tk.titul_label = tk.Label(ventana, text="ALGORITMOS DE ORDENACION", font="times 18 bold underline",
                          bg="royalblue").place(x=70, y=30)


# ······ MODULOS PARA LA MANIPULACION DE LOS DATOS
def ext_dato():
    global data_arr
    file_name = filedialog.askopenfilename()
    sctextUn.configure(state="normal")
    if (file_name == ""):
        messagebox.showwarning("Error al cargar archivo", "Inserte un nombre de archivo valido*")
        data_arr = "No hay datos*"
    else:
        try:
            data = open(file_name, 'r')
            lines = []
            for line in data:
                lines.append(line)
            # print("extraccion correcta*")
            data.close()
            messagebox.showinfo("Archivo cargado correctamente", "Cantidad de elementos cargados: " + str(len(lines)))
            data_arr = lines

            dt = conv(data_arr)
            txt = "NRO. \t CONTENIDO\n"
            for i in range(len(dt)):
                txt+=str(i+1)+ " \t " + str(dt[i])+"\n"


            sctextUn.insert(tk.INSERT, txt)
            sctextUn.configure(state="disabled")

            return data_arr
        except FileNotFoundError:
            messagebox.showerror("Error al extraer datos", "Verifique el nombre del archivo*")
            #f.delete(0, len(f.get()))
            data_arr = "No hay datos*"
            return data_arr
        except FileExistsError:
            messagebox.showerror("Error al extraer datos", "Verifique el nombre del archivo*")
            #f.delete(0, len(f.get()))
            data_arr = "No hay datos*"
            return data_arr


def conv(arr):
    k = arr[0]
    try:
        if (isinstance(int(k), int) == True):
            for i in range(len(arr)):
                arr[i] = int(arr[i])
    except:
        for i in range(len(arr)):
            arr[i] = arr[i].rstrip("\n")
    return arr
    # if arr != "No hay datos*":
    # else:
    #   messagebox.showwarning("Error al cargar datos","Cargue nuevamente el archivo")


def escribirArch(arr, namefile, ind):
    if (ind == 1):  # ----> Palabras
        try:
            filewrite = open("out/" + namefile, 'w')
            for i in arr:
                filewrite.write(i)
            filewrite.close()
            messagebox.showinfo("Mensaje", "Archivo ordenado creado satisfactoriamente")
        except:
            messagebox.showwarning("Error al escribir archivo", "Vuelva a escribir el archivo, error desconocido*")
    else:  # -------> Numeros
        try:
            filewrite = open("out/" + namefile, 'w')
            for i in arr:
                print(i, file=filewrite)
            filewrite.close()
            messagebox.showinfo("Mensaje", "Archivo ordenado creado satisfactoriamente")
        except:
            messagebox.showwarning("Error al escribir archivo", "Vuelva a escribir el archivo, error desconocido*")


def textosalida(lista):
    arrA = conv(lista)
    sctextUn.configure(state="normal")
    textom = "NRO. \t CONTENIDO\n"
    for i in range(len(arrA)):
        textom+=str(i+1)+" \t "+str(arrA[i])+"\n"
    
    
    sctextOr.insert(tk.INSERT, textom)
    sctextOr.configure(state="disabled")


def mostrar_tiempo(total):
    texto = str(round(total, 6))
    textMostrar.set(texto)

def elim1():
    sctextUn.configure(state="normal")
    sctextUn.delete('0.0', tk.END)
    
def elim2():
    sctextOr.configure(state="normal")
    sctextOr.delete('0.0', tk.END)

def run():
    global data_arr
    ArrDef = conv(data_arr)
    tam = len(ArrDef)
    temporal = copy.copy(ArrDef)
    first = ArrDef[0]
    opcion = opcion_ord.get()

    if (isinstance(first, str) == True):
        if (opcion == 1):
            # medir el tiempo de ejecucion
            start_time = time()
            shell_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Shell-ord-pal", 1)
            textosalida(temporal)
        elif (opcion == 2):
            start_time = time()
            insert_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Insert-ord-pal", 1)
            textosalida(temporal)
        elif (opcion == 3):
            start_time = time()
            bubble_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Bubble-ord-pal", 1)
            textosalida(temporal)
        elif (opcion == 5):
            start_time = time()
            quick_sort(temporal, 0, tam - 1)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Quick-ord-pal", 1)
            textosalida(temporal)
        elif (opcion == 8):
            start_time = time()
            heap_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Heap-ord-pal", 1)
            textosalida(temporal)
        elif (opcion == 12):
            start_time = time()
            stooge_sort(temporal, 0, tam - 1)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Stooge-ord-pal", 1)
            textosalida(temporal)
        else:
            messagebox.showwarning("Error al ordenar", "PALABRAS no se pueden ordenar mediante este algoritmo...*")
    else:
        if (opcion == 1):
            start_time = time()
            shell_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Shell-ord", 2)
            textosalida(temporal)
        elif (opcion == 2):
            start_time = time()
            insert_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Insert-ord", 2)
            textosalida(temporal)
        elif (opcion == 3):
            start_time = time()
            bubble_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Bubble-ord", 2)
            textosalida(temporal)
        elif (opcion == 4):
            start_time = time()
            merge_sort(temporal, 0, tam - 1)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Merge-ord", 2)
            textosalida(temporal)
        elif (opcion == 5):
            start_time = time()
            quick_sort(temporal, 0, tam - 1)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Quick-ord", 2)
            textosalida(temporal)
        elif (opcion == 6):
            start_time = time()
            tempB = bucket_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(tempB, "Bucket-ord", 2)
            textosalida(temporal)
        elif (opcion == 7):
            start_time = time()
            radix_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Radix-ord", 2)
            textosalida(temporal)
        elif (opcion == 8):
            start_time = time()
            heap_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Heap-ord", 2)
            textosalida(temporal)
        elif (opcion == 9):
            start_time = time()
            tempC = count_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(tempC, "Count-ord", 2)
            textosalida(temporal)
        elif (opcion == 10):
            start_time = time()
            tempBi = bin_sort(temporal)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(tempBi, "Bin-ord", 2)
            textosalida(temporal)
        elif (opcion == 11):
            start_time = time()
            for i in range(1, tam + 1):
                random_select(temporal, 0, tam - 1, i)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Random-ord", 0)
            textosalida(temporal)
        elif (opcion == 12):
            start_time = time()
            stooge_sort(temporal, 0, tam - 1)
            end_time = time()
            total_time = end_time - start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal, "Stooge-ord", 2)
            textosalida(temporal)


def comparar():
    global data_arr
    Arr = conv(data_arr)
    prim = Arr[0]
    temp = copy.copy(Arr)
    tam = len(Arr)
    # PALABRAS
    Palabras = ["INSERT", "SHELL", "BUBBLE", "QUICK", "HEAP"]
    NUMEROS = ["INSERT", "SHELL", "BUBBLE", "MERGE", "QUICK", "HEAP", "BUCKET", "COUNT", "RADIX", "BIN", "RANDOM"]
    EXEC_PAL = []
    EXEC_NUM = []
    if isinstance(prim, str):
        # INSERT SORT
        i1 = time()
        insert_sort(temp)
        f1 = time()
        EXEC_PAL.append(f1 - i1)
        # SHELL SORT
        temp = copy.copy(Arr)
        i2 = time()
        shell_sort(temp)
        f2 = time()
        EXEC_PAL.append(f2-i2)
        #BUBBLE SORT
        temp = copy.copy(Arr)
        i3 = time()
        bubble_sort(temp)
        f3 = time()
        EXEC_PAL.append(f3 - i3)
        #QUICK SORT
        temp = copy.copy(Arr)
        i4 = time()
        quick_sort(temp,0,tam-1)
        f4 = time()
        EXEC_PAL.append(f4 - i4)
        #HEAP SORT
        temp = copy.copy(Arr)
        i5 = time()
        heap_sort(temp)
        f5 = time()
        EXEC_PAL.append(f5 - i5)
        #DIBUJAR PLOT
        ypos = np.arange(len(Palabras))
        plt.xticks(ypos,Palabras)
        plt.ylabel("Tiempo de ejecucion (Seg.)")
        plt.title("Alg. Ordenacion - Palabras")
        plt.bar(ypos,EXEC_PAL)
        plt.show()
    else:
        #INSERT SORT
        i6 = time()
        insert_sort(temp)
        f6 = time()
        print(f6-i6)
        EXEC_NUM.append(f6-i6)
        #SHELL SORT
        temp = copy.copy(Arr)
        i7 = time()
        shell_sort(temp)
        f7 = time()
        print(f7 - i7)
        EXEC_NUM.append(f7 - i7)
        # BUBBLE SORT
        temp = copy.copy(Arr)
        i8 = time()
        bubble_sort(temp)
        f8 = time()
        print(f8 - i8)
        EXEC_NUM.append(f8 - i8)
        #MERGE SORT
        temp = copy.copy(Arr)
        i9 = time()
        merge_sort(temp,0,tam-1)
        f9 = time()
        print(f9-i9)
        EXEC_NUM.append(f9-i9)
        # QUICK SORT
        temp = copy.copy(Arr)
        iA = time()
        quick_sort(temp, 0, tam - 1)
        fA = time()
        print(fA - iA)
        EXEC_NUM.append(fA - iA)
        # HEAP SORT
        temp = copy.copy(Arr)
        iB = time()
        heap_sort(temp)
        fB = time()
        print(fB-iB)
        EXEC_NUM.append(fB - iB)
        #BUCKET SORT
        temp = copy.copy(Arr)
        iC = time()
        bucket_sort(temp)
        fC = time()
        print(fC-iC)
        EXEC_NUM.append(fC-iC)
        #COUNT SORT
        temp = copy.copy(Arr)
        iD = time()
        count_sort(temp)
        fD = time()
        print(fD-iD)
        EXEC_NUM.append(fD-iD)
        #RADIX SORT
        temp = copy.copy(Arr)
        iF = time()
        radix_sort(temp)
        fF = time()
        print(fF - iF)
        EXEC_NUM.append(fF - iF)
        #BIN SORT
        temp = copy.copy(Arr)
        iG = time()
        bin_sort(temp)
        fG = time()
        print(fG - iG)
        EXEC_NUM.append(fG - iG)
        #RANDOMIZED SORT SELECTION
        temp = copy.copy(Arr)
        iH = time()
        for i in range(1, tam + 1):
            random_select(temp, 0, tam - 1, i)
        fH = time()
        print(fH-iH)
        EXEC_NUM.append(fH-iH)

        # DIBUJAR PLOT
        ypos = np.arange(len(NUMEROS))
        plt.xticks(ypos, NUMEROS)
        plt.ylabel("Tiempo de ejecucion (Seg.)")
        plt.title("Alg. Ordenacion - Numeros")
        plt.bar(ypos, EXEC_NUM)
        plt.show()

#f = tk.Entry(ventana, width=25)
#f.place(x=60, y=100, height=25)
tk.Button(ventana, text="Cargar Archivo", font="times 12 bold", bg="royalblue", image=img_load, command=ext_dato,
          compound=tk.TOP, border=0).place(x=250, y=85)
tk.Label(ventana, text="Ordenar por:", font="times 16 bold", bg="royalblue", fg="blue4").place(x=200, y=140)
# opciones de ordenamiento
rb_shellSort = tk.Radiobutton(ventana, text="Shell Sort", font="times 12 bold", bg="royalblue", variable=opcion_ord,
                              value=1).place(x=90, y=175)
rb_insertSort = tk.Radiobutton(ventana, text="Insert Sort", font="times 12 bold", bg="royalblue", variable=opcion_ord,
                               value=2).place(x=90, y=195)
rb_bubbleSort = tk.Radiobutton(ventana, text="Bubble Sort", font="times 12 bold", bg="royalblue", variable=opcion_ord,
                               value=3).place(x=90, y=215)
rb_mergeSort = tk.Radiobutton(ventana, text="Merge Sort", font="times 12 bold", bg="royalblue", variable=opcion_ord,
                              value=4).place(x=90, y=235)
rb_quickSort = tk.Radiobutton(ventana, text="Quick Sort", font="times 12 bold", bg="royalblue", variable=opcion_ord,
                              value=5).place(x=90, y=255)
rb_bucketSort = tk.Radiobutton(ventana, text="Bucket Sort", font="times 12 bold", bg="royalblue", variable=opcion_ord,
                               value=6).place(x=90, y=275)
rb_radixSort = tk.Radiobutton(ventana, text="Radix Sort", font="times 12 bold", bg="royalblue", variable=opcion_ord,
                              value=7).place(x=325, y=175)
rb_heapSort = tk.Radiobutton(ventana, text="Heap Sort", font="times 12 bold", bg="royalblue", variable=opcion_ord,
                             value=8).place(x=325, y=195)
rb_countSort = tk.Radiobutton(ventana, text="Count Sort", font="times 12 bold", bg="royalblue", variable=opcion_ord,
                              value=9).place(x=325, y=215)
rb_binSort = tk.Radiobutton(ventana, text="Bin Sort", font="times 12 bold", bg="royalblue", variable=opcion_ord,
                            value=10).place(x=325, y=235)
rb_rselectSort = tk.Radiobutton(ventana, text="Random Select Sort", font="times 12 bold", bg="royalblue",
                                variable=opcion_ord, value=11).place(x=325, y=255)
rb_stoogeSort = tk.Radiobutton(ventana, text="Stooge Sort", font="times 12 bold", bg="royalblue", variable=opcion_ord,
                               value=12).place(x=325, y=275)

sctextUn = st.ScrolledText(ventana, width=28,height=24, bg="silver")
sctextUn.place(x=500,y=90)
sctextOr = st.ScrolledText(ventana, width=28,height=24, bg="silver")
sctextOr.place(x=760,y=90)

buDel1 = tk.Button(ventana, text="Limpiar", command=elim1).place(x=590,y=55)
buDel2 = tk.Button(ventana, text="Limpiar", command=elim2).place(x=850,y=55)


tk.Button(ventana, text="Run...!!!", image=img_btn_run, bg="royalblue", border=0, command=run).place(x=225, y=310)

tk.Button(ventana, text="Comparar tiempos", bg="royalblue", border=0, font="times 14 bold", command=comparar).place(x=175, y=340)

# mostrar los tiempos de ejecucion
timelabel = tk.Label(ventana, text="Tiempo de ejecucion:", font="times 17 bold", bg="royalblue").place(x=50, y=380)
showtime = tk.Label(ventana, text="", font="Helvetica 16 bold", bg="royalblue", fg="lightblue2",
                    textvariable=textMostrar).place(x=275, y=381)
second_lab = tk.Label(ventana, text="Seg.", font="times 17 bold", fg="lightblue2", bg="royalblue").place(x=385, y=380)
bu_salir = tk.Button(ventana, image=img_exit, bg="royalblue", command=ventana.quit).place(x=215, y=430)
ventana.mainloop()

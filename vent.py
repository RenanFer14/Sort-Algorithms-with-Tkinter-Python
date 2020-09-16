from tkinter import *
from tkinter import messagebox
from time import time
import random
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
        #analizar la parte izq del arreglo y buscar la pos correcta de key_item
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
    #comenzamos con un gap grande y luego lo reducimos    
    n = len(arr) 
    gap = n//2  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0:   
        for i in range(gap,n):   
            # agregar arr[i] a los elementos que han sido ordenados
            # guardar a[i] en temp y hacer espacio en la posicion i 
            temp = arr[i]   
            # cambiar los elementos ordenados antes de gap  hasta hallar la ubicacion para arr[i]
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
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
        for j in range(0, n-i-1):   
            # recorrer el arr desde 0 hasta n-i-1 
            # cambiar si el elemento encontrado es mayor que el siguiente elemento 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]


#   4. Merge Sort
def merge_sort(A, p, r):
    if(p < r):
        q = int((p + r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return A

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    #arrays para las particiones derecha e izquierda
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    i = 1
    j = 1

    #verificar si algun elemento queda por asignar 
    while i <= n1:
        L[i-1] = A[p+i-1]
        i = i + 1
    while j <= n2:
        R[j-1] = A[q+j]
        j = j + 1
    #asignar valores maximos
    L[n1] = float("inf")
    R[n2] = float("inf")
    i = 0
    j = 0

    #copiar datos a los arrays der e izq
    for k in range(p, r + 1):
        if(L[i] < R[j]):
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    return A


#   5. Quick Sort
def partition(arr,low,high): 
    # indice del elemento mas pequeño 
    i = ( low-1 )
    # pivote
    pivot = arr[high]  
    for j in range(low , high):   
        # si el elemento actual es menor que el pivote 
        if   arr[j] < pivot:           
            # incrementar el indice del elemento pequeño 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    # intercambiar elementos
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# Function to do Quick sort 
def quick_sort(arr,low,high): 
    if low < high:   
        # pi es indice de la particion, arr[p] esta en la posicion correcta
        pi = partition(arr,low,high)   
        # ordenar elementos de forma separada antes y despues del pivot
        quick_sort(arr, low, pi-1) 
        quick_sort(arr, pi+1, high) 

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
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # poner la raiz en el heap. 
        heapify(arr, n, largest) 
   
def heap_sort(arr): 
    n = len(arr) 
  
    # construir un maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # extraer los elementos uno a uno 
    for i in range(n-1, 0, -1): 
        # swap
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0) 


#   7. Bucket Sort
def bucket_sort(lista):
    k = len(lista) - 1
    #crear buckets/cajas para ir almacenando
    buckets = [[] for i in range (k)]
    maxValue = max(lista)
    # distribuir los elementos de manera uniforme
    for i in range(k, -1, -1):
        buckets[lista[i] * k // (maxValue + 1)].insert(0, lista[i])
    #usar insert_sort para ordenar cada bucket
    for i in range(0, k):
        insert_sort(buckets[i])
    returnList = []
    #concatenar las listas ordenadas
    for bucket in buckets:
        returnList.extend(bucket)
    return returnList

#   8. Count Sort
def count_sort(list):
    
    #crear una lista de 0's de tamaño igual al maximo valor de la lista dada + 1
    c = [0]*(max(list)+1) 
    # el arr final ordenado sera devuelto del mismo tamaño que el dado
    b = [0]*len(list)      
    #para cada elemento en la lista, el numero de ocurrencias se guarda en su respectivo indice en la lista C
    for i in list:
        c[i] = c[i] + 1    
    #cada elemento en C incluye el valor de su elemento previo
    for k in range(1, len(c)):
        c[k] = c[k] + c[k-1]   
    # iterando la lista en reversa
    for l in list[::-1]:
         # modificamos cada valor en la lista al idnice daod por C, restadole 1    
        b[c[l]-1] = l       
        c[l] = c[l] - 1
    return b

#   9. Radix Sort
def radix_sort(array):
    #determinar el maximo valor del array para saber el numero digitos
    m = max(array)    
    #aplicar counting sort para cada digito
    i = 1
    while(m/i > 0):
        count_sort(array)        
        i*=10

#   10. Bin Sort
#### BIN SORT = BUCKET SORT
def bin_sort(lista):
    k = len(lista) - 1
    buckets = [[] for i in range (k)]
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
#modulo para intercambiar valores
def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
#modulo para realizar una particion
def partition_r(a,l,r,p_index):
    p = a[p_index]
    swap(a,l,p_index)
    i = l+1
    for j in range(l+1,r+1):
        if(a[j] < p):
            swap(a, i, j)
        i+=1
    swap(a,l,i-1)
    return a.index(p)

def random_select(a,l,r,i):
    n = r-l
    if (n==1):
        return a[l]
    p = random.randint(l,r)
    val = a[p]
    j = partition_r(a,l,r,p)
    if(i==j): 
        return val
    if (j>i): 
        return random_select(a,l,j-1,i)
    if (j<i): 
        return random_select(a,j+1,r,i-j)
#   12. Stooge Sort
def stooge_sort(arr, l, h): 

    if l >= h: 
        return   
    # si el primer elemento es menor que el ultimo se intercambia
    if arr[l]>arr[h]: 
        t = arr[l] 
        arr[l] = arr[h] 
        arr[h] = t 
   
    # si hay mas de dos elementos en el arra 
    if h-l + 1 > 2: 
        t = (int)((h-l + 1)/3)    
        # ordenar recursivamente los primeros 2 / 3 elementos 
        stooge_sort(arr, l, (h-t)) 
   
        # ordenar recursivamente los ultimos 2 / 3 elementos 
        stooge_sort(arr, l + t, (h))    
        # # ordenar recursivamente los primeros 2 / 3 elementos OTRA VEZ para confirmar
        stooge_sort(arr, l, (h-t))
        
#################### END REGION ALGORITMOS ########################## 
# ··························································································· 
#################### REGION VENTANA DE INTERFAZ ##########################
#configuracion de la ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.resizable(0,0)
ventana.title("Algoritmos de Ordenacion")
ventana.configure(background="royalblue")

#imagenes a usar
img_load = PhotoImage(file="img/ext_dat.png")
img_btn_run = PhotoImage(file="img/start.png")
img_exit = PhotoImage(file="img/exit.png") 

#variables generales
opcion_ord = IntVar()
textMostrar = StringVar()
textMostrar.set("0.00")

#titulo de ventana
titul_label = Label(ventana, text="ALGORITMOS DE ORDENACION",font="times 18 bold underline", bg="royalblue").place(x=70,y=30)

#······ MODULOS PARA LA MANIPULACION DE LOS DATOS
def ext_dato():
    global data_arr
    file_name = f.get()
    if (file_name == ""):
        messagebox.showwarning("Error al cargar archivo","Inserte un nombre de archivo valido*")
        data_arr =  "No hay datos*"
    else:
        try:               
            data = open(file_name,'r')
            lines = []
            for line in data:
                lines.append(line)
            #print("extraccion correcta*")            
            data.close()
            messagebox.showinfo("Archivo cargado correctamente","Cantidad de elementos cargados: "+str(len(lines)))
            data_arr = lines
            return data_arr           
        except FileNotFoundError:
            messagebox.showerror("Error al extraer datos","Verifique el nombre del archivo*")
            f.delete(0,len(f.get()))
            data_arr = "No hay datos*"
            return data_arr
        except FileExistsError:
            messagebox.showerror("Error al extraer datos","Verifique el nombre del archivo*")
            f.delete(0,len(f.get()))
            data_arr = "No hay datos*"
            return data_arr
def conv(arr):
    k = arr[0] 
    try:
        if(isinstance(int(k),int) == True):
            for i in range(len(arr)):
                arr[i] = int(arr[i])
    except:
           pass    
    return arr
    #if arr != "No hay datos*":
    #else:        
    #   messagebox.showwarning("Error al cargar datos","Cargue nuevamente el archivo")

def escribirArch(arr,namefile,ind):
    if(ind == 1):# ----> Palabras
        try:
            filewrite = open("out/"+namefile,'w')
            for i in arr:
                filewrite.write(i)
            filewrite.close()
            messagebox.showinfo("Mensaje","Archivo ordenado creado satisfactoriamente")
        except:
            messagebox.showwarning("Error al escribir archivo","Vuelva a escribir el archivo, error desconocido*")
    else:   #-------> Numeros
        try:
            filewrite = open("out/"+namefile,'w')
            for i in arr:
                print(i,file=filewrite)
            filewrite.close()
            messagebox.showinfo("Mensaje","Archivo ordenado creado satisfactoriamente")
        except:
            messagebox.showwarning("Error al escribir archivo","Vuelva a escribir el archivo, error desconocido*")

def mostrar_tiempo(total):    
    texto = str(round(total,6))
    textMostrar.set(texto)

def run():
    global data_arr
    ArrDef = conv(data_arr)
    tam = len(ArrDef)
    temporal = ArrDef
    first = ArrDef[0]
    opcion = opcion_ord.get()
    
    if(isinstance(first,str) == True):
        if(opcion == 1):
            #medir el tiempo de ejecucion
            start_time = time()    
            shell_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Shell-ord",1)
        elif(opcion == 2): 
            start_time = time()           
            insert_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Insert-ord",1)
        elif(opcion == 3):     
            start_time = time()       
            bubble_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Bubble-ord",1)
        elif(opcion == 4):     
            start_time = time()       
            merge_sort(temporal,0,tam-1)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Merge-ord",1)
        elif(opcion == 5):     
            start_time = time()       
            quick_sort(temporal,0,tam-1)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Quick-ord",1)
        elif(opcion == 8):     
            start_time = time()       
            heap_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Heap-ord",1)
        elif(opcion == 12):    
            start_time = time()        
            stooge_sort(temporal,0,tam-1)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Stooge-ord",1)
        else:
            messagebox.showwarning("Error al ordenar","PALABRAS no se pueden ordenar mediante este algoritmo...*")
    else:
        if(opcion == 1):      
            start_time = time()      
            shell_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Shell-ord",2)
        elif(opcion == 2):     
            start_time = time()       
            insert_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Insert-ord",2)
        elif(opcion == 3):     
            start_time = time()       
            bubble_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Bubble-ord",2)
        elif(opcion == 4):     
            start_time = time()       
            merge_sort(temporal,0,tam-1)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Merge-ord",2)
        elif(opcion == 5):     
            start_time = time()       
            quick_sort(temporal,0,tam-1)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Quick-ord",2)
        elif(opcion == 6):     
            start_time = time()       
            tempB = bucket_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(tempB,"Bucket-ord",2)
        elif(opcion == 7):     
            start_time = time()       
            radix_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Radix-ord",2)
        elif(opcion == 8):     
            start_time = time()       
            heap_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Heap-ord",2)
        elif(opcion == 9):     
            start_time = time()       
            tempC = count_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(tempC,"Count-ord",2)
        elif(opcion == 10):    
            start_time = time()        
            tempBi = bin_sort(temporal)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(tempBi,"Bin-ord",2)
        elif(opcion == 11):    
            start_time = time()        
            random_select(temporal,0,tam-1,0)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Random-ord",2)
        elif(opcion == 12):    
            start_time = time()        
            stooge_sort(temporal,0,tam-1)
            end_time = time()
            total_time =  end_time-start_time
            mostrar_tiempo(total_time)
            escribirArch(temporal,"Stooge-ord",2)
    

f = Entry(ventana,width=25)
f.place(x=60,y=100,height=25)
Button(ventana, text="Cargar Archivo",font="times 12 bold",bg="royalblue",image=img_load,command=ext_dato,compound=TOP,border=0).place(x=250,y=85)
Label(ventana,text="Ordenar por:",font="times 16 bold",bg="royalblue", fg="blue4").place(x=200,y=140)
#opciones de ordenamiento
rb_shellSort = Radiobutton(ventana, text="Shell Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=1).place(x=90,y=175)
rb_insertSort = Radiobutton(ventana, text="Insert Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=2).place(x=90,y=195)
rb_bubbleSort = Radiobutton(ventana, text="Bubble Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=3).place(x=90,y=215)
rb_mergeSort = Radiobutton(ventana, text="Merge Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=4).place(x=90,y=235)
rb_quickSort = Radiobutton(ventana, text="Quick Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=5).place(x=90,y=255)
rb_bucketSort = Radiobutton(ventana, text="Bucket Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=6).place(x=90,y=275)
rb_radixSort = Radiobutton(ventana, text="Radix Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=7).place(x=325,y=175)
rb_heapSort = Radiobutton(ventana, text="Heap Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=8).place(x=325,y=195)
rb_countSort = Radiobutton(ventana, text="Count Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=9).place(x=325,y=215)
rb_binSort = Radiobutton(ventana, text="Bin Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=10).place(x=325,y=235)
rb_rselectSort = Radiobutton(ventana, text="Random Select Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=11).place(x=325,y=255)
rb_stoogeSort = Radiobutton(ventana, text="Stooge Sort",font="times 12 bold",bg="royalblue",variable=opcion_ord, value=12).place(x=325,y=275)

Button(ventana, text="Run...!!!",image = img_btn_run,bg="royalblue",border=0,command=run).place(x=225,y=310)

#mostrar los tiempos de ejecucion
timelabel = Label(ventana, text="Tiempo de ejecucion:",font="times 17 bold", bg="royalblue").place(x=50,y = 380)
showtime = Label(ventana, text="",font="Helvetica 16 bold",bg="royalblue",fg="lightblue2", textvariable = textMostrar).place(x= 275, y=381)
second_lab = Label(ventana, text="Seg.",font="times 17 bold", fg="lightblue2", bg="royalblue").place(x=385,y=380)
bu_salir = Button(ventana, image=img_exit,bg="royalblue", command=ventana.quit).place(x=215,y=430)
ventana.mainloop()
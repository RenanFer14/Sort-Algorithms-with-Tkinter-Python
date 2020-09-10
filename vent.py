from tkinter import *
from tkinter import messagebox
import random


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
  
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n//2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0:   
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap //= 2

#   3. Bubble Sort

def bubble_sort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n):  
        # Last i elements are already in place 
        for j in range(0, n-i-1):   
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]


#   4. Merge Sort

def merge_sort(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_sort(L) # Sorting the first half 
        merge_sort(R) # Sorting the second half 
  
        i = j = k = 0          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1


#   5. Quick Sort
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quick_sort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quick_sort(arr, low, pi-1) 
        quick_sort(arr, pi+1, high) 

#   6. Heap Sort
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heap_sort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 


#   7. Bucket Sort
def bucket_sort(lista):
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
#   8. Count Sort
def count_sort(list):
    c = [0]*(max(list)+1)  # creating a memory list of 0's, the number of 0's is equal to the max number in the given list + 1 to be inclusive
    b = [0]*len(list)      # the final sorted list to be returned, same length as provided, unsorted list

    for i in list:
        c[i] = c[i] + 1    # for each element in list, the number of its occurences is recorded in its respective index in list c

    for k in range(1, len(c)):
        c[k] = c[k] + c[k-1]   # each element in c includes the value of its previous element

    for l in list[::-1]:     #iterating over list backwards
        b[c[l]-1] = l        # setting each value in list at the index indicated by c, subtracting by 1 to be exclusive
        c[l] = c[l] - 1      # decrementing by 1 since that position will now be filled
    return b
#   9. Radix Sort
def radix_sort(array):
    m = max(array)    
    i = 1
    while(m/i > 0):
        count_sort(array)        
        i*=10
#   10. Bin Sort
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
def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
  
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
    # If first element is smaller 
    # than last, swap them 
    if arr[l]>arr[h]: 
        t = arr[l] 
        arr[l] = arr[h] 
        arr[h] = t 
   
    # If there are more than 2 elements in 
    # the array 
    if h-l + 1 > 2: 
        t = (int)((h-l + 1)/3) 
   
        # Recursively sort first 2 / 3 elements 
        stooge_sort(arr, l, (h-t)) 
   
        # Recursively sort last 2 / 3 elements 
        stooge_sort(arr, l + t, (h)) 
   
        # Recursively sort first 2 / 3 elements 
        # again to confirm 
        stooge_sort(arr, l, (h-t))
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
def ext_dato():
    global data_arr
    file_name = f.get()
    if (file_name == ""):
        messagebox.showwarning("Error al cargar archivo","Inserte un nombre de archivo valido*")
        data_arr =  "No hay datos*"
    else:
        try:               
            data = open(file_name,'r')
            datos = data.readlines()
            #print("extraccion correcta*")            
            data.close()
            messagebox.showinfo("Archivo cargado correctamente","Cantidad de elementos cargados: "+str(len(datos)))
            data_arr = datos            
        except FileNotFoundError:
            messagebox.showerror("Error al extraer datos","Verifique el nombre del archivo*")
            f.delete(0,len(f.get()))
            data_arr = "No hay datos*"
        except FileExistsError:
            messagebox.showerror("Error al extraer datos","Verifique el nombre del archivo*")
            f.delete(0,len(f.get()))
            data_arr = "No hay datos*"
        finally:
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

            
    
        

def run():
    global data_arr
    ArrDef = conv(data_arr)
    
    

f = Entry(ventana,width=25)
f.place(x=60,y=100)
Button(ventana, text="Cargar Archivo...",width=14,command=ext_dato).place(x=250,y=100)
Label(ventana,text="Ordenar por:",font="Helvetica 12 bold",bg="skyblue").place(x=200,y=140)
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

Button(ventana, text="Run...!!!", command=run).place(x=225,y=310)

ventana.mainloop()
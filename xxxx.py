import tkinter as tk
root = tk.Tk()
variable = tk.StringVar()
def prueba():
    print("Se ha elegido la opcion" + variable.get())

radiobutton1 = tk.Radiobutton(root,text="Opcion 1", variable=variable, value=1, command=prueba)
radiobutton2 = tk.Radiobutton(root,text="Opcion 2", variable=variable, value=2, command=prueba)
radiobutton3 = tk.Radiobutton(root,text="Opcion 3", variable=variable, value=3, command=prueba)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
variable.get()
tk.mainloop()
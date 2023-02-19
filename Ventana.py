from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING

class Ventana_principal(Tk):
    # Constructor de la clase, definimos las dimensiones de la ventana principal y su nombre 
    # y llamamos al metodo build
    def __init__(self, master = NONE):
        super().__init__(master)
        self.title("Gestor de clientes (Ventana principal)")
        self.geometry("750x500")
        self.build()

    def build(self):
        frame = Frame(self)
        frame.pack()
        
        self.treeview = ttk.Treeview(self, colmns = ("Nombre", "Apellidos", "DNI", "Telefono", "Email"))

        # Definimos el numero de columnas, su nombre y anchos de cada una, los cuales son CENTER para que 
        # el texto se escriba en el centro de la columna. La columna 0 es la del Id, el cual se generara automaticamente
        self.treeview.column("#0", width = 0, stretch = NO)
        self.treeview.column("Nombre", anchor = CENTER)
        self.treeview.column("Apellidos", anchor = CENTER)
        self.treeview.column("DNI", anchor = CENTER)
        self.treeview.column("Telefono", anchor = CENTER)
        self.treeview.column("Email", anchor = CENTER)

        # Definimos el encabezado de cada columna, el cual sera el nombre de la columna. El encabezado de la 
        # columna 0 sera Id, el cual se generara automaticamente
        self.treeview.heading("#0", text = "Id", anchor = CENTER)
        self.treeview.heading("Nombre", text = "Nombre", anchor = CENTER)
        self.treeview.heading("Apellidos", text = "Apellidos", anchor = CENTER)
        self.treeview.heading("DNI", text = "DNI", anchor = CENTER)
        self.treeview.heading("Telefono", text = "Telefono", anchor = CENTER)
        self.treeview.heading("Email", text = "Email", anchor = CENTER)

        # Definimos un scrollbar para la tabla
        self.scrollbar = Scrollbar(self)

        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.treeview["yscrollcommand"] = self.scrollbar.set

        self.scrollbar.pack(side = BOTTOM, fill = X)
        self.treeview["xscrollcommand"] = self.scrollbar.set

        self.treeview.pack()

        # Definimos los botones de la ventana principal
        frame = Frame(self)
        frame.pack(pady = 20)

        Button(frame, text = "Crear", command = self.crear).grid(row = 0, column = 0)
        Button(frame, text = "Editar", command = self.editar).grid(row = 0, column = 1)
        Button(frame, text = "Eliminar", command = self.eliminar).grid(row = 0, column = 2)

    def crear(self):
        self.crear = Ventana_crear_cliente(self)
        pass

    def editar(self):
        pass

    def eliminar(self):
        pass

class Ventana_crear_cliente(Toplevel):
    # Constructor de la clase, definimos las dimensiones de la ventana crear cliente y su nombre 
    # y llamamos al metodo build
    def __init__(self, master = None):
        super().__init__()
        self.master = master
        self.title("Paises Base de Datos")
        self.geometry("150x300")
        self.build()

    def build(self):
        frame2 = Frame(self)
        frame2.pack()

        # Crear las casillas de texto para introducir los datos del cliente
        lbl1 = Label(frame2, text = "Nombre: ")
        lbl1.place(x = 3, y = 5)
        self.textoISO3 = Entry(frame2)
        self.textoISO3.place(x = 3, y = 25, width = 50, height = 20)

        lbl2 = Label(frame2, text = "Apellido: ")
        lbl2.place(x = 3, y = 55)
        self.textoPais = Entry(frame2)
        self.textoPais.place(x = 3, y = 75, width = 100, height = 20)

        lbl3 = Label(frame2, text = "DNI: ")
        lbl3.place(x = 3, y = 105)
        self.textoCapiltal = Entry(frame2)
        self.textoCapiltal.place(x = 3, y = 125, width = 100, height = 20)

        lbl4 = Label(frame2, text = "Telefono: ")
        lbl4.place(x = 3, y = 155)
        self.textoPoblacion = Entry(frame2)
        self.textoPoblacion.place(x = 3, y = 175, width = 50, height = 20)

        lbl4 = Label(frame2, text = "Telefono: ")
        lbl4.place(x = 3, y = 155)
        self.textoPoblacion = Entry(frame2)
        self.textoPoblacion.place(x = 3, y = 175, width = 50, height = 20)

        lbl5 = Label(frame2, text = "Email: ")
        lbl5.place(x = 3, y = 205)
        self.textoPoblacion = Entry(frame2)
        self.textoPoblacion.place(x = 3, y = 225, width = 100, height = 20)

        # Crear los botones de la ventana crear cliente
        frame = Frame(self)
        frame.pack(pady = 20)

        self.Guardar = Button(frame2, text = "Guardar", command = self.guardar_datos)
        self.Guardar.place(x = 10, y = 275, width = 60, height = 60)
        self.Cancelar = Button(frame2, text = "Cancelar", command = self.close)
        self.Cancelar.place(x = 80, y = 275, width = 60, height = 30)

    def guardar_datos(self):
        pass

    def close(self):
        self.destroy()
        self.update()

class Ventana_editar_cliente(Toplevel):
    # Constructor de la clase, definimos las dimensiones de la ventana crear cliente y su nombre 
    # y llamamos al metodo build
    def __init__(self, master = None):
        super().__init__()
        self.master = master
        self.title("Paises Base de Datos")
        self.geometry("150x300")
        self.build()

    def build(self):
        frame3 = Frame(self)
        frame3.pack(padx = 20, pady = 20)

        # Crear las casillas de texto para introducir los datos del cliente
        lbl1 = Label(frame3, text = "Nombre: ")
        lbl1.place(x = 3, y = 5)
        self.textoISO3 = Entry(frame3)
        self.textoISO3.place(x = 3, y = 25, width = 50, height = 20)

        lbl2 = Label(frame3, text = "Apellido: ")
        lbl2.place(x = 3, y = 55)
        self.textoPais = Entry(frame3)
        self.textoPais.place(x = 3, y = 75, width = 100, height = 20)

        lbl3 = Label(frame3, text = "DNI: ")
        lbl3.place(x = 3, y = 105)
        self.textoCapiltal = Entry(frame3)
        self.textoCapiltal.place(x = 3, y = 125, width = 100, height = 20)

        lbl4 = Label(frame3, text = "Telefono: ")
        lbl4.place(x = 3, y = 155)
        self.textoPoblacion = Entry(frame3)
        self.textoPoblacion.place(x = 3, y = 175, width = 50, height = 20)

        lbl4 = Label(frame3, text = "Telefono: ")
        lbl4.place(x = 3, y = 155)
        self.textoPoblacion = Entry(frame3)
        self.textoPoblacion.place(x = 3, y = 175, width = 50, height = 20)

        lbl5 = Label(frame3, text = "Email: ")
        lbl5.place(x = 3, y = 205)
        self.textoPoblacion = Entry(frame3)
        self.textoPoblacion.place(x = 3, y = 225, width = 100, height = 20)

        # Crear los botones de la ventana crear cliente
        frame3 = Frame(self)
        frame3.pack(pady = 20)

        self.actualizar = Button(frame3, text = "Actualizar", command = self.edit_client)
        self.actualizar.place(x = 10, y = 275, width = 60, height = 60)
        self.cancelar = Button(frame3, text = "Cancelar", command = self.close)
        self.cancelar.place(x = 80, y = 275, width = 60, height = 30)

    def edit_client(self):
        pass

    def close(self):
        self.destroy()
        self.update()



if __name__ == '__main__':
    app = Ventana_principal()
    app.mainloop()






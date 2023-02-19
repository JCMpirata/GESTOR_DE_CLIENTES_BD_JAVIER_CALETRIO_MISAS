from tkinter import *
from Ventana import *

def main():
    root = Tk()
    root.title("Paises Base de Datos")
    app = Ventana_principal(root)
    root.mainloop()

if __name__ == '__main__':
    main()
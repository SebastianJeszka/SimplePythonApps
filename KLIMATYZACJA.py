import tkinter
from tkinter import *

root = tkinter.Tk()
root.geometry('600x500')
root.title("Klimatyzator")
root.configure(bg='lightblue')


b = Label(root, text ="Klimatyzator")
b.pack()


MenuGlowne = tkinter.Menu()
root.config(menu=MenuGlowne)
MenuOpcje = tkinter.Menu(MenuGlowne)
MenuGlowne.add_cascade(label='Opcje', menu=MenuOpcje)

MenuOpcje.add_command(label='Wybierz tryb zimowy lub letni')
MenuOpcje.add_command(label='Wybierz docelową temperaturę')
MenuOpcje.add_command(label='Wybierz ocieplenie budynku')
MenuOpcje.add_separator()
MenuOpcje.add_command(label='Podgląd pracy klimatyzatora')
MenuOpcje.add_separator()

MenuAutor = tkinter.Menu(MenuGlowne)
MenuGlowne.add_cascade(label='Dodatkowe informacje', menu=MenuAutor)
MenuAutor.add_command(label='Poradnik obsługi aplikacji')
MenuAutor.add_command(label='Informacje o Autorach')

root.mainloop()
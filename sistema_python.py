import time
from tkinter import *

import pygame

pygame.init()
#formulário principal, root
root = Tk()
root.title('SISTEMA DE VENDAS')
root.geometry('1352x750+0+0')
root.configure(background='yellow')

#cria um frame principal, bd=border, relief = RIDGE, formato curvo
FrameABC = Frame(root, bg= 'blue', bd=20, relief = RIDGE)
FrameABC.grid()

#frame secundário
FrameABC1 = Frame(FrameABC, bg= 'blue', bd=10, relief = RIDGE)
FrameABC1.grid(row=0, column=0, columnspan=4, sticky = W)

# frame secundário
FrameABC2 = Frame(FrameABC, bg='blue', bd=10, relief=RIDGE)
FrameABC2.grid(row=1, column=0, sticky=W)

# frame secundário
FrameABC3 = Frame(FrameABC, bg='blue', bd=10, relief=RIDGE)
FrameABC3.grid(row=1, column=1, sticky=W)

# frame secundário
FrameABC4 = Frame(FrameABC, bg='blue', bd=10, relief=RIDGE)
FrameABC4.grid(row=1, column=2, sticky=W)

# frame secundário, dentro do FRAMEABC4
FrameABC5 = Frame(FrameABC4, bg='blue', bd=10, relief=RIDGE)
FrameABC5.grid(row=0, column=0, sticky=W)

# frame secundário, dentro do FRAMEABC4
FrameABC6 = Frame(FrameABC4, bg='blue', bd=10, relief=RIDGE)
FrameABC6.grid(row=1, column=0, columnspan=4, sticky=W)

# variáveis de hora e data
Date1 = StringVar()
Time1 = StringVar()

Date1.set(time.strftime('%d/%m/%Y'))
Time1.set(time.strftime('%H:%M:%S'))

# cria um label de data e coloca no FrameABC1
lblDate = Label(FrameABC1, textvariable=Date1, font=('arial', 30, 'bold'), padx=0, pady=9, bd=14, bg='Cadet Blue',
                fg='Cornsilk', justify=CENTER).grid(row=0, column=0)

# cria um label de título e coloca no FrameABC1
lblTitle = Label(FrameABC1, text='\tSistema de Vendas\t', font=('arial', 30, 'bold'), padx=0, pady=9, bd=14,
                 bg='Cadet Blue', fg='Cornsilk', justify=CENTER).grid(row=0, column=1)

# cria um label de hora e coloca no FrameABC1
lblTime = Label(FrameABC1, textvariable=Time1, font=('arial', 30, 'bold'), padx=0, pady=9, bd=14, bg='Cadet Blue',
                fg='Cornsilk', justify=CENTER).grid(row=0, column=2)




root.mainloop()
from tkinter import *
import time
import datetime
import pygame
import sys
import random


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

root.mainloop()
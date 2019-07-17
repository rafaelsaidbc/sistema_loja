import time
from tkinter import *

import pygame

pygame.init()
#formulário principal, root
root = Tk()
root.title('SISTEMA DE VENDAS')
# congela a janela para não ser redimensionada, False para altura e False para largura
root.resizable(False, False)
root.configure(background='black')

#cria um frame principal, bd=border, relief = RIDGE, formato curvo
FrameABC = Frame(root, bg='black', bd=20, relief=RIDGE)
FrameABC.grid()

#frame secundário
FrameABC1 = Frame(FrameABC, bg='forestgreen', bd=10, relief=RIDGE)
FrameABC1.grid(row=0, column=0, columnspan=4, sticky = W)

# frame secundário
FrameABC2 = Frame(FrameABC, bg='green', bd=10, relief=RIDGE)
FrameABC2.grid(row=1, column=0, sticky=W)

# frame secundário
FrameABC3 = Frame(FrameABC, bg='green', bd=10, relief=RIDGE)
FrameABC3.grid(row=1, column=1, sticky=W)

# frame secundário
FrameABC4 = Frame(FrameABC, bg='green', bd=10, relief=RIDGE)
FrameABC4.grid(row=1, column=2, sticky=W)

# frame secundário, dentro do FRAMEABC4
FrameABC5 = Frame(FrameABC4, bg='green', bd=10, relief=RIDGE)
FrameABC5.grid(row=0, column=0, sticky=W)

# frame secundário, dentro do FRAMEABC4
FrameABC6 = Frame(FrameABC4, bg='green', bd=10, relief=RIDGE)
FrameABC6.grid(row=1, column=0, columnspan=4, sticky=W)

# variáveis de hora e data
Date1 = StringVar()
Time1 = StringVar()

Date1.set(time.strftime('%d/%m/%Y'))
Time1.set(time.strftime('%H:%M:%S'))

# ===================== LABEL DATA, TÍTULO, HORA =====================

# cria um label de data e coloca no FrameABC1
lblDate = Label(FrameABC1, width=16, textvariable=Date1, font=('arial', 30, 'bold'), padx=9, pady=9, bd=14,
                bg='Cadet Blue',
                fg='Cornsilk', justify=CENTER).grid(row=0, column=0)

# cria um label de título e coloca no FrameABC1
lblTitle = Label(FrameABC1, width=15, text='\tSistema de Vendas\t', font=('arial', 30, 'bold'), padx=9, pady=9, bd=14,
                 bg='Cadet Blue', fg='Cornsilk', justify=CENTER).grid(row=0, column=1)

# cria um label de hora e coloca no FrameABC1
lblTime = Label(FrameABC1, width=16, textvariable=Time1, font=('arial', 30, 'bold'), padx=9, pady=9, bd=14,
                bg='Cadet Blue',
                fg='Cornsilk', justify=CENTER).grid(row=0, column=2)

# ===================== LABEL FEMININO =====================
# cria um label de seção Feminino
lblFeminino = Label(FrameABC2, text='Feminino', font=('arial', 20, 'bold'), padx=8, pady=1, bd=8, bg='yellow',
                    fg='black', width=25, justify=CENTER).grid(row=0, column=0, columnspan=4)

# cria um label de seção Jeans Blusa
lblJeansBlusa = Label(FrameABC2, text='Jeans blusa', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                      justify=LEFT).grid(row=1, column=0)

# cria um label de seção Casaco
lblCoatsjackets = Label(FrameABC2, text='Casaco', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                        justify=LEFT).grid(row=2, column=0)

# cria um label de seção Roupa Sport
lblSportwear = Label(FrameABC2, text='Roupa Sport', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                     justify=LEFT).grid(row=3, column=0)

# cria um label de seção Vestidos
lblDresses = Label(FrameABC2, text='Vestidos', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                   justify=LEFT).grid(row=4, column=0)

# ===================== CAIXAS DE TEXTO FEMININO =====================
# cria uma caixa de texto Entry de seção Jeans Blusa
txtJeansBlusa = Entry(FrameABC2, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=1,
                                                                                                              column=1,
                                                                                                              pady=1)

# cria uma caixa de texto Entry de seção Casaco
txtCoatsjackets = Entry(FrameABC2, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=2,
                                                                                                                column=1,
                                                                                                                pady=1)

# cria uma caixa de texto Entry de seção Roupa Sport
txtSportwear = Entry(FrameABC2, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=3,
                                                                                                             column=1,
                                                                                                             pady=1)

# cria uma caixa de texto Entry de seção Vestidos
txtDresses = Entry(FrameABC2, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=4,
                                                                                                           column=1,
                                                                                                           pady=1)

# ===================== LABEL CRIANÇAS =====================
# cria um label de seção Feminino
lblCrianca = Label(FrameABC2, text='Crianças', font=('arial', 20, 'bold'), padx=8, pady=1, bd=8, bg='yellow',
                   fg='black', width=25, justify=CENTER).grid(row=5, column=0, columnspan=4)

# cria um label de seção Vestidos
lblSkirts = Label(FrameABC2, text='Saias', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                  justify=LEFT).grid(row=6, column=0)

# cria um label de seção Vestidos
lblSwimwear = Label(FrameABC2, text='Natação', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                    justify=LEFT).grid(row=7, column=0)

# cria um label de seção Vestidos
lblSchoolUniform = Label(FrameABC2, text='Uniforme', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                         justify=LEFT).grid(row=8, column=0)

# cria um label de seção Vestidos
lblPyjamas = Label(FrameABC2, text='Pijama', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                   justify=LEFT).grid(row=9, column=0)

# ===================== CAIXAS DE TEXTO CRIANÇAS =====================
# cria uma caixa de texto Entry de seção Jeans Blusa
txtSkirts = Entry(FrameABC2, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=6,
                                                                                                          column=1,
                                                                                                          pady=1)

# cria uma caixa de texto Entry de seção Casaco
txtSwimwear = Entry(FrameABC2, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=7,
                                                                                                            column=1,
                                                                                                            pady=1)

# cria uma caixa de texto Entry de seção Roupa Sport
txtSchoolUniform = Entry(FrameABC2, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=8,
                                                                                                                 column=1,
                                                                                                                 pady=1)

# cria uma caixa de texto Entry de seção Vestidos
txtPyjamas = Entry(FrameABC2, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=9,
                                                                                                           column=1,
                                                                                                           pady=1)

# ==================== FRAMEABC3 ===========================

# ===================== LABEL FEMININO =====================
# cria um label de seção Feminino
lblFeminino = Label(FrameABC3, text='Feminino', font=('arial', 20, 'bold'), padx=8, pady=1, bd=8, bg='yellow',
                    fg='black', width=25, justify=CENTER).grid(row=0, column=0, columnspan=4)

# cria um label de seção Jeans Blusa
lblJeansBlusa = Label(FrameABC3, text='Jeans blusa', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                      justify=LEFT).grid(row=1, column=0)

# cria um label de seção Casaco
lblCoatsjackets = Label(FrameABC3, text='Casaco', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                        justify=LEFT).grid(row=2, column=0)

# cria um label de seção Roupa Sport
lblSportwear = Label(FrameABC3, text='Roupa Sport', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                     justify=LEFT).grid(row=3, column=0)

# cria um label de seção Vestidos
lblDresses = Label(FrameABC3, text='Vestidos', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                   justify=LEFT).grid(row=4, column=0)

# ===================== CAIXAS DE TEXTO FEMININO =====================
# cria uma caixa de texto Entry de seção Jeans Blusa
txtJeansBlusa = Entry(FrameABC3, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=1,
                                                                                                              column=1,
                                                                                                              pady=1)

# cria uma caixa de texto Entry de seção Casaco
txtCoatsjackets = Entry(FrameABC3, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=2,
                                                                                                                column=1,
                                                                                                                pady=1)

# cria uma caixa de texto Entry de seção Roupa Sport
txtSportwear = Entry(FrameABC3, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=3,
                                                                                                             column=1,
                                                                                                             pady=1)

# cria uma caixa de texto Entry de seção Vestidos
txtDresses = Entry(FrameABC3, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=4,
                                                                                                           column=1,
                                                                                                           pady=1)

# ===================== LABEL CRIANÇAS =====================
# cria um label de seção Feminino
lblCrianca = Label(FrameABC3, text='Crianças', font=('arial', 20, 'bold'), padx=8, pady=1, bd=8, bg='yellow',
                   fg='black', width=25, justify=CENTER).grid(row=5, column=0, columnspan=4)

# cria um label de seção Vestidos
lblSkirts = Label(FrameABC3, text='Saias', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                  justify=LEFT).grid(row=6, column=0)

# cria um label de seção Vestidos
lblSwimwear = Label(FrameABC3, text='Natação', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                    justify=LEFT).grid(row=7, column=0)

# cria um label de seção Vestidos
lblSchoolUniform = Label(FrameABC3, text='Uniforme', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                         justify=LEFT).grid(row=8, column=0)

# cria um label de seção Vestidos
lblPyjamas = Label(FrameABC3, text='Pijama', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                   justify=LEFT).grid(row=9, column=0)

# ===================== CAIXAS DE TEXTO CRIANÇAS =====================
# cria uma caixa de texto Entry de seção Jeans Blusa
txtSkirts = Entry(FrameABC3, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=6,
                                                                                                          column=1,
                                                                                                          pady=1)

# cria uma caixa de texto Entry de seção Casaco
txtSwimwear = Entry(FrameABC3, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=7,
                                                                                                            column=1,
                                                                                                            pady=1)

# cria uma caixa de texto Entry de seção Roupa Sport
txtSchoolUniform = Entry(FrameABC3, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=8,
                                                                                                                 column=1,
                                                                                                                 pady=1)

# cria uma caixa de texto Entry de seção Vestidos
txtPyjamas = Entry(FrameABC3, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black', justify=LEFT).grid(row=9,
                                                                                                           column=1,
                                                                                                           pady=1)

# ===================== RECIBO =====================
textReceipt = Text(FrameABC5, height=23, width=37, bd=23, font=('arial', 9, 'bold'))
textReceipt.grid(row=0, column=0)

# ===================== BOTÕES =====================
btnTotal = Button(FrameABC6, padx=1, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, bg='orange',
                  text='Total').grid(row=0, column=0)

btnLimpar = Button(FrameABC6, padx=1, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, bg='yellow',
                   text='Limpar').grid(row=0, column=2)

btnSair = Button(FrameABC6, padx=1, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, bg='red',
                 text='Sair').grid(row=0, column=3)



root.mainloop()
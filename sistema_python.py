import time
from tkinter import *
from tkinter import messagebox

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

# # ===================== VARIÁVEIS =====================
Date1 = StringVar()
Time1 = StringVar()

Receipt_Ref = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()

Jeans_Jeggers = StringVar()
Coats_Jackets = StringVar()
Sportwear = StringVar()
Dresses = StringVar()
Skirts = StringVar()
Swimwear = StringVar()
School_Uniform = StringVar()
Pyjamas = StringVar()

Jackets_Blazers = StringVar()
Formal_Trousers = StringVar()
Formal_Shirts = StringVar()
Mens_Boots = StringVar()

Bed_Sheet = StringVar()
Pillows = StringVar()
Patterned_Bedding = StringVar()
Mattress_Protectors = StringVar()

# ====== setando as variáveis como 0 ======

Jeans_Jeggers.set('0')
Coats_Jackets.set('0')
Sportwear.set('0')
Dresses.set('0')
Skirts.set('0')
Swimwear.set('0')
School_Uniform.set('0')
Pyjamas.set('0')
Jackets_Blazers.set('0')
Formal_Trousers.set('0')
Formal_Shirts.set('0')
Mens_Boots.set('0')
Bed_Sheet.set('0')
Pillows.set('0')
Patterned_Bedding.set('0')
Mattress_Protectors.set('0')


Date1.set(time.strftime('%d/%m/%Y'))
Time1.set(time.strftime('%H:%M:%S'))


# ===================== FUNÇÕES DOS BOTÕES =====================
# botão sair
def Exit():
    result = messagebox.askquestion('rafasaid@gmail.com', 'Deseja realmente sair?')
    if result == 'yes':
        root.destroy()
        return


# botão limpar
def Reset():
    textReceipt.delete('1.0', END)
    Jeans_Jeggers.set('0')
    Coats_Jackets.set('0')
    Sportwear.set('0')
    Dresses.set('0')
    Skirts.set('0')
    Swimwear.set('0')
    School_Uniform.set('0')
    Pyjamas.set('0')
    Jackets_Blazers.set('0')
    Formal_Trousers.set('0')
    Formal_Shirts.set('0')
    Mens_Boots.set('0')
    Bed_Sheet.set('0')
    Pillows.set('0')
    Patterned_Bedding.set('0')
    Mattress_Protectors.set('0')


# botão total
def Total():
    Item1 = float(Jeans_Jeggers.get())
    Item2 = float(Coats_Jackets.get())
    Item3 = float(Sportwear.get())
    Item4 = float(Dresses.get())
    Item5 = float(Skirts.get())
    Item6 = float(Swimwear.get())
    Item7 = float(School_Uniform.get())
    Item8 = float(Pyjamas.get())
    Item9 = float(Jackets_Blazers.get())
    Item10 = float(Formal_Trousers.get())
    Item11 = float(Formal_Shirts.get())
    Item12 = float(Mens_Boots.get())
    Item13 = float(Bed_Sheet.get())
    Item14 = float(Pillows.get())
    Item15 = float(Patterned_Bedding.get())
    Item16 = float(Mattress_Protectors.get())

    PriceofItem1 = ('£') + str('%.2f' % (Item1 * 20.00))
    PriceofItem2 = ('£') + str('%.2f' % (Item2 * 18.00))
    PriceofItem3 = ('£') + str('%.2f' % (Item3 * 10.00))
    PriceofItem4 = ('£') + str('%.2f' % (Item4 * 15.00))
    PriceofItem5 = ('£') + str('%.2f' % (Item5 * 7.00))
    PriceofItem6 = ('£') + str('%.2f' % (Item6 * 11.00))
    PriceofItem7 = ('£') + str('%.2f' % (Item7 * 5.00))
    PriceofItem8 = ('£') + str('%.2f' % (Item8 * 8.00))
    PriceofItem9 = ('£') + str('%.2f' % (Item9 * 9.00))
    PriceofItem10 = ('£') + str('%.2f' % (Item10 * 30.00))
    PriceofItem11 = ('£') + str('%.2f' % (Item11 * 22.00))
    PriceofItem12 = ('£') + str('%.2f' % (Item12 * 25.00))
    PriceofItem13 = ('£') + str('%.2f' % (Item13 * 40.00))
    PriceofItem14 = ('£') + str('%.2f' % (Item14 * 3.00))
    PriceofItem15 = ('£') + str('%.2f' % (Item15 * 2.00))
    PriceofItem16 = ('£') + str('%.2f' % (Item16 * 31.00))




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
txtJeansBlusa = Entry(FrameABC2, textvariable=Jeans_Jeggers, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black',
                      justify=CENTER).grid(row=1,
                                                                                                              column=1,
                                                                                                              pady=1)

# cria uma caixa de texto Entry de seção Casaco
txtCoatsjackets = Entry(FrameABC2, textvariable=Coats_Jackets, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black',
                        justify=CENTER).grid(row=2,
                                                                                                                column=1,
                                                                                                                pady=1)

# cria uma caixa de texto Entry de seção Roupa Sport
txtSportwear = Entry(FrameABC2, textvariable=Sportwear, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black',
                     justify=CENTER).grid(row=3,
                                                                                                             column=1,
                                                                                                             pady=1)

# cria uma caixa de texto Entry de seção Vestidos
txtDresses = Entry(FrameABC2, textvariable=Dresses, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black',
                   justify=CENTER).grid(row=4,
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
txtSkirts = Entry(FrameABC2, textvariable=Skirts, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black',
                  justify=CENTER).grid(row=6,
                                                                                                          column=1,
                                                                                                          pady=1)

# cria uma caixa de texto Entry de seção Casaco
txtSwimwear = Entry(FrameABC2, textvariable=Swimwear, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black',
                    justify=CENTER).grid(row=7,
                                                                                                            column=1,
                                                                                                            pady=1)

# cria uma caixa de texto Entry de seção Roupa Sport
txtSchoolUniform = Entry(FrameABC2, textvariable=School_Uniform, font=('arial', 18, 'bold'), bd=2, bg='white',
                         fg='black', justify=CENTER).grid(row=8,
                                                                                                                 column=1,
                                                                                                                 pady=1)

# cria uma caixa de texto Entry de seção Vestidos
txtPyjamas = Entry(FrameABC2, textvariable=Pyjamas, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black',
                   justify=CENTER).grid(row=9,
                                                                                                           column=1,
                                                                                                           pady=1)

# ==================== FRAMEABC3 ===========================

# ===================== LABEL MASCULINO =====================
# cria um label de seção Feminino
lblMasculino = Label(FrameABC3, text='Masculino', font=('arial', 20, 'bold'), padx=8, pady=1, bd=8, bg='yellow',
                    fg='black', width=25, justify=CENTER).grid(row=0, column=0, columnspan=4)

# cria um label de seção Jeans Blusa
lblJackets_Blazers = Label(FrameABC3, text='Casacos', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                      justify=LEFT).grid(row=1, column=0)

# cria um label de seção Casaco
lblFormal_Trousers = Label(FrameABC3, text='Calças', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                        justify=LEFT).grid(row=2, column=0)

# cria um label de seção Roupa Sport
lblFormal_Shirts = Label(FrameABC3, text='Camisetas', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                     justify=LEFT).grid(row=3, column=0)

# cria um label de seção Vestidos
lblBoots = Label(FrameABC3, text='Botas', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                   justify=LEFT).grid(row=4, column=0)

# ===================== CAIXAS DE TEXTO MASCULINO =====================
# cria uma caixa de texto Entry de seção Jeans Blusa
txtJackets_Blazers = Entry(FrameABC3, textvariable=Jackets_Blazers, font=('arial', 18, 'bold'), bd=2, bg='white',
                           fg='black', justify=CENTER).grid(row=1,
                                                                                                              column=1,
                                                                                                              pady=1)

# cria uma caixa de texto Entry de seção Casaco
txtFormal_Trousers = Entry(FrameABC3, textvariable=Formal_Trousers, font=('arial', 18, 'bold'), bd=2, bg='white',
                           fg='black', justify=CENTER).grid(row=2,
                                                                                                                column=1,
                                                                                                                pady=1)

# cria uma caixa de texto Entry de seção Roupa Sport
txtFormal_Shirts = Entry(FrameABC3, textvariable=Formal_Shirts, font=('arial', 18, 'bold'), bd=2, bg='white',
                         fg='black', justify=CENTER).grid(row=3,
                                                                                                             column=1,
                                                                                                             pady=1)

# cria uma caixa de texto Entry de seção Vestidos
txtBoots = Entry(FrameABC3, textvariable=Mens_Boots, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black',
                 justify=CENTER).grid(row=4,
                                                                                                           column=1,
                                                                                                           pady=1)

# ===================== LABEL ROUPAS DE CAMA=====================
# cria um label de seção
lblroupas = Label(FrameABC3, text='Roupas de cama', font=('arial', 20, 'bold'), padx=8, pady=1, bd=8, bg='yellow',
                   fg='black', width=25, justify=CENTER).grid(row=5, column=0, columnspan=4)

# cria um label de seção Vestidos
lblBedSheet = Label(FrameABC3, text='Lençol', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                  justify=LEFT).grid(row=6, column=0)

# cria um label de seção Vestidos
lblPillows = Label(FrameABC3, text='Travesseiros', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                    justify=LEFT).grid(row=7, column=0)

# cria um label de seção Vestidos
lblPatternedBedding = Label(FrameABC3, text='Estampa', font=('arial', 18, 'bold'), bd=8, bg='green', fg='yellow',
                         justify=LEFT).grid(row=8, column=0)

# cria um label de seção Vestidos
lblMattressProtectors = Label(FrameABC3, text='Protetor colchão', font=('arial', 18, 'bold'), bd=8, bg='green',
                              fg='yellow',
                   justify=LEFT).grid(row=9, column=0)

# ===================== CAIXAS DE TEXTO ROUPAS =====================
# cria uma caixa de texto Entry de seção Jeans Blusa
txtBedSheet = Entry(FrameABC3, textvariable=Bed_Sheet, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black',
                    justify=CENTER).grid(row=6,
                                                                                                          column=1,
                                                                                                          pady=1)

# cria uma caixa de texto Entry de seção Casaco
txtPillows = Entry(FrameABC3, textvariable=Pillows, font=('arial', 18, 'bold'), bd=2, bg='white', fg='black',
                   justify=CENTER).grid(row=7,
                                                                                                            column=1,
                                                                                                            pady=1)

# cria uma caixa de texto Entry de seção Roupa Sport
txtPatteredBedding = Entry(FrameABC3, textvariable=Patterned_Bedding, font=('arial', 18, 'bold'), bd=2, bg='white',
                           fg='black', justify=CENTER).grid(row=8,
                                                                                                                 column=1,
                                                                                                                 pady=1)

# cria uma caixa de texto Entry de seção Vestidos
txtMattressProtectors = Entry(FrameABC3, textvariable=Mattress_Protectors, font=('arial', 18, 'bold'), bd=2, bg='white',
                              fg='black', justify=CENTER).grid(row=9,
                                                                                                           column=1,
                                                                                                           pady=1)

# ===================== RECIBO =====================
textReceipt = Text(FrameABC5, height=23, width=37, bd=23, font=('arial', 9, 'bold'))
textReceipt.grid(row=0, column=0)

# ===================== BOTÕES =====================
btnTotal = Button(FrameABC6, padx=1, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, bg='orange',
                  text='Total').grid(row=0, column=0)

btnLimpar = Button(FrameABC6, padx=1, pady=1, bd=4, fg='black', command=Reset, font=('arial', 16, 'bold'), width=7,
                   bg='yellow',
                   text='Limpar').grid(row=0, column=2)

btnSair = Button(FrameABC6, padx=1, pady=1, bd=4, fg='black', command=Exit, font=('arial', 16, 'bold'), width=7,
                 bg='red',
                 text='Sair').grid(row=0, column=3)



root.mainloop()
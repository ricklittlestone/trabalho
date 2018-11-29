from tkinter import *
from tkinter import Tk
class Carrinho(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Tela')
        self.geometry('350x350+175+175')
        self.transient(parent)
        self.grab_set()
        self.title('Especificações Carro')
        self.config(background='green')
        Label(self, text='Chevrolet Camaro 2018\nFicha Técnica:\n Ano=2018\nPlaca=OVS-1245\nModelo=Camaro\nCor=Amarelo').grid(row=0, column=2, padx=20, pady=10)

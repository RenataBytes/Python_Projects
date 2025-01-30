import tkinter as tk
from tkinter import LabelFrame, Button, Label, PhotoImage
import random

def escolheu_pedra():
    jokenpo(escolha_usuario='pedra')

def escolheu_papel():
    jokenpo(escolha_usuario='papel')

def escolheu_tesoura():
    jokenpo(escolha_usuario='tesoura')

def jokenpo(escolha_usuario):
    escolha_computador = random.choice(['pedra', 'papel', 'tesoura'])
    if escolha_usuario == escolha_computador:
        mensagem = f'''
Você: {escolha_usuario.upper()}
Eu: {escolha_computador.upper()}


Resultado: EMPATE!!

        '''
    elif(escolha_usuario == 'pedra' and escolha_computador == 'tesoura') \
            or (escolha_usuario == 'papel' and escolha_computador == 'pedra') \
            or (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        mensagem = f'''
Você: {escolha_usuario.upper()}
Eu: {escolha_computador.upper()}


Resultado: VOCÊ GANHOU!!

        '''
    else:
        mensagem = f'''
Você: {escolha_usuario.upper()}
Eu: {escolha_computador.upper()}

Resultado: EU VENCI!!
        '''

    resultado.config(text=mensagem)

#Conf da janela principal
janela = tk.Tk()

frame = LabelFrame(janela, text='Qual é a sua escolha?', padx=10, pady=10,fg='#000080', font=('Arial', 12, 'bold'))
frame.pack()


# Cargar imágenes correctamente
simbolo_pedra = PhotoImage(file='pedras.png')
simbolo_papel = PhotoImage(file='documento.png')
simbolo_tesoura = PhotoImage(file='tesoura.png')


# Asegurar que las imágenes se mantienen en memoria
janela.simbolo_pedra = simbolo_pedra
janela.simbolo_papel = simbolo_papel
janela.simbolo_tesoura = simbolo_tesoura

Button(frame, text='Pedra', fg='#8E4585', font=('Arial', 10, 'bold'), padx=10, pady=10, command=escolheu_pedra, image=simbolo_pedra, compound=tk.LEFT).grid(column=1, row=1)
Button(frame, text='Papel', fg='#8E4585', font=('Arial', 10, 'bold'), padx=10, pady=10, command=escolheu_papel, image=simbolo_papel, compound=tk.LEFT).grid(column=2, row=1)
Button(frame, text='Tesoura', fg='#8E4585', font=('Arial', 10, 'bold'), padx=10, pady=10, command=escolheu_tesoura, image=simbolo_tesoura, compound=tk.LEFT).grid(column=3, row=1)


resultado = Label(frame,padx=10, pady=10,fg='#000080', font=('Arial', 10, 'bold'), justify=tk.LEFT)
resultado.grid(column=0, row=2, columnspan=3)

janela.title('Pedra, Papel e Tesoura made by Renata d Almeida')
janela.geometry('500x200+700+200')
janela.mainloop()
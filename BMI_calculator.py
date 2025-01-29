import tkinter as tk
from tkinter import Frame, Label, Entry, Button

def calcula_imc():
    try:
        peso_valor = float(peso.get())  # Conversao do peso a float
        altura_valor = float(altura.get())  # Convertir a altura a float
        imc= peso_valor / (altura_valor ** 2)  # Calcular o IMC
        resultado['text']=f'O seu IMC é {imc:.2f}' #mostrar o IMC com 2 decimais
    except ValueError:
        resultado['text'] = "Por favor, introduza valores numéricos válidos."

janela = tk.Tk()
janela.configure(bg='#F5F5F5')  # Gris muy claro




frame = Frame(janela, padx=40, pady=40)
frame.configure(bg='#FFFFFF')   # Fondo blanco
frame.grid(column=1, row=1)

#Texto que aparece na janela
Label(frame, text='Para saber o seu IMC digite os seus valores mais abaixo', pady=40, fg='#8E4585', font=('Arial', 12, 'bold'),bg='#FFFFFF').grid(column=1, row=1, columnspan=2)

Label(frame, text='Qual é o seu peso em (Kg)?',fg='#000080', font=('Arial', 10, 'bold'),bg='#FFFFFF').grid(column=1, row=2)
peso = Entry(frame)
peso.grid(column=2, row=2)

Label(frame, text='Qual é a sua altura em (m)?', fg='#000080', font=('Arial', 10, 'bold'),bg='#FFFFFF').grid(column=1, row=3)
altura = Entry(frame)
altura.grid(column=2, row=3)

Button(frame, text='Calcular', command=calcula_imc).grid(column=2, row=4)
resultado = Label(frame, fg='#8E4585', font=('Arial', 12, 'bold'),bg='#FFFFFF')
resultado.grid(column=1, row=5, columnspan=2)

janela.title('Calculadora de IMC Renata d Almeida')
janela.mainloop()
import tkinter as tk
import datetime
import os
import time

def alarm():
    # Confirmar que o formato tempo ñ tem espaços
    set_alarm_time = f'{hour.get()}:{minute.get()}:{second.get()}'
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    print(current_time, set_alarm_time)
        
    if current_time == set_alarm_time:
        def play_sound():
            os.system('electronic.mp3')
        
    else:
        # Re-programar a funçao alarm() para que se execute depois de 1000 ms (1 segundo)
        root.after(1000, alarm)

# Para crear a janela
root = tk.Tk()
root.geometry('400x200')
root.title('Alarme Pythonico | Made by: Renata d Almeida ')

tk.Label(root, text='Alarme Pythonico', font=('Arial 20 bold'), fg='#000080').pack(pady=10)
tk.Label(root, text='Definir Alarme', font=('Arial 12 bold'), fg='#8E4585').pack(pady=5)

frame = tk.Frame(root)
frame.pack()

def option(value):
    opt = tk.StringVar(root)
    options = [str(i).zfill(2) for i in range(value)]
    opt.set(options[0])
    tk.OptionMenu(frame, opt, *options).pack(side=tk.LEFT)
    return opt

hour = option(24)
minute = option(60)
second = option(60)

tk.Button(root, text='Definir', font=('Arial 10 bold'), fg='#8E4585', command=lambda: root.after(1000, alarm)).pack(pady=20)

# Ejecutar a janela
root.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:28:11 2017

@author: igor.jaqueira
"""

import datetime
import time
import tkinter as tk
import datetime
from tkinter import ttk
import tkinter.simpledialog as inp
import tkinter.messagebox as out
import re


LARGE_FONT=("Verdana",12)
fonte=('times',30,'bold')


    
    
class Tempo():
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Contagem Regressiva para suas férias")
        self.root.configure(background='dark blue')
        
        self.texto = tk.Label(self.root,font=fonte,bg='dark blue',fg='white',
                              text='Tempo para suas férias:')
        self.texto.place(relx=0.5,rely=0.3,anchor='center')
            
        def close_window():
            self.root.destroy()

        def entra():
            ano=inp.askinteger('Ano','Por favor insira o ANO das suas férias',initialvalue='2017')
            mes=inp.askinteger('Mes','Por favor insira o MES das suas férias',initialvalue='12')
            dia=inp.askinteger('Dia','Por favor insira o DIA do mes das suas férias',initialvalue='22')
            hora=inp.askinteger('Horario de saída','Por favor insira o horário usual de saída do trabalho',initialvalue='19')

            tick(ano=ano,mes=mes,dia=dia,hora=hora)

        def tick(ano=int(2017),mes=int(12),dia=int(22),hora=int(19),time1=''):
            ano2=ano
            mes2=mes
            dia2=dia
            hora2=hora
            clock_frame = tk.Label(self.root,font=fonte,bg='dark blue',fg='white',relief='raised')
            #clock_frame.grid(row=5,column=2,columnspan=2,pady=5,padx=5)   
            clock_frame.place(relx=0.5,rely=0.5,anchor='center')  
            #Get current local time from the PC
            time0=datetime.datetime.now()
            time2=datetime.datetime(ano,mes,dia,hora)
            time3=time2-time0
            time4=str(time3)
            d=re.findall('[0-9]+',time4)
            time_format=str(d[0]+' Dia(s), ' + d[1]+' Hora(s), '+ d[2]+
            ' Minuto(s), '+ d[3]+' Segundo(s)')
            # if string has changed, update it
            if time3 != time1 :
                time1=time3
                clock_frame.config(text=time_format)
            # Calls itself every 200 ms to update
            clock_frame.after(1000,tick,ano2,mes2,dia2,hora2,time1)



        
        buttonframe=tk.Frame(self.root)
        buttonframe.configure(background='dark blue')
        buttonframe.place(relx=0.5,rely=0.7,anchor='center')       
    
        button=tk.Button(buttonframe, text="Iniciar", command=entra)
        button.grid(row=0, column=0,padx=15,pady=5,ipadx=10,ipady=5)
    
        button2=tk.Button(buttonframe, text="Sair", command=close_window)
        button2.grid(row=0, column=1,padx=15,pady=5,ipadx=10,ipady=5)
    
        
        
    


app=Tempo()
app.root.geometry("900x400")
app.root.mainloop()

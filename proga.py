
# def calculate_loan(principal, interest_rate, term):
#     n = term * 12
#     annuity = (principal * ((interest_rate * (1 + interest_rate) ** n)) / ((1 + interest_rate) ** n - 1))
#     monthly_payment = round(annuity, 2)
#     total_interest = round((monthly_payment * n - principal), 2)
#     return (monthly_payment, total_interest)
# result = calculate_loan(500000, 0.07, 20)
# print("Ежемесячный платеж:", result[0], "Общий процентный доход:", result[1])


# def is_odd(n):
#     return n % 2 != 0
# def is_even(n):
#     return n % 2 == 0

# data = [5, 1, 2, 4, 3, 6, 10, 8, 9]
# print(sorted(data, key= lambda n: n%2 != 0))

# class Item:
#     def __init__(self,price,brand):
#         self.price = price
#         self.brand = brand

#     def __repr__(self):
#         return self.brand

# item_list = [Item(100, "Apple"), Item(1200, "Apple"), Item(900, "Samsung"), Item(700, "Samsung"), Item(660, 'Xiaomi')]

# result = [item for item in item_list if item.brand == "Apple"]
# print(result)

# Импорты
import threading
import time
from gtts import gTTS
from math import sqrt
from ast import For
from secrets import choice
from xml.dom.minidom import Element
import pickle
import sys
import traceback
from datetime import datetime
from tkinter import *
import os
from random import *
import random
from PIL import Image, ImageTk
import os.path
from io import BytesIO
import speech_recognition as sr
import pyttsx3
from bs4 import BeautifulSoup as bs
import requests
import pathlib
from pathlib import Path
from tkinter import filedialog
import pygame
from tkinter import colorchooser
from playsound import playsound
import tkinter as tk
from tkinter import messagebox

pygame.init()
pygame.mixer.init()

global pag

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Основные комманды
def start():
    global photob
    global pag
    canvas.delete("all")
    try:
        pat = Path('backgrounds','bg.txt')
        f = open(pat, 'r')
        try:
            photob = PhotoImage(file=f.read(), width=800)
            canvas.create_image(0, 0, anchor = NW, image = photob)
            f.close()
        except:
             quiq()
    except FileNotFoundError:
        canvas.delete("all")
    canvas.create_line(20, 72, 790, 72, width=3, fill='white')
    pg1()
def exit():
    window.destroy()
    timer_clear()

def cls():
    global photob
    canvas.delete("all")
    rsound = [(Path('other', 'sound1.mp3')), (Path('other', 'sound2.mp3')), (Path('other', 'sound3.mp3'))]
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(random.choice(rsound)))
    try:
        pat = Path('backgrounds','bg.txt')
        f = open(pat, 'r')
        try:
            photob = PhotoImage(file=f.read(), width=800)
            canvas.create_image(0, 0, anchor = NW, image = photob)
            f.close()
        except:
             quiq()
    except FileNotFoundError:
        canvas.delete("all")
def sound():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound5.mp3')))
def quiq():
    pass

# Секретные коды
def good():
     global com
     Label(com,text='Успешно   ', font='Calibri 10').place(x=0, y= 39)
def bad():
     global com
     Label(com,text='Безусешно', font='Calibri 10').place(x=0, y= 39)

def commandone(): 
    global entrcom
    what = entrcom.get()
    if what == '0645':
        try:
            os.remove(path)
            os.remove(pathl)
            good()
        except:
             bad()
    elif what == '0752':
        try:
            cls()
            f = open('C:\\Program Files (x86)\\pas.text')
            f2 = open('C:\\Program Files (x86)\\log.text')
            f3 = open('C:\\Program Files (x86)\\cards.text')
            readtex = Label(text=f'Логин: {f2.read()} \nПароль: {f.read()} \nКарточки.. {f3.read()}', font='Arial 20', bg='#424242', fg='white',wraplength=770, justify=LEFT, borderwidth = 1,relief="sunken")
            canvas.create_window(10, 100, anchor=NW, window=readtex)
            good()
            f2.close()
            f.close()
        except:
             bad()
    elif what == '0195':
         try:
              os.remove('C:\\Program Files (x86)\\cards.text')
              good()
         except:
             bad()
    elif what == '1111':
        try:
            fon6()
            good()
        except:
            bad()
    elif what == '1234':
        try:
            os.remove(Path('backgrounds','bg.txt'))
            os.remove(Path('backgrounds','color.txt'))
            os.remove(Path('backgrounds','colornumbg.txt'))
            good()
        except:
            bad()
    elif what == '8900':
        try:
            fon6()
            good()
        except:
            bad()
    elif what == '8901':
        kn_dif()
    else:
        bad()
def comman():
    global com
    global entrcom
    com = Toplevel()
    com.bind('<Return>', lambda c: commandone())
    com.bind('<Escape>', lambda c: com.destroy())

    com.resizable(0,0)
    com.geometry('130x70')
    com.title('Ввод кода')
    entrcom = Entry(com, font='Calibri 20', width= 5)
    comdonebut = Button(com,text='ввод', font='Calibri 13',command=commandone)
    entrcom.place(x=0, y=0)
    entrcom.focus()
    comdonebut.place(x=74, y= 0)
 
    com.mainloop()

# Бинды
def unbind():
    window.unbind('1')
    window.unbind('2')
    window.unbind('3')
    window.unbind('4')
    window.unbind('5')
    window.unbind('<Return>')
    window.unbind('<KeyPress-Left>')
    window.unbind('<KeyPress-Right>')

def move_up(event):
    pygame.mixer.Channel(7).play(pygame.mixer.Sound(Path('other', 'sound9.mp3')))
    event.widget.tk_focusPrev().focus_set()
def move_down(event):
    pygame.mixer.Channel(7).play(pygame.mixer.Sound(Path('other', 'sound9.mp3')))
    event.widget.tk_focusNext().focus_set()

def allbind():
    window.bind('<KeyPress-Left>', lambda c: back())
    window.bind('<KeyPress-Right>', lambda c: next())
def bind1():
    window.bind('1', lambda c: age())
    window.bind('2', lambda c: chep())
    window.bind('3', lambda c: calc())
    window.bind('4', lambda c: ugch())
    allbind()
def bind2():
    window.bind('1', lambda c: game())
    window.bind('2', lambda c: urav())
    window.bind('3', lambda c: blocknot())
    window.bind('4', lambda c: mp3())
    window.bind('5', lambda c: readdone())
    allbind()
def bind3():
    window.bind('1', lambda c: val())
    window.bind('2', lambda c: fon())
    window.bind('3', lambda c: anekdot())
    window.bind('4', lambda c: fact_get())
    window.bind('5', lambda c: mus())
    allbind()
def bind4():
    window.bind('1', lambda c: alarm())
    window.bind('2', lambda c: timer())
    window.bind('3', lambda c: anekdot())
    window.bind('4', lambda c: fact_get())
    window.bind('5', lambda c: mus())
    allbind()

# Вход и регистрация
def withoutpas():   
    global password, name, warn
    try:
        warn.destroy()
    except:
        quiq()
    if str(name.get()) == '' or str(name.get())[0] == ' ':
        pygame.mixer.Channel(6).play(pygame.mixer.Sound(Path('other', 'sound11.mp3')))
        warn = Label(text='Для первого входа нужен логин', font='Calibri 15', relief=GROOVE, borderwidth=3, bg='#DEDEDE').place(x=0, y=152)
    else:
        pygame.mixer.Channel(6).play(pygame.mixer.Sound(Path('other', 'sound10.mp3')))
        f = open(path, 'w')
        fl = open(pathl, 'w')
        fl.write(name.get())
        f.write('•°☑')
        password.destroy()

def reg():
    global name, path, password, entpas, warn
    try:
        warn.destroy()
    except:
        quiq()

    if str(name.get()) == '' or str(name.get())[0] == ' ' or str(entpas.get()) == '' or str(entpas.get())[0] == ' ':
        pygame.mixer.Channel(6).play(pygame.mixer.Sound(Path('other', 'sound11.mp3')))
        warn = Label(text='Здесь не должно быть пустых мест', font='Calibri 15', relief=GROOVE, borderwidth=3, bg='#DEDEDE')
        warn.place(x=0, y=152)

    else:
        pygame.mixer.Channel(6).play(pygame.mixer.Sound(Path('other', 'sound10.mp3')))
        L = entpas.get()
        N = name.get()
        password.destroy()
        f = open(path,'w')
        f.write(L)
        f.close()
        fl = open(pathl, 'w')
        fl.write(N)
        fl.close()
def ent():
     global name
     f = open(path, 'r')
     fl = open(pathl, 'r')
     pasw = f.read()
     login = fl.read()
     if str(entpas.get()) == pasw and str(name.get()) == login:
          pygame.mixer.Channel(6).play(pygame.mixer.Sound(Path('other', 'sound10.mp3')))
          password.destroy()
     else:
          pygame.mixer.Channel(6).play(pygame.mixer.Sound(Path('other', 'sound11.mp3')))
          uncor = Label(text='Неверно!', font='Aria 20', fg = '#E80000', relief=GROOVE, borderwidth=3)
          uncor.place(x=219,y=110)
     f.close()
    
path ='C:\\Program Files (x86)\\pas.text'
pathl ='C:\\Program Files (x86)\\log.text'
try:
    try:
        global color
        pat = Path('backgrounds','color.txt')
        f = open(pat, 'r')
        color = f.read()
        # fonbg = f. readline(0)
        f.close()
    except FileNotFoundError:
        color = '#363636'

    f = open(path, 'r')
    if f.read() != '•°☑':
        (f.read())
        password = Tk()
        password.config(bg=color)
        password.geometry('350x200')
        password.resizable(0,0)
        password.protocol("WM_DELETE_WINDOW", quiq)
        password.title('Вход')

        name = Entry(width=9,font="Aria 20", relief=GROOVE, borderwidth=3)
        name.place(x=197,y=10)
        labnamepas = Label(text='Введите логин:', font='Aria 20', relief=GROOVE, borderwidth=3)
        labnamepas.place(x=0,y=10)

        entpas = Entry(width=8,font="Aria 20", relief=GROOVE, borderwidth=3)
        entpas.place(x=215,y=70)
        labpas = Label(text='Введите пароль:', font='Aria 20', fg='#464646', relief=GROOVE, borderwidth=3)
        labpas.place(x=0,y=70)

        name.focus()
        password.bind('<Return>', lambda c: ent())
        name.bind('<Down>', move_down)
        entpas.bind('<Up>', move_up)

        candon = Button(text="Готово↲", command=ent,font='Calibri 20', bg= '#0EE7F1', relief=RIDGE, borderwidth=2, activebackground='#0EE7F1')
        candon.place(x=0, y=140)
        password.mainloop()     
    f.close()
except FileNotFoundError:
    password = Tk()
    password.geometry('400x200')
    password.resizable(0,0)
    password.config(bg=color)
    password.protocol("WM_DELETE_WINDOW", quiq)
    password.title('Регистрация')

    name = Entry(width=9,font="Aria 20", relief=GROOVE, borderwidth=3)
    name.place(x=247,y=10)

    entpas = Entry(width=8,font="Aria 20", relief=GROOVE, borderwidth=3)
    entpas.place(x=266,y=70)

    labnamepas = Label(text='Придумайте логин:', font='Aria 20', relief=GROOVE, borderwidth=3)
    labnamepas.place(x=0,y=10)

    labpas = Label(text='Придумайте пароль:', font='Aria 20', fg='#464646', relief=GROOVE, borderwidth=3)
    labpas.place(x=0,y=70)

    candon = Button(text="Готово↲", command=reg,font='Calibri 15', bg= '#0EE7F1', activebackground='#0EE7F1', relief=RIDGE)
    candon.place(x=1, y=110)
    candon = Button(text="Входить без пароля ␛", command=withoutpas,font='Calibri 15', bg='#84FF4F', activebackground='#84FF4F', relief=RIDGE)
    candon.place(x=90, y=110)

    password.bind('<Return>', lambda c: reg())
    password.bind('<Escape>', lambda c: withoutpas())
    name.focus()
    name.bind('<Down>', move_down)
    entpas.bind('<Up>', move_up)

    password.mainloop()

countime = 0
timec = 0

def timec0():
    global timec
    timec = 0
# Дата и время
def time_change():
    datpl.destroy()
    todaypl.destroy()
    thistime()
    window.after(500, time_change)
def thistime():
    global datpl
    global todaypl
    global tim
    global dat, timecolor, timec

    dat = datetime.now()
    dat = dat.strftime('%H:%M:%S')

    datpl.destroy()
    todaypl.destroy()

    datpl= Label(text=dat, fg = timecolor, font=('Times New Roman', 15), bg = color)
    datpl.place(x=800,y=3, anchor=NE)


    today = datetime.today()
    today = today.strftime('%d/%m/%Y')

    todaypl = Label(text=today, fg = timecolor, font=('Times New Roman', 15), bg = color)
    todaypl.place(x=0, y=3)

    timealarms = f'{dat}\n'

    with open(Path('other', 'alarms.txt'), 'a') as alarm:
        with open(Path('other', 'alarms.txt'), 'r') as alarm:
            for tim in alarm:
                if tim == timealarms and timec != 1:
                    alarm_rang()
                    timec = 1
                    window.after(2000, timec0)

    window.after(1000, thistime)

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Кнопки
def buttons():
    global nextbut, backbut

    nextbut = Button(text=">", bg= "#6F6F6F", font= "Calibri 25",fg = "#EAEAEA",command=next, relief="ridge", borderwidth=3, activebackground="#6F6F6F", activeforeground="#EAEAEA")
    nextbut.place(x = 753, y = 34)

    backbut = Button(text="<", bg= "#6F6F6F", font= "Calibri 25",fg = "#EAEAEA",command=back, relief="ridge", borderwidth=3, activebackground="#6F6F6F", activeforeground="#EAEAEA")
    backbut.place(x = 3, y = 34)
def next():
    pygame.mixer.init()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound4.mp3')))
    pg1()
def back():
    pygame.mixer.init()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound4.mp3')))
    pg0()

def pg1():
    global pag, ageb, chepbut, calcbut, ugchbut, gamebut, uravbut, blockbut, mp3but, watchbut, bank, cast, anek, fac, music, alarmbut, timerbut, todaypl, datpl, timecolor
    
    pag += 1
    if pag == 4:
        pag = 0
    if pag == -1:
         pag = 3

    yb = 34

    clb()
    timecolor = "#3AFF32"

    forg = '#081A0E'

    thistime()
    if pag == 0:
        bind1()
        
        Welcome.config(fg="#3AFF32")
        timecolor = "#3AFF32"
        todaypl.config(fg="#3AFF32")
        datpl.config(fg="#3AFF32")

        ageb = Button(text="Возраст¹", bg= "#3AFF32", font= "Calibri 25",command=age, activebackground="#3AFF32", relief=RIDGE, fg = forg, activeforeground= forg)
        ageb.place(x = 47, y = yb)

        chepbut = Button(text="Чепуха²", bg= "#36DF30", font= "Calibri 25",command=chep, activebackground="#36DF30", relief=RIDGE, width=8, fg = forg, activeforeground= forg)
        chepbut.place(x = 187, y = yb)

        calcbut = Button(text="Калькулятор³", bg= "#2DC028", font= "Calibri 25",command=calc, activebackground="#2DC028", relief=RIDGE, width=12, fg = forg, activeforeground= forg)
        calcbut.place(x = 325, y = yb)

        ugchbut = Button(text="Угадать число⁴", bg= "#25A020", font= "Calibri 25",command=ugch, activebackground="#25A020", relief=RIDGE, width=13, fg = forg, activeforeground= forg)
        ugchbut.place(x = 532, y = yb)
    if pag == 1:
        bind2()

        Welcome.config(fg="#86FF32")
        timecolor = "#86FF32"
        todaypl.config(fg="#86FF32")
        datpl.config(fg="#86FF32")

        gamebut = Button(text="Игры¹", bg= "#86FF32", font= "Calibri 25",command=game, activebackground="#86FF32", relief="ridge", width= 6, fg = forg, activeforeground= forg)
        gamebut.place(x = 47, y = yb)

        uravbut = Button(text="Кв. уравн.²", bg= "#7CEB2E", font= "Calibri 25",command=urav, activebackground="#7CEB2E", relief="ridge", fg = forg, activeforeground= forg)
        uravbut.place(x = 157, y = yb)

        blockbut = Button(text="Блокнот³", bg= "#6FD12A", font= "Calibri 25",command=blocknot, activebackground="#6FD12A", relief="ridge", fg = forg, activeforeground= forg)
        blockbut.place(x = 328, y = yb)

        mp3but = Button(text="Озвучка⁴", bg= "#65BE27", font= "Calibri 25",command=mp3, activebackground="#65BE27", relief="ridge", fg = forg, activeforeground= forg)
        mp3but.place(x = 475, y = yb)

        watchbut = Button(text="Чтение⁵", bg= "#5AA923", font= "Calibri 25",command=readdone, activebackground="#5AA923", relief="ridge", fg = forg, activeforeground= forg)
        watchbut.place(x = 618, y = yb)
    if pag == 2:
        bind3()

        Welcome.config(fg="#3AFF64")
        timecolor = "#3AFF64"
        todaypl.config(fg="#3AFF64")
        datpl.config(fg="#3AFF64")

        bank = Button(text="Курс валют¹", bg= "#3AFF64", font= "Calibri 25",command=val, activebackground="#3AFF64", relief="ridge", fg = forg, activeforeground= forg)
        bank.place(x = 46, y = yb)

        cast = Button(text="Фон²", bg= "#35D158", font= "Calibri 25",command=fon, activebackground="#35D158", relief="ridge", fg = forg, activeforeground= forg)
        cast.place(x = 236, y = yb)

        anek = Button(text="Анекдоты³ ", bg= "#2DB84C", font= "Calibri 25",command=anekdot, activebackground="#2DB84C", relief="ridge", fg = forg, activeforeground= forg)
        anek.place(x = 329, y = yb)

        fac = Button(text="Факты⁴", bg= "#29A344", font= "Calibri 25",command=fact_get, activebackground="#29A344", relief="ridge", fg = forg, activeforeground= forg)
        fac.place(x = 504, y = yb)

        music = Button(text="Плеер⁵", bg= "#269940", font= "Calibri 25",command=mus, activebackground="#269940", relief="ridge", width=7, fg = forg, activeforeground= forg)
        music.place(x = 624, y = yb)
    if pag == 3:
        bind4()

        Welcome.config(fg="#3AFFA2")
        timecolor = "#3AFFA2"
        todaypl.config(fg="#3AFFA2")
        datpl.config(fg="#3AFFA2")
        
        alarmbut =  Button(text="Будильник¹", bg= "#3AFFA2", font= "Calibri 25",command=alarm, activebackground="#3AFFA2", relief="ridge", fg = forg, activeforeground= forg)
        alarmbut.place(x = 40, y = yb)

        timerbut = Button(text="Таймер²", bg= "#35DC8D", font= "Calibri 25",command=timer, activebackground="#35DC8D", relief="ridge", fg = forg, activeforeground= forg)
        timerbut.place(x = 219, y = yb)
    buttons()
def pg0():
    global pag
    pag -= 2
    pg1()

def clb():
    global ageb, chepbut, calcbut, ugchbut, gamebut, uravbut, blockbut, mp3but, watchbut, bank, cast, anek, fac, music, alarmbut, timerbut, nextbut, backbut

    canvasbutton.delete('all')

    try:
        nextbut.destroy()
        backbut.destroy()
    except:
        quiq()

    try: 
        ageb.destroy()
        chepbut.destroy()
        calcbut.destroy()
        ugchbut.destroy()
    except:
        quiq()

    try:
        gamebut.destroy()
        uravbut.destroy()
        blockbut.destroy()
        mp3but.destroy()
        watchbut.destroy()
    except:
        quiq()

    try:
        bank.destroy()
        cast.destroy()
        fac.destroy()
        anek.destroy()
        music.destroy()
    except:
        quiq()
    
    try:
        alarmbut.destroy()
        timerbut.destroy()
    except:
        quiq()
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Фон
def fon():
    global col
    global colorent
    cls()
    colodone = Button(text="Выбрать цвет", bg= "#0EE7F1", font= "Calibri 20", command=fondone, relief= RIDGE, borderwidth= 2, activebackground="#0EE7F1")
    canvas.create_window(10, 100, anchor=NW, window=colodone)

    colosbros = Button(text="Сброс", bg= "#FF3636", font= "Calibri 20",command=fonsbros, relief= RIDGE, borderwidth= 2, activebackground="#FF3636")
    canvas.create_window(185, 100, anchor=NW, window=colosbros)
#-------------------------------------------------------------------------------------------------
    colb = Button(text=" ", bg= "#F7F7F7", font= "Calibri 20",command=colset('white').set)
    canvas.create_window(400, 230, anchor=NW, window=colb, width= 40, height= 40)

    colb = Button(text=" ", bg= "black", font= "Calibri 20",command=colset('black').set)
    canvas.create_window(440, 230, anchor=NW, window=colb, width= 40, height= 40)

    colb = Button(text=" ", bg= "blue", font= "Calibri 20",command=colset('blue').set)
    canvas.create_window(400, 270, anchor=NW, window=colb, width= 40, height= 40)

    colb = Button(text=" ", bg= "#429EFF", font= "Calibri 20",command=colset('lblue').set)
    canvas.create_window(440, 270, anchor=NW, window=colb, width= 40, height= 40)

    colb = Button(text=" ", bg= "green", font= "Calibri 20",command=colset('green').set)
    canvas.create_window(400, 310, anchor=NW, window=colb, width= 40, height= 40)

    colb = Button(text=" ", bg= "lime", font= "Calibri 20",command=colset('lime').set)
    canvas.create_window(440, 310, anchor=NW, window=colb, width= 40, height= 40)

    colb = Button(text=" ", bg= "pink", font= "Calibri 20",command=colset('pink').set)
    canvas.create_window(400, 350, anchor=NW, window=colb, width= 40, height= 40)

    colb = Button(text=" ", bg= "purple", font= "Calibri 20",command=colset('purple').set)
    canvas.create_window(440, 350, anchor=NW, window=colb, width= 40, height= 40)

    colb = Button(text=" ", bg= "red", font= "Calibri 20",command=colset('red').set)
    canvas.create_window(400, 390, anchor=NW, window=colb, width= 40, height= 40)

    colb = Button(text=" ", bg= "yellow", font= "Calibri 20",command=colset('yellow').set)
    canvas.create_window(440, 390, anchor=NW, window=colb, width= 40, height= 40)
#-------------------------------------------------------------------------------------------------
    fgradb = Button(text="Свой фон", bg= "#195D8D", font= "Calibri 20",command= fon7, relief= RIDGE, borderwidth= 2, activebackground="#195D8D", width=18)
    canvas.create_window(10, 157, anchor=NW, window=fgradb)
    
    fgradb = Button(text="Градиент", bg= "#1F79B9", font= "Calibri 20",command= fon1, relief= RIDGE, borderwidth= 2, activebackground="#1F79B9", width=18)
    canvas.create_window(10, 214, anchor=NW, window=fgradb)

    fgradw = Button(text="Сферы", bg= "#2996E5", font= "Calibri 20",command=fon2, relief= RIDGE, borderwidth= 2, activebackground="#2996E5", width=18)
    canvas.create_window(10, 271, anchor=NW, window=fgradw)

    fpoints = Button(text="Точки", bg= "#31A9FF", font= "Calibri 20",command= fon3, relief= RIDGE, borderwidth= 2, activebackground="#31A9FF", width=18)
    canvas.create_window(10, 328, anchor=NW, window=fpoints)

    fsph = Button(text="Обратные сферы", bg= "#59BAFF", font= "Calibri 20",command=fon4, relief= RIDGE, borderwidth= 2, activebackground="#59BAFF", width=18)
    canvas.create_window(10, 385, anchor=NW, window=fsph)

    fvin = Button(text="Виньетка", bg= "#89CEFF", font= "Calibri 20",command=fon5, relief= RIDGE, borderwidth= 2, activebackground="#89CEFF", width=18)
    canvas.create_window(10, 442, anchor=NW, window=fvin)

    fvin = Button(text="Пусто", bg= "#B3DFFF", font= "Calibri 18",command=fonclear, relief= RIDGE, borderwidth= 2, activebackground="#B3DFFF", width=21)
    canvas.create_window(10, 499, anchor=NW, window=fvin)

def fondone():
    global Welcome
    global pag
    global canvas
    global color
    try:
        sound()
        pat = Path('backgrounds','color.txt')
        with open(pat, 'w') as f:
            color = colorchooser.askcolor()[1]
            f.write(color)
            f.close()

        Welcome.destroy()
        Welcome = Label(text= "И.Г.О.Р.Ь", fg= "#3AE99C", bg= color, font= "Corbel, 17", width=1000)
        Welcome.pack()

        canvas.destroy()
        canvas = Canvas(bg=color,height=600, width=800)
        canvas.pack()

        pag = 1
        pg1()
        buttons()
        fon()
    except:
        fonsbros()
def fonsbros():
    global Welcome
    global pag
    global canvas
    global color
    global colorent

    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound6.mp3')))
    os.remove(Path('backgrounds','color.txt'))

    color = '#363636'
    Welcome.destroy()
    Welcome = Label(text= "И.Г.О.Р.Ь", fg= "#3AE99C", bg= color, font= "Corbel, 17", width=1000)
    Welcome.pack()

    canvas.destroy()
    canvas = Canvas(bg=color,height=600, width=800)
    canvas.pack()

    pag = 1
    pg1()
    buttons()
    fon()

class Fonphot:
    def __init__(self,phot):
         self.phot = phot
    def goplace(self):
        global photob
        pat = Path('backgrounds','bg.txt')
        with open(pat, 'w') as f:
            f.write(f'{self.phot}')

        photob = PhotoImage(file=self.phot, width=800)
        canvas.create_image(0, 0, anchor = NW, image = photob)
def writecol():
    patcol = Path('backgrounds','colornumbg.txt')
    with open(patcol, 'w') as colnum:
        colnum.write(str(col))

def fon1():
    global col
    col = 1
    Fonphot(Path('backgrounds','gradient','black.png')).goplace()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound5.mp3')))
    writecol()
def fon2():
     global col
     col = 2
     Fonphot(Path('backgrounds','speres','black.png')).goplace()
     pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound5.mp3')))
     writecol()
def fon3():
     global col
     col = 3
     Fonphot(Path('backgrounds','points','black.png')).goplace()
     pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound5.mp3')))
     writecol()
def fon4():
    global col
    col = 4
    Fonphot(Path('backgrounds','backsperes','black.png')).goplace()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound5.mp3')))
    writecol()
def fon5():
     global col
     col = 5
     Fonphot(Path('backgrounds','vin','black.png')).goplace()
     pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound5.mp3')))
     writecol()
def fon6():
     global col
     col = 6
     Fonphot(Path('backgrounds','И.Г.О.Р.ь','black.png')).goplace()
     writecol()
def fon7():
    global col
    col = 7
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound5.mp3')))

    file_path = filedialog.askopenfilename(
        initialdir="\\",
        title="Выберите файл",
        filetypes=[("Изображение", ("*.png")), ("Все файлы", ("*"))]
    )
    # Если пользователь выбрал файл, изменяем его размер
    if file_path:
        image = Image.open(file_path)
        size = (800,600)
        resized_image = image.resize(size)
        resized_image.save(Path('backgrounds', 'image.png'))
        Fonphot(Path('backgrounds', 'image.png')).goplace()
        writecol()

class colset:
    global col
    def __init__(self, chvet):
          self.chvet = chvet
    def set(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound7.mp3')))
        try:
             global col
             patcolnum = Path('backgrounds','colornumbg.txt')
             with open(patcolnum, 'r') as colnum:
                  col = int(colnum.read())
        except:
             quiq()
        if col == 1:
            Fonphot(Path('backgrounds','gradient',f'{self.chvet}.png')).goplace()
        if col == 2:
            Fonphot(Path('backgrounds','speres',f'{self.chvet}.png')).goplace()
        if col == 3:
            Fonphot(Path('backgrounds','points',f'{self.chvet}.png')).goplace()
        if col == 4:
            Fonphot(Path('backgrounds','backsperes',f'{self.chvet}.png')).goplace()
        if col == 5:
            Fonphot(Path('backgrounds','vin',f'{self.chvet}.png')).goplace()
        if col == 6:
            Fonphot(Path('backgrounds','И.Г.О.Р.ь',f'{self.chvet}.png')).goplace()

def fonclear():
    global col
    col = 0
    patcolnum = Path('backgrounds', 'colornumbg.txt')
    patim = Path('backgrounds', 'image.png')
    pat = Path('backgrounds','bg.txt')
    try:
        os.remove(pat)
    except:
        quiq()
    
    try:
        os.remove(patim)
    except:
        quiq()

    try:
        os.remove(patcolnum)
    except:
        quiq()
    cls()
    fon()

# try:
#     global color
#     pat = Path('backgrounds','color.txt')
#     f = open(pat, 'r')
#     color = f.read()
#     # fonbg = f. readline(0)
#     f.close()
# except FileNotFoundError:
#     color = '#363636'

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Возраст
def agedone():
        bind1()

        today = datetime.today()
        today = today.strftime('%Y')

        fl = open(pathl,'r')
        im = fl.read()
        fl.close

        dat = int(today) - int(entry.get())
        label = Label(font= "Californian 25", text=f"{im}, Вам {entry.get()} лет! \n Вы родились в {dat} году", bg="#373737", fg="#FFFFFF", relief="sunken", borderwidth= 3)
        canvas.create_window(8, 135, anchor=NW, window=label)
def age():
    cls()
    global entry
    entry = Entry(width=5, font="Californian  30", relief= RIDGE, borderwidth= 3)
    canvas.create_window(275, 80, anchor=NW, window=entry,width=125, height=55)
    entry.focus_set()

    unbind()

    window.bind('<Return>', lambda c: agedone())

    agetext = Label(text="Ваш возраст:", font= "Perpetua 31", relief= RIDGE, borderwidth= 3)
    canvas.create_window(10, 80, anchor=NW, window=agetext)

    aged = Button(text="Готово↲", bg= "#0EE7F1", font= "Perpetua 20",command=agedone, relief= GROOVE, borderwidth= 2, activebackground="#0EE7F1")
    canvas.create_window(400, 80, anchor=NW, window=aged)

# Чепуха
def chepdone():
    cls()
    bind1()

    animals = [anim1.get(), anim2.get(), anim3.get()]
    descriptions = [desc1.get(), desc2.get(), desc3.get()]
    random_animals = random.sample(animals, len(animals))
    random_descriptions = random.sample(descriptions, len(descriptions))
    result = ""
    for i in range(len(random_animals)):
        result += f"{random_descriptions[i]} {random_animals[i]}\n"
    result_label = Label(text=result.lower(), font="Californian 30", bg=color, fg="#D3EEFF", relief="sunken", borderwidth=1, justify=LEFT)
    canvas.create_window(10, 80, anchor=NW, window=result_label)
    # def chepdone():
    #     cls()
    #     bind1()

    #     anim = [anim1.get(), anim2.get(), anim3.get()]
    #     desc = [desc1.get(), desc2.get(), desc3.get()]

        
    #     animd1 = Label(text=f"{choice(desc)} {choice(anim)}", font= "Calibri 30", fg= '#E359FF', bg=color, relief="sunken", borderwidth= 1)
    #     canvas.create_window(10, 112, anchor=NW, window=animd1)

    #     animd1 = Label(text=f"{choice(desc)} {choice(anim)}", font= "Calibri 30", fg= '#D202FC', bg=color, relief="sunken", borderwidth= 1)
    #     canvas.create_window(10, 192, anchor=NW, window=animd1)

    #     animd1 = Label(text=f"{choice(desc)} {choice(anim)}", font= "Calibri 30", fg= '#E359FF', bg=color, relief="sunken", borderwidth= 1)
    #     canvas.create_window(10, 272, anchor=NW, window=animd1)
def chep():
    cls()
    global color
    global anim1 
    global anim2
    global anim3
    global desc1
    global desc2
    global desc3

    unbind()
    window.bind('<Return>', lambda c: chepdone())

    anim1text = Label(text= 'Первое животное:',font= "Calibri 25", bg=color, fg= "#D3EEFF", relief="sunken", borderwidth= 1)
    canvas.create_window(10, 80, anchor=NW, window=anim1text)
    anim1 = Entry(font="Calibri 25",fg= "#D3EEFF",bg=color, relief="sunken", borderwidth= 2, )
    canvas.create_window(271, 79, anchor=NW, window=anim1, height=45,width=200)

    anim1.focus_set()

    anim2text = Label(text= 'Второе животное:',font= "Calibri 25", bg=color, fg= "#D3EEFF", relief="sunken", borderwidth= 1)
    canvas.create_window(10, 130, anchor=NW, window=anim2text)
    anim2 = Entry(width=4, font="Calibri 25",fg= "#D3EEFF",bg=color,border=0, relief="sunken", borderwidth= 2)
    canvas.create_window(266, 129, anchor=NW, window=anim2, height=45,width=205)

    anim3text = Label(text= 'Третье животное:',font= "Calibri 25", bg=color, fg= "#D3EEFF", relief="sunken", borderwidth= 1)
    canvas.create_window(10, 180, anchor=NW, window=anim3text)
    anim3 = Entry(width=5, font="Calibri 25",fg= "#D3EEFF",bg=color,border=0, relief="sunken", borderwidth= 2)
    canvas.create_window(262, 179, anchor=NW, window=anim3, height=45,width=208)

    desc1text = Label(text= 'Первое описание:',font= "Calibri 25", bg=color, fg= "#AADEFF", relief="sunken", borderwidth= 1)
    canvas.create_window(10, 250, anchor=NW, window=desc1text)
    desc1 = Entry(width=5, font="Calibri 25",fg= "#AADEFF",bg=color,relief="sunken", borderwidth= 2)
    canvas.create_window(267, 249, anchor=NW, window=desc1, height=45,width=202)

    desc2text = Label(text= 'Второе описание:',font= "Calibri 25", bg=color, fg= "#AADEFF", relief="sunken", borderwidth= 1)
    canvas.create_window(10, 300, anchor=NW, window=desc2text)
    desc2 = Entry(width=5, font="Calibri 25",fg= "#AADEFF",bg=color, relief="sunken", borderwidth= 2)
    canvas.create_window(263, 299, anchor=NW, window=desc2, height=45,width=206)

    desc3text = Label(text= 'Третье описание:',font= "Calibri 25", bg=color, fg= "#AADEFF", relief="sunken", borderwidth= 1)
    canvas.create_window(10, 350, anchor=NW, window=desc3text)
    desc3 = Entry(width=5, font="Calibri 25",fg= "#AADEFF",bg=color, relief="sunken", borderwidth= 2)
    canvas.create_window(259, 349, anchor=NW, window=desc3, height=45,width=209)

    chepbutton = Button(text="Готово↲", bg= "#0EE7F1", font= "Calibri 25",command=chepdone, relief= GROOVE, borderwidth= 2, activebackground="#0EE7F1")
    canvas.create_window(5, 400, anchor=NW, window=chepbutton)

    anim1.bind("<Down>", move_down)
    anim2.bind("<Up>", move_up)
    anim2.bind("<Down>", move_down)
    anim3.bind("<Up>", move_up)
    anim3.bind("<Down>", move_down)
    desc1.bind("<Up>", move_up)
    desc1.bind("<Down>", move_down)
    desc2.bind("<Up>", move_up)
    desc2.bind("<Down>", move_down)
    desc3.bind("<Up>", move_up)

# Калькулятор
def add_digit(digit):
    value = calcent.get()
    if value[0] == "0" and len(value) == 1:
        value= value [1:]
    calcent.delete(0,END)
    calcent.insert(0,value+digit)
def add_operation(operation):
    value = calcent.get()
    if value[-1] in "-+/*":
        value = value[:-1]
    elif "+" in value or "*" in value or "/" in value or "-" in value:
        calculat()
        value = calcent.get()
    calcent.delete(0,END)
    calcent.insert(0,value+operation)
def calculat():
    value = calcent.get()
    if value[-1] in "+-*/":
        value = value + value[:-1]
    if value[-1] in "0" and value[-2] in "/":
        value = '0'
    calcent.delete(0,END)
    calcent.insert(0,eval(value))
def clear():
    calcent.delete(0,END)
    calcent.insert(0,0)
def mdb(digit):
    return Button(text=digit, bd=5,font=('Arial',15), command=lambda : add_digit(digit))
def mob(operation):
    return Button(text=operation, bd=5,font=('Arial',15), command=lambda : add_operation(operation), fg="#1F77FF")
def mсb(operation):
    return Button(text=operation, bd=5,font=('Arial',15), command=calculat, fg="#F46B6B")
def mсlb(operation):
    return Button(text=operation, bd=5,font=('Arial',15), command=clear, fg="#FE8E00")

def calc():
    cls()
    global calcent
    global canvas

    unbind()

    calcent = Entry(window,justify=RIGHT, font= ("Arial",25), width=15)
    calcent.insert(0,"0")
    canvas.create_window(240, 210-40, window=calcent,width=288, height=55)

    canvas.create_window(130, 276-40, window=mdb("1"),width=70, height=70)
    canvas.create_window(203, 276-40, window=mdb("2"),width=70, height=70)
    canvas.create_window(276, 276-40, window=mdb("3"),width=70, height=70)
    canvas.create_window(130, 347-40, window=mdb("4"),width=70, height=70)
    canvas.create_window(203, 347-40, window=mdb("5"),width=70, height=70)
    canvas.create_window(276, 347-40, window=mdb("6"),width=70, height=70)
    canvas.create_window(130, 418-40, window=mdb("7"),width=70, height=70)
    canvas.create_window(203, 418-40, window=mdb("8"),width=70, height=70)
    canvas.create_window(276, 418-40, window=mdb("9"),width=70, height=70)
    canvas.create_window(203, 489-40, window=mdb("0"),width=70, height=70)
    canvas.create_window(349, 347-40, window=mob('+'),width=70, height=70)
    canvas.create_window(349, 276-40, window=mob('-'),width=70, height=70)
    canvas.create_window(349, 418-40, window=mob('*'),width=70, height=70)
    canvas.create_window(349, 489-40, window=mob('/'),width=70, height=70)
    canvas.create_window(130, 489-40, window=mсlb("C"),width=70, height=70)
    canvas.create_window(276, 489-40, window=mсb("="),width=70, height=70)

# Угадать число
def cardone():
    fl = open(pathl,'r')
    im = fl.read()
    fl.close

    unbind()
    bind1()

    file = open('C:\\Program Files (x86)\\cards.text', 'a', encoding= 'utf-8')
    file.write(f'\n{im} - Номер: {ent1.get()}, Имя: {ent2.get()}, Срок действия: {ent3.get()}, Три цифры: {ent4.get()}')
    file.close()
def ugchdone():
    global popitka
    global popit
    global chis
    global photocart
    global ent1     
    global ent2   
    global ent3 
    global ent4

    for i in range (popitka):
        if int(chis.get()) == rand:
            cls()
            win = Label(text=f"Ты победил за {ost - popitka + 1} попыток!", font="Arial 40", bg=color, fg='#5FFF42', relief="sunken", borderwidth= 2)
            canvas.create_window(10, 100, anchor=NW, window=win)

            card = Label(text=f"Введите данные своей карты и получите денежный приз", font="Arial 21", bg=color, fg='#009BFF', relief="sunken", borderwidth= 2)
            canvas.create_window(10, 180, anchor=NW, window=card)

            photocart = PhotoImage(file=(Path('other','bank.png')))
            canvas.create_image(400, 370, image=photocart)


            ent1 = Entry(width=16, font= 'Arial 16')
            canvas.create_window(40, 350, anchor=NW, window=ent1)
            ent2 = Entry(width=25, font= 'Arial 16')
            canvas.create_window(35, 445, anchor=NW, window=ent2)
            ent3 = Entry(width=5, font= 'Arial 16')
            canvas.create_window(300, 400, anchor=NW, window=ent3)
            ent4 = Entry(width=3, font= 'Arial 16')
            canvas.create_window(695, 342, anchor=NW, window=ent4)
            
            window.bind('<Return>', lambda c: cardone())

            ugchd = Button(text="Готово↲", bg= "#0EE7F1", font= "Calibri 20",command=cardone, relief= GROOVE, borderwidth= 2, activebackground="#0EE7F1")
            canvas.create_window(10, 500, anchor=NW, window=ugchd)
        if int(chis.get()) != rand:
            sound()
            loose = Label(text=f"НЕТ!", font="Arial 25", bg=color, fg='#FF0000', relief="sunken", borderwidth= 2)
            canvas.create_window(8, 270, anchor=NW, window=loose)
            popitka = popitka - 1
            chis.delete(0, END)
            popit = Label(text=f"У тебя {popitka} попыток", font="Arial 25", bg=color, fg='#C5FF84', relief="sunken", borderwidth= 4)
            canvas.create_window(10, 100, anchor=NW, window=popit)
            if popitka == 0:
                cls()
                bind1()
                gameov = Label(text=f"Игра окончена, ты проиграл!", font="Arial 40", bg=color, fg='#FF0000', relief="sunken", borderwidth= 2)
                canvas.create_window(10, 100, anchor=NW, window=gameov)
def ugch():
    cls()

    unbind()
    
    global ost
    global popit
    global popitka
    global chis
    global rand
    rand = randint(1, 5)
    popitka = int(randint(1, 4))
    ost = popitka
    play = Label(text=f"Я загадал число от 1 до 5 попробуй его отгадать:", font="Arial 25", relief= RIDGE, borderwidth= 3)
    canvas.create_window(10, 150, anchor=NW, window=play)
    popit = Label(text=f"У тебя {popitka} попыток", font="Arial 25", bg=color, fg='#C5FF84', relief="sunken", borderwidth= 4)
    canvas.create_window(10, 100, anchor=NW, window=popit)

    chis = Entry(width=1, font="TimesNewRoman 50")
    canvas.create_window(10, 200, anchor=NW, window=chis)
    chis.focus_set()

    window.bind('<Return>',lambda c: ugchdone())

    ugchd = Button(text="Готово↲", bg= "#0EE7F1", font= "Calibri 25",command=ugchdone, relief= GROOVE, borderwidth= 2, activebackground="#0EE7F1")
    canvas.create_window(52, 200, anchor=NW, window=ugchd)



# Игры
def game():
    global window_m
    global img
    global igs
    global image
    global images
    global imas
    global imgsa
    global imgphot

    unbind()
    bind2()

    window_m = Toplevel()
    cls()
    pg = 1

    icon = PhotoImage(file = Path('icons','game.png'))
    window_m.iconphoto(False, icon)

    window_m.geometry('800x600')
    window_m.title('Игры ИГОРя')
    canvas_m = Canvas(window_m, width = 800, height = 600, bg='#1f1f1f' )
    # canvas_m.pack()
    window_m.resizable(0,0)

    choose = Label(window_m,text = 'Выберите игру', fg= '#1e589e', font= 'Arial 40', bg = '#f2e6f7')
    choose.place(x=220, y = 30)

    igs = PhotoImage(file = (Path('games','mbg.png')))
    imas = canvas_m.create_image(0, 0, anchor='nw',image=igs)


    but1 = Button(window_m,text='Играть',background= '#189DFF', width= 11, height= 1, font= 'Arial 20', command= tennis_dif)
    but1.place(x = 20, y = 370 )

    imgs = PhotoImage(file = (Path('games','balls.png')))
    images = canvas_m.create_image(7, 432, anchor='nw',image=imgs)
    

    but2 = Button(window_m,text='Играть',background= '#189DFF', width= 11, height= 1, font= 'Arial 20', command= tictactoemod)
    but2.place(x = 600, y = 370 )

    img = PhotoImage(file = (Path('games','tttoe.png')))
    image = canvas_m.create_image(577, 432, anchor='nw',image=img)
    canvas_m.grid(row=2,column=2)


    but3 = Button(window_m,text='Играть',background= '#189DFF', width= 11, height= 1, font= 'Arial 20', command= alhimsave)
    but3.place(x = 20, y = 70 )

    imgsa = PhotoImage(file = (Path('games','alhim.png')))
    canvas_m.create_image(7, 132, anchor='nw',image=imgsa)

    but4 = Button(window_m,text='Играть',background= '#189DFF', width= 11, height= 1, font= 'Arial 20', command= photorob)
    but4.place(x = 600, y = 70 )

    imgphot = PhotoImage(file = (Path('games','photorobot.png')))
    canvas_m.create_image(577, 132, anchor='nw',image=imgphot)
    # , command= tennis_dif
    # , command= d = 1

    
    canvas_m.pack()
    window_m.mainloop()

# Теннис
def tennis_dif():
     global window_m
     global tendif
     global counter
     window_m.destroy()
     tendif = Toplevel()
     sound()

     icon = PhotoImage(file = Path('icons','diff.png'))
     tendif.iconphoto(False, icon)

     tendif.geometry('475x200')
     tendif.resizable(1,0)
     canvas_tendif = Canvas
     tendif.title('Выбор сложности')

     tendif.focus_force()

     textdif = Label(tendif, text = 'Выберите сложность', fg= '#1e589e', font= 'Arial 20')
     textdif.pack()

     canvas_tendif = Canvas(tendif, width = 100000, height = 100000, bg='#6C92AF', relief=RIDGE, borderwidth= 3)
     canvas_tendif.pack()

     but_ten_easy = Button(tendif, text=' лёгкая¹', bg= '#77DD77', font='TimesNewRoman 25', command=teasy, activebackground="#77DD77", relief=RIDGE)
     but_ten_easy.place(x = 5, y = 41)

     but_ten_normal = Button(tendif, text=' средняя²', bg= '#DCD36A', font='TimesNewRoman 25', command= tnormal, activebackground="#DCD36A", relief=RIDGE)
     but_ten_normal.place(x = 148, y = 41)

     but_ten_hard = Button(tendif, text='сложная³', bg= '#DD9475', font='TimesNewRoman 25', command= thard, activebackground="#DD9475", relief=RIDGE)
     but_ten_hard.place(x = 318, y = 41)

     but_ten_impossible = Button(tendif, text='невозможная⁴', bg= '#D60010', font='TimesNewRoman 25', command= timpossible, activebackground="#D60010", relief=RIDGE)
     but_ten_impossible.place(x = 473, y = 41)

     but_exit = Button(tendif, text='выйти ␛', bg= '#B88FEF', font='TimesNewRoman 15', command= tendif.destroy, activebackground="#B88FEF", relief=RIDGE)
     but_exit.place(x = 3, y = 158)

     tendif.bind('1', lambda c:teasy())
     tendif.bind('2', lambda c:tnormal())
     tendif.bind('3', lambda c:thard())
     tendif.bind('4', lambda c:timpossible())
     tendif.bind('<Escape>', lambda c: tendif.destroy())

     tendif.mainloop()

     global counter
     counter = 0
     global dif
     dif = 3
     tennis()

def teasy():
     global counter
     counter = 0
     global dif
     dif = 0
     tennis()
def tnormal():
     global counter
     counter = 0
     global dif
     dif = 1
     tennis()
def thard():
     global counter
     counter = 0
     global dif
     dif = 2
     tennis()
def timpossible():
     global counter
     counter = 0
     global dif
     dif = 3
     tennis()

def ten_destroy():
    global windowt
    windowt.destroy()
    pygame.mixer.Channel(0).stop()
def tennis_sounds():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('games', 'tennis', 'sound1.mp3')))

def tennis():
    global windowt
    global countmus
    global tendif
    global bg_photo
    tendif.destroy()

    pygame.mixer.Channel(0).play(pygame.mixer.Sound(Path('games', 'tennis', 'bgmusic.mp3')), -1)

    if dif == 0:
        positspeed = [2,1]
    if dif == 1:
        positspeed = [2,3]
    if dif == 2:
        positspeed = [3,4, -4,5]
    if dif == 3:
        positspeed = [5, 8, 7, 6]
    
    bg_photo = PhotoImage(file=(Path('games','tennis','tenbg.png')))

    class Ball:
        # Конструктор шара
        def __init__(self, canvas, color, platform):
                self.canvas = canvas
                # СОздаём шар с заданными параметрами
                self.oval = canvas.create_oval(200, 200, 215, 215, fill = color)
                if dif == 0:
                    self.speeds = [-2, -1, 1, 2]
                if dif == 1:
                    self.speeds = [-3, -2, 2, 3]
                if dif == 2:
                    self.speeds = [-3, 3, -4, 4, -4.5]
                if dif == 3:
                    self.speeds = [-5, 5, 8, -7, -6, 6, 7, -8, 9, -9]
                if dif == -1:
                     self.speeds = [-1, 1]
                self.platform = platform
                # Параметр положения по оси x и y
                self.x = random.choice(self.speeds)
                self.y = -1
                # Параметр проверки коснулся ли шарик дна
                self.t_bottom = False

        # Метод отрисовки шара
        def draw(self):
                self.canvas.move(self.oval, self.x, self.y)
                # Проверка выхода шарика за границы окна
                #----------------------------
                # Получаем координаты шарика(Метод коордс возращает 4 числа)
                pos= self.canvas.coords(self.oval)
                # Проверка координаты x0
                # if pos[0] <= 0:
                #         self.x = 1
                # if pos[1] <= 0:
                #         self.y = 1
                # if pos[2] >= 500:
                #         self.x = -1
                # if pos[3] >= 400:
                #         self.y = -1

                if pos[0] <= 0:
                        tennis_sounds()
                        if self.x < 0:
                            self.x = random.choice(positspeed)
                        if self.x > 0:
                            self.x = - random.choice(positspeed)
                        self.x = - self.x
                if pos[1] <= 0:
                        tennis_sounds()
                        self.y = - self.y
                if pos[2] >= 500:
                        tennis_sounds()
                        if self.x < 0:
                            self.x = random.choice(positspeed)
                        if self.x > 0:
                            self.x = - random.choice(positspeed)
                if pos[3] >= 400:
                        self.t_bottom = True

                if self.tp (pos) == True:
                        self.y = - 1

        # Проверка столкновения шарика и платформы
        def tp(self,ball_pos):
                # Получаем координаты платформы
                platform_pos = self.canvas.coords(self.platform.rect)

                if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
                        if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                                global counttext
                                global counter
                                counter += 1

                                pygame.mixer.music.load(Path('games', 'tennis', 'sound2.mp3'))
                                pygame.mixer.music.play(0)

                                counttext.destroy()
                                counttext = Label(holst, text= (f'{counter}/10'), font= 'Calibri 40')
                                counttext.place(x = 0 , y = 350)
                                return True
                return False

    # Создаём класс платформа
    class Platform:
            def __init__(self, canvas, color):
                    self.canvas = canvas
                    # СОздаём прямоугольник с заданными параметрами
                    self.rect = canvas.create_rectangle(230, 300, 330, 310, fill = color)
                    self.x = 0

                    # Кнопки для движения
                    self.canvas.bind_all('<KeyPress-Left>',self.left)
                    self.canvas.bind_all('<KeyPress-Right>',self.right)

            def right(self, event):
                    self.x = 2
            def left(self, event):
                    self.x = -2

            # Метод отрисовки платформы
            def draw(self):
                    self.canvas.move(self.rect, self.x, 0)
                    pos= self.canvas.coords(self.rect)
                    if pos[0] <= 0:
                            pygame.mixer.music.load(Path('games', 'tennis', 'sound3.mp3'))
                            pygame.mixer.music.play(0)
                            self.x = 2
                    if pos[2] >= 500:
                            pygame.mixer.music.load(Path('games', 'tennis', 'sound3.mp3'))
                            pygame.mixer.music.play(0)
                            self.x = -2

    colis = 0

    width = 500
    height = 404

    global counter

    windowt = Toplevel()
    windowt.title('Аркада')
    windowt.geometry(f'{width}x{height}')
    windowt.protocol("WM_DELETE_WINDOW", ten_destroy)
    icon = PhotoImage(file = Path('icons','tennis.png'))
    windowt.iconphoto(False, icon)
    windowt.focus_force()
    # Фиксируем размеры окна по x и y
    windowt.resizable(0,0)

    countmus = 1

    while countmus == 1:
        countmus = 0
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(Path('games', 'tennis', 'bgmusic.mp3')), -1)

    # Создаём холст для отображение объектов игры
    holst = Canvas(windowt, width= 500, height= 400)
    holst.create_image(252,200,image=bg_photo)

    but_exit = Button(windowt, text='выйти ␛', bg= '#B88FEF', font='TimesNewRoman 12', activebackground="#B88FEF", relief=RIDGE, command= ten_destroy)
    but_exit.place(x = 420, y = 370)

    global counttext
    counttext = Label(holst, text= '0/10', font= 'Calibri 40')
    counttext.place(x = 0 , y = 350)

    holst.pack()
    
    platform = Platform(canvas= holst, color= '#272727')

    # Создаём объект класса Ball
    ball = Ball(canvas = holst, color= '#DF093A', platform = platform)

    windowt.bind('<Escape>', lambda c: ten_destroy())

    # Создаём основной цикл игры
    while True:
            if counter == 10:
                holst.delete('all')
                holst.create_text(width/2, height/2, text= 'Ты выиграл', font= 'Arial 50', fill = '#36E738')
                pygame.mixer.Channel(0).stop()

            # Проверка, что коснулись дна
            if ball.t_bottom == False:
            # Отрисовываем шар
                    ball.draw()
                    # Отрисовываем платформу
                    platform.draw()
            else:
                    # holst.delete('all')
                    counttext.destroy()
                    holst.create_text(width/2, height/2, text= 'Ты проиграл', font= 'Arial 50', fill = '#D40808')
                    pygame.mixer.Channel(0).stop()
            windowt.update()
            time.sleep(0.01)

# Рыцарь
def kn_dif():
    #  global window_m
    #  window_m.destroy()
     sound()
     global kndif
     global iconk
     kndif = Toplevel()
     kndif.geometry('475x200')
     kndif.resizable(1,0)
     kndif.focus_force()
     canvas_tendif = Canvas
     kndif.title('Выбор сложности')

     iconk = PhotoImage(file = Path('icons','diff.png'))
     kndif.iconphoto(False, iconk)

     textdif = Label(kndif, text = 'Выберите сложность', fg= '#1e589e', font= 'Arial 20')
     textdif.pack()

     canvas_tendif = Canvas(kndif, width = 100000, height = 100000, bg='#6C92AF', relief=RIDGE, borderwidth= 3)
     canvas_tendif.pack()

     but_ten_easy = Button(kndif, text=' лёгкая¹', bg= '#77DD77', font='TimesNewRoman 25',command= keasy, activebackground="#77DD77", relief=RIDGE)
     but_ten_easy.place(x = 5, y = 41)

     but_ten_normal = Button(kndif, text=' средняя²', bg= '#DCD36A', font='TimesNewRoman 25', command= knormal, activebackground="#DCD36A", relief=RIDGE)
     but_ten_normal.place(x = 148, y = 41)

     but_ten_hard = Button(kndif, text='сложная³', bg= '#DD9475', font='TimesNewRoman 25', command= khard, activebackground="#DD9475", relief=RIDGE)
     but_ten_hard.place(x = 318, y = 41)

     but_ten_impossible = Button(kndif, text='невозможная⁴', bg= '#D60010', font='TimesNewRoman 25', command= kimpossible, activebackground="#D60010", relief=RIDGE)
     but_ten_impossible.place(x = 473, y = 41)

     but_exit = Button(kndif, text='выйти ␛', bg= '#B88FEF', font='TimesNewRoman 15', command= kndif.destroy, activebackground="#B88FEF", relief=RIDGE)
     but_exit.place(x = 3, y = 158)

     kndif.bind('1', lambda c:keasy())
     kndif.bind('2', lambda c:knormal())
     kndif.bind('3', lambda c:khard())
     kndif.bind('4', lambda c:kimpossible())
     kndif.bind('<Escape>', lambda c: kndif.destroy())

     kndif.mainloop()

def keasy():
     global kdif
     kdif = 0
     knight()
def knormal():
     global kdif
     kdif = 1
     knight()
def khard():
     global kdif
     kdif = 2
     knight()
def kimpossible():
     global kdif
     kdif = 3
     knight()

def equel(dif, txtname):
          global rec
          if kdif == dif:
            try:
                with open(Path('games', 'knight', txtname), 'r') as f:
                    fdif = f.read()
                    if int(fdif) > kill:
                        rec = int(fdif)
                    if int(fdif) < kill:
                        with open(Path('games', 'knight', txtname), 'w') as f:
                            f.write(str(rec))
                            rec = kill
            except:
                with open(Path('games', 'knight', txtname), 'w') as f:
                    rec = kill
                    f.write(str(rec))

def knclose():
    global windowk
    windowk.destroy()
    pygame.mixer.Channel(0).stop()
    equel(0, 'easy.txt')
    equel(1, 'normal.txt')
    equel(2, 'hard.txt')
    equel(3, 'impossible.txt')

def knight():
    global kndif, kill, counkn, textcoun, muscoun, windowk
    kndif.destroy()
    global bg_photo
    global knightph
    global dragph
    windowk = Toplevel()

    icon = PhotoImage(file = Path('icons','knight.png'))
    windowk.iconphoto(False, icon)

    knightph = PhotoImage(file= (Path('games','knight','knight.png')))
    dragph = PhotoImage(file= (Path('games','knight','dragon.png')))
    windowk.wm_attributes('-topmost', 1)
    windowk.focus_force()
    windowk.title('Рыцарь')
    windowk.resizable(0, 0)
    windowk.protocol("WM_DELETE_WINDOW",knclose)
    # Переменные для высоты и ширины
    w = 600
    h = 600

    kill = 0
    muscoun = 0

    # Размеры
    windowk.geometry(f'{w}x{h}')

    # Холст для игрового поля фотки
    canvask = Canvas(windowk, width = w, height = h)

    # Распологаем холст на оке
    canvask.place(in_=windowk,x =-2, y= 0)

    # Картинку на холст
    bg_photo = PhotoImage(file= (Path('games','knight','bgk.png')))
    
    counkn = 0
    
    # Рыцарь класс
    class Knight:
            # Конструктор класса
            def __init__(self):
                    # Положение рыцаря
                    self.x = 70
                    self.y = h // 2
                    # Скорость
                    self.v = 0
                    # Изображение
                    self.photo = knightph

            # Перемещение вверх
            def up(self, event):
                    self.v = -3
                    if self.y < 64:
                        self.y = 64
            # Перемещение вниз
            def down(self, event):   
                    self.v = 3
                    if self.y > 531:
                        self.y = 531
            # Остановка
            def stop(self, event):   
                    self.v = 0

    def music():
        if muscoun == 0:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(Path('games', 'knight', 'sound3.mp3')))
            windowk.after(8700, music)
    music()

    vlist = []
    vlistinf = []
    if kdif == 0:
        speed = 5
    if kdif == 1:
        speed = 9
    if kdif == 2:
        speed = 14
    if kdif == 3:
        speed = 18
    for i in range (1, speed):
        vlist.append(i)
        vlistinf.append(i)
        i += 1

    # Дракон класс
    class Dragon:
            # Конструктор
            def __init__(self):
                    # Положение дракона
                    self.y = random.randint(100,400)
                    # Скорость
                    if len(vlist) > 1:
                        self.v = random.choice(vlist)
                        vlist.remove(self.v)
                    else:
                        vlist[1:1] = vlistinf
                        self.v = random.choice(vlist)
                        vlist.remove(self.v)
  
                    if self.v >= 6:
                        randel = random.randint(2, 7)
                        self.v = self.v/randel
                        self.x = 1100 * self.v + (self.y*random.randint(2,6))
                    else:
                        siz = 1
                        self.x = 1100 - (self.v*100)
                    
                    
                    # Изображение
                    if kdif == 1:
                        siz = (random.randint(1, 2)) 
                        self.photo = dragph.zoom(siz, siz)
                    if kdif > 1:
                        siz = (random.randint(1, 3)) 
                        self.photo = dragph.zoom(siz, siz)
                    else:
                        self.photo = dragph

    def killcoun():
        global kill
        try:
            killplaces.destroy()
        except:
            pass
        killplaces= Label(windowk,text=f'{kill}', font = 'Verdana 20', fg= '#A20E07', relief=GROOVE, border= 2, bg= '#E1D5E9')
        killplaces.place(x = 1, y = 1)

    textcoun = 0

    def placetext():
        global recplace, killplace, textcoun, difplace, kdif

        # recplace.destroy()
        # killplace.destroy()

        try:
            if textcoun > 3:
                recplace.destroy()
                killplace.destroy()
                difplace.destroy()
        except:
            pass

        killplace= Label(windowk,text=f'Убито: {kill}', font = 'Verdana 30', fg= '#E21153', relief=RIDGE, border= 6, width = 21, justify= CENTER, bg= '#F9ECFF')
        
        recplace = Label(windowk, text=f'Рекорд: {rec} ', font = 'Verdana 30', fg= '#E21153', relief=RIDGE, border= 6, width = 21, justify= CENTER, bg= '#F9ECFF')

        if kdif == 0:
            difscreen = 'легко'
        if kdif == 1:
            difscreen = 'нормально'
        if kdif == 2:
            difscreen = 'сложно'
        if kdif == 3:
            difscreen = 'невозможно'

        difplace = Label(windowk, text=f'Сложность: {difscreen} ', font = 'Verdana 30', fg= '#E21153', relief=RIDGE, border= 6, width = 21, justify= CENTER, bg= '#F9ECFF')

        killplace.place(x = 40, y = 188)
        recplace.place(x = 40, y = 243)
        difplace.place(x = 40, y = 299)

        textcoun += 1
    # Функция игры (анимацию)
    def game():
            global kill, counkn, rec, recplace, killplace, difplace, muscoun
            # Очищаем поле
            canvask.delete('all')
            # Отображаем задний фон
            canvask.create_image(300, 300, image = bg_photo)
            # Отображаем рыцаря
            canvask.create_image(knight.x, knight.y, image = knight.photo, tag='knight')
            # Меняем положение рыцаря
            knight.y += knight.v
            # Логика отображения драконов
            # Счётчик данного дракона
            current_dragon = 0
            # Какого дракона нужно удалить
            dragon_delete = -1

            # Проходимся по каждому дракону
            for dragon  in dragons:
                    # Перемещаем дракона влево
                    dragon.x -= dragon.v
                    # Отображаем дракона левее
                    canvask.create_image(dragon.x, dragon.y, image = dragon.photo)

                    # Если рыцарь столкнётся с драконом
                    if ((knight.x - dragon.x)**2 + (knight.y - dragon.y)**2) <= 96**2 and counkn != 1:
                            dragon_delete = current_dragon
                            dragons.append(Dragon())
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('games', 'knight', 'sound2.mp3')))
                            kill += 1
                            killcoun()

                    # К следующему дракону
                    current_dragon += 1

                    # Если хотябы 1 дракон перелетел
                    if dragon.x <= 0:
                        if muscoun == 0:
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(Path('games', 'knight', 'sound1.mp3')))
                            muscoun = 1
                        counkn = 1
                        canvask.delete('knight')

                        equel(0, 'easy.txt')
                        equel(1, 'normal.txt')
                        equel(2, 'hard.txt')
                        equel(3, 'impossible.txt')

                        canvask.create_text(w // 2, 30, text='Ты проиграл', font = 'Verdana 40', fill= 'red', tag='knight')

                        try:
                            with open(Path('games', 'knight', 'easy.txt'), 'r+') as f:
                                receasy = f.read()
                        except:
                            receasy = "нет данных"
                        try:
                            with open(Path('games', 'knight', 'normal.txt'), 'r+') as f:
                                recnormal= f.read()
                        except:
                            recnormal = "нет данных"
                        try:
                            with open(Path('games', 'knight', 'hard.txt'), 'r+') as f:
                                rechard = f.read()
                        except:
                            rechard = "нет данных"
                        try:
                            with open(Path('games', 'knight', 'impossible.txt'), 'r+') as f:
                                recimpos = f.read()
                        except:
                            recimpos = "нет данных"

                        canvask.create_text(195,510, text=f'Общие рекорды:\nЛегко: {receasy}\nНормально: {recnormal}\nСложно: {rechard}\nНевозможно: {recimpos}', font = 'Verdana 20', fill= '#F28502', tag='knight')
                    
                        # killplace= Label(windowk,text=f'Убито: {kill}', font = 'Verdana 30', fg= 'red', relief=RIDGE, border= 4, width = 15, justify= CENTER)
        
                        # recplace = Label(windowk, text=f' Рекорд: {rec} ', font = 'Verdana 30', fg= 'red', relief=RIDGE, border= 4, width = 15, justify= CENTER)

                        # recplace.destroy()
                        # killplace.destroy()

                        placetext()
                        
                        break
            # Если есть дракон, которого нужно удалить
            if dragon_delete > -1:
                    # Удаляем дракона
                    del dragons[dragon_delete]
            
            windowk.after(10, game)

    # Создаём объект рыцаря
    knight = Knight()

    # Список с драконами
    dragons = []

    if kdif == 0:
        for i in range(random.randint(3,5)):
            dragons.append(Dragon())
    if kdif == 1:
        for i in range(random.randint(5,9)):
            dragons.append(Dragon())
    if kdif == 2:
        for i in range(random.randint(8,12)):
            dragons.append(Dragon())
    if kdif == 3:
        for i in range(1, 12):
                dragons.append(Dragon())

    # Кнопки движения
    windowk.bind('<Key-Up>', knight.up)
    windowk.bind('<Key-Down>', knight.down)
    windowk.bind('<KeyRelease>', knight.stop)

    windowk.bind('<Escape>', lambda c: windowk.destroy())

    game()

    windowk.mainloop()

# Алхимия
def alhimsave():
    global window_m
    window_m.destroy()
    sound()
    global alsav
    alsav = Toplevel()
    icon = PhotoImage(file = Path('icons','diff.png'))
    alsav.iconphoto(False, icon)

    alsav.focus_force()
    alsav.geometry('485x200')
    alsav.resizable(0,0)
    alsav.title('Сохранения')

    textdif = Label(alsav, text = 'Продолжить?', fg= '#1e589e', font= 'Arial 20')
    textdif.pack()   
    canvas_alhim = Canvas(alsav, width = 100000, height = 100000, bg='#6C92AF', relief=RIDGE, borderwidth= 3)
    canvas_alhim.pack()

    but_ten_easy = Button(alsav, text='Продолжить¹', bg= '#77DD77', font='TimesNewRoman 25',command= cont, activebackground="#77DD77", relief=RIDGE, width= 13)
    but_ten_easy.place(x = 3, y = 41)

    but_ten_normal = Button(alsav, text='Новая игра²', bg= '#8D77DD', font='TimesNewRoman 25', command= newgame, activebackground="#8D77DD", relief=RIDGE, width= 12)
    but_ten_normal.place(x = 244, y = 41)

    but_exit = Button(alsav, text='выйти ␛', bg= '#B88FEF', font='TimesNewRoman 15', command= alsav.destroy, activebackground="#B88FEF", relief=RIDGE)
    but_exit.place(x = 3, y = 158)

    alsav.bind('1', lambda c: cont())
    alsav.bind('2', lambda c: newgame())
    alsav.bind('<Escape>', lambda c: alsav.destroy())
def cont():
    global con
    con = 1
    alhim()
def newgame():
    global con
    con = 0
    alhim()

def alhim_destroy():
    global winal
    winal.destroy()
    pygame.mixer.Channel(0).stop()

def alhim_sound():
    rsound = [(Path('games', 'alhim', 'sound1.mp3')), (Path('games', 'alhim', 'sound2.mp3')), (Path('games', 'alhim', 'sound3.mp3'))]
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(random.choice(rsound)))

def chek(elem):
    global elements
    global elementsgo
    try:
        pat = (Path('games','alhim','elements.txt'))
        with open(pat, 'r') as f:
            if str(elem) in (f.read()):
                elements.append(elem)
                elementsgo.append(elem())
    except:
        pass
def alhim():
    global winal
    global alsav
    alsav.destroy()
    global coun
    global canvasal
    global con
    global elements
    global elementsgo
    global elcount
    elcount = 22
    winal = Toplevel()
    winal.protocol("WM_DELETE_WINDOW", alhim_destroy)

    pygame.mixer.Channel(0).play(pygame.mixer.Sound(Path('games', 'alhim', 'bgmusic.mp3')), -1)

    icon = PhotoImage(file = Path('icons','alhim.png'))
    winal.iconphoto(False, icon)

    winal.geometry('1000x750')
    winal.title('Aлхимия')
    winal.focus_force()

    class X2():
        image = PhotoImage(file=(Path('games','alhim','x2.png')))
        def __add__(self,other):
            if isinstance(other,Fire):
                return Lava
            if isinstance(other,Plant):
                return Tree
            if isinstance(other,Brick):
                return Hut
            
    class Fire:
        image = PhotoImage(file=(Path('games','alhim','fire.png')))
        def __add__(self,other):
            if isinstance(other,Mud):
                return Brick
            if isinstance(other,Water):
                return Steam
            if isinstance(other,X2):
                return Lava
            if isinstance(other,Wind):
                return Energy
    class Brick:
        image = PhotoImage(file=(Path('games','alhim','brick.png')))
        def __add__(self,other):
            if isinstance(other,X2):
                return Hut
            
    class Water:
        image = PhotoImage(file=(Path('games','alhim','water.png')))
        def __add__(self,other):
            if isinstance(other,Fire):
                return Steam
            if isinstance(other,Earth):
                return Mud
            if isinstance(other,Stone):
                return Sand
            
    class Earth:
        image = PhotoImage(file=(Path('games','alhim','earth.png')))
        def __add__(self,other):
            if isinstance(other,Water):
                return Mud
            if isinstance(other,Mud):
                return Plant
            if isinstance(other,Lizard):
                return Animal
            
    class Wind:
        image = PhotoImage(file=(Path('games','alhim','wind.png')))
        def __add__(self,other):
            if isinstance(other,Lava):
                return Stone
            if isinstance(other,Fire):
                return Energy

    class Steam:
        image = PhotoImage(file=(Path('games','alhim','steam.png')))

    class Stone:
        image = PhotoImage(file=(Path('games','alhim','stone.png')))
        def __add__(self,other):
            if isinstance(other,Life):
                return Egg
            if isinstance(other,Water):
                return Sand

    class Mud:
        image = PhotoImage(file=(Path('games','alhim','mud.png')))
        def __add__(self,other):
            if isinstance(other,Fire):
                return Brick
            if isinstance(other,Water):
                return Plant
    class Lava:
        image = PhotoImage(file=(Path('games','alhim','lava.png')))
        def __add__(self, other):
            if isinstance(other,Wind):
                return Stone
    class Plant:
        image = PhotoImage(file=(Path('games','alhim','plant.png')))
        def __add__(self,other):
            if isinstance(other,X2):
                return Tree
            if isinstance(other,Energy):
                return Life
            if isinstance(other,Egg):
                return Lizard
    
    class Tree:
        image = PhotoImage(file=(Path('games','alhim','tree.png')))

    class Energy:
        image = PhotoImage(file=(Path('games','alhim','energy.png')))
        def __add__(self,other):
            if isinstance(other,Plant):
                return Life

    class Life:
        image = PhotoImage(file=(Path('games','alhim','life.png')))
        def __add__(self,other):
            if isinstance(other,Stone):
                return Egg
            if isinstance(other,Animal):
                return Human

    class Egg:
        image = PhotoImage(file=(Path('games','alhim','egg.png')))
        def __add__(self,other):
            if isinstance(other,Plant):
                return Lizard
            if isinstance(other,Sand):
                return Turtle

    class Lizard:
        image = PhotoImage(file=(Path('games','alhim','lizard.png')))
        def __add__(self,other):
            if isinstance(other,Earth):
                return Animal
    
    class Animal:
        image = PhotoImage(file=(Path('games','alhim','animal.png')))
        def __add__(self,other):
            if isinstance(other,Life):
                return Human

    class Human:
        image = PhotoImage(file=(Path('games','alhim','human.png')))  
        def __add__(self,other):
            if isinstance(other,Turtle):
                return TMNT

    class Hut:
        image = PhotoImage(file=(Path('games','alhim','hut.png')))
    
    class Sand:
        image = PhotoImage(file=(Path('games','alhim','sand.png')))    
        def __add__(self,other):
            if isinstance(other,Egg):
                return Turtle
    
    class Turtle:
        image = PhotoImage(file=(Path('games','alhim','turtle.png')))  
        def __add__(self,other):
            if isinstance(other,Human):
                return TMNT

    class TMNT:
        image = PhotoImage(file=(Path('games','alhim','TMNT.png'))) 

    def move(event):
        imagid = canvasal.find_overlapping(event.x , event.y, event.x+5, event.y + 5)
        canvasal.coords(imagid, event.x, event.y)
        if len(imagid) == 2:
            elem_id1 = imagid[0]
            elem_id2 = imagid[1]
            elem_1 = elementsgo[elem_id1 - 1]
            elem_2 = elementsgo[elem_id2 - 1]

            newelem = elem_1 + elem_2

            if newelem:
                if newelem not in elements:
                    global coun
                    coun += 1
                    alhim_sound()
                    counttext = Label(canvasal,text= (f'{coun}/{elcount}'), font= 'Calibri 40')
                    counttext.place(x = 0 , y = 680)
                    pat = (Path('games','alhim','elements.txt'))
                    with open(pat, 'a') as f:
                        f.write(str(newelem) + '\n')
                    canvasal.create_image(event.x + 50, event.y + 50, image=newelem.image)
                    elementsgo.append(newelem())
                    elements.append(newelem)

    canvasal = Canvas(winal,width=1000, height=750, bg ='#0F1113')

    # Список с элементами
    elements = [Water, Fire, Wind, Earth, X2]
    elementsgo = [Water(), Fire(), Wind(), Earth(), X2()]

    if con == 1:
        chek(Steam)
        chek(Brick)
        chek(Lava)
        chek(Stone)
        chek(Mud)
        chek(Plant)
        chek(Energy)
        chek(Tree)
        chek(Life)
        chek(Egg)
        chek(Lizard)
        chek(Animal)
        chek(Human)
        chek(Hut)
        chek(Sand)
        chek(Turtle)
        chek(TMNT)
    else:
        try:
             pat = (Path('games','alhim','elements.txt'))
             os.remove(pat)
        except:
             pass
        
    coun = len(elements)
    counttext = Label(canvasal,text= f'{coun}/{elcount}', font= 'Calibri 40')
    counttext.place(x = 0 , y = 680)

    but_exit = Button(canvasal, text='выйти ␛', bg= '#B88FEF', font='TimesNewRoman 25', command= alhim_destroy, activebackground="#B88FEF", relief=RIDGE)
    but_exit.place(x = 835, y = 681)

    for elem in elementsgo:
        canvasal.create_image(randint(50, 700), randint(50, 700), image=elem.image)
    
    #связываем ЛКМ с перемещением картинки
    winal.bind('<B1-Motion>', move)
    winal.bind('<Escape>', lambda c: alhim_destroy())

    canvasal.pack()
    winal.mainloop()

# Фоторобот
def button_sound():
    rsound = [(Path('games', 'photorobot', 'sound5.mp3')), (Path('games', 'photorobot', 'sound6.mp3')), (Path('games', 'photorobot', 'sound7.mp3'))]
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(random.choice(rsound)))

def photorob():
    global timecoun

    global face
    global eye
    global hair
    global brow
    global mouth
    global nose

    global eyesave
    global browsave
    global hairsave
    global mouthsave
    global nosesave

    global x
    global y
    cls()

    window_m.destroy()

    x = -240
    y = 0

    face = PhotoImage(file= (Path('games','photorobot','face.png')))
    canvas.create_image(x,y, image= face, anchor = NW)

    randomf = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']

    eyesave = Path('games','photorobot','eye', random.choice(randomf))
    eye = PhotoImage(file= (eyesave))
    canvas.create_image(x,y, image= eye, anchor = NW)

    browsave = Path('games','photorobot','brow', random.choice(randomf))
    brow = PhotoImage(file= (browsave))
    canvas.create_image(x,y, image= brow, anchor = NW)

    hairsave = Path('games','photorobot','hair', random.choice(randomf))
    hair = PhotoImage(file= (hairsave))
    canvas.create_image(x,y, image= hair, anchor = NW)

    mouthsave = Path('games','photorobot','mouth', random.choice(randomf))
    mouth = PhotoImage(file= (mouthsave))
    canvas.create_image(x,y, image= mouth, anchor = NW)

    randomnose = ['1.png', '2.png', '3.png', '4.png']
    nosesave = Path('games','photorobot','nose', random.choice(randomnose))
    nose = PhotoImage(file= (nosesave))
    canvas.create_image(x,y, image= nose, anchor = NW)

    timecoun = 4
    timerandgame()

def timerandgame():
    global eyenum
    global hairnum
    global brownum
    global mouthnum
    global nosenum

    global timecoun

    global x1

    x1 = 300

    if timecoun > 0 :   
        if timecoun == 3:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('games', 'photorobot', 'sound3.mp3')))
        elif timecoun == 2:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('games', 'photorobot', 'sound2.mp3')))
        elif timecoun == 1:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('games', 'photorobot', 'sound1.mp3')))

        timecoun = timecoun - 1
        window.after(1000, timerandgame)
        print(timecoun)
    else:
        cls()
        global face
        face = PhotoImage(file= (Path('games','photorobot','face.png')))
        canvas.create_image(x,y, image= face, anchor = NW)

        eyenum = 0
        brownum = 0
        hairnum = 0
        mouthnum = 0
        nosenum = 0

        eyebut = Button(text='Eyes', bg='#FFB807', font='Calibri 15', command= eyeplace)
        canvas.create_window(370, 150, anchor= NW, window=eyebut, tag='facebutton')

        browsbut = Button(text='Brows', bg='#FFC32D', font='Calibri 15', command= browplace)
        canvas.create_window(370, 200, anchor= NW, window=browsbut, tag='facebutton')

        hairbut = Button(text='Hair', bg='#FFC943', font='Calibri 15', command= hairplace)
        canvas.create_window(370, 250, anchor= NW, window=hairbut, tag='facebutton')

        mouthbut = Button(text='Mouth', bg='#FFD261', font='Calibri 15', command= mouthplace)
        canvas.create_window(370, 300, anchor= NW, window=mouthbut, tag='facebutton')

        nosebut = Button(text='Nose', bg='#FFD876', font='Calibri 15', command= noseplace)
        canvas.create_window(370, 350, anchor= NW, window=nosebut, tag='facebutton')

        donebut = Button(text='DONE', bg='#FFBF76', font='Calibri 15', command= facedone)
        canvas.create_window(370, 400, anchor= NW, window=donebut, tag='facebutton')

def eyeplace():
    button_sound()
    global eyenum
    global neweye

    global eyeplaces

    eyenum += 1

    if eyenum == 7:
        eyenum = 1

    if eyenum == 1:
        eyeplaces = Path('games','photorobot','eye', '1.png')
        neweye = PhotoImage(file= (eyeplaces))
        canvas.create_image(x,y, image= neweye, anchor = NW)

    if eyenum == 2:
        eyeplaces = Path('games','photorobot','eye', '2.png')
        neweye = PhotoImage(file= (eyeplaces))
        canvas.create_image(x,y, image= neweye, anchor = NW)

    if eyenum == 3:
        eyeplaces = Path('games','photorobot','eye', '3.png')
        neweye = PhotoImage(file= (eyeplaces))
        canvas.create_image(x,y, image= neweye, anchor = NW)
    
    if eyenum == 4:
        eyeplaces = Path('games','photorobot','eye', '4.png')
        neweye = PhotoImage(file= (eyeplaces))
        canvas.create_image(x,y, image= neweye, anchor = NW)

    if eyenum == 5:
        eyeplaces = Path('games','photorobot','eye', '5.png')
        neweye = PhotoImage(file= (eyeplaces))
        canvas.create_image(x,y, image= neweye, anchor = NW)
    
    if eyenum == 6:
        eyeplaces = Path('games','photorobot','eye', '6.png')
        neweye = PhotoImage(file= (eyeplaces))
        canvas.create_image(x,y, image= neweye, anchor = NW)
def browplace():
    button_sound()
    global brownum
    global newbrow

    global browplaces

    brownum += 1

    if brownum == 7:
        brownum = 1

    if brownum == 1:
        browplaces = Path('games','photorobot','brow', '1.png')
        newbrow = PhotoImage(file= (browplaces))
        canvas.create_image(x,y, image= newbrow, anchor = NW)

    if brownum == 2:
        browplaces = Path('games','photorobot','brow', '2.png')
        newbrow = PhotoImage(file= (browplaces))
        canvas.create_image(x,y, image= newbrow, anchor = NW)

    if brownum == 3:
        browplaces = Path('games','photorobot','brow', '3.png')
        newbrow = PhotoImage(file= (browplaces))
        canvas.create_image(x,y, image= newbrow, anchor = NW)
    
    if brownum == 4:
        browplaces = Path('games','photorobot','brow', '4.png')
        newbrow = PhotoImage(file= (browplaces))
        canvas.create_image(x,y, image= newbrow, anchor = NW)

    if brownum == 5:
        browplaces = Path('games','photorobot','brow', '5.png')
        newbrow = PhotoImage(file= (browplaces))
        canvas.create_image(x,y, image= newbrow, anchor = NW)
    
    if brownum == 6:
        browplaces = Path('games','photorobot','brow', '6.png')
        newbrow = PhotoImage(file= (browplaces))
        canvas.create_image(x,y, image= newbrow, anchor = NW)       
def hairplace():
    button_sound()
    global hairnum
    global newhair

    global hairplaces

    hairnum += 1

    if hairnum == 7:
        hairnum = 1

    if hairnum == 1:
        hairplaces = Path('games','photorobot','hair', '1.png')
        newhair = PhotoImage(file= (hairplaces))
        canvas.create_image(x,y, image= newhair, anchor = NW)

    if hairnum == 2:
        hairplaces = Path('games','photorobot','hair', '2.png')
        newhair = PhotoImage(file= (hairplaces))
        canvas.create_image(x,y, image= newhair, anchor = NW)

    if hairnum == 3:
        hairplaces = Path('games','photorobot','hair', '3.png')
        newhair = PhotoImage(file= (hairplaces))
        canvas.create_image(x,y, image= newhair, anchor = NW)
    
    if hairnum == 4:
        hairplaces = Path('games','photorobot','hair', '4.png')
        newhair = PhotoImage(file= (hairplaces))
        canvas.create_image(x,y, image= newhair, anchor = NW)

    if hairnum == 5:
        hairplaces = Path('games','photorobot','hair', '5.png')
        newhair = PhotoImage(file= (hairplaces))
        canvas.create_image(x,y, image= newhair, anchor = NW)
    
    if hairnum == 6:
        hairplaces = Path('games','photorobot','hair', '6.png')
        newhair = PhotoImage(file= (hairplaces))
        canvas.create_image(x,y, image= newhair, anchor = NW)
def mouthplace():
    button_sound()
    global mouthnum
    global newmouth

    global mouthplaces

    mouthnum += 1

    if mouthnum == 7:
        mouthnum = 1

    if mouthnum == 1:
        mouthplaces = Path('games','photorobot','mouth', '1.png')
        newmouth = PhotoImage(file= (mouthplaces))
        canvas.create_image(x,y, image= newmouth, anchor = NW)

    if mouthnum == 2:
        mouthplaces = Path('games','photorobot','mouth', '2.png')
        newmouth = PhotoImage(file= (mouthplaces))
        canvas.create_image(x,y, image= newmouth, anchor = NW)

    if mouthnum == 3:
        mouthplaces = Path('games','photorobot','mouth', '3.png')
        newmouth = PhotoImage(file= (mouthplaces))
        canvas.create_image(x,y, image= newmouth, anchor = NW)
    
    if mouthnum == 4:
        mouthplaces = Path('games','photorobot','mouth', '4.png')
        newmouth = PhotoImage(file= (mouthplaces))
        canvas.create_image(x,y, image= newmouth, anchor = NW)

    if mouthnum == 5:
        mouthplaces = Path('games','photorobot','mouth', '5.png')
        newmouth = PhotoImage(file= (mouthplaces))
        canvas.create_image(x,y, image= newmouth, anchor = NW)
    
    if mouthnum == 6:
        mouthplaces = Path('games','photorobot','mouth', '6.png')
        newmouth = PhotoImage(file= (mouthplaces))
        canvas.create_image(x,y, image= newmouth, anchor = NW)
def noseplace():
    button_sound()
    global nosenum
    global newnose

    global noseplaces

    nosenum += 1

    if nosenum == 5:
        nosenum = 1

    if nosenum == 1:
        noseplaces = Path('games','photorobot','nose', '1.png')
        newnose = PhotoImage(file= (noseplaces))
        canvas.create_image(x,y, image= newnose, anchor = NW)

    if nosenum == 2:
        noseplaces = Path('games','photorobot','nose', '2.png')
        newnose = PhotoImage(file= (noseplaces))
        canvas.create_image(x,y, image= newnose, anchor = NW)

    if nosenum == 3:
        noseplaces = Path('games','photorobot','nose', '3.png')
        newnose = PhotoImage(file= (noseplaces))
        canvas.create_image(x,y, image= newnose, anchor = NW)
    
    if nosenum == 4:
        noseplaces = Path('games','photorobot','nose', '4.png')
        newnose = PhotoImage(file= (noseplaces))
        canvas.create_image(x,y, image= newnose, anchor = NW)

def facedone():

    global faceold
    global x1

    progress = 0

    if eyenum != 0 and brownum !=0 and hairnum != 0 and mouthnum !=0 and nosenum != 0:
        if x1 != 240:
            x1 = x1 - 1
            canvas.delete('new')
            canvas.delete('facebutton')
            faceold = PhotoImage(file= (Path('games','photorobot','face.png')))

            canvas.create_image(x1,y, image= faceold, anchor = NW, tag = 'new')
            canvas.create_image(x1,y, image= eye, anchor = NW, tag = 'new')
            canvas.create_image(x1,y, image= brow, anchor = NW, tag = 'new')
            canvas.create_image(x1,y, image= hair, anchor = NW, tag = 'new')
            canvas.create_image(x1,y, image= mouth, anchor = NW, tag = 'new')
            canvas.create_image(x1,y, image= nose, anchor = NW, tag = 'new')

            window.after(10, facedone)
        else:
            if eyeplaces == eyesave:
                progress += 20
            if browplaces == browsave:
                progress += 20
            if hairplaces == hairsave:
                progress += 20
            if mouthplaces == mouthsave:
                progress += 20
            if noseplaces == nosesave:
                progress += 20
                
            result = Label(text= f'{progress}%',  bg='#424242', fg='white', font='Calibri 50', borderwidth = 4, relief="sunken")
            canvas.create_window(330, 280, window= result, anchor=NW)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('games', 'photorobot', 'sound4.mp3')))
        
# Крестики-нолики
def tictactoemod():
    global window_m
    global tttmode
    window_m.destroy()
    sound()
    global tttmode
    tttmode = Toplevel()
    icon = PhotoImage(file = Path('icons','diff.png'))
    tttmode.iconphoto(False, icon)

    tttmode.geometry('485x200')
    tttmode.resizable(0,0)
    tttmode.title('Выбор режима игры')

    textdif = Label(tttmode, text = 'Выберите режим игры', fg= '#1e589e', font= 'Arial 20')
    textdif.pack()   
    canvas_tttmode = Canvas(tttmode, width = 100000, height = 100000, bg='#6C92AF' )
    canvas_tttmode.pack()

    but_1 = Button(tttmode, text='1 Игрок', bg= '#77DD77', font='TimesNewRoman 25',command= tictactoediff)
    but_1.place(x = 65, y = 100)

    but_2 = Button(tttmode, text='2 Игрока', bg= '#DCD36A', font='TimesNewRoman 25', command= tttoe2mode)
    but_2.place(x = 270, y = 100)

    but_exit = Button(tttmode, text='выйти', bg= '#B88FEF', font='TimesNewRoman 10', command= tttmode.destroy)
    but_exit.place(x = 5, y = 170)

def tictactoediff():
    global tttmode
    tttmode.destroy()
    sound()
    tttmode = Toplevel()
    icon = PhotoImage(file = Path('icons','diff.png'))
    tttmode.iconphoto(False, icon)

    tttmode.geometry('485x200')
    tttmode.resizable(0,0)
    tttmode.title('Выбор сложности')

    textdif = Label(tttmode, text = 'Выберите сложность', fg= '#1e589e', font= 'Arial 20')
    textdif.pack()   
    canvas_tttmode = Canvas(tttmode, width = 100000, height = 100000, bg='#6C92AF' )
    canvas_tttmode.pack()

    but_1 = Button(tttmode, text=' лёгкая ', bg= '#77DD77', font='TimesNewRoman 25',command= tttoe1modeeasy)
    but_1.place(x = 65, y = 100)

    but_2 = Button(tttmode, text=' сложная ', bg= '#DD9475', font='TimesNewRoman 25', command= tttoe1modehard)
    but_2.place(x = 270, y = 100)

    but_exit = Button(tttmode, text='выйти', bg= '#B88FEF', font='TimesNewRoman 10', command= tttmode.destroy)
    but_exit.place(x = 5, y = 170)

def tictactoe_sound():
    rsound = [(Path('games', 'tic-tac-toe', 'sound1.mp3')), (Path('games', 'tic-tac-toe', 'sound2.mp3')), (Path('games', 'tic-tac-toe', 'sound3.mp3'))]
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(random.choice(rsound)))


def tttoe1modeeasy():
    tttmode.destroy()

    global current_player, game_field, AI_player, tttcoun, tttcoun2, icon

    tttcoun = 1
    tttcoun2 = 0

    def AI_Play():
        tictactoe_sound()
        global game_field, AI_player, current_player
        # Поиск пустой клетки
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if game_field[row][col] == "":
                    empty_cells.append((row, col))
        if empty_cells:
            # Генерация случайного хода
            random_choice = random.choice(empty_cells)
            row = random_choice[0]
            col = random_choice[1]
            # Изменение клетки и обновление поля
            game_field[row][col] = AI_player
            button = button_list[row][col]
            button.config(text=AI_player, state=tk.DISABLED, font=("Comic Sans MS", 20, 'bold'), disabledforeground="#C9F3FF")
            check_winner()
            # Убираем ограничение после хода компьютера
            enable_buttons()
            if hplayer == 'O':
                current_player = "O" 
            if hplayer == 'X':
                current_player = "X" 
    
    tictactoewin = Toplevel()
    icon = PhotoImage(file = Path('icons','tic-tac-toe_easy.png'))
    tictactoewin.iconphoto(False, icon)
    tictactoewin.title("Крестики-нолики")
    tictactoewin.resizable(0,0)

    canvasttt = Canvas(width = 100, height = 100)

    players = ['X', 'O']

    hplayer = random.choice(players)

    current_player = hplayer
    players.remove(hplayer)

    game_field = [["", "", ""], ["", "", ""], ["", "", ""]] 
    AI_player = random.choice(players)

    def play(row, col, button):
        tictactoe_sound()
        global current_player, game_field, AI_Player
        button.config(text=current_player, state=tk.DISABLED, font=("Comic Sans MS", 20, 'bold')) 
        game_field[row][col] = current_player
        check_winner()
        
        if current_player == "X":
            button.config(disabledforeground="white") 
            current_player = "O" 
            # Добавляем ограничение на использование кнопки после хода игрока
            disable_buttons()
            # Запускаем ход ИИ
            tictactoewin.after(500, AI_Play)
            
        else:
            tictactoewin.after(500, AI_Play)
            button.config(disabledforeground="white") 
            current_player = "X" 
            # Убираем ограничение после хода компьютера
            enable_buttons()
            # Снимаем ограничение только после хода компьютера
            button.config(command=lambda row=row, col=col, button=button: None) 

    def disable_buttons():
        for row in range(3):
            for col in range(3):
                button_list[row][col].config(state=tk.DISABLED)

    def enable_buttons():
        for row in range(3):
            for col in range(3):
                if game_field[row][col] == "":
                    button_list[row][col].config(state=tk.NORMAL)

    def check_winner():
        global game_field, tttcoun
        
        for row in range(3):
            if game_field[row][0] == game_field[row][1] == game_field[row][2] != "":
                win(game_field[row][0])
                tttcoun = 0
        for col in range(3):
            if game_field[0][col] == game_field[1][col] == game_field[2][col] != "":
                win(game_field[0][col])
                tttcoun = 0
        if game_field[0][0] == game_field[1][1] == game_field[2][2] != "":
            win(game_field[0][0])
            tttcoun = 0
        if game_field[0][2] == game_field[1][1] == game_field[2][0] != "":
            win(game_field[0][2])
            tttcoun = 0

        elif all(game_field[row][col] != "" for row in range(3) for col in range(3)) and tttcoun != 0:
            win("")

    def win(winner):
        global tttcoun2
        if winner != "" and tttcoun2 != 1:
            messagebox.showinfo("Крестики-нолики", "Выиграл игрок " + winner)
            tttcoun2 = 1
            tictactoewin.destroy()
        if winner == "" and tttcoun2 != 1:
            messagebox.showinfo("Крестики-нолики", "Ничья!")
            tttcoun2 = 1
            tictactoewin.destroy()

    # Создание списка кнопок
    button_list = list()

    # Создание игрового поля
    for row in range(3):
        button_col = tk.Frame(tictactoewin)
        button_col.pack(side=tk.LEFT)
        button_row = list()
        
        for col in range(3):
            button = tk.Button(button_col, text="", bg ='#417251', height=2, width=5, disabledforeground="white", activebackground="#417251") 
            button.pack()
            button.config(font=("Comic Sans MS", 20, 'bold'), bg='#417251', fg='white') 
            
            # Добавление команды только после старта игры
            if "import random" not in button.config()["command"]:
                button.config(command=lambda row=row, col=col, button=button: play(row, col, button)) 
            
            button_row.append(button)
            
        button_list.append(button_row)

    if AI_player == 'X':
        disable_buttons()
        tictactoewin.after(1000, AI_Play)

    canvasttt.pack()
    tictactoewin.mainloop()

def tttoe1modehard():
    tttmode.destroy()
    global current_player, game_field, AI_player, tttcoun, tttcoun2, icon, first_move

    tttcoun = 1
    tttcoun2 = 0
    first_move = None

    def minimax(game_state, is_maximizing):
        # Проверка наличия выигрышной комбинации
        winner = None
        for row in range(3):
            if game_state[row][0] == game_state[row][1] == game_state[row][2] and game_state[row][0] != "":
                winner = game_state[row][0]
                break
        for col in range(3):
            if game_state[0][col] == game_state[1][col] == game_state[2][col] and game_state[0][col] != "":
                winner = game_state[0][col]
                break
        if game_state[0][0] == game_state[1][1] == game_state[2][2] and game_state[0][0] != "":
            winner = game_state[0][0]
        if game_state[0][2] == game_state[1][1] == game_state[2][0] and game_state[0][2] != "":
            winner = game_state[0][2]
            
        # Возврат оценки в случае выигрыша, проигрыша или ничьи
        if winner == AI_player:
            return 1
        elif winner == hplayer:
            return -1
        elif all(game_state[row][col] != "" for row in range(3) for col in range(3)):
            return 0
        
        # Рекурсивный вызов минимакса
        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if game_state[row][col] == "":
                        game_state[row][col] = AI_player
                        score = minimax(game_state, False)
                        game_state[row][col] = ""
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if game_state[row][col] == "":
                        game_state[row][col] = hplayer
                        score = minimax(game_state, True)
                        game_state[row][col] = ""
                        best_score = min(best_score, score)
            return best_score

    def AI_Play():
        global first_move
        global game_field, AI_player, current_player
        best_score = -float('inf')
        best_move = None

        enable_buttons()
        tictactoe_sound()
        
        # Проверяем, чей первый ход в игре
        if first_move == 'AI':
            row, col = random.choice([(0, 0), (0, 2), (2, 0), (2, 2)])
            game_field[row][col] = AI_player
            button = button_list[row][col]
            button.config(text=AI_player, state=tk.DISABLED, font=("Comic Sans MS", 20, 'bold'), disabledforeground="#C9F3FF")
            first_move = None
            current_player = hplayer
        else:
            for row in range(3):
                for col in range(3):
                    if game_field[row][col] == "":
                        game_field[row][col] = AI_player
                        score = minimax(game_field, False)
                        game_field[row][col] = ""
                        if score > best_score:
                            best_score = score
                            best_move = (row, col)
            row, col = best_move
            game_field[row][col] = AI_player
            button = button_list[row][col]
            button.config(text=AI_player, state=tk.DISABLED, font=("Comic Sans MS", 20, 'bold'), disabledforeground="#C9F3FF")
            check_winner()
            if hplayer == 'O':
                current_player = 'O'
            if hplayer == 'X':
                current_player = 'X'     
                  

    tictactoewin = tk.Toplevel()

    icon = PhotoImage(file = Path('icons','tic-tac-toe_hard.png'))
    tictactoewin.iconphoto(False, icon)

    tictactoewin.title("Крестики-нолики")
    tictactoewin.geometry('285x300')
    tictactoewin.resizable(0,0)

    canvasttt = Canvas(width = 100, height = 100)

    players = ['X', 'O']

    hplayer = random.choice(players)

    current_player = hplayer
    players.remove(hplayer)

    game_field = [["", "", ""], ["", "", ""], ["", "", ""]] 
    AI_player = random.choice(players)

    if AI_player == 'X':
        first_move = 'AI'
    else:
        first_move = None

    def play(row, col, button):
        tictactoe_sound()
        global current_player, game_field, AI_Player
        button.config(text=current_player, state=tk.DISABLED, font=("Comic Sans MS", 20, 'bold')) 
        game_field[row][col] = current_player
        check_winner()
        
        if current_player == "X":
            button.config(disabledforeground="white") 
            current_player = "O" 
            # Добавляем ограничение на использование кнопки после хода игрока
            disable_buttons()
            # Запускаем ход ИИ
            tictactoewin.after(500, AI_Play)
            
        else:
            tictactoewin.after(500, AI_Play)
            button.config(disabledforeground="white") 
            current_player = "X" 
            # Убираем ограничение после хода компьютера
            enable_buttons()
            # Снимаем ограничение только после хода компьютера
            button.config(command=lambda row=row, col=col, button=button: None) 

    def disable_buttons():
        for row in range(3):
            for col in range(3):
                button_list[row][col].config(state=tk.DISABLED)

    def enable_buttons():
        for row in range(3):
            for col in range(3):
                if game_field[row][col] == "":
                    button_list[row][col].config(state=tk.NORMAL)

    def check_winner():
        global game_field, tttcoun
        
        for row in range(3):
            if game_field[row][0] == game_field[row][1] == game_field[row][2] != "":
                win(game_field[row][0])
                tttcoun = 0
        for col in range(3):
            if game_field[0][col] == game_field[1][col] == game_field[2][col] != "":
                win(game_field[0][col])
                tttcoun = 0
        if game_field[0][0] == game_field[1][1] == game_field[2][2] != "":
            win(game_field[0][0])
            tttcoun = 0
        if game_field[0][2] == game_field[1][1] == game_field[2][0] != "":
            win(game_field[0][2])
            tttcoun = 0

        elif all(game_field[row][col] != "" for row in range(3) for col in range(3)) and tttcoun != 0:
            win("")

    def win(winner):
        global tttcoun2
        if winner != "" and tttcoun2 != 1:
            messagebox.showinfo("Крестики-нолики", "Выиграл игрок " + winner)
            tttcoun2 = 1
            tictactoewin.after(500, tictactoewin.destroy())
        if winner == "" and tttcoun2 != 1:
            messagebox.showinfo("Крестики-нолики", "Ничья!")
            tttcoun2 = 1
            tictactoewin.after(500, tictactoewin.destroy())

    # Создание списка кнопок
    button_list = list()

    # Создание игрового поля
    for row in range(3):
        button_col = tk.Frame(tictactoewin)
        button_col.pack(side=tk.LEFT)
        button_row = list()
        
        for col in range(3):
            button = tk.Button(button_col, text="", bg ='#417251', height=2, width=5, disabledforeground="white", activebackground="#417251") 
            button.pack()
            button.config(font=("Comic Sans MS", 20, 'bold'), bg='#417251', fg='white') 
            
            # Добавление команды только после старта игры
            if "import random" not in button.config()["command"]:
                button.config(command=lambda row=row, col=col, button=button: play(row, col, button)) 
            
            button_row.append(button)
            
        button_list.append(button_row)

    if AI_player == 'X':
        disable_buttons()
        tictactoewin.after(1000, AI_Play)

    canvasttt.pack()
    tictactoewin.mainloop()

def tttoe2mode():
    tttmode.destroy()

    global current_player, game_field, tttcoun
    global tictactoewin

    tttcoun = 1

    tictactoewin = Toplevel()

    icon = PhotoImage(file = Path('icons','tic-tac-toe_two_players.png'))
    tictactoewin.iconphoto(False, icon)

    tictactoewin.title("Крестики-нолики")
    tictactoewin.resizable(0,0)

    current_player = "X"
    game_field = [["", "", ""], ["", "", ""], ["", "", ""]]

    def play(row, col, button):
        tictactoe_sound()
        global current_player, game_field
        button.config(text=current_player, state=tk.DISABLED, font=("Comic Sans MS", 20, 'bold'))
        game_field[row][col] = current_player
        check_winner()
        if current_player == "X":
            button.config(disabledforeground="white")
            current_player = "O"
        else:
            current_player = "X"
            button.config(disabledforeground="#C9F3FF")

    def check_winner():
        global game_field, tttcoun
        for row in range(3):
            if game_field[row][0] == game_field[row][1] == game_field[row][2] != "":
                win(game_field[row][0])
                tttcoun = 0
        for col in range(3):
            if game_field[0][col] == game_field[1][col] == game_field[2][col] != "":
                win(game_field[0][col])
                tttcoun = 0
        if game_field[0][0] == game_field[1][1] == game_field[2][2] != "":
            win(game_field[0][0])
            tttcoun = 0
        if game_field[0][2] == game_field[1][1] == game_field[2][0] != "":
            win(game_field[0][2])
            tttcoun = 0

        elif all(game_field[row][col] != "" for row in range(3) for col in range(3)) and tttcoun != 0:
            win("")

    def win(winner):
        if winner != "":
            messagebox.showinfo("Крестики-нолики", "Выиграл игрок " + winner)
            tictactoewin.destroy()
        else:
            messagebox.showinfo("Крестики-нолики", "Ничья!")
            tictactoewin.destroy()
        

    button_frame = tk.Frame(tictactoewin)
    button_frame.pack()

    for row in range(3):
        button_col = tk.Frame(button_frame)
        button_col.pack(side=tk.LEFT)
        for col in range(3):
            button = tk.Button(button_col, text="", bg ='#417251', height=2, width=5, disabledforeground="white", activebackground="#417251")
            button.pack()
            button.config(command=lambda row=row, col=col, button=button: play(row, col, button), font=("Comic Sans MS", 20, 'bold'), bg='#417251', fg='white')

    tictactoewin.mainloop()


# Квадратные уравнения
def uravdon():
    global color
    global a
    global b
    global c
    sound()

    unbind()
    bind2()

    a = int(a.get())
    b = int(b.get())
    c = int(c.get())
    # if a <0:
    #         a = -a
    #         b = -b
    #         c = -c
    # elif a <0:
    #         pm = '+'
    #         a = -a
    #         b=-b
    #         c=-c
    # elif c <0:
    #         pm = '+'
    #         c = -c
    # else:
    #         pm = '-'
    D = b**2 - (4 * a * c)
    dis = Label(text=f'Дискриминант = {b}² - (4 · {a} · {c}) = {b**2} - {4 * a * c} = {D}',font='calibri 25',bg = color,fg='white', relief=RIDGE, borderwidth= 2)
    canvas.create_window(10, 150, window= dis, anchor=NW)

    if D > 0:
        x1 = Label(text=f'x₁ = {-b} + √{D} / 2 · {a} = {-b} + {sqrt(D)} / {2*a} = {(-b + sqrt(D))/(2*a)}',font='calibri 25',bg = color,fg='#35FAE0', relief=RIDGE, borderwidth= 2)
        canvas.create_window(10, 200, window= x1, anchor=NW)

        x2 = Label(text=f'x₂ = {-b} - √{D} / 2 · {a} = {-b} - {sqrt(D)} / {2*a} = {(-b - sqrt(D))/(2*a)}',font='calibri 25',bg = color,fg='#35BEFA', relief=RIDGE, borderwidth= 2)
        canvas.create_window(10, 250, window= x2, anchor=NW)
    if D == 0:
         x = Label(text=f'x = {-b} +- √{D} / 2 · {a} = {-b} +- {sqrt(D)} / {2*a} = {(-b - sqrt(D))/(2*a)}',font='calibri 25',bg = color,fg='#35BEFA', relief=RIDGE, borderwidth= 2)
         canvas.create_window(10, 200, window= x, anchor=NW)
    if D < 0:
        kn = Label(text=f'Корней нет',font='calibri 25',bg = color,fg='#FA3535', relief=RIDGE, borderwidth= 2)
        canvas.create_window(10, 200, window= kn, anchor=NW)
def urav():
    cls()
    unbind()
    global color
    global a
    global b
    global c
    a = Entry(font='calibri 30', width=4, justify=RIGHT,bg='#313131',fg='white')
    canvas.create_window(75, 110, window= a)

    a.focus()

    alab = Label(font='calibri 30',bg = color, text='x² +',fg='white', relief="sunken", borderwidth= 1)
    canvas.create_window(150, 110, window= alab)
    b = Entry(font='calibri 30', width=4, justify=RIGHT,bg='#313131',fg='white')
    canvas.create_window(230, 110, window= b)
    blab = Label(font='calibri 30',bg = color, text='x +',fg='white', relief="sunken", borderwidth= 1)
    canvas.create_window(298, 110, window= blab)
    c = Entry(font='calibri 30', width=4, justify=RIGHT,bg='#313131',fg='white')
    canvas.create_window(370, 110, window= c)

    aged = Button(text="Готово↲", bg= "#0EE7F1", font= "Calibri 18",command=uravdon, relief= GROOVE, borderwidth= 2, activebackground="#0EE7F1")
    canvas.create_window(464, 110, window=aged)

    window.bind('<Return>', lambda c: uravdon())
    a.bind('<Right>', move_down)
    b.bind('<Left>', move_up)
    b.bind('<Right>', move_down)
    c.bind('<Left>', move_up)
    # c.bind('<Down>', move_down)


# Блокнот
def blocksave():
    global color
    global what
    global filename
    global entex

    bind2()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound7.mp3')))
    blockname = filename.get()
    if not os.path.isdir('C:\\Igortexts'):
        os.mkdir('C:\\Igortexts')
    f = open(f'C:\\Igortexts\\{blockname}', 'w')
    if entex.get() == '':
        tex = what
    else:
         tex = entex.get()
    f.write(tex)
    f.close
    nice = Label(text='Файл успешно сохранён!', bg =color, fg='#52FF06', font='TimesNewRoman 20', relief="sunken", borderwidth= 2)
    canvas.create_window(10, 100, anchor=NW, window= nice)
def blocksaveap():
    global color
    global what
    global filename
    global entex

    bind2()

    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path('other', 'sound6.mp3')))
    blockname = filename.get()
    if not os.path.isdir('C:\\Igortexts'):
        os.mkdir('C:\\Igortexts')
    f = open(f'C:\\Igortexts\\{blockname}', 'a')
    if entex.get() == '':
        tex = what
    else:
         tex = entex.get()
    f.write(tex)
    f.close
    nice = Label(text='Файл успешно дописан!', bg =color, fg='#52FF06', font='TimesNewRoman 20', relief="sunken", borderwidth= 2)
    canvas.create_window(10, 100, anchor=NW, window= nice)

def blocknot():
    global color
    global filename
    global entex
    cls()
    unbind()

    tex =Label(text='Введите текст:', bg =color, fg='#E7E7E7', font='TimesNewRoman 20', relief="sunken", borderwidth= 2)
    canvas.create_window(10, 75, anchor=NW, window= tex)

    mic =Label(text='Чтобы воспользоваться микрофоном сотрите всё с текстового поля', bg =color, fg='#FFE66C', font='TimesNewRoman 15', relief="sunken", borderwidth= 2)
    canvas.create_window(10, 175, anchor=NW, window= mic)

    entex = Entry(font='TimesNewRoman 20', justify=LEFT, relief= GROOVE, borderwidth= 2)
    canvas.create_window(10, 115, anchor=NW, window= entex,width=780, height=55)

    microbut = Button(font='TimesNewRoman 20', text= 'Записать с микрофона', bg='#70CFFE', command= microrec, relief= GROOVE, borderwidth= 2, activebackground="#70CFFE")
    canvas.create_window(10, 502, anchor=NW, window= microbut)

    savebut = Button(text="Сохранить как новый", bg= "#A870FE", font= "Calibri 20",command=blocksave, relief= GROOVE, borderwidth= 2, activebackground="#A870FE")
    canvas.create_window(403, 502, anchor=NW, window=savebut)
    savebut = Button(text="Дописать", bg= "#C870FE", font= "Calibri 20",command=blocksaveap, relief= GROOVE, borderwidth= 2, activebackground="#C870FE")
    canvas.create_window(670, 502, anchor=NW, window=savebut)

    filename = Entry(font='TimesNewRoman 20', justify=LEFT,width=12)
    filename.insert(0,'название.txt')

    entex.focus()

    canvas.create_window(610, 460, anchor=NW, window= filename)

def microrec():
    global color
    global what
    rec = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
                text = 'Говорите'
                tts = pyttsx3.init()
                rate = tts.getProperty('rate') #Скорость произношения
                tts.setProperty('rate', rate-40)
                volume = tts.getProperty('volume') #Громкость голоса
                tts.setProperty('volume', volume+0.9)
                voices = tts.getProperty('voices')
                tts.setProperty('voice', 'ru') 
                tts.say(text)
                tts.runAndWait()
                audio = rec.listen(source)
    what = rec.recognize_google(audio, language= 'ru_RU').lower()
    (what)

    say = Label(text='Текст успешно записан!', bg =color, fg='#9DFE70', font='TimesNewRoman 20', relief="sunken", borderwidth= 2)
    canvas.create_window(10, 450, anchor=NW, window= say)
    bind2()

# Озвучка
def mp3file():
    global filepath
    filepath = filedialog.askopenfilename(initialdir="C:\\Igortexts", filetypes=(("Текстовые файлы", "*.txt *.text *.json"),("Все файлы", "*")))

    if filepath != '':
        canvas.delete('al')
        fileisex = Label(text='✓', bg ='green', fg='white', font='TimesNewRoman 32',width=2)
        canvas.create_window(195, 100, anchor=NW, window=fileisex, tag = 'al')
    else:
        canvas.delete('al')
        fileisex = Label(text='x', bg ='red', fg='white', font='TimesNewRoman 32',width=2)
        canvas.create_window(195, 100, anchor=NW, window=fileisex, tag = 'al')

def mp3():
    rus()
    cls()
    unbind()

    window.bind('<Return>', lambda c: mp3done())

    global color
    global nameentmp3
    global filepath

    direcl = Button(text='Указать путь', bg ='#63B924', fg='#E7FFEE', font='TimesNewRoman 20', command= mp3file, relief= GROOVE, borderwidth= 2, activebackground="#E7FFEE")

    namelmp3 = Label(text='Имя итогового файла: ', bg =color, fg='#FFCAAC', font='TimesNewRoman 20', relief="sunken", borderwidth= 2)
    nameentmp3 = Entry(font='TimesNewRoman 20', justify=LEFT,width=20, bg ='#FFCAAC')
    nameentmp3.insert(1,'звук')

    canvas.create_window(10, 220, anchor=NW, window= nameentmp3)
    canvas.create_window(10, 170, anchor=NW, window=namelmp3)

    ru = Radiobutton(text='Русский', bg =color, font='TimesNewRoman 20', fg= 'white',command=rus, relief="sunken", borderwidth= 2)
    canvas.create_window(10, 300, anchor=NW, window= ru)
    en = Radiobutton(text='Английский', bg =color, font='TimesNewRoman 20', fg= 'white',command=eng, relief="sunken", borderwidth= 2)
    canvas.create_window(10, 350, anchor=NW, window= en)

    canvas.create_window(10, 100, anchor=NW, window=direcl)

    fileisex = Label(text='x', bg ='red', fg='white', font='TimesNewRoman 32',width=2)
    canvas.create_window(195, 100, anchor=NW, window=fileisex, tag = 'al')

    mpdonebut = Button(text="Готово↲", bg= "#A870FE", font= "Calibri 20",command=mp3done, relief= GROOVE, borderwidth= 2, activebackground="#A870FE")
    canvas.create_window(10, 400, anchor=NW, window=mpdonebut)

def rus():
     global lan
     lan = 'ru'
def eng():
     global lan
     lan = 'en'

def mp3done():
    global color
    global directent
    global nameent
    global filepath

    bind2()

    if filepath != "":
        with open(filepath, "r") as file:
            data_text = file.read()
            tts = gTTS(text = data_text, lang= lan)
            tts.save(f'{nameentmp3.get()}.mp3')
            nice = Label(text='Файл успешно сохранён в папку с приложением!', bg =color, fg='#52FF06', font='TimesNewRoman 15', relief="sunken", borderwidth= 2)
            canvas.create_window(10, 260, anchor=NW, window= nice)

# Чтение
def readdone():
    global color
    global directentread
    global nameentread
    cls()
    unbind()
    bind2()
    filepath = filedialog.askopenfilename(initialdir="C:\\Igortexts", filetypes=(("Текстовые файлы", "*.txt *.text *.json"),("Все файлы", "*")))
    if filepath != "":
        with open(filepath, "r") as file:
            f = file.read()

    # if str(directentread.get()) == '':
    #     c = 'C:\\Igortexts\\'
    # else:
    #     c = directentread.get()
    # f = open(c + nameentread.get())
    readtex = Label(text=f, font='Arial 20', bg='#424242', fg='white',wraplength=770, justify=LEFT, borderwidth = 1,relief="sunken")
    canvas.create_window(10, 100, anchor=NW, window=readtex)



# Валюты
def val():
    cls() 
    unbind()
    bind3()

    def update_data():
    # получить новые данные
        response = requests.get(url, params= payload)
        xml = bs(response.content, features='xml')
        # обновить метки с курсом
        usd.config(text='$ Доллар США = ' + get_data('R01235'))
        eur.config(text='€ Евро = ' + get_data('R01239'))
        # запустить функцию снова через 10 секунд
        print('€ Евро = ' + get_data('R01239'))
        window.after(10000, update_data)

    def get_data(id):
        return xml.find('Valute', {'ID' : id}).Value.text
    valnews = Label(text='Новости валют', font = 'Calibri 25', bg='#1f2020', fg='#21B8FF', relief="sunken", borderwidth= 2)
    canvas.create_window(10, 93, anchor=NW, window=valnews)

    url = 'http://www.cbr.ru/scripts/XML_daily.asp?'

    today = datetime.today()
    today = today.strftime('%d/%m/%Y')

    payload = {'date_req': today}
    response = requests.get(url, params= payload)
    xml = bs(response.content, features='xml')

    # img_logo2 = PhotoImage(file = 'dragon.png')

    # logo2 = Label(canvas, image= img_logo2, bg = '#1f2020')
    # canvas.create_window(10, 200, anchor=NW, window=logo2)

    # img_logo = PhotoImage(file = 'dragon.png')
    # logo = Label(canvas, image= img_logo, bg = '#1f2020')
    # canvas.create_window(10, 200, anchor=NW, window=logo)

    data = Label(canvas, text= 'Курс на '+ today.replace('/', '.'), fg = '#0BDA51', font = 'Arial 20',bg = '#1f2020', relief="sunken", borderwidth= 2)
    canvas.create_window(10, 140, anchor=NW, window=data)

    usd = Label(canvas, text= '$ Доллар США = ' + get_data('R01235'), font = 'Arial 25', relief="sunken", borderwidth= 1)
    canvas.create_window(10, 182, anchor=NW, window=usd)

    eur = Label(canvas, text= '€ Евро = ' + get_data('R01239'), font = 'Arial 25', relief="sunken", borderwidth= 1)
    canvas.create_window(10, 230, anchor=NW, window=eur)

    update_data()

# Анекдоты
def anekdot():
    cls()
    unbind()
    bind3()

    url = 'https://anekdoty.ru'
    response = requests.get(url)
    soup = bs(response.text, 'lxml')

    data = soup.find('p').text
    if 'екс' in data or 'фил' in data or 'ук' in data or 'амасут' in data or 'рак' in data:
        data = soup.find('p').text
    canvas.delete('an')
    anec = Label(text=data, font='Arial 20', bg='#424242', fg='white',wraplength=790, justify=LEFT, borderwidth = 4,relief="sunken")
    canvas.create_window(5, 100, anchor=NW, window=anec, tag='an')

# Факты
def fact_get():
    cls()
    unbind()
    bind3()

    url = 'https://randstuff.ru/fact/'

    response = requests.get(url)

    soup = bs(response.text, 'lxml')

    data = soup.find('td').text

    canvas.delete('fact')

    canvas.create_window(20, 100,window=Label(text = data,font='Arial 20', bg='#424242', fg='white',wraplength=770, justify=LEFT, borderwidth = 4,relief="sunken"), anchor=NW, tag='fact')

# Плеер
def mus():
    cls()
    unbind()
    bind3()

    class MusicPlayer:
        def __init__(self, master):
            self.master = master
            self.canvas = canvas
            # Создаем кнопку для выбора директории
            self.select_button = Button(self.canvas, text="Выбрать папку", command=self.select_folder, font='Calibri 20', bg='#7832D6', relief= RIDGE, borderwidth= 2, activebackground="#7832D6")
            self.canvas.create_window(10, 100, window = self.select_button, anchor= NW)

            # Создаем кнопки для управления проигрыванием
            self.play_button = Button(self.canvas, text="⏸️", command=self.play_pause, font='Calibri 20')
            self.canvas.create_window(50, 260, window = self.play_button)

            self.prev_button = Button(self.canvas, text="⏪", command=self.play_prev, font='Calibri 20')
            self.canvas.create_window(120, 230, window = self.prev_button)

            self.next_button = Button(self.canvas, text="⏩", command=self.play_next, font='Calibri 20')
            self.canvas.create_window(180, 230, window = self.next_button)

            window.bind('<space>', lambda c: self.play_pause())

            # Создаем виджет с названием трека
            self.track_name = StringVar()
            self.track_label = Label(self.canvas, textvariable=self.track_name, font='Calibri 20',wraplength=620, justify=LEFT, borderwidth = 2, bg='#B485F2', relief= RIDGE)
            self.canvas.create_window(200, 100, window = self.track_label, anchor= NW)

            # Создаем ползунок громкости
            self.volume_scale = Scale(self.canvas, from_=0, to=100, orient=HORIZONTAL, command=self.change_volume, font='Calibri 20', length=111)
            self.volume_scale.set(50)
            self.canvas.create_window(149, 290, window = self.volume_scale)

            # Инициализируем pygame для воспроизведения музыки
            pygame.init()

            # Создаем переменные для хранения списка треков и текущего трека
            self.playlist = []
            self.current_track = None

        def select_folder(self):
            # Открываем диалог выбора папки
            sound()
            directory = filedialog.askdirectory()

            if directory:
                # Получаем список файлов в папке
                files = os.listdir(directory)
                self.playlist = []

                # Ищем музыкальные файлы в списке файлов и добавляем их в плейлист
                for file in files:
                    if file.endswith(".mp3") or file.endswith(".wav"):
                        self.playlist.append(os.path.join(directory, file))

                # Если были найдены музыкальные файлы, играем первый трек
                if len(self.playlist) > 0:
                    self.current_track = 0
                    self.play_track()

        def play_track(self):
            # Воспроизводим текущий трек
            # pygame.mixer.music.load(self.playlist[self.current_track])
            # pygame.mixer.music.play()
            # self.play_button.config(text="⏸️")
            self.track_name.set(os.path.basename(self.playlist[self.current_track]))

            # Загружаем и играем выбранный трек
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

            # Обновляем виджет с названием трека
            self.track.set(self.playlist[self.current_track])

            # Ожидаем окончания проигрывания для автоматического переключения на следующий трек
            while pygame.mixer.music.get_busy():
                window.update()
            self.play_next()

        def play_pause(self):
            # Ставим на паузу или возобновляем проигрывание текущего трека
            if pygame.mixer.music.get_busy() == True:
                pygame.mixer.music.pause()
                self.play_button.config(text="▶")
            else:
                pygame.mixer.music.unpause()
                self.play_button.config(text="⏸️")

        def play_prev(self):
            self.play_button.config(text="⏸️")
            # Играем предыдущий трек в плейлисте
            if self.current_track > 0:
                self.current_track -= 1
                self.play_track()
            else:
                # Если играет первый трек, то играем последний в плейлисте
                self.current_track = len(self.playlist) - 1
                self.play_track()

        def play_next(self): # Играем следующий трек в плейлисте 
            self.play_button.config(text="⏸️")
            if self.current_track < len(self.playlist) - 1:
                self.current_track += 1 
                self.play_track() 
            else: # Если достигли конца плейлиста, играем первый трек 
                self.current_track = 0; self.play_track()

        def change_volume(self, volume):
            # Изменяем громкость проигрывания
            pygame.mixer.music.set_volume(int(volume) / 100)

        def __del__(self):
            # Освобождаем занятые ресурсы при закрытии окна
            pygame.mixer.music.stop()
            pygame.mixer.quit()

    player = MusicPlayer(window)



# Будильник
def alarm():
    global alarm_x
    global alarm_y
    global alarmscountlabel
    cls()
    bind4()

    alarmlabel = Label(text='Ваши будильники:', bg = color, fg='#9CFC1A', relief='sunken', borderwidth=5, font='Arial 20')
    canvas.create_window(10, 100, window = alarmlabel, anchor= NW)

    alarm_button = Button(text='➕', bg = '#F0F0F0', font='Arial 20', command= addalarm)
    canvas.create_window(10, 150, window = alarm_button, anchor= NW)

    reload_button = Button(text='🔄', bg = '#F0F0F0', font='Arial 22', width=-2, command= alarm)
    canvas.create_window(10, 210, window = reload_button, anchor= NW)

    reload_button = Button(text='🧺', bg = '#F0F0F0', font='Arial 22', width=-2, command= alarm_clear)
    canvas.create_window(10, 273, window = reload_button, anchor= NW)

    alarm_x = 80
    # 110
    alarm_y = 110

    try:
        pat = Path('other','alarms.txt')
        with open(pat, 'r') as file:
            for alarms in file:
                alarmscountlabel = Label(text=alarms.replace('\n', ''), bg = color, fg='#39FC1A', relief='sunken', borderwidth=2, font='Arial 20')

                alarm_y += 40
                if alarm_y >= 520:
                    alarm_x += 120
                    alarm_y = 110
                    alarm_y += 40
                canvas.create_window(alarm_x, alarm_y, window = alarmscountlabel, anchor= NW, tag= 'Time')
    except:
        quiq()

def addalarm():
    global hoursalarm
    global minalarm
    global alarmwin, timephon

    unbind()

    alarmwin = Toplevel(bg=color)
    alarmwin.geometry('400x300')
    alarmwin.title('Новый будильник')
    alarmwin.resizable(0, 0)

    canvastime = Canvas(alarmwin, height=300, width= 400)

    timephon = PhotoImage(file=(Path('other', 'time.png')))

    canvastime.pack()

    clockicon = PhotoImage(file = Path('icons','clock.png'))
    alarmwin.iconphoto(False, clockicon)

    Label(alarmwin, text=':', bg= '#1E1E1E', fg = 'white', font='Arial 50').place(x=132, y= 100)
    Button(alarmwin, text='Установить', bg = '#20BBFF', font='Arial 19', height=2, command = addalarm_done, relief=RIDGE, activebackground= '#20BBFF').place(x = 240, y = 102)

    hoursalarm = Entry(alarmwin, font='Arial 50', width=2)
    hoursalarm.place(x= 50, y = 100)

    hour = datetime.now()
    hoursalarm.insert(1,hour.strftime('%H'))

    minalarm = Entry(alarmwin, font='Arial 50', width=2)
    minalarm.place(x= 160, y = 100)

    minute = datetime.now()
    minalarm.insert(1, minute.strftime('%M'))

    hoursalarm.focus_set()

    hoursalarm.bind('<Right>', move_down)
    minalarm.bind('<Left>', move_up)

    alarmwin.bind('<Return>', lambda c: addalarm_done())

    canvastime.create_image(0, 0, anchor = NW, image=timephon)
    # alarmwin.mainloop()
def addalarm_done():
    pat = Path('other','alarms.txt')
    with open(pat, 'a') as file:
        file.write(f'{hoursalarm.get()}:{minalarm.get()}:00\n')
    alarm()
    alarmwin.destroy()

def alarm_clear():
    os.remove(Path('other','alarms.txt'))
    file = open(Path('other','alarms.txt'), 'w')
    file.close()
    alarm()

def alarm_rang():
    global timec
    rangwindow = Toplevel(bg = '#A3E3FF', relief='sunken', borderwidth=5)

    rangwindow.geometry('200x100')
    rangwindow.resizable(0, 0)
    rangwindow.title('Время')
    rangwindow.attributes("-topmost",True)

    clockicon = PhotoImage(file = Path('icons','clock.png'))
    rangwindow.iconphoto(False, clockicon)

    Label(rangwindow, text = dat, font='Arial 20', bg='#A3E3FF').pack()
    pygame.mixer.Channel(3).play(pygame.mixer.Sound(Path('other', 'sound8.mp3')))

# Таймер
def timer():
    global alarm_x
    global alarm_y
    global alarmscountlabel
    cls()
    bind4()

    alarmlabel = Label(text='Ваши таймеры:', bg = color, fg='#9CFC1A', relief='sunken', borderwidth=5, font='Arial 20')
    canvas.create_window(10, 100, window = alarmlabel, anchor= NW)

    alarm_button = Button(text='➕', bg = '#F0F0F0', font='Arial 20', command= addtimer)
    canvas.create_window(10, 150, window = alarm_button, anchor= NW)

    reload_button = Button(text='🔄', bg = '#F0F0F0', font='Arial 22', width=-2, command= timer)
    canvas.create_window(10, 210, window = reload_button, anchor= NW)

    reload_button = Button(text='🧺', bg = '#F0F0F0', font='Arial 22', width=-2, command= timer_clear)
    canvas.create_window(10, 273, window = reload_button, anchor= NW)

    alarm_x = 80
    # 110
    alarm_y = 110

    try:
        pat = Path('other','timers.txt')
        with open(pat, 'r') as file:
            for alarms in file:
                alarmscountlabel = Label(text=alarms.replace('\n', ''), bg = color, fg='#39FC1A', relief='sunken', borderwidth=2, font='Arial 20')

                alarm_y += 40
                if alarm_y >= 520:
                    alarm_x += 120
                    alarm_y = 110
                    alarm_y += 40
                canvas.create_window(alarm_x, alarm_y, window = alarmscountlabel, anchor= NW, tag= 'Time')
    except:
        quiq()
def start_timer(hours, minutes, seconds):
    # переводим время в секунды
    pat = Path('other','timers.txt')
    pat2 = Path('other','timers2.txt')
    timertime = f'{hours}:{minutes}:{seconds}'

    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    # создаем функцию для запуска таймера в новом потоке
    def start_timer_thread():
        print("Таймер запущен на {0} часов {1} минут {2} секунд".format(hours, minutes, seconds))

        time.sleep(total_seconds)

        with open(pat) as infile, open(pat2, "w") as outfile:
            for line in infile:
                if timertime not in line:
                    outfile.write(line)
        os.remove(pat)
        os.rename(pat2, pat)

        timer()
        alarm_rang()
    
    # запускаем функцию в отдельном потоке, чтобы не блокировать основной поток
    t = threading.Thread(target=start_timer_thread)
    t.start()

def addtimer():
    global hourstimer
    global mintimer
    global sectimer
    global timerwin, timephon1

    unbind()

    timerwin = Toplevel(bg=color)
    timerwin.geometry('400x300')
    timerwin.title('Новый таймер')
    timerwin.resizable(0, 0)

    clockicon = PhotoImage(file = Path('icons','clock.png'))
    timerwin.iconphoto(False, clockicon)

    canvastime1 = Canvas(timerwin, height=300, width= 400)

    timephon1 = PhotoImage(file=(Path('other', 'time.png')))

    Button(timerwin, text='Установить', bg = '#20BBFF', font='Arial 19', height=2, command = addtimer_done, relief=RIDGE, activebackground= '#20BBFF').place(x = 200, y = 200)

    hourstimer = Entry(timerwin, font='Arial 50', width=2)
    hourstimer.place(x= 50, y = 100)

    hourstimer.insert(1,00)

    mintimer = Entry(timerwin, font='Arial 50', width=2)
    mintimer.place(x= 160, y = 100)

    mintimer.insert(1, 00)

    sectimer = Entry(timerwin, font='Arial 50', width=2)
    sectimer.place(x= 270, y = 100)

    Label(timerwin, text=':', bg= '#1E1E1E', fg='#B7FFFA', font='Arial 50').place(x=132, y= 100)

    Label(timerwin, text=':', bg= '#1E1E1E', fg='#B7FFFA', font='Arial 50').place(x=240, y= 100)

    sectimer.insert(1, 00)

    hourstimer.focus_set()

    hourstimer.bind('<Right>', move_down)
    mintimer.bind('<Left>', move_up)
    mintimer.bind('<Right>', move_down)
    sectimer.bind('<Left>', move_up)

    timerwin.bind('<Return>', lambda c: addtimer_done())

    canvastime1.create_image(0, 0, anchor = NW, image=timephon1)
    canvastime1.pack()
    # timerwin.mainloop()
def addtimer_done():
    pat = Path('other','timers.txt')
    
    with open(pat, 'a') as file:
        file.write(f'{hourstimer.get()}:{mintimer.get()}:{sectimer.get()}\n')
    start_timer(int(hourstimer.get()), int(mintimer.get()), int(sectimer.get()))
    timer()
    timerwin.destroy()
def timer_clear():
    os.remove(Path('other','timers.txt'))
    file = open(Path('other','timers.txt'), 'w')
    file.close()
    timer()

window = Tk()
window.geometry('800x600')
window.resizable(0,0)
window.title('Идеальный Гиппер-Обязательный Работник Ь')
window.config(bg = color)
window.protocol("WM_DELETE_WINDOW",exit)
window.focus_force()

icon = PhotoImage(file = Path('icons','igor64.png'))
window.iconphoto(False, icon)

datpl= Label(text='Дата', fg = color, font=('Times New Roman', 15), bg = color)
datpl.place(x=800,y=3, anchor=NE)
todaypl = Label(text='Время', fg = color, font=('Times New Roman', 15), bg = color)
todaypl.place(x=0, y=3)

canvasbutton = Canvas(bg=color,height=558, width=795)
canvas = Canvas(bg=color,height=600, width=800)

Welcome = Label(text= "И.Г.О.Р.Ь", fg= "#3AE99C", bg= color, font= "Corbel, 17", width=1000)
Welcome.pack()

combut = Button(text="", bg= "#642B2B", font= "Calibri 10",command=comman)
combut.place(x = 787, y = 572)

window.bind('<KeyPress-Tab>', lambda c: comman())

pag = -1

start()
buttons()
time_change


canvasbutton.place(x = 2.5,y = 40)
canvas.pack()
window.mainloop()
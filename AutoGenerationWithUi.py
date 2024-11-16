from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from ast import main
import os
#import pandas as pd
#import openpyxl
import numpy as np


def main():
    print("main") 
    GUI()

def btnPathClc():
    filename = filedialog.askdirectory()
    lblPathText.configure(text = "Папка: " + filename, font = ("Arial", 14))

def GUI():
    lblPathText.grid(column = 0, row = 0)
    btnPath.grid(column = 1, row = 0)
    
    lblUserName.grid(column = 0, row = 1)
    txtUserName.grid(column = 1, row = 1)
    txtUserName.insert(0,"u0001")

    lblSNFlash.grid(column = 0, row = 2)
    txtSNFlash.grid(column = 1, row = 2)
    txtSNFlash.insert(0,"AVP000000001")

    lblIpSec.grid(column = 0, row = 3)
    txtIpSec1.grid(column = 0, row = 0)
    txtIpSec1.insert(0,"10")
    txtIpSec2.grid(column = 1, row = 0)
    txtIpSec2.insert(0,"236")
    txtIpSec3.grid(column = 2, row = 0)
    txtIpSec3.insert(0,"254")
    txtIpSec4.grid(column = 3, row = 0)
    txtIpSec4.insert(0,"1")
    frameIpSec.grid(column=1,row=3)
    
    tab_control.pack(expand = 1, fill = 'both') 
    window.mainloop() 



window = Tk()
window.geometry('600x400')
window.title("RSMOB Generator")

tab_control = ttk.Notebook(window)
batGen = ttk.Frame(tab_control)  
upoGen = ttk.Frame(tab_control) 
tab_control.add(batGen, text = 'Генерация контейнеров')  
tab_control.add(upoGen, text = 'Генерация ПО') 

lblPathText = Label(batGen, text = "Укажите путь для создания папки", font = ("Arial", 14)) 
#lblPathText.pack(side = LEFT)
btnPath = Button(batGen, text = "Выбрать путь", command = btnPathClc, width = 15)
#btnPath.pack(side = LEFT)

lblUserName = Label(batGen, text = "Укажите имя клиента: ", font = ("Arial", 14))
#lblUserName.pack(side = LEFT)
txtUserName = Entry(batGen, width = 18)
#txtUserName.pack(side = LEFT)

lblSNFlash = Label(batGen, text = "Укажите SN ключа: ", font = ("Arial", 14))
txtSNFlash = Entry(batGen, width = 18)

lblIpSec = Label(batGen, text = "Укажите IPSec клиента: ", font = ("Arial", 14))
frameIpSec = ttk.Frame(batGen)
txtIpSec1 = Entry(frameIpSec, justify = CENTER, width = 4)
txtIpSec2 = Entry(frameIpSec, justify = CENTER, width = 4)
txtIpSec3 = Entry(frameIpSec, justify = CENTER, width = 4)
txtIpSec4 = Entry(frameIpSec, justify = CENTER, width = 4)

if __name__ == "__main__":main()
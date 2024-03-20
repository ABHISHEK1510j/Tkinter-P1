# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:37:43 2024

@author: ABHISHEK
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
a=tk.Tk()
a1=tk.Label(a,text='Calculator',font='Bell 20',fg='red',bg='blue')
a1.grid(row=0,column=5,padx=400,pady=10)

def Button_back():
    b1=tk.Button(a,text='back',fg='red',height=5,width=10,command=Button_settings)
    b1.grid(row=1,column=6)
def Button_settings():
    b2=tk.Button(a,text='settings',fg='red',height=5,width=10,command=Button_back)
    b2.grid(row=1,column=6)
#a2=tk.Button(a,text='Settings',fg='maroon',bg='black',height=5,width=10,command=Button_back)
#a2.grid(row=1,column=6)
Button_settings()
a.mainloop() 
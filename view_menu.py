import tkinter as tk
from tkinter import Menu
global time
import time
import datetime
from time import strftime
global window
global menu
global button_background
global button_text
global credential
global count
import os
import sys

#Dictonaries-----------------------------------------------------------
credential = {'HHS':{'password':'2021',},'ADMIN':{'password':'2021',},'Tech':{'password':'2021',},'':{'password':'',}}

#Fonts------------------------------------------------------------------------------------------------------------------------------------------------------------
global font_global
global font_global_15
global font_global_20
font_global = ("Comic Sans MS", 10, "bold")
font_global_15 = ("Comic Sans MS", 15, "bold")
font_global_20 = ("Comic Sans MS", 20, "bold")
button_background = ('green')
button_text = ('white')

#Define Functions----------------------------------------------------------------------------------------------------------------------------------------------------
def pizza_palace():
    window.destroy()
    os.system("python joshua_paterson_as91896_henderson_pizza_palace.py")
    sys.exit()

def open_evening():
    window.destroy()
    os.system("python open_evening_script.py")
    sys.exit()
    
def login():
    from tkinter import messagebox
    tk.messagebox.showinfo('Login/HomePage','You have made it to the Login/HomePage!')    

def new_order():
    from tkinter import messagebox
    tk.messagebox.showinfo('Place a new order','You have made it to the place a new order!')    

def view_menu():
        canvas = tk.Canvas(window, width = 725, height = 700)      
        canvas.pack()      
        img1 = tk.PhotoImage(file="images/henderson_pizza_palace/menu.png")
        canvas.create_image(375,350, image=img1)

        b1 = tk.Button(window, text =("Place a new order"),bg=button_background, fg=button_text, font=font_global, width=20, command=new_order)
        b1.pack()
        b1.place(relx=.02, rely=.95)
        b2 = tk.Button(window, text =("Login/HomePage"),bg=button_background, fg=button_text, font=font_global, width=20, command=login)
        b2.pack()
        b2.place(relx=.800, rely=.95)
        window.mainloop()
  
def dtime():
    e = datetime.datetime.now()
    info.config(text = "%s/%s/%s" % (e.day, e.month, e.year)+ "\n"+ strftime('%H:%M:%S %p'))
    info.after(1, dtime)
    
def restart():
    window.destroy()
    os.system("python template.py")
    sys.exit()
    
def leave():
        from tkinter import messagebox
        leave_box = tk.messagebox.askquestion ('Quit Program','Are you sure you want to quit the application?',icon = 'warning')
        if leave_box == 'yes':
            window.destroy()
            os.system("python jp_software.py")
            sys.exit()
        else:
                tk.messagebox.showinfo('Return','Returning back to the application.')    

def system_logout():
        from tkinter import messagebox
        leave_box = tk.messagebox.askquestion ('System Log Off','Are you sure you want to log out of the computer?',icon = 'warning')
        if leave_box == 'yes':
                os.system("shutdown -l")
    
def system_restart():
        from tkinter import messagebox
        leave_box = tk.messagebox.askquestion ('System Restart','Are you sure you want to restart the computer?',icon = 'warning')
        if leave_box == 'yes':
                os.system("shutdown /r /t 0")
    
def system_shutdown():
        from tkinter import messagebox
        leave_box = tk.messagebox.askquestion ('System Shutdown','Are you sure you want to shutdown the application and the computer?',icon = 'warning')
        if leave_box == 'yes':
                os.system("shutdown /s /t 0")

#Window Function------------------------------------------------------------------------------------------------------------------------------------------------------
window=tk.Tk()
window.geometry('1000x700')
window.title("Henderson Pizza Palace Menu")
window.iconphoto(False, tk.PhotoImage(file="images/henderson_pizza_palace_logo.png"))

global info
info = tk.Label(window, text="""""", font=font_global,height =2,border=0 )
info.pack()
info.place(relx=0.05,rely=0.001)
dtime()

# JP Software Menu----------------------------------------------------------------------------------------------------------------------------------------------------------              
openevening_logo = tk.PhotoImage(file="images/open_evening/hhs-logo.png")
pizzapalace_logo = tk.PhotoImage(file="images/henderson_pizza_palace_logo.png")
jp_software_logo_img = tk.PhotoImage(file="images/jp_software-icon-2.png")
jp_software_control = tk.Menubutton(window, image=jp_software_logo_img ,height =35, width=45, border=0)      
jp_software_control.menu = Menu(jp_software_control)  
jp_software_control["menu"]= jp_software_control.menu  
jp_software_control.menu.add_command(label = "", image=openevening_logo, command=open_evening)
jp_software_control.menu.add_command(label = "", image=pizzapalace_logo, command=pizza_palace)
jp_software_control.menu.add_command(label = "Leave Application", command=leave)
jp_software_control.menu.add_command(label = "Restart Application", command=restart)
jp_software_control.menu.add_command(label = "Shut Down PC",command=system_shutdown)
jp_software_control.menu.add_command(label = "Restart PC",command=system_restart)
jp_software_control.menu.add_command(label = "Log Off PC",command=system_logout)
jp_software_control.pack() 
jp_software_control.place(relx=0.0,rely=0.003)
view_menu()
window.mainloop()

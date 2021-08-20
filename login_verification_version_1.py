def pizza_palace():
    window.destroy()
    os.system("python joshua_paterson_as91896_henderson_pizza_palace.py")
    sys.exit()

def open_evening():
    window.destroy()
    os.system("python open_evening_script.py")
    sys.exit()

def login():
    global input_login_user
    global input_login_pass
    global label_1
    global label_2
    global b1
    
    label_1 = tk.Label(window,font=font_global,text="Please insert your username?")
    label_2 = tk.Label(window,font=font_global,text="Please insert your password?")
    label_1.pack()
    label_2.pack()
    label_1.place(relx=0.33,rely=0.70)
    label_2.place(relx=0.33,rely=0.75)
        
    input_login_user = tk.Text(window,font=font_global,height = 1,width = 10)
    input_login_pass = tk.Text(window,font=font_global,height = 1,width = 10)
    input_login_user.pack()
    input_login_pass.pack()
    input_login_user.place(relx=0.53,rely=0.70)
    input_login_pass.place(relx=0.53,rely=0.75)
                                                     
    b1 = tk.Button(window, text ="View menu",bg=button_background, fg=button_text, font=font_global, width=20, command=view_menu)
    b1.pack()
    b1.place(relx=0.50,rely=0.8) 
    
    b2 = tk.Button(window, text ="Place a new order",bg=button_background, fg=button_text, font=font_global, width=20, command=verify)
    b2.pack()
    b2.place(relx=0.30,rely=0.8) 
    window.mainloop()


def verify():
    username = input_login_user.get(1.0, "end-1c").strip()
    password = input_login_pass.get(1.0, "end-1c").strip()

    if username in credential:
        if password == credential[username]['password']:
            new_order()
        else:
            from tkinter import messagebox
            tk.messagebox.showerror('Incorret Username/Password','Sorry, you have entered an incorrect username/password.')

    else:
        from tkinter import messagebox
        tk.messagebox.showerror('Incorret Username/Password','Sorry, you have entered an incorrect username/password.')

def view_menu():
        from tkinter import messagebox
        tk.messagebox.showinfo('View Menu','You have made it to the menu script!')

def new_order():
        from tkinter import messagebox
        tk.messagebox.showinfo ('Place a new order','You have made it to the place a new order script!')

  
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
window.title("Henderson Pizza Palace")
window.iconphoto(False, tk.PhotoImage(file="images/henderson_pizza_palace_logo.png"))

global info
info = tk.Label(window, text="""""", font=font_global,height =2,border=0 )
info.pack()
info.place(relx=0.45,rely=0.934)
dtime()

global canva
canva = tk.Canvas(window, width = 1000, height = 750)      
canva.pack()      
img = tk.PhotoImage(file="images/henderson_pizza_palace/henderson_pizza_palace_logo_w_word_1.png")      
canva.create_image(500,250, image=img)

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
login()
window.mainloop()

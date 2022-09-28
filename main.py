from tkinter import *
from tkinter import ttk
import time
from obeserver import Inicio, Pid
import obeserver




root = Tk()
root.title('Obeservador - Ph0b14')
root.iconbitmap(r'C:\Users\Berg\Documents\Projetos vscode\Python Projects\CHALLENGE_100%\phobia.ico')
root.geometry("950x650")
bg = PhotoImage(file='Challenge2.png')
root.resizable(0,0)
label1 = Label(root, image=bg)
label1.place(x=0,y=0)
root.config(background='black')

def increment(*args):
    for i in range(100):
        p1["value"] = i+1
        root.update()
        time.sleep(0.1)
p1 = ttk.Progressbar(root, length=400, cursor='spider',
                        mode="determinate",
                        orient=HORIZONTAL)
p1.pack()
p1.place(x=270,y=320)

is_on = True

# Create Label to display the message
label = Label()

# Define our switch function
def button_mode():
    global is_on

#Determine it is on or off
    if is_on:
        on_.config(image=on)
        label.config(bg ="black", fg= "black")
        is_on = False
    else:
        on_.config(image = off)
        label.config(bg="black", fg="black")
        is_on = True
        Pid()


# Define Our Images
on = PhotoImage(file ="on4.png")
off = PhotoImage(file ="off4.png")
def comandos():
    button_mode()
    increment()
    Inicio()
    
# Create A Button
on_= Button(root,image =off,bd =0,command = comandos, background='black')
#on_.pack(pady = 50)
on_.place(x=800,y=30)

'''if  == 1:
    def change_color():
        #box.pack(padx=270, pady=320)
        current_color = box.cget("background")
        next_color = "black" if current_color == "red" else "red"
        box.config(background=next_color,)
        root.after(500, change_color)
    box = Text(root, background="green")
    box = Label(root, text = "Ransomware Detectado!!", fg = 'white', width=200, height=5, font=('Helvetica bold', 20))
    box.pack()
    change_color()'''
root.mainloop()


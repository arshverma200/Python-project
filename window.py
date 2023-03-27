from tkinter import *
import math
from tkinter import messagebox,filedialog
from tkcalendar import Calendar
import datetime
import time
import winsound
from threading import *
from pytube import YouTube
from PIL import Image, ImageTk
import turtle,os
import pygame
from pygame.locals import *
import random,qrcode


def btn_clicked():
    print("Button Clicked")


window = Tk()
window.title("MULTI UTILITY")
window.geometry("1302x748")
window.configure(bg = "#040404")
canvas = Canvas(
    window,
    bg = "#040404",
    height = 748,
    width = 1302,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    661.5, 407.0,
    image=background_img)

##calender
def calender():


    # Create Object
    root = Tk()
    root.title("Calender")
    # Set geometry
    root.geometry("400x400")

    # Add Calendar
    cal = Calendar(root, selectmode='day',
                   year=2022, month=12,
                   day=19)

    cal.pack(pady=20)

    def grad_date():
        date.config(text="Selected Date is: " + cal.get_date())

    # Add Button and Label
    Button(root, text="Get Date",
           command=grad_date).pack(pady=20)

    date = Label(root, text="")
    date.pack(pady=20)

    # Execute Tkinter
    root.mainloop()


img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = calender,
    relief = "flat")

b0.place(
    x = 1025, y = 348,
    width = 166,
    height = 82)

#sc

#scientific
def sc():


    root = Tk()
    root.title("Team knights- CALCULATOR")
    root.configure(background='white')
    root.resizable(width=False, height=False)
    root.geometry("480x568+450+90")
    calc = Frame(root)
    calc.grid()

    class Calc():
        def _init_(self):
            self.total = 0
            self.current = ''
            self.input_value = True
            self.check_sum = False
            self.op = ''
            self.result = False

        def numberEnter(self, num):
            self.result = False
            firstnum = txtDisplay.get()
            secondnum = str(num)
            if self.input_value:
                self.current = secondnum
                self.input_value = False
            else:
                if secondnum == '.':
                    if secondnum in firstnum:
                        return
                self.current = firstnum + secondnum
            self.display(self.current)

        def sum_of_total(self):
            self.result = True
            self.current = float(self.current)
            if self.check_sum == True:
                self.valid_function()
            else:
                self.total = float(txtDisplay.get())

        def display(self, value):
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, value)

        def valid_function(self):
            if self.op == "add":
                self.total += self.current
            if self.op == "sub":
                self.total -= self.current
            if self.op == "multi":
                self.total *= self.current
            if self.op == "divide":
                self.total /= self.current
            if self.op == "mod":
                self.total %= self.current
            self.input_value = True
            self.check_sum = False
            self.display(self.total)

        def operation(self, op):
            self.current = float(self.current)
            if self.check_sum:
                self.valid_function()
            elif not self.result:
                self.total = self.current
                self.input_value = True
            self.check_sum = True
            self.op = op
            self.result = False

        def Clear_Entry(self):
            self.result = False
            self.current = "0"
            self.display(0)
            self.input_value = True

        def All_Clear_Entry(self):
            self.Clear_Entry()
            self.total = 0

        def pi(self):
            self.result = False
            self.current = math.pi
            self.display(self.current)

        def tau(self):
            self.result = False
            self.current = math.tau
            self.display(self.current)

        def e(self):
            self.result = False
            self.current = math.e
            self.display(self.current)

        def mathPM(self):
            self.result = False
            self.current = -(float(txtDisplay.get()))
            self.display(self.current)

        def squared(self):
            self.result = False
            self.current = math.sqrt(float(txtDisplay.get()))
            self.display(self.current)

        def cos(self):
            self.result = False
            self.current = math.cos(math.radians(float(txtDisplay.get())))
            self.display(self.current)

        def cosh(self):
            self.result = False
            self.current = math.cosh(math.radians(float(txtDisplay.get())))
            self.display(self.current)

        def tan(self):
            self.result = False
            self.current = math.tan(math.radians(float(txtDisplay.get())))
            self.display(self.current)

        def tanh(self):
            self.result = False
            self.current = math.tanh(math.radians(float(txtDisplay.get())))
            self.display(self.current)

        def sin(self):
            self.result = False
            self.current = math.sin(math.radians(float(txtDisplay.get())))
            self.display(self.current)

        def sinh(self):
            self.result = False
            self.current = math.sinh(math.radians(float(txtDisplay.get())))
            self.display(self.current)

        def log(self):
            self.result = False
            self.current = math.log(float(txtDisplay.get()))
            self.display(self.current)

        def exp(self):
            self.result = False
            self.current = math.exp(float(txtDisplay.get()))
            self.display(self.current)

        def acosh(self):
            self.result = False
            self.current = math.acosh(float(txtDisplay.get()))
            self.display(self.current)

        def asinh(self):
            self.result = False
            self.current = math.asinh(float(txtDisplay.get()))
            self.display(self.current)

        def expm1(self):
            self.result = False
            self.current = math.expm1(float(txtDisplay.get()))
            self.display(self.current)

        def lgamma(self):
            self.result = False
            self.current = math.lgamma(float(txtDisplay.get()))
            self.display(self.current)

        def degrees(self):
            self.result = False
            self.current = math.degrees(float(txtDisplay.get()))
            self.display(self.current)

        def log2(self):
            self.result = False
            self.current = math.log2(float(txtDisplay.get()))
            self.display(self.current)

        def log10(self):
            self.result = False
            self.current = math.log10(float(txtDisplay.get()))
            self.display(self.current)

        def log1p(self):
            self.result = False
            self.current = math.log1p(float(txtDisplay.get()))
            self.display(self.current)

    added_value = Calc()

    txtDisplay = Entry(calc, font=('Helvetica', 20, 'bold'),
                       bg='black', fg='white',
                       bd=30, width=28, justify=RIGHT)
    txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
    txtDisplay.insert(0, "0")

    numberpad = "789456123"
    i = 0
    btn = []
    for j in range(2, 5):
        for k in range(3):
            btn.append(Button(calc, width=6, height=2,
                              bg='black', fg='white',
                              font=('Helvetica', 20, 'bold'),
                              bd=4, text=numberpad[i]))
            btn[i].grid(row=j, column=k, pady=1)
            btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
            i += 1

    btnClear = Button(calc, text=chr(67), width=6,
                      height=2, bg='powder blue',
                      font=('Helvetica', 20, 'bold')
                      , bd=4, command=added_value.Clear_Entry
                      ).grid(row=1, column=0, pady=1)

    btnAllClear = Button(calc, text=chr(67) + chr(69),
                         width=6, height=2,
                         bg='powder blue',
                         font=('Helvetica', 20, 'bold'),
                         bd=4,
                         command=added_value.All_Clear_Entry
                         ).grid(row=1, column=1, pady=1)

    btnsq = Button(calc, text="\u221A", width=6, height=2,
                   bg='powder blue', font=('Helvetica',
                                           20, 'bold'),
                   bd=4, command=added_value.squared
                   ).grid(row=1, column=2, pady=1)

    btnAdd = Button(calc, text="+", width=6, height=2,
                    bg='powder blue',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=lambda: added_value.operation("add")
                    ).grid(row=1, column=3, pady=1)

    btnSub = Button(calc, text="-", width=6,
                    height=2, bg='powder blue',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=lambda: added_value.operation("sub")
                    ).grid(row=2, column=3, pady=1)

    btnMul = Button(calc, text="x", width=6,
                    height=2, bg='powder blue',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=lambda: added_value.operation("multi")
                    ).grid(row=3, column=3, pady=1)

    btnDiv = Button(calc, text="/", width=6,
                    height=2, bg='powder blue',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=lambda: added_value.operation("divide")
                    ).grid(row=4, column=3, pady=1)

    btnZero = Button(calc, text="0", width=6,
                     height=2, bg='black', fg='white',
                     font=('Helvetica', 20, 'bold'),
                     bd=4, command=lambda: added_value.numberEnter(0)
                     ).grid(row=5, column=0, pady=1)

    btnDot = Button(calc, text=".", width=6,
                    height=2, bg='powder blue',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=lambda: added_value.numberEnter(".")
                    ).grid(row=5, column=1, pady=1)
    btnPM = Button(calc, text=chr(177), width=6,
                   height=2, bg='powder blue', font=('Helvetica', 20, 'bold'),
                   bd=4, command=added_value.mathPM
                   ).grid(row=5, column=2, pady=1)

    btnEquals = Button(calc, text="=", width=6,
                       height=2, bg='powder blue',
                       font=('Helvetica', 20, 'bold'),
                       bd=4, command=added_value.sum_of_total
                       ).grid(row=5, column=3, pady=1)
    # ROW 1 :
    btnPi = Button(calc, text="pi", width=6,
                   height=2, bg='black', fg='white',
                   font=('Helvetica', 20, 'bold'),
                   bd=4, command=added_value.pi
                   ).grid(row=1, column=4, pady=1)

    btnCos = Button(calc, text="Cos", width=6,
                    height=2, bg='black', fg='white',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=added_value.cos
                    ).grid(row=1, column=5, pady=1)

    btntan = Button(calc, text="tan", width=6,
                    height=2, bg='black', fg='white',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=added_value.tan
                    ).grid(row=1, column=6, pady=1)

    btnsin = Button(calc, text="sin", width=6,
                    height=2, bg='black', fg='white',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=added_value.sin
                    ).grid(row=1, column=7, pady=1)

    # ROW 2 :
    btn2Pi = Button(calc, text="2pi", width=6,
                    height=2, bg='black', fg='white',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=added_value.tau
                    ).grid(row=2, column=4, pady=1)

    btnCosh = Button(calc, text="Cosh", width=6,
                     height=2, bg='black', fg='white',
                     font=('Helvetica', 20, 'bold'),
                     bd=4, command=added_value.cosh
                     ).grid(row=2, column=5, pady=1)

    btntanh = Button(calc, text="tanh", width=6,
                     height=2, bg='black', fg='white',
                     font=('Helvetica', 20, 'bold'),
                     bd=4, command=added_value.tanh
                     ).grid(row=2, column=6, pady=1)

    btnsinh = Button(calc, text="sinh", width=6,
                     height=2, bg='black', fg='white',
                     font=('Helvetica', 20, 'bold'),
                     bd=4, command=added_value.sinh
                     ).grid(row=2, column=7, pady=1)

    # ROW 3 :
    btnlog = Button(calc, text="log", width=6,
                    height=2, bg='black', fg='white',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=added_value.log
                    ).grid(row=3, column=4, pady=1)

    btnExp = Button(calc, text="exp", width=6, height=2,
                    bg='black', fg='white',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=added_value.exp
                    ).grid(row=3, column=5, pady=1)

    btnMod = Button(calc, text="Mod", width=6,
                    height=2, bg='black', fg='white',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=lambda: added_value.operation("mod")
                    ).grid(row=3, column=6, pady=1)

    btnE = Button(calc, text="e", width=6,
                  height=2, bg='black', fg='white',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command=added_value.e
                  ).grid(row=3, column=7, pady=1)

    # ROW 4 :
    btnlog10 = Button(calc, text="log10", width=6,
                      height=2, bg='black', fg='white',
                      font=('Helvetica', 20, 'bold'),
                      bd=4, command=added_value.log10
                      ).grid(row=4, column=4, pady=1)

    btncos = Button(calc, text="log1p", width=6,
                    height=2, bg='black', fg='white',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=added_value.log1p
                    ).grid(row=4, column=5, pady=1)

    btnexpm1 = Button(calc, text="expm1", width=6,
                      height=2, bg='black', fg='white',
                      font=('Helvetica', 20, 'bold'),
                      bd=4, command=added_value.expm1
                      ).grid(row=4, column=6, pady=1)

    btngamma = Button(calc, text="gamma", width=6,
                      height=2, bg='black', fg='white',
                      font=('Helvetica', 20, 'bold'),
                      bd=4, command=added_value.lgamma
                      ).grid(row=4, column=7, pady=1)
    # ROW 5 :
    btnlog2 = Button(calc, text="log2", width=6,
                     height=2, bg='black', fg='white',
                     font=('Helvetica', 20, 'bold'),
                     bd=4, command=added_value.log2
                     ).grid(row=5, column=4, pady=1)

    btndeg = Button(calc, text="deg", width=6,
                    height=2, bg='black', fg='white',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=added_value.degrees
                    ).grid(row=5, column=5, pady=1)

    btnacosh = Button(calc, text="acosh", width=6,
                      height=2, bg='black', fg='white',
                      font=('Helvetica', 20, 'bold'),
                      bd=4, command=added_value.acosh
                      ).grid(row=5, column=6, pady=1)

    btnasinh = Button(calc, text="asinh", width=6,
                      height=2, bg='black', fg='white',
                      font=('Helvetica', 20, 'bold'),
                      bd=4, command=added_value.asinh
                      ).grid(row=5, column=7, pady=1)

    lblDisplay = Label(calc, text="Scientific Calculator",
                       font=('Helvetica', 30, 'bold'),
                       bg='black', fg='white', justify=CENTER)

    lblDisplay.grid(row=0, column=4, columnspan=4)

    def iExit():
        iExit = tkinter.messagebox.askyesno("Scientific Calculator",
                                            "Do you want to exit ?")
        if iExit > 0:
            root.destroy()
            return

    def Scientific():
        root.resizable(width=False, height=False)
        root.geometry("944x568+0+0")

    def Standard():
        root.resizable(width=False, height=False)
        root.geometry("480x568+0+0")

    menubar = Menu(calc)

    # ManuBar 1 :
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label="Standard", command=Standard)
    filemenu.add_command(label="Scientific", command=Scientific)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=iExit)

    # ManuBar 2 :
    editmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Edit', menu=editmenu)
    editmenu.add_command(label="Cut")
    editmenu.add_command(label="Copy")
    editmenu.add_separator()
    editmenu.add_command(label="Paste")

    root.config(menu=menubar)

    root.mainloop()
img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = sc,
    relief = "flat")

b1.place(
    x = 110, y = 348,
    width = 166,
    height = 82)

##notepad

def notepad():
    root = Tk()
    root.geometry("900x500+100+50")
    root.title("Notepad")
    def openFiles():
        op = filedialog.askopenfile(title="Select file", defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")],)
        if op != None:

            for i in op:
                txt_area.insert(END, str(i))
            op.close()

    def saveAs():
        op = filedialog.asksaveasfile(title="SAVE AS", defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")],)
        if op != None:
            op.write(txt_area.get('1.0', END))
            op.close()
            messagebox.showinfo("SAVE AS", "File has been saved")

    def save_file():
        if var_filename.get() == "":
            saveAs()
        else:
            op = open(var_filename.get(), "w")
            op.write(txt_area.get('1.0', END))
            op.close()
            messagebox.showinfo("Save As", "File has been saved")

    btn = Button(root, text="OPEN", command=openFiles, bg='#ffffff', activebackground='grey', relief=GROOVE).place(x=30,
                                                                                                                   y=10,
                                                                                                                   width=100)
    btn = Button(root, text="SAVE", command=save_file, bg='#ffffff', activebackground='grey', relief=GROOVE).place(
        x=130, y=10, width=100)
    btn = Button(root, text="SAVE AS", command=saveAs, bg='#ffffff', activebackground='grey', relief=GROOVE).place(
        x=230, y=10, width=100)
    var_filename=StringVar()
    lbl_name = Label(root, text="FileName", font=("arial", 15))
    lbl_name.place(x=50, y=100)
    txt_area = Text(root, font=("arial", 15), bd=2, relief=RIDGE)
    txt_area.place(x=0, y=50, width=1600, height=800)
    root.mainloop()




img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = notepad,
    relief = "flat")

b2.place(
    x = 461, y = 346,
    width = 166,
    height = 82)

##qr
def qr():
    cp = Tk()
    cp.title('QR CODE')
    cp.geometry('700x250')
    cp.config(bg='#e52165')

    def generate():
        img = qrcode.make(msg.get())
        type(img)
        img.save(f'{save_name.get()}.png')
        Label(cp, text='File Saved!', bg='#e52165', fg='black', font=('Arial Black', 8)).pack()

    def show():
        img = qrcode.make(msg.get())
        type(img)
        img.show()

    frame = Frame(cp, bg='#e52165')
    frame.pack(expand=True)

    # ENTER THE TEXT OR URL

    Label(frame, text='Enter the Text or URL : ', font=('Arial', 16),
          bg='#e52165').grid(row=0, column=0, sticky='w')

    msg = Entry(frame)
    msg.grid(row=0, column=1)

    # ENTER THE FILE NAME

    Label(frame, text='File Name(Save As) : ', font=('Arial', 16),
          bg='#e52165').grid(row=1, column=0, sticky='w')

    save_name = Entry(frame)
    save_name.grid(row=1, column=1)

    # BUTTONS TO SHOW OR SAVE QRCODE

    btn = Button(cp, text='Show QR code', bd='5', command=show, width=15)
    btn.pack()
    btn = Button(cp, text='Save QR code', command=generate, bd='5', width=15)
    btn.pack()

    cp.mainloop()


img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = qr,
    relief = "flat")

b3.place(
    x = 784, y = 338,
    width = 166,
    height = 82)

##Youtube video downlaoder

def yt():
    import tkinter as tk
    from pytube import YouTube

    def Download_Video():
        url = YouTube(str(link.get()))
        video = url.streams.first()
        video.download()
        tk.Label(window, text='Your Video is downloaded!', font='arial 15', fg="White", bg="#EC7063").place(x=10, y=140)

    window =tk.Tk()
    window.geometry("600x200")
    window.config(bg="#EC7063")
    window.resizable(width=False, height=False)
    window.title('YouTube Video Downloader')

    link = tk.StringVar()
    tk.Label(window, text='                   Youtube Video Downloader                    ', font='arial 20 bold',
             fg="White", bg="Black").pack()
    tk.Label(window, text='Paste Your YouTube Link Here:', font='arial 20 bold', fg="Black", bg="#EC7063").place(x=5,
                                                                                                                 y=60)
    link_enter = tk.Entry(window, width=53, textvariable=link, font='arial 15 bold', bg="lightgreen").place(x=5, y=100)

    tk.Button(window, text='DOWNLOAD VIDEO', font='arial 15 bold', fg="white", bg='black', padx=2,
              command=Download_Video).place(x=385, y=140)

    window.mainloop()

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = yt,
    relief = "flat")

b4.place(
    x = 110, y = 538,
    width = 166,
    height = 82)

##pingpong

def pingpong():
    # First, we will create screen
    screen_1 = turtle.Screen()
    screen_1.title("KNIGHT HAWKS-IV Ping-Pong Game")
    screen_1.bgcolor("light Blue")
    screen_1.setup(width=1050, height=650)

    # Left paddle
    left_paddle = turtle.Turtle()
    left_paddle.speed(0)
    left_paddle.shape("square")
    left_paddle.color("Red")
    left_paddle.shapesize(stretch_wid=4, stretch_len=1)  # 6,2
    left_paddle.penup()
    left_paddle.goto(-400, 0)

    # Right paddle
    right_paddle = turtle.Turtle()
    right_paddle.speed(0)
    right_paddle.shape("square")
    right_paddle.color("maroon")
    right_paddle.shapesize(stretch_wid=4, stretch_len=1)
    right_paddle.penup()
    right_paddle.goto(400, 0)

    # Ball of circle shape
    hit_ball = turtle.Turtle()
    hit_ball.speed(40)
    hit_ball.shape("circle")
    hit_ball.color("Black")
    hit_ball.penup()
    hit_ball.goto(0, 0)
    hit_ball.dx = 5
    hit_ball.dy = -5

    # Now, we will initialize the score
    left_player = 0
    right_player = 0

    # Displaying of the score
    sketch_1 = turtle.Turtle()
    sketch_1.speed(0)
    sketch_1.color("red")
    sketch_1.penup()
    sketch_1.hideturtle()
    sketch_1.goto(0, 260)
    sketch_1.write("Left Player : 0    Right Player: 0",
                   align="center", font=("Courier", 24, "normal"))

    # Implementing the functions for moving paddle vertically
    def paddle_L_up():
        y = left_paddle.ycor()
        y += 30  # 20
        left_paddle.sety(y)

    def paddle_L_down():
        y = left_paddle.ycor()
        y -= 30
        left_paddle.sety(y)

    def paddle_R_up():
        y = right_paddle.ycor()
        y += 30
        right_paddle.sety(y)

    def paddle_R_down():
        y = right_paddle.ycor()
        y -= 30
        right_paddle.sety(y)

    # Then, binding the keys for moving the paddles up and down.
    screen_1.listen()
    screen_1.onkeypress(paddle_L_up, "w")
    screen_1.onkeypress(paddle_L_down, "s")
    screen_1.onkeypress(paddle_R_up, "Up")
    screen_1.onkeypress(paddle_R_down, "Down")

    while True:
        screen_1.update()

        hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
        hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

        # Check all the borders
        if hit_ball.ycor() > 280:
            hit_ball.sety(280)
            hit_ball.dy *= -1

        if hit_ball.ycor() < -280:
            hit_ball.sety(-280)
            hit_ball.dy *= -1

        if hit_ball.xcor() > 500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            left_player += 1
            sketch_1.clear()
            sketch_1.write("Left_player : {}    Right_player: {}".format(
                left_player, right_player), align="center",
                font=("Courier", 24, "normal"))

        if hit_ball.xcor() < -500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            right_player += 1
            sketch_1.clear()
            sketch_1.write("Left_player : {}    Right_player: {}".format(
                left_player, right_player), align="center",
                font=("Courier", 24, "normal"))

        # Collision of ball and paddles
        if (hit_ball.xcor() > 360 and
            hit_ball.xcor() < 370) and (hit_ball.ycor() < right_paddle.ycor() + 40 and
                                        hit_ball.ycor() > right_paddle.ycor() - 40):
            hit_ball.setx(360)
            hit_ball.dx *= -1

        if (hit_ball.xcor() < -360 and
            hit_ball.xcor() > -370) and (hit_ball.ycor() < left_paddle.ycor() + 40 and
                                         hit_ball.ycor() > left_paddle.ycor() - 40):
            hit_ball.setx(-360)
            hit_ball.dx *= -1

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = pingpong,
    relief = "flat")

b5.place(
    x = 473, y = 538,
    width = 166,
    height = 82)

##flappy
def flappy():


    pygame.init()

    clock = pygame.time.Clock()
    fps = 50

    screen_width = 860
    screen_height = 790

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Flappy Bird KNIGHTHAWKS-IV')

    # define font
    font = pygame.font.SysFont('Bauhaus 93', 60)

    # define colours
    white = (0, 0, 0)

    # define game variables
    ground_scroll = 0
    scroll_speed = 6
    flying = False
    game_over = False
    pipe_gap = 160
    pipe_frequency = 1500  # milliseconds
    last_pipe = pygame.time.get_ticks() - pipe_frequency
    score = 0
    pass_pipe = False

    # load images
    bg = pygame.image.load('bg3.jpg')
    ground_img = pygame.image.load('ground.png')
    button_img = pygame.image.load('restart.png')

    # function for outputting text onto the screen
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def reset_game():
        pipe_group.empty()
        flappy.rect.x = 100
        flappy.rect.y = int(screen_height / 2)
        score = 0
        return score

    class Bird(pygame.sprite.Sprite):

        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            self.index = 0
            self.counter = 0
            for num in range(1, 4):
                img = pygame.image.load(f"bird{num}.png")    #ANIMATION OF BIRD
                self.images.append(img)
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.vel = 0
            self.clicked = False

        def update(self):

            if flying == True:
                # apply gravity
                self.vel += 0.5
                if self.vel > 8:
                    self.vel = 8
                if self.rect.bottom < 768:
                    self.rect.y += int(self.vel)

            if game_over == False:
                # jump
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.vel = -10
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                # handle the animation
                flap_cooldown = 5
                self.counter += 1

                if self.counter > flap_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0
                    self.image = self.images[self.index]

                # rotate the bird
                self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
            else:
                # point the bird at the ground
                self.image = pygame.transform.rotate(self.images[self.index], -90)

    class Pipe(pygame.sprite.Sprite):

        def __init__(self, x, y, position):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("pipe.png")
            self.rect = self.image.get_rect()
            # position variable determines if the pipe is coming from the bottom or top
            # position 1 is from the top, -1 is from the bottom
            if position == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
            elif position == -1:
                self.rect.topleft = [x, y + int(pipe_gap / 2)]

        def update(self):
            self.rect.x -= scroll_speed
            if self.rect.right < 0:
                self.kill()

    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def draw(self):
            action = False

            # get mouse position
            pos = pygame.mouse.get_pos()

            # check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    action = True

            # draw button
            screen.blit(self.image, (self.rect.x, self.rect.y))

            return action

    pipe_group = pygame.sprite.Group()
    bird_group = pygame.sprite.Group()

    flappy = Bird(100, int(screen_height / 2))

    bird_group.add(flappy)

    # create restart button instance
    button = Button(screen_width // 2 - 50, screen_height // 2 - 100, button_img)

    run = True
    while run:

        clock.tick(fps)

        # draw background
        screen.blit(bg, (0, 0))

        pipe_group.draw(screen)
        bird_group.draw(screen)
        bird_group.update()

        # draw and scroll the ground
        screen.blit(ground_img, (ground_scroll, 728))

        # check the score
        if len(pipe_group) > 0:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left \
                    and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right \
                    and pass_pipe == False:
                pass_pipe = True
            if pass_pipe == True:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    pass_pipe = False
        draw_text(str(score), font, white, int(screen_width / 2), 20)

        # look for collision
        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
            game_over = True
        # once the bird has hit the ground it's game over and no longer flying
        if flappy.rect.bottom >= 728:
            game_over = True
            flying = False

        if flying == True and game_over == False:
            # generate new pipes
            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > pipe_frequency:
                pipe_height = random.randint(-100, 100)
                btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
                top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)
                last_pipe = time_now

            pipe_group.update()

            ground_scroll -= scroll_speed
            if abs(ground_scroll) > 35:
                ground_scroll = 0

        # check for game over and reset
        if game_over == True:
            if button.draw():
                game_over = False
                score = reset_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
                flying = True

        pygame.display.update()

    pygame.quit()

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = flappy,
    relief = "flat")

b6.place(
    x = 787, y = 538,
    width = 166,
    height = 82)

canvas.create_text(
    242.0, 660.5,
    text = "  Youtube video downloader",
    fill = "#ffffff",
    font = ("None", int(24.0)))

canvas.create_text(
    882.0, 450.5,
    text = "QR- code Maker",
    fill = "#ffffff",
    font = ("None", int(24.0)))

canvas.create_text(
    698.5, 105.5,
    text = "Welcome to Multi-Utility App\n  ",
    fill = "#fffefe",
    font = ("None", int(64.0)))

canvas.create_text(
    545.0, 450.5,
    text = "   Notepad",
    fill = "#ffffff",
    font = ("None", int(24.0)))

canvas.create_text(
    234.0, 453.5,
    text = "Scientific calculator",
    fill = "#ffffff",
    font = ("None", int(24.0)))

canvas.create_text(
    595.0, 660.5,
    text = "Ping- Pong",
    fill = "#ffffff",
    font = ("None", int(24.0)))

canvas.create_text(
    873.0, 664.5,
    text = "   Flappy Bird",
    fill = "#ffffff",
    font = ("None", int(24.0)))

#alarm cloclk


def aarm():
    root = Tk()

    # Set geometry
    root.geometry("400x400")

    # Use Threading
    def Threading():
        t1 = Thread(target=alarm)
        t1.start()

    def alarm():
        # Infinite Loop
        while True:
            # Set Alarm
            set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

            # Wait for one seconds
            time.sleep(1)

            # Get current time
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time, set_alarm_time)

            # Check whether set alarm is equal to current time or not
            if current_time == set_alarm_time:
                print("Time to Wake up")
                # Playing sound
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

    # Add Labels, Frame, Button, Optionmenus
    Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
    Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

    frame = Frame(root)
    frame.pack()

    hour = StringVar(root)
    hours = ('00', '01', '02', '03', '04', '05', '06', '07',
             '08', '09', '10', '11', '12', '13', '14', '15',
             '16', '17', '18', '19', '20', '21', '22', '23', '24'
             )
    hour.set(hours[0])

    hrs = OptionMenu(frame, hour, *hours)
    hrs.pack(side=LEFT)

    minute = StringVar(root)
    minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
               '08', '09', '10', '11', '12', '13', '14', '15',
               '16', '17', '18', '19', '20', '21', '22', '23',
               '24', '25', '26', '27', '28', '29', '30', '31',
               '32', '33', '34', '35', '36', '37', '38', '39',
               '40', '41', '42', '43', '44', '45', '46', '47',
               '48', '49', '50', '51', '52', '53', '54', '55',
               '56', '57', '58', '59', '60')
    minute.set(minutes[0])

    mins = OptionMenu(frame, minute, *minutes)
    mins.pack(side=LEFT)

    second = StringVar(root)
    seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
               '08', '09', '10', '11', '12', '13', '14', '15',
               '16', '17', '18', '19', '20', '21', '22', '23',
               '24', '25', '26', '27', '28', '29', '30', '31',
               '32', '33', '34', '35', '36', '37', '38', '39',
               '40', '41', '42', '43', '44', '45', '46', '47',
               '48', '49', '50', '51', '52', '53', '54', '55',
               '56', '57', '58', '59', '60')
    second.set(seconds[0])

    secs = OptionMenu(frame, second, *seconds)
    secs.pack(side=LEFT)

    Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

    # Execute Tkinter
    root.mainloop()

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command =aarm,
    relief = "flat")

b7.place(
    x = 1025, y = 538,
    width = 166,
    height = 82)

canvas.create_text(
    1126.0, 453.5,
    text = "Calender",
    fill = "#ffffff",
    font = ("None", int(24.0)))

canvas.create_text(
    1139.0, 723.0,
    text = "BY KNIGHTHAWKS-IV",
    fill = "#ffffff",
    font = ("None", int(24.0)))

canvas.create_text(
    1126.0, 664.5,
    text = " Alarm- Clock",
    fill = "#ffffff",
    font = ("None", int(24.0)))

window.resizable(False, False)
window.mainloop()

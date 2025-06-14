#!/usr/bin/python3
import tkinter as tk
import mysql.connector as ms
from Household_Management_System import *
from sign_in import *



class LoginDesignApp:
    def log(self):
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute("Select * from login;")
            data=cur.fetchall()
            self.u=self.user.get()
            self.p=self.password.get()
            for d in data:
                
                if d[0]==self.u and d[1]==self.p:
                    NewprojectApp(self.u,d[2])    
                    break
    #sign In
    def sign(self):
        Sign_in()
                    
    def __init__(self,master=None):
        # build ui
        self.u=''
        self.p=''
        self.Login = tk.Tk() if master is None else tk.Toplevel(master)
        self.Login.configure(height=600, width=800)
        self.Login_Frame = tk.Frame(self.Login)
        self.Login_Frame.configure(background="#ffffff", height=600, width=800)
        self.header = tk.Label(self.Login_Frame)
        self.header.configure(
            background="#1a73e8",
            font="{Arial} 14 {bold}",
            foreground="#ffffff",
            justify="center",
            text='HOUSEHOLD MANAGMENT SYSTEM')
        self.Login.resizable(0,0)
        self.header.place(anchor="nw", height=50, width=800, x=0, y=0)
        label2 = tk.Label(self.Login_Frame)
        label2.configure(
            background="#ffffff",
            font="{Georgia} 16 {}",
            text='User Name')
        label2.place(anchor="nw", height=30, width=150, x=350, y=150)
        self.user = tk.Entry(self.Login_Frame)
        self.user.configure(font="{Cambria} 12 {bold}")
        self.user.place(anchor="nw", height=30, width=200, x=550, y=150)
        label3 = tk.Label(self.Login_Frame)
        label3.configure(
            background="#ffffff",
            font="{Georgia} 16 {}",
            text='Password')
        label3.place(anchor="nw", height=30, width=150, x=350, y=220)
        self.password = tk.Entry(self.Login_Frame)
        self.password.configure(font="{Cambria} 12 {bold}")
        self.password.place(anchor="nw", height=30, width=200, x=550, y=220)
        label4 = tk.Label(self.Login_Frame)
        '''self.img_login = tk.PhotoImage(file="login.png")
        label4.configure(
            background="#ffffff",
            font="{Georgia} 16 {}",
            image=self.img_login)
        label4.place(anchor="nw", x=40, y=120)'''

        self.login = tk.Button(self.Login_Frame)
        self.login.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='Login',
            command=self.log)
        self.login.place(anchor="nw", height=30, width=120, x=500, y=300)
        
        self.signin = tk.Button(self.Login_Frame)
        self.signin.configure(
            background="#ffffff",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {bold}",
            foreground="#0f4897",
            text='Sign in',
            command=self.sign)
        self.signin.place(anchor="nw", height=30, width=90, x=520, y=400)

        label5 = tk.Label(self.Login_Frame)
        label5.configure(
            background="#ffffff",
            font="{Georgia} 16 {bold}",
            text='Do not have Account?')
        label5.place(anchor="nw", height=30, width=260, x=270, y=400)
        
        self.Login_Frame.place(anchor="nw", height=600, width=800, x=0, y=0)
        
    
        

        # Main widget
        self.mainwindow = self.Login

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = LoginDesignApp()
    app.run()


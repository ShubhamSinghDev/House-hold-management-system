#!/usr/bin/python3
import tkinter as tk
from Login import *

class Sign_in:
    
    def sign_in(self):
        con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
        cur=con.cursor()
        try:    
            if(len(self.ph_no.get())!=10):
                messagebox.showerror("Error","enter a valid number")
            else:             
                if self.passwd.get()==self.cpasswd.get():
                    try:
                        cur.execute('Create table login(user varchar(30) primary key, password varchar(30), phone varchar(10) unique);')
                    except:
                        
                        cur.execute('insert into login values("{}","{}","{}");'.format(self.email.get(),self.passwd.get(),self.ph_no.get()))            
                        con.commit()          
                        cur.execute('Create table {}(type varchar(30), category varchar(30),name varchar(30), id varchar(30) not null, quantity integer, quantity_type varchar(30), price integer, store varchar(30), exp_date date, date date, quantity_left integer, total integer);'.format(self.email.get()+'_item_stocks'))
                        cur.execute('create table {}(type varchar(30),category varchar(30),Id varchar(30),name varchar(30) ,primary key(type, category, name));'.format(self.email.get()+'_items'))            
                        con.close()
                        messagebox.showinfo("Message","Successfully Sign.")
                        messagebox.showinfo("Message","DataBase Successfully created for {}.".format(self.email.get()))
                        LoginDesignApp()
                else:
                    messagebox.showerror("Error","Password Mismatched.")
        except:
            messagebox.showerror("Error","User or Phnoe No. already exist.")
                
            
            
    def __init__(self, master=None):
        # build ui
        self.Sign_In = tk.Tk() if master is None else tk.Toplevel(master)
        self.Sign_In.configure(height=600, width=800)
        self.Signin_Frame = tk.Frame(self.Sign_In)
        self.Signin_Frame.configure(
            background="#ffffff", height=600, width=800)
        self.header = tk.Label(self.Signin_Frame)
        self.header.configure(
            background="#1a73e8",
            font="{Arial} 14 {bold}",
            foreground="#ffffff",
            justify="center",
            text='HOUSEHOLD MANAGMENT SYSTEM')
        self.header.place(anchor="nw", height=50, width=800, x=0, y=0)
        label2 = tk.Label(self.Signin_Frame)
        label2.configure(
            background="#ffffff",
            font="{Georgia} 16 {}",
            text='Phone No.')
        label2.place(anchor="nw", height=30, width=150, x=250, y=150)
        self.ph_no = tk.Entry(self.Signin_Frame)
        self.ph_no.configure(font="{Cambria} 12 {bold}")
        self.ph_no.place(anchor="nw", height=30, width=200, x=450, y=150)
        label3 = tk.Label(self.Signin_Frame)
        label3.configure(
            background="#ffffff",
            font="{Georgia} 16 {}",
            text='User Name')
        label3.place(anchor="nw", height=30, width=150, x=250, y=220)
        self.email = tk.Entry(self.Signin_Frame)
        self.email.configure(font="{Cambria} 12 {bold}")
        self.email.place(anchor="nw", height=30, width=200, x=450, y=220)
        self.signin = tk.Button(self.Signin_Frame)
        self.signin.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='Sign in',
            command=self.sign_in)
        self.signin.place(anchor="nw", height=30, width=120, x=400, y=450)
        self.passwd = tk.Entry(self.Signin_Frame,show="*")
        self.passwd.configure(font="{Cambria} 12 {bold}")
        self.passwd.place(anchor="nw", height=30, width=200, x=450, y=290)
        
        self.cpasswd = tk.Entry(self.Signin_Frame,show="*")
        self.cpasswd.configure(font="{Cambria} 12 {bold}")
        self.cpasswd.place(anchor="nw", height=30, width=200, x=450, y=370)
        label1 = tk.Label(self.Signin_Frame)
        label1.configure(
            background="#ffffff",
            font="{Georgia} 16 {}",
            text='Password')
        label1.place(anchor="nw", height=30, width=150, x=250, y=290)

        label5 = tk.Label(self.Signin_Frame)
        label5.configure(
            background="#ffffff",
            font="{Georgia} 16 {}",
            text='Confirm Password')
        label5.place(anchor="nw", height=30, width=180, x=250, y=370)
        self.Signin_Frame.place(anchor="nw", height=600, width=800, x=0, y=0)

        # Main widget
        self.mainwindow = self.Sign_In

    def run(self):
        self.mainwindow.mainloop()
    

if __name__ == "__main__":
    app = Sign_in()
    app.run()


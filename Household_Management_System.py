#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import pymysql as ms
import datetime as dtime
from datetime import datetime
from pygubu.widgets.tkscrolledframe import TkScrolledFrame
from tkinter.scrolledtext import ScrolledText
import os
import tempfile
from tkinter import messagebox
from sign_in import *
from Login import *


class NewprojectApp:
    #global
    pname=[]
    data1=[]

    #Clear Entry in view Item
    def clr(self,event):
        if self.vi_search1.get()=="Name/ID" or self.vi_search1.get()=="":
            self.vi_search1.delete(0,40)


 
    #Shoping List Filter
    def shoping_filter(self,event):
        if self.sl_type.get()=="Select_Type" and self.sl_category.get()=="Select_Category":
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute("select Name,quantity-quantity_left,quantity_type,price*(quantity-quantity_left) from {} where quantity_left<=quantity*50/100 and month(date)='{}';".format(self.us+'_item_stocks',self.sl_month.get()))
            data=cur.fetchall()
        elif self.sl_type.get()!="Select_Type" and self.sl_category.get()=="Select_Category":
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute("select Name,quantity-quantity_left,quantity_type,price*(quantity-quantity_left) from {} where quantity_left<=quantity*50/100 and month(date)='{}' and type='{}';".format(self.us+'_item_stocks',self.sl_month.get(),self.sl_type.get()))
            data=cur.fetchall()
        elif self.sl_type.get()=="Select_Type" and self.sl_category.get()!="Select_Category":
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute("select Name,quantity-quantity_left,quantity_type,price*(quantity-quantity_left) from {} where quantity_left<=quantity*50/100 and month(date)='{}' and category='{}';".format(self.us+'_item_stocks',self.sl_month.get(),self.sl_category.get()))
            data=cur.fetchall()
        elif self.sl_type.get()!="Select_Type" and self.sl_category.get()!="Select_Category":
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute("select Name,quantity-quantity_left,quantity_type,price*(quantity-quantity_left) from {} where quantity_left<=quantity*50/100 and month(date)='{}' and type='{}' and category='{}';".format(self.us+'_item_stocks',self.sl_month.get(),self.sl_type.get(),self.sl_category.get()))
            data=cur.fetchall()
        total=0
        for d in data:
            total+=d[3]
        self.sl_total.delete(0,10)
        self.sl_total.insert(0,total)

        self.sl_text_area = ScrolledText(self.Shoping_List_Frame)
        self.sl_text_area.configure(
                background="#c0c0c0",
                font="{Arial} 12 {}",
                )
        for i in data:
            s=""
            for val in i:
                s=s+str(val)+" "
            s=s+"Rs\n"
            self.sl_text_area.insert('insert',s)
        self.sl_text_area.place(
            anchor="nw",
            height=420,
            width=250,
            x=10,
            y=70)
            

    #View Item Table
    def table_filter(self,event):
            #try:
            if self.vi_search1.get()!="Name/ID" and self.vi_search1.get()!="" and self.vi_quantity1.get()==0 and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where name='{}' or Id='{}';".format(self.us+'_item_stocks',self.vi_search1.get(),self.vi_search1.get()))
                #cur.execute("select * from {} where name like '{}%' or Id like '{}%';".format(self.us+'_item_stocks',self.vi_search1.get(),self.vi_search1.get()))
                data=cur.fetchall()
                con.close()

            elif self.vi_search1.get()!="Name/ID" and self.vi_search1.get()!="" and self.vi_quantity1.get()==0 and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where name='{}' or Id='{}' and month(date)={};".format(self.us+'_item_stocks',self.vi_search1.get(),self.vi_search1.get(),self.vi_month.get()))
                #cur.execute("select * from {} where name like '{}%' or Id like '{}%';".format(self.us+'_item_stocks',self.vi_search1.get(),self.vi_search1.get()))
                data=cur.fetchall()
                con.close()
        
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()=="Select_Category"  and self.vi_quantity1.get()==0 and self.vi_day1.get()=='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}';".format(self.us+'_item_stocks',self.vi_type1.get()))
                data=cur.fetchall()
                con.close()
                
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()=='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where category='{}';".format(self.us+'_item_stocks',self.vi_category1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()=='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where quantity_left<=quantity*{}/100".format(self.us+'_item_stocks',self.vi_quantity1.get()))
                data=cur.fetchall()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()!='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where datediff(exp_date,date)<={} and datediff(exp_date,date)>=0".format(self.us+'_item_stocks',self.vi_day1.get()))
                data=cur.fetchall()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()=='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where month(date)='{}';".format(self.us+'_item_stocks',self.vi_month.get()))
                data=cur.fetchall()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()=='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and category='{}';".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_category1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()=='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where category='{}' and quantity_left<=quantity*{}/100;".format(self.us+'_item_stocks',self.vi_category1.get(),self.vi_quantity1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()=='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and quantity_left<=quantity*{}/100;".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_quantity1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()!=''  and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0;".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_day1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()!='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where category='{}' and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0;".format(self.us+'_item_stocks',self.vi_category1.get(),self.vi_day1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()!='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where quantity_left<=quantity*{}/100 and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0;".format(self.us+'_item_stocks',self.vi_quantity1.get(),self.vi_day1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()!='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and quantity_left<=quantity*{}/100 and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0;".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_quantity1.get(),self.vi_day1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()=='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and category='{}' and quantity_left<=quantity*{}/100;".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_category1.get(),self.vi_quantity1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()!='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and category='{}' and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0;".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_category1.get(),self.vi_day1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()!='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where category='{}' and quantity_left<=quantity*{}/100 and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0;".format(self.us+'_item_stocks',self.vi_category1.get(),self.vi_quantity1.get(),self.vi_day1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()!='' and self.vi_month.get()=="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and category='{}' and quantity_left<=quantity*{}/100 and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0;".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_category1.get(),self.vi_quantity1.get(),self.vi_day1.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()=='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and month(date)='{}';".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()=='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where category='{}' and month(date)='{}';".format(self.us+'_item_stocks',self.vi_category1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()=='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where quantity_left<=quantity*{}/100 and month(date)='{}';".format(self.us+'_item_stocks',self.vi_quantity1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()!='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where datediff(exp_date,date)<={} and datediff(exp_date,date)>=0 and month(date)='{}';".format(self.us+'_item_stocks',self.vi_day1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()=='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and category='{}' and month(date)='{}';".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_category1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()=='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and quantity_left<=quantity*{}/100 and month(date)='{}';".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_quantity1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()!='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0 and month(date)='{}';".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_day1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()=='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where category='{}' and quantity_left<=quantity*{}/100 and month(date)='{}';".format(self.us+'_item_stocks',self.vi_category1.get(),self.vi_quantity1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()!='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where category='{}' and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0 and month(date)='{}';".format(self.us+'_item_stocks',self.category1.get(),self.vi_day1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()!='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where quantity_left<=quantity*{}/100 and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0 and month(date)='{}';".format(self.us+'_item_stocks',self.vi_quantity1.get(),self.vi_day1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()=='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and category='{}' and quantity_left<=quantity*{}/100 and month(date'{}';".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_category1.get(),self.vi_quantity1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()==0 and self.vi_day1.get()!='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and category='{}' and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0 and month(date);".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_category1.get(),self.vi_day1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()=="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()!='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and quantity_left<=quantity*{}/100 and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0 and month(date);".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_quantity1.get(),self.vi_day1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()=="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()!='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where category='{}' and quantity_left<=quantity*{}/100 and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0 and month(date);".format(self.us+'_item_stocks',self.vi_category1.get(),self.vi_quantity1.get(),self.vi_day1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()
            elif self.vi_type1.get()!="Select_Type" and self.vi_category1.get()!="Select_Category" and self.vi_quantity1.get()!=0 and self.vi_day1.get()!='' and self.vi_month.get()!="Month":
                con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
                cur=con.cursor()
                cur.execute("select * from {} where type='{}' and category='{}' and quantity_left<=quantity*{}/100 and datediff(exp_date,date)<={} and datediff(exp_date,date)>=0 and month(date);".format(self.us+'_item_stocks',self.vi_type1.get(),self.vi_category1.get(),self.vi_quantity1.get(),self.vi_day1.get(),self.vi_month.get()))
                data=cur.fetchall()
                con.close()

            self.vi_table = ttk.Treeview(self.View_Item_Frame)
            h_clr=ttk.Style(self.View_Item_Frame)
            h_clr.theme_use("clam")
            h_clr.configure("Treeview.Heading",font=('Helvetica',9,"bold"))

            self.vi_table['show']='headings'
            self.vi_table["columns"]=('S.N','Type','Category','Name','Id','Quantity','Price','Store','Exp. Date','Date','Q_Left','Total')
        
            self.vi_table.column('S.N',width=40,anchor='n',minwidth=40)
            self.vi_table.column('Type',width=60,anchor='center',minwidth=60)
            self.vi_table.column('Category',width=60,anchor='center',minwidth=60)
            self.vi_table.column('Name',width=70,anchor='center',minwidth=70)
            self.vi_table.column('Id',width=65,anchor='center',minwidth=65)
            self.vi_table.column('Quantity',width=60,anchor='n',minwidth=60)
            #self.vi_table.column('Q_Type',width=30,anchor='center',minwidth=30)
            self.vi_table.column('Price',width=40,anchor='center',minwidth=40)
            self.vi_table.column('Store',width=60,anchor='center',minwidth=60)
            self.vi_table.column('Exp. Date',width=75,anchor='center',minwidth=75)
            self.vi_table.column('Date',width=75,anchor='center',minwidth=75)
            self.vi_table.column('Q_Left',width=50,anchor='center',minwidth=50)
            self.vi_table.column('Total',width=50,anchor='center',minwidth=50)
            

            self.vi_table.heading('S.N',text='S.N',anchor='center')
            self.vi_table.heading('Type',text='Type',anchor='center')
            self.vi_table.heading('Category',text='Category',anchor='center')
            self.vi_table.heading('Name',text='Name',anchor='center')
            self.vi_table.heading('Id',text='Id',anchor='center')
            self.vi_table.heading('Quantity',text='Quantity',anchor='center')
            #self.vi_table.heading('Q_Type',text='Q_Type',anchor='center')
            self.vi_table.heading('Price',text='Price',anchor='center')
            self.vi_table.heading('Store',text='Store',anchor='center')
            self.vi_table.heading('Exp. Date',text='Exp. Date',anchor='center')
            self.vi_table.heading('Date',text='Date',anchor='center')
            self.vi_table.heading('Q_Left',text='Q_Left',anchor='center')
            self.vi_table.heading('Total',text='Total',anchor='center')

            c=1
            for i in data:
                if c%2:
                    self.vi_table.insert('',c,text="",values=(c,i[0],i[1],i[2],i[3],str(i[4])+' '+i[5],str(i[6])+' Rs',i[7],i[8],i[9],i[10],i[4]*i[6]),tags=('odd',))
                else:
                    self.vi_table.insert('',c,text="",values=(c,i[0],i[1],i[2],i[3],str(i[4])+' '+i[5],str(i[6])+' Rs',i[7],i[8],i[9],i[10],i[4]*i[6]),tags=('even',))
                c+=1
            self.vi_table.tag_configure('even',background="gray",foreground="white")

            hor_view=ttk.Scrollbar(self.View_Item_Frame,orient="horizontal")
            hor_view.configure(command=self.vi_table.xview)
            self.vi_table.configure(xscrollcommand=hor_view.set)
            hor_view.place(x=10,y=481,width=580)

            ver_view=ttk.Scrollbar(self.View_Item_Frame,orient="vertical")
            ver_view.configure(command=self.vi_table.yview)
            self.vi_table.configure(yscrollcommand=hor_view.set)
            ver_view.place(x=580,y=200,height=280)

            self.vi_table.place(x=10,y=200,height=280,width=580)
                
            '''self.vi_table = TkScrolledFrame(
                self.View_Item_Frame, scrolltype="both")
            self.vi_table.innerframe.configure(background="#c0c0c0")
            self.vi_table.configure(usemousewheel=True)
            self.vi_table.place(anchor="nw", height=340, width=580, x=10, y=200)
            
            total_rows = len(data)
            total_columns =len(data[0])
            eh=20
            ew=46
            ex=5
            ey=0
            lst=['S.N','Type','Category','Name','Id','Quantity','Q_Type','Price','Store','Exp. Date','Date','Q_Left','Total']
            for i in range(total_rows):
                ey+=21
                newdata=list(data[i])
                newdata.insert(0,i+1)
                newdata.append('Update')
                for j in range(total_columns+1):
                    self.l = ttk.Label(self.vi_table)
                    self.l.place(height=eh, width=ew, x=ex, y=0)
                    self.l.configure(text=lst[j],font="{Cambria} 8 {}")
                    self.e = ttk.Entry(self.vi_table)
                    self.e.configure(font="{Cambria} 8 {}")
                    self.e.place(height=eh, width=ew, x=ex, y=ey)
                    self.e.insert(0,str(newdata[j]))
                    self.e.bind("<Return>",self.update_item)
                    ex+=47
                
                ex=5
            
            

            
            self.View_Item_Frame.place(
                anchor="nw", height=550, width=600, x=200, y=50)'''
            '''except:
            messagebox.showinfo('Info', 'No record found.')
            self.vi_table = TkScrolledFrame(self.View_Item_Frame, scrolltype="both")
            self.vi_table.innerframe.configure(background="#c0c0c0")
            self.vi_table.configure(usemousewheel=True)
            self.vi_table.place(anchor="nw", height=340, width=580, x=10, y=200)
            self.l = ttk.Label(self.vi_table)
            self.l.place(height=30, width=150, x=210, y=5)
            self.l.configure(text="No value found",font="{Cambria} 16 {}",background="#c0c0c0")'''



    #Registration Filter
    def rg_filter(self,event):
        self.all_item_list.delete(0,10)
        if self.type.get()=="Select_Type":
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute("select name from {} where category='{}';".format(self.us+'_items',self.category.get()))
            data=cur.fetchall()
            con.close()
            c=1
            for i in data:   
                self.all_item_list.insert(c,i)
                c+=1
        elif self.category.get()=="Select_Category":
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()      
            cur.execute("select name from {} where type='{}';".format(self.us+'_items',self.type.get()))
            data=cur.fetchall()
            con.close()
            c=1
            for i in data:   
                self.all_item_list.insert(c,i)
                c+=1
        else :
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute("select name from {} where type='{}' and category='{}';".format(self.us+'_items',self.type.get(),self.category.get()))
            data=cur.fetchall()
            con.close()
            c=1
            for i in data:   
                self.all_item_list.insert(c,i)
                c+=1
            
            

    
    #aied_filter1 for combobox
    def aied_filter(self,event):
        self.pname=[]
        self.aied_name.config(values='Select_Product')

        con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
        cur=con.cursor()
        data=[]
        if self.aied_type.get()!="Select_Type" and self.aied_category.get()!="Select_Category":
            cur.execute("select name from {} where type='{}' and category='{}';".format(self.us+'_items',self.aied_type.get(),self.aied_category.get()))
            data=cur.fetchall()
        con.close()
        for i in data:
            self.pname.append(i[0])
        self.aied_name.config(values=self.pname)
        

    #aied_filter2 for combobox
    def aied_filter2(self,event):
        con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute("select Id from {} where name='{}';".format(self.us+'_items',self.aied_name.get()))
        data=cur.fetchall()
        con.close()
        self.aied_id.configure(text=data[0][0])


    
    #Register Item 
    def register_item(self):
        try:
            #ID GENERATION
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute("select * from {} where category='{}' and type='{}';".format(self.us+'_items',self.category.get(),self.type.get()))
            self.data=cur.fetchall()
            
            generated_id=self.type.get()[:3].upper()+self.category.get()[:2].upper()+str(len(self.data)+1)
            
            self.id.configure(text=generated_id)

            cur.execute('INSERT INTO {} VALUES("{}","{}","{}","{}");'.format(self.us+'_items',self.type.get(),self.category.get(),generated_id,self.name.get()))
            con.commit()
            
            messagebox.showinfo("Message","Successfully Register.")
            
            cur.execute("select name from {} where type='{}' and category='{}';".format(self.us+'_items',self.type.get(),self.category.get()))
            data=cur.fetchall()
            con.close()
            self.all_item_list.delete(0,1000)
            c=1
            for i in data:   
                self.all_item_list.insert(c,i)
                c+=1
        except:
            messagebox.showerror("Error","Item Already Registeredadd Item into database")

            
    #Add and Delete items from list in register Frame
    def register_add(self):
            
            index=self.all_item_list.curselection()
            r=self.all_item_list.get(index)
            
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute('Select * from {} where name="{}";'.format(self.us+'_items',r[0]))
            data=cur.fetchall()
            con.commit()
            self.add_item()
            self.ai_type.configure(text=data[0][0])
            self.ai_category.configure(text=data[0][1])
            self.ai_name.configure(text=data[0][3])
            self.ai_id.config(text=data[0][2])

    def register_delete(self):
            index=self.all_item_list.curselection()
            r=self.all_item_list.get(index)
            self.all_item_list.delete(index)

            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute('Delete from {} where name="{}";'.format(self.us+'_items',r[0]))
            con.commit()
    #add Item into database
    def added_fun(self):
        try:
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute('select id,date from {};'.format(self.us+'_item_stocks'))
            data= cur.fetchall()
            available=[(0,)]
            dt=0
            for i in data:
                if self.aied_id.cget('text')==i[0]:
                    dt=i[1]
            for i in data:
                if self.aied_id.cget('text') in i:
                    cur.execute('select quantity_left from {} where id="{}" and date="{}";'.format(self.us+'_item_stocks',self.aied_id.cget('text'),dt))
                    available=cur.fetchall()   
            cur.execute('insert into {} values("{}","{}","{}","{}",{},"{}",{},"{}","{}","{}",{},{});'.format(self.us+'_item_stocks',self.aied_type.get(),self.aied_category.get(),self.aied_name.get(),self.aied_id.cget("text"),self.aied_quantity.get(),self.aied_quantity_type.get(),self.aied_price.get(),self.aied_store.get(),self.aied_exp.get(),self.aied_date.cget("text"),(int(self.aied_quantity.get())+available[-1][0]),int(self.aied_quantity.get())*int(self.aied_price.get())))
            con.commit()
            con.close()
            messagebox.showinfo("Message","Successfully Added.")
        except:
            if self.aied_type.get()=="Select_Type" or self.aied_category.get()=="Select_Category" or self.aied_name.get()=="Select_Product" or self.aied_quantity.get()==0 or self.aied_quantity_type.get()=="Select" or self.aied_price.get()=="" or self.aied_store.get()=="":
                messagebox.showerror("Error","Fill all field!")
            elif self.aied_price.get().isalpha():
                messagebox.showerror("Error","Invalid price!")
            else:
                messagebox.showerror("Error","Invalid Date!")
                
    def add_fun(self):
        try:
            con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
            cur=con.cursor()
            cur.execute('select id,date from {};'.format(self.us+'_item_stocks'))
            data= cur.fetchall()
            available=[(0,)]
            dt=0
            for i in data:
                if self.ai_id.cget('text')==i[0]:
                    dt=i[1]
            for i in data:
                if self.ai_id.cget('text') in i:
                    cur.execute('select quantity_left from {} where id="{}" and date="{}";'.format(self.us+'_item_stocks',self.ai_id.cget('text'),dt))
                    available=cur.fetchall()   
            cur.execute('insert into {} values("{}","{}","{}","{}",{},"{}",{},"{}","{}","{}",{},{});'.format(self.us+'_item_stocks',self.ai_type.cget("text"),self.ai_category.cget("text"),self.ai_name.cget("text"),self.ai_id.cget("text"),self.ai_quantity.get(),self.ai_quantity_type.get(),self.ai_price.get(),self.ai_store.get(),self.ai_exp.get(),self.ai_date.cget("text"),(int(self.ai_quantity.get())+available[-1][0]),int(self.ai_quantity.get())*int(self.ai_price.get())))
            con.commit()
            con.close()
            messagebox.showinfo("Message","Successfully Added.")
        except:
            if self.ai_type.get()=="Select_Type" or self.ai_category.get()=="Select_Category" or self.ai_name.get()=="Select_Product" or self.ai_quantity.get()==0 or self.ai_quantity_type.get()=="Select" or self.ai_price.get()=="" or self.ai_store.get()=="":
                messagebox.showerror("Error","Fill all field!")
            elif self.ai_price.get().isalpha():
                messagebox.showerror("Error","Invalid price!")
            else:
                messagebox.showerror("Error","Invalid Date!")
            

    #update Item into database
    def update_fun(self):
        con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute('update {} set  type="{}",category="{}",name="{}",quantity={},quantity_type="{}",price={},store="{}",exp_date="{}",quantity_left={} where id="{}";'.format(self.us+'_item_stocks',self.ui_type.get(),self.ui_category.get(),self.ui_name.get(),self.ui_quantity.get(),self.ui_quantity_type.get(),self.ui_price.get(),self.ui_store.get(),self.ui_exp.get(),self.ui_quantity_left.get(),self.ui_id.cget("text")))
        con.commit()
        con.close()
        messagebox.showinfo("Message","Successfully Updated.")

    '''#Update filtter
    def update_filter(self,event):
        con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute("Select * from {} where name='{}';".format(self.us+'_item_stocks',self.data1[3]))
        self.data1=cur.fetchall()
        print(self.data1)
        
        self.ui_type.delete(0,20)
        self.ui_type.insert(0,self.data1[1])
        

        self.ui_category.delete(0,20)
        self.ui_category.insert(0,self.data1[2])

        self.ui_name.delete(0,20)
        self.ui_name.insert(0,self.data1[3])
        

        self.ui_id.configure(text=self.data1[4])

        self.ui_quantity.delete(0,20)
        self.ui_quantity.insert(0,self.data1[5].split()[0])

        self.ui_quantity_type.delete(0,20)
        self.ui_quantity_type.insert(0,self.data1[5].split()[1])

        self.ui_price.delete(0,20)
        self.ui_price.insert(0,self.data1[5].split()[0])

        self.ui_store.delete(0,20)
        self.ui_store.insert(0,self.data1[7])

        self.ui_exp.delete(0,20)
        self.ui_exp.insert(0,self.data1[8])

        self.ui_store.delete(0,20)
        self.ui_store.insert(0,self.data1[7])'''
        
    

    #print Shoping List
    def sl_prints(self):
        temp_file = tempfile.mktemp('.txt')
        open(temp_file, 'w').write(self.sl_text_area.get("1.0","end-1c"))
        
        os.startfile(temp_file, 'print')

    #whatsapp
    def whatsapp(self):
        import pywhatkit
        pywhatkit.sendwhatmsg("+91"+self.ph,self.sl_text_area.get("1.0","end-1c"),datetime.now().hour,datetime.now().minute+1)
        
    #update in treeview
    def update_item1(self,tree):
        
        try:
            val=tree.focus()
            self.data1=tree.item(val,"values")             

            self.ui_type.delete(0,20)
            self.ui_type.insert(0,self.data1[1])
            

            self.ui_category.delete(0,20)
            self.ui_category.insert(0,self.data1[2])

            self.ui_name.delete(0,20)
            self.ui_name.insert(0,self.data1[3])
            

            self.ui_id.configure(text=self.data1[4])

            self.ui_quantity.delete(0,20)
            self.ui_quantity.insert(0,self.data1[5].split()[0])

            self.ui_quantity_type.delete(0,20)
            self.ui_quantity_type.insert(0,self.data1[5].split()[1])

            self.ui_price.delete(0,20)
            self.ui_price.insert(0,self.data1[6].split()[0])

            self.ui_store.delete(0,20)
            self.ui_store.insert(0,self.data1[7])

            self.ui_exp.delete(0,20)
            self.ui_exp.insert(0,self.data1[8])

            self.ui_quantity_left.delete(0,20)
            self.ui_quantity_left.insert(0,self.data1[10])
        except:
            messagebox.showerror("Error","Select Data First!")
            self.view_item()
        
    def delete_item(self,tree):
        val=tree.focus()
        data=tree.item(val,"values")
        print(data)
        con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute('select id,date from item_stocks;')
        data= cur.fetchall()

    
    #Resgister Design
    def register(self):
        self.Register_Frame = tk.Frame(self.main)
        self.Register_Frame.configure(
            background="#ffffff", height=200, width=200)
        self.label4 = tk.Label(self.Register_Frame)
        self.label4.configure(
            background="#ffffff",
            font="{Arial} 14 {bold underline}",
            foreground="#000000",
            justify="center",
            text='REGISTER ITEM')
        self.label4.place(anchor="nw", height=50, width=200, x=200, y=10)
        self.label5 = tk.Label(self.Register_Frame)
        self.label5.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Category :')
        self.label5.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=130,
            x=10,
            y=140)
        self.label6 = tk.Label(self.Register_Frame)
        self.label6.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Id:')
        self.label6.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=130,
            x=10,
            y=260)
        self.label7 = tk.Label(self.Register_Frame)
        self.label7.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Name:')
        self.label7.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=130,
            x=10,
            y=200)
        self.label9 = tk.Label(self.Register_Frame)
        self.label9.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            justify="left",
            text='Type :')
        self.label9.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=130,
            x=10,
            y=80)
        self.type = ttk.Combobox(self.Register_Frame)
        self.type.insert(0,"Select_Type")
        self.type.configure(state="readonly",
                            values='Grocery Medicine',
                            font="{Cambria} 14 {}")
        self.type.place(anchor="nw", height=30, width=150, x=160, y=80)
        self.type.bind("<<ComboboxSelected>>",self.rg_filter)
        self.category = ttk.Combobox(self.Register_Frame)
        self.category.insert(0,"Select_Category")
        self.category.configure(state="readonly",
                                values='All Baby Kids Men Woman Old',
                                font="{Cambria} 14 {}")
        self.category.place(anchor="nw", height=30, width=150, x=160, y=140)
        self.category.bind("<<ComboboxSelected>>",self.rg_filter)
        self.name = ttk.Entry(self.Register_Frame)
        self.name.configure(font="{Cambria} 14 {}")
        self.name.place(anchor="nw", height=30, width=150, x=160, y=200)
        self.id = tk.Label(self.Register_Frame)
        self.id.configure(
            background="#c0c0c0",
            font="{Arial} 12 {bold}",
            foreground="#000000")
        self.id.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=150,
            x=160,
            y=260)
        self.save = tk.Button(self.Register_Frame)
        self.save.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='SAVE',
            command=self.register_item)
        self.save.place(anchor="nw", height=30, width=120, x=110, y=320)
        self.all_item_list = tk.Listbox(self.Register_Frame)
        self.all_item_list.configure(background="#c0c0c0",font="{Cambria} 14 {}")
        self.all_item_list.place(
            anchor="nw",
            height=350,
            width=200,
            x=350,
            y=100)
        self.label11 = tk.Label(self.Register_Frame)
        self.label11.configure(
            background="#ffffff",
            font="{Arial} 14 {bold underline}",
            foreground="#000000",
            justify="center",
            text='Unadded Items')
        self.label11.place(anchor="nw", height=30, width=200, x=350, y=65)
        self.Register_Frame.place(
            anchor="nw", height=550, width=600, x=200, y=50)
        
        #List of Items
        con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute("select name from {};".format(self.us+'_items'))
        data=cur.fetchall()
        con.close()

        con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute("select distinct(name) from {};".format(self.us+'_item_stocks'))
        data1=cur.fetchall()
        con.close()
        
        c=1
        for i in data:
            if i not in data1:
                self.all_item_list.insert(c,i)
                c+=1

        
        self.rg_add = tk.Button(self.Register_Frame)
        self.rg_add.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='Add',
            command=self.register_add)
        self.rg_add.place(anchor="nw", height=30, width=120, x=250, y=480)

        self.rg_del = tk.Button(self.Register_Frame)
        self.rg_del.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='DELETE',
            command=self.register_delete)
        self.rg_del.place(anchor="nw", height=30, width=120, x=450, y=480)

        # Main widget
        self.mainwindow = self.main
        

    #Add Item Design
    def add_item(self):
        self.Add_Item_frame = tk.Frame(self.main)
        self.Add_Item_frame.configure(
            background="#ffffff", height=200, width=200)
        self.label1 = tk.Label(self.Add_Item_frame)
        self.label1.configure(
            background="#ffffff",
            font="{Arial} 14 {bold underline}",
            foreground="#000000",
            justify="center",
            text='ADD ITEM')
        self.label1.place(anchor="nw", height=50, width=200, x=200, y=10)
        self.label3 = tk.Label(self.Add_Item_frame)
        self.label3.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Id:')
        self.label3.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=80)
        self.ai_type = tk.Label(self.Add_Item_frame)
        self.ai_type.configure(
            background="#c0c0c0",
            font="{Arial} 12 {bold}",
            foreground="#000000")
        self.ai_type.place(anchor="nw", height=30, width=150, x=10, y=140)
        #self.ai_type.bind("<<ComboboxSelected>>",self.ai_filter) 
        self.ai_category = tk.Label(self.Add_Item_frame)
        self.ai_category.configure(
            background="#c0c0c0",
            font="{Arial} 12 {bold}",
            foreground="#000000")
        self.ai_category.place(anchor="nw", height=30, width=150, x=10, y=200)
        #self.ai_category.bind("<<ComboboxSelected>>",self.ai_filter) 
        self.ai_id = tk.Label(self.Add_Item_frame)
        self.ai_id.configure(
            background="#c0c0c0",
            font="{Arial} 12 {bold}",
            foreground="#000000")
        self.ai_id.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=150,
            x=300,
            y=80)
        self.ai_name = tk.Label(self.Add_Item_frame)
        self.ai_name.configure(
            background="#c0c0c0",
            font="{Arial} 12 {bold}",
            foreground="#000000")
        self.ai_name.place(anchor="nw", height=30, width=150, x=10, y=260)
        #self.ai_name.bind("<<ComboboxSelected>>",self.ai_filter2) 
        self.label14 = tk.Label(self.Add_Item_frame)
        self.label14.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Quantity:')
        self.label14.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=140)
        self.label15 = tk.Label(self.Add_Item_frame)
        self.label15.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Price :')
        self.label15.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=200)
        self.label16 = tk.Label(self.Add_Item_frame)
        self.label16.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Store:')
        self.label16.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=260)
        self.ai_date = tk.Label(self.Add_Item_frame)
        self.ai_date.configure(
            background="#c0c0c0",
            font="{Arial} 10 {bold}",
            foreground="#000000",
            text=dtime.date.today())
        self.ai_date.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=150,
            x=10,
            y=80)
        self.ai_quantity = tk.Spinbox(self.Add_Item_frame)
        self.ai_quantity.configure(
            font="{Calibri} 12 {bold}", from_=1, to=1000)
        self.ai_quantity.place(anchor="nw", height=30, width=60, x=300, y=140)
        self.ai_quantity_type = ttk.Combobox(self.Add_Item_frame)
        self.ai_quantity_type.insert(0,"Select")
        self.ai_quantity_type.configure(state="readonly",
                                        values='Pcs Gram KG Ltr',
                                        font="{Cambria} 14 {}")
        self.ai_quantity_type.place(
            anchor="nw", height=30, width=80, x=370, y=140)
        self.ai_price = tk.Entry(self.Add_Item_frame)
        self.ai_price.configure(font="{Cambria} 14 {}")
        self.ai_price.place(anchor="nw", height=30, width=150, x=300, y=200)
        self.ai_store = tk.Entry(self.Add_Item_frame)
        self.ai_store.configure(font="{Cambria} 14 {}")
        self.ai_store.place(anchor="nw", height=30, width=150, x=300, y=260)
        self.label18 = tk.Label(self.Add_Item_frame)
        self.label18.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Exp Date:')
        self.label18.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=320)
        self.ai_exp = tk.Entry(self.Add_Item_frame)
        self.ai_exp.configure(font="{Cambria} 14 {}")
        self.ai_exp.place(anchor="nw", height=30, width=150, x=300, y=320)
        self.label30 = tk.Label(self.Add_Item_frame)
        self.label30.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='(yyyy/mm/dd)')
        self.label30.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=455,
            y=320)
        self.ai_add = tk.Button(self.Add_Item_frame)
        self.ai_add.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='Add',
            command=self.add_fun)
        self.ai_add.place(anchor="nw", height=30, width=120, x=250, y=370)
        self.Add_Item_frame.place(
            anchor="nw", height=550, width=600, x=200, y=50)

        # Main widget
        self.mainwindow = self.main

    #Added Item Design
    def added_item(self):
        self.Added_Item_frame = tk.Frame(self.main)
        self.Added_Item_frame.configure(
            background="#ffffff", height=200, width=200)
        self.label51 = tk.Label(self.Added_Item_frame)
        self.label51.configure(
            background="#ffffff",
            font="{Arial} 14 {bold underline}",
            foreground="#000000",
            justify="center",
            text='ADD ITEM')
        self.label51.place(anchor="nw", height=50, width=200, x=200, y=10)
        self.label52 = tk.Label(self.Added_Item_frame)
        self.label52.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Id:')
        self.label52.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=80)
        self.aied_type = ttk.Combobox(self.Added_Item_frame)
        self.aied_type.insert(0,"Select_Type")
        self.aied_type.configure(state="readonly",
            values='Grocery Medicine Other',
            font="{Cambria} 14 {}")
        self.aied_type.place(anchor="nw", height=30, width=150, x=10, y=140)
        self.aied_type.bind("<<ComboboxSelected>>",self.aied_filter) 
        self.aied_category = ttk.Combobox(self.Added_Item_frame)
        self.aied_category.insert(0,"Select_Category")
        self.aied_category.configure(state="readonly",
            values='All Baby Kids Men Woman Old',
            font="{Cambria} 14 {}")
        self.aied_category.place(anchor="nw", height=30, width=150, x=10, y=200)
        self.aied_category.bind("<<ComboboxSelected>>",self.aied_filter) 
        self.aied_id = tk.Label(self.Added_Item_frame)
        self.aied_id.configure(
            background="#c0c0c0",
            font="{Arial} 12 {bold}",
            foreground="#000000")
        self.aied_id.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=150,
            x=300,
            y=80)
        self.aied_name = ttk.Combobox(self.Added_Item_frame)
        self.aied_name.insert(0,"Select_Product")
        self.aied_name.configure(state="readonly",
            font="{Cambria} 14 {}")
        self.aied_name.place(anchor="nw", height=30, width=150, x=10, y=260)
        self.aied_name.bind("<<ComboboxSelected>>",self.aied_filter2) 
        self.label53 = tk.Label(self.Added_Item_frame)
        self.label53.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Quantity:')
        self.label53.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=140)
        self.label54 = tk.Label(self.Added_Item_frame)
        self.label54.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Price :')
        self.label54.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=200)
        self.label55 = tk.Label(self.Added_Item_frame)
        self.label55.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Store:')
        self.label55.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=260)
        self.aied_date = tk.Label(self.Added_Item_frame)
        self.aied_date.configure(
            background="#c0c0c0",
            font="{Arial} 10 {bold}",
            foreground="#000000",
            text=dtime.date.today())
        self.aied_date.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=150,
            x=10,
            y=80)
        self.aied_quantity = tk.Spinbox(self.Added_Item_frame)
        self.aied_quantity.configure(
            font="{Calibri} 12 {bold}", from_=1, to=1000)
        self.aied_quantity.place(anchor="nw", height=30, width=60, x=300, y=140)
        self.aied_quantity_type = ttk.Combobox(self.Added_Item_frame)
        self.aied_quantity_type.insert(0,"Select")
        self.aied_quantity_type.configure(state="readonly",
                                        values='Pcs Gram KG Ltr',
                                        font="{Cambria} 14 {}")
        self.aied_quantity_type.place(
            anchor="nw", height=30, width=80, x=370, y=140)
        self.aied_price = tk.Entry(self.Added_Item_frame)
        self.aied_price.configure(font="{Cambria} 14 {}")
        self.aied_price.place(anchor="nw", height=30, width=150, x=300, y=200)
        self.aied_store = tk.Entry(self.Added_Item_frame)
        self.aied_store.configure(font="{Cambria} 14 {}")
        self.aied_store.place(anchor="nw", height=30, width=150, x=300, y=260)
        self.label56 = tk.Label(self.Added_Item_frame)
        self.label56.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Exp Date:')
        self.label56.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=320)
        self.aied_exp = tk.Entry(self.Added_Item_frame)
        self.aied_exp.configure(font="{Cambria} 14 {}")
        self.aied_exp.place(anchor="nw", height=30, width=150, x=300, y=320)
        self.label60 = tk.Label(self.Added_Item_frame)
        self.label60.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='(yyyy/mm/dd)')
        self.label60.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=455,
            y=320)
        self.aied_add = tk.Button(self.Added_Item_frame)
        self.aied_add.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='Add',
            command=self.added_fun)
        self.aied_add.place(anchor="nw", height=30, width=120, x=250, y=370)
        self.Added_Item_frame.place(
            anchor="nw", height=550, width=600, x=200, y=50)

        # Main widget
        self.mainwindow = self.main    



    #View Items Design
    def view_item(self):
        self.View_Item_Frame = tk.Frame(self.main)
        self.View_Item_Frame.configure(
            background="#ffffff", height=200, width=200)
        self.label21 = tk.Label(self.View_Item_Frame)
        self.label21.configure(
            background="#ffffff",
            font="{Arial} 14 {bold underline}",
            foreground="#000000",
            justify="center",
            text='VIEW ITEM')
        self.label21.place(anchor="nw", height=50, width=200, x=200, y=10)
        self.vi_type1 = ttk.Combobox(self.View_Item_Frame)
        self.vi_type1.insert(0,"Select_Type")
        self.vi_type1.configure(state="readonly",
            values='Select_Type Grocery Medicine ')
        self.vi_type1.place(anchor="nw", height=30, width=150, x=180, y=80)
        self.vi_type1.bind("<<ComboboxSelected>>",self.table_filter)
        self.vi_category1 = ttk.Combobox(self.View_Item_Frame)
        self.vi_category1.insert(0,"Select_Category")
        self.vi_category1.configure(state="readonly",
            values='Select_Category All Baby Kids Men Woman Old')
        self.vi_category1.place(anchor="nw", height=30, width=150, x=350, y=80)
        self.vi_category1.bind("<<ComboboxSelected>>",self.table_filter)
        self.vi_month = ttk.Combobox(self.View_Item_Frame)
        self.vi_month.insert(0,"Month")
        self.vi_month.configure(state="readonly",
            values='Month 1 2 3 4 5 6 7 8 9 10 11 12')
        self.vi_month.place(anchor="nw", height=30, width=70, x=520, y=80)
        self.vi_month.bind("<<ComboboxSelected>>",self.table_filter)
        self.vi_search1 = ttk.Entry(self.View_Item_Frame)
        self.vi_search1.insert(0,"Name/ID")
        self.vi_search1.place(anchor="nw", height=30, width=150, x=10, y=80)
        self.vi_search1.bind("<Return>",self.table_filter)
        #self.vi_search1.bind("<Key>",self.table_filter)
        if self.vi_search1.get()=="Name/ID":
            self.vi_search1.bind("<Enter>",self.clr)
        self.label26 = tk.Label(self.View_Item_Frame)
        self.label26.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Days Left:')
        self.label26.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=130,
            x=330,
            y=140)
        self.vi_day1 = ttk.Spinbox(self.View_Item_Frame)
        self.vi_day1.configure(
            font="{Calibri} 12 {bold}", from_=1, to=365)
        self.vi_day1.place(anchor="nw", width=100, x=470, y=145)
        self.vi_day1.bind("<Button-1>",self.table_filter)
        self.vi_quantity1 = tk.Scale(self.View_Item_Frame)
        self.vi_quantity1.configure(orient="horizontal")
        self.vi_quantity1.place(anchor="nw", height=40, width=150, x=160, y=140)
        self.vi_quantity1.bind("<ButtonRelease-1>",self.table_filter)
        self.label28 = tk.Label(self.View_Item_Frame)
        self.label28.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Quantity Left(%) :')
        self.label28.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=130,
            x=10,
            y=140)


        con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute("select * from {};".format(self.us+'_item_stocks'))
        data=cur.fetchall()
        con.close()

        

        self.vi_table = ttk.Treeview(self.View_Item_Frame)

        h_clr=ttk.Style(self.View_Item_Frame)
        h_clr.theme_use("clam")
        h_clr.configure("Treeview.Heading",font=('Helvetica',9,"bold"))

        self.vi_table['show']='headings'
        self.vi_table["columns"]=('S.N','Type','Category','Name','Id','Quantity','Price','Store','Exp. Date','Date','Q_Left','Total')
        
        self.vi_table.column('S.N',width=40,anchor='n',minwidth=0)
        self.vi_table.column('Type',width=60,anchor='center',minwidth=60)
        self.vi_table.column('Category',width=60,anchor='center',minwidth=60)
        self.vi_table.column('Name',width=70,anchor='center',minwidth=70)
        self.vi_table.column('Id',width=65,anchor='center',minwidth=65)
        self.vi_table.column('Quantity',width=60,anchor='n',minwidth=60)
        #self.vi_table.column('Q_Type',width=30,anchor='center',minwidth=30)
        self.vi_table.column('Price',width=40,anchor='center',minwidth=40)
        self.vi_table.column('Store',width=60,anchor='center',minwidth=60)
        self.vi_table.column('Exp. Date',width=75,anchor='center',minwidth=75)
        self.vi_table.column('Date',width=75,anchor='center',minwidth=75)
        self.vi_table.column('Q_Left',width=50,anchor='center',minwidth=50)
        self.vi_table.column('Total',width=50,anchor='center',minwidth=50)
        

        self.vi_table.heading('S.N',text='S.N',anchor='center')
        self.vi_table.heading('Type',text='Type',anchor='center')
        self.vi_table.heading('Category',text='Category',anchor='center')
        self.vi_table.heading('Name',text='Name',anchor='center')
        self.vi_table.heading('Id',text='Id',anchor='center')
        self.vi_table.heading('Quantity',text='Quantity',anchor='center')
        #self.vi_table.heading('Q_Type',text='Q_Type',anchor='center')
        self.vi_table.heading('Price',text='Price',anchor='center')
        self.vi_table.heading('Store',text='Store',anchor='center')
        self.vi_table.heading('Exp. Date',text='Exp. Date',anchor='center')
        self.vi_table.heading('Date',text='Date',anchor='center')
        self.vi_table.heading('Q_Left',text='Q_Left',anchor='center')
        self.vi_table.heading('Total',text='Total',anchor='center')

        c=1
        for i in data:
            if c%2:
                self.vi_table.insert('',c,text="",values=(c,i[0],i[1],i[2],i[3],str(i[4])+' '+i[5],str(i[6])+' Rs',i[7],i[8],i[9],i[10],i[4]*i[6]),tags=('odd',))
            else:
                self.vi_table.insert('',c,text="",values=(c,i[0],i[1],i[2],i[3],str(i[4])+' '+i[5],str(i[6])+' Rs',i[7],i[8],i[9],i[10],i[4]*i[6]),tags=('even',))
            c+=1
        self.vi_table.tag_configure('even',background="gray",foreground="white")

        hor_view=ttk.Scrollbar(self.View_Item_Frame,orient="horizontal")
        hor_view.configure(command=self.vi_table.xview)
        self.vi_table.configure(xscrollcommand=hor_view.set)
        hor_view.place(x=10,y=481,width=580)

        ver_view=ttk.Scrollbar(self.View_Item_Frame,orient="vertical")
        ver_view.configure(command=self.vi_table.yview)
        self.vi_table.configure(yscrollcommand=ver_view.set)
        ver_view.place(x=580,y=200,height=280)

        self.vi_table.place(x=10,y=200,height=280,width=570)
        
        self.update = tk.Button(self.View_Item_Frame)
        self.update.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='update',
            command=self.update_item)
            #command=lambda:self.update_item1(self.vi_table))
        self.update.place(anchor="nw", height=30, width=100, x=480, y=505)
        self.View_Item_Frame.place(
            anchor="nw", height=550, width=600, x=200, y=50)
        
        self.View_Item_Frame.place(
                anchor="nw", height=550, width=600, x=200, y=50)
        
        
        
        # Main widget
        self.mainwindow = self.main


    #Update Frame
    def update_item(self):
    
        con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute("select distinct(name) from {};".format(self.us+"_item_stocks"))
        data=cur.fetchall()
        con.close()
            
        self.Update_Item_frame = tk.Frame(self.main)
        self.Update_Item_frame.configure(
            background="#ffffff", height=200, width=200)
        self.label1 = tk.Label(self.Update_Item_frame)
        self.label1.configure(
            background="#ffffff",
            font="{Arial} 14 {bold underline}",
            foreground="#000000",
            justify="center",
            text='UPDATE ITEM')
        self.label1.place(anchor="nw", height=50, width=200, x=200, y=10)
        self.label3 = tk.Label(self.Update_Item_frame)
        self.label3.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Id:')
        self.label3.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=80)
        self.ui_type = ttk.Combobox(self.Update_Item_frame)
        self.ui_type.insert(0,"Select_Type")
        self.ui_type.configure(
            values='Grocery Medicine ',
            font="{Cambria} 14 {}")
        self.ui_type.place(anchor="nw", height=30, width=150, x=10, y=140)
        self.ui_category = ttk.Combobox(self.Update_Item_frame)
        self.ui_category.insert(0,"Select_Category")
        self.ui_category.configure(
            values='All Baby Kids Men Woman Old',
            font="{Cambria} 14 {}")
        self.ui_category.place(anchor="nw", height=30, width=150, x=10, y=200)
        self.ui_id = tk.Label(self.Update_Item_frame)
        self.ui_id.configure(
            background="#c0c0c0",
            font="{Arial} 12 {bold}",
            foreground="#000000")
        self.ui_id.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=150,
            x=300,
            y=80)

        self.label14 = tk.Label(self.Update_Item_frame)
        self.label14.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Quantity:')
        self.label14.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=140)
        self.label15 = tk.Label(self.Update_Item_frame)
        self.label15.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Price :')
        self.label15.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=200)
        self.label16 = tk.Label(self.Update_Item_frame)
        self.label16.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Store:')
        self.label16.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=260)
        self.ui_name = tk.Entry(self.Update_Item_frame)
        self.ui_name.configure(font="{Cambria} 14 {}")
        self.ui_name.place(anchor="nw", height=30, width=150, x=10, y=80)
        self.ui_quantity = tk.Spinbox(self.Update_Item_frame)
        self.ui_quantity.configure(
            font="{Calibri} 12 {bold}", from_=1, to=1000)
        self.ui_quantity.place(anchor="nw", height=30, width=60, x=300, y=140)
        self.ui_quantity_type = ttk.Combobox(self.Update_Item_frame)
        self.ui_quantity_type.insert(0,"Select")
        self.ui_quantity_type.configure(values='Pcs Gram KG Ltr',font="{Cambria} 14 {}")
        self.ui_quantity_type.place(
            anchor="nw", height=30, width=80, x=370, y=140)
        self.ui_price = tk.Entry(self.Update_Item_frame)
        self.ui_price.configure(font="{Cambria} 14 {}")
        self.ui_price.place(anchor="nw", height=30, width=150, x=300, y=200)
        self.ui_store = tk.Entry(self.Update_Item_frame)
        self.ui_store.configure(font="{Cambria} 14 {}")
        self.ui_store.place(anchor="nw", height=30, width=150, x=300, y=260)
        self.label18 = tk.Label(self.Update_Item_frame)
        self.label18.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Exp Date:')
        self.label18.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=320)
        self.label19 = tk.Label(self.Update_Item_frame)
        self.label19.configure(
            background="#ffffff",
            font="{Arial} 12 {bold}",
            foreground="#000000",
            text='Quantity Left:')
        self.label19.place(
            anchor="nw",
            height=30,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=180,
            y=380)
        self.ui_exp = tk.Entry(self.Update_Item_frame)
        self.ui_exp.configure(font="{Cambria} 14 {}")
        self.ui_exp.place(anchor="nw", height=30, width=150, x=300, y=320)
        self.ui_quantity_left = tk.Spinbox(self.Update_Item_frame)
        self.ui_quantity_left.configure(
            font="{Calibri} 12 {bold}", from_=1, to=1000)
        self.ui_quantity_left.place(anchor="nw", height=30, width=60, x=300, y=380)
        self.ui_update = tk.Button(self.Update_Item_frame)
        self.ui_update.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='update',
            command=self.update_fun)
        self.ui_update.place(anchor="nw", height=30, width=120, x=250, y=450)
        self.Update_Item_frame.place(
            anchor="nw", height=550, width=600, x=200, y=50)

        self.update_item1(self.vi_table)

        # Main widget
        self.mainwindow = self.main
    #Shoping List Design
    def shoping_list_design(self):
        
        self.Shoping_List_Frame = tk.Frame(self.main)
        self.Shoping_List_Frame.configure(
            background="#ffffff", height=200, width=200)
        self.label8 = tk.Label(self.Shoping_List_Frame)
        self.label8.configure(
            background="#ffffff",
            font="{Arial} 14 {bold underline}",
            foreground="#000000",
            justify="center",
            text='SHOPING LIST')
        self.label8.place(anchor="nw", height=50, width=200, x=200, y=10)

        self.label9 = tk.Label(self.Shoping_List_Frame)
        self.label9.configure(
            background="#ffffff",
            font="{Arial} 12 {}",
            foreground="#000000",
            justify="center",
            text='Total :')
        self.label9.place(anchor="nw", height=50, width=70, x=290, y=190)
        self.sl_total = tk.Entry(self.Shoping_List_Frame)
        self.sl_total.configure(font="{Cambria} 14 {}")
        self.sl_total.place(anchor="nw", height=30, width=85, x=365, y=200)
        

        self.sl_type = ttk.Combobox(self.Shoping_List_Frame)
        self.sl_type.insert(0,"Select_Type")
        self.sl_type.configure(state="readonly",
            values='Select_Type Grocery Medicine ',font="{Cambria} 14 {}")
        self.sl_type.place(anchor="nw", height=30, width=150, x=300, y=110)
        self.sl_type.bind("<<ComboboxSelected>>",self.shoping_filter)
        self.sl_category = ttk.Combobox(self.Shoping_List_Frame)
        self.sl_category.insert(0,"Select_Category")
        self.sl_category.configure(state="readonly",
            values='Select_Category All Baby Kids Men Woman Old',font="{Cambria} 14 {}")
        self.sl_category.place(anchor="nw", height=30, width=150, x=300, y=150)
        self.sl_category.bind("<<ComboboxSelected>>",self.shoping_filter)
        self.sl_month = ttk.Combobox(self.Shoping_List_Frame)
        self.sl_month.insert(0,datetime.now().month)
        self.sl_month.configure(state="readonly",
            values='1 2 3 4 5 6 7 8 9 10 11 12',font="{Cambria} 14 {}")
        self.sl_month.place(anchor="nw", height=30, width=150, x=300, y=70)
        self.sl_month.bind("<<ComboboxSelected>>",self.shoping_filter)
        
        
        #Fetching Data from database
        
        con=ms.connect(host="localhost",database="house",user="root",passwd="12345")
        cur=con.cursor()
        cur.execute("select Name,quantity-quantity_left,quantity_type,price*(quantity-quantity_left) from {} where quantity_left<=quantity*50/100 and month(date)='{}';".format(self.us+'_item_stocks',self.sl_month.get()))
        data=cur.fetchall()
        
        self.sl_text_area = ScrolledText(self.Shoping_List_Frame)
        self.sl_text_area.configure(
                background="#c0c0c0",
                font="{Arial} 12 {}",
                )
        for i in data:
            s=""
            for val in i:
                s=s+str(val)+" "
            s=s+"Rs\n"
            self.sl_text_area.insert('insert',s)
        self.sl_text_area.place(
            anchor="nw",
            height=420,
            width=250,
            x=10,
            y=70)

        
        self.Shoping_List_Frame.place(
            anchor="nw", height=550, width=600, x=200, y=50)
        '''self.sl_generate_list = tk.Button(self.Shoping_List_Frame)
        self.sl_generate_list.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='Generate List')
        self.sl_generate_list.place(
            anchor="nw", height=30, width=120, x=40, y=510)'''
        self.sl_whatsapp = tk.Button(self.Shoping_List_Frame)
        self.sl_whatsapp.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='Whatsapp',
            command=self.whatsapp)
        self.sl_whatsapp.place(anchor="nw", height=30, width=120, x=210, y=510)
        self.sl_print = tk.Button(self.Shoping_List_Frame)
        self.sl_print.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='Print',
            command=self.sl_prints)
        self.sl_print.place(anchor="nw", height=30, width=120, x=380, y=510)

        self.shoping_filter(self)

        # Main widget
        self.mainwindow = self.main
        
    def __init__(self,u,p,master=None):
        # build ui
        #LoginDesignApp.__init__(self)
        self.us=u
        self.ph=p
        self.main = tk.Tk() if master is None else tk.Toplevel(master)
        self.main.configure(background="#ffffff", height=600, width=800)
        self.main.title("HouseHold Managment System")
        self.main.resizable(0,0)
        self.header = tk.Label(self.main)
        self.header.configure(
            background="#1a73e8",
            font="{Arial} 14 {bold}",
            foreground="#ffffff",
            justify="left",
            text='HOUSEHOLD MANAGMENT SYSTEM')
        self.header.place(anchor="nw", height=50, width=800, x=0, y=0)
        self.sep = ttk.Separator(self.main)
        self.sep.configure(orient="vertical")
        self.sep.place(anchor="nw", height=550, width=2, x=199, y=50)
        self.REGISTER = tk.Button(self.main)
        self.REGISTER.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='REGISTER',
            command=self.register)
        self.REGISTER.place(anchor="nw", height=30, width=120, x=40, y=70)
        
        self.add = tk.Button(self.main)
        self.add.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='ADD ITEM',
            command=self.added_item)
        self.add.place(anchor="nw", height=30, width=120, x=40, y=130)
        self.show_items = tk.Button(self.main)
        self.show_items.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='SHOW ITEM',
            command=self.view_item)
        self.show_items.place(anchor="nw", height=30, width=120, x=40, y=190)
        self.shoping_List = tk.Button(self.main)
        self.shoping_List.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='SHOPING LIST',
            command=self.shoping_list_design)
        self.shoping_List.place(anchor="nw", height=30, width=120, x=40, y=250)
        '''self.update = tk.Button(self.main)
        self.update.configure(
            background="#1a73e8",
            disabledforeground="#ffffff",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='UPDATE',
            command=self.update_item)
        self.update.place(anchor="nw", height=30, width=120, x=40, y=310)'''

        '''self.setting = tk.Menubutton(self.main)
        self.setting.configure(
            background="#1a73e8",
            font="{Cambria} 14 {}",
            foreground="#ffffff",
            text='SETTING')
        self.setting.place(anchor="nw", height=30, width=120, x=40, y=310)'''

        self.user = tk.Label(self.main)
        self.user.configure(
            background="#1a73e8",
            font="{Arial} 14 {bold}",
            foreground="#ff0000",
            justify="center",
            text=self.us)
        self.user.place(anchor="nw", height=30, width=120, x=600, y=10)

        
        '''self.mb=tk.Menu(self.setting)
        self.setting['menu']=self.mb
        self.mb.add_command(label="Add Type")
        self.mb.add_command(label="Add Category")
        self.mb.add_command(label="Delete Type")
        self.mb.add_command(label="Delete Category")'''
    
        '''self.home_icon = tk.Label(self.main)
        self.img = tk.PhotoImage(file="icon.png")
        self.home_icon.configure(
            cursor="hand2",
            image=self.img,
            text='label1')
        self.home_icon.place(
            anchor="nw", height=220, width=270, x=350, y=70)'''
       

        # Main widget
        self.mainwindow = self.main

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NewprojectApp("")
    app.run()

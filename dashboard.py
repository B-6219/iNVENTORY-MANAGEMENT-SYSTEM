from  tkinter import *
from tkinter import ttk

def employee_form():
    global back_image
    employee_frame =Frame(root, width=1070,height=567)
    employee_frame.place(x=200,y=100)
    heading_label = Label(employee_frame,text='Manage Employee Details', font=('times new roman',16, 'bold') ,bg='#0f4d7d',fg='white')
    heading_label.place(x=0,y=0,relwidth=1)
    
    back_image =PhotoImage (file='logout.png')
    back_button =Button(employee_frame, image=back_image,cursor='hand2',command=lambda: emp_frame.place_forget())
    back_button.place(x=10,y=30)
    
    top_frame = Frame(employee_frame)
    top_frame.place(x=0,y=60,relwidth=1,height=200)
    search_frame = Frame(top_frame)
    search_frame.pack()
    
    search_combobox =ttk.Combobox(search_frame,values=('Id', 'Name','Email'),state='readnly',font=('monospace 10'),justify='center')
    search_combobox.set('Search By')
    search_combobox.grid(column=0,row=0,padx=20)
    
    search_entry =Entry(search_frame,font=('monospace',10),bg='lightyellow',cursor='hand2')
    search_entry.grid(row=0,column=2)
    
    search_button =Button(search_frame,text='Search',font=('times new roman'),cursor='hand2')
    search_button.grid(column=2,row=0 ,padx=20)
    
    show_button =Button(search_frame,bg="blue",fg="red",text='Show All',font=('times new roman'),cursor='hand2')
    show_button.grid(column=3,row=0 ,padx=20)
    
    employee_treeview =ttk.Treeview(top_frame,columns=('empid','name','email'),show='headings')
    employee_treeview.pack(pady=9)
    
    employee_treeview.heading('empid' , text='ID')
    employee_treeview.heading('name' , text='Name')
    employee_treeview.heading('email' , text='Email')

#GUI INterface
root = Tk()

root.title('Inventory Management System')
root.geometry("900x700+0+0")
root.resizable(False ,False)
root.config(bg="black")


bg_Image = PhotoImage(file='inventory.png')
titleLabel = Label(root, image=bg_Image,compound=LEFT,text='Inventory management System',font=('times new roman',30,'bold'),bg='#010c48', fg='white',anchor='w',padx=20)
titleLabel.place(x=0, y=10,relwidth=1)

logoutButton = Button ( root,text='logout',font=('times new roman', 20 ,'bold'),fg='#010c48')
logoutButton.place(x=800,y=10)


subtitle_label = Label(root, text='Welcome Admin \t\t Date: 08-08-2024 \t\t Time: 08:00',font=('times new roman',16),bg='#4d636d',fg='white')
subtitle_label.place(x= 0, y=70, relwidth=1)


left_Frame = Frame(root)
left_Frame.place(x=0, y=100,width=200,height=560)

logoImage=PhotoImage(file="logo.png")
image_label = Label(left_Frame,image=logoImage)
image_label.pack()

menuLabel = Label(left_Frame,text='Menu',  font= ('times new roman',20),bg='#009688')
menuLabel.pack(fill=X)

employee_icon =PhotoImage(file='teamwork.png')
employee_button = Button(left_Frame, image=employee_icon,compound='left', text='Employee',font=('times new roman' , 20, 'bold'),anchor='w',padx=10,command=employee_form)
employee_button.pack(fill=X)

suppliers_icon =PhotoImage(file='increase.png')
suppliers_button = Button(left_Frame, image=suppliers_icon,compound='left', text='Suppliers',font=('times new roman' , 20, 'bold'),anchor='w',padx=10)
suppliers_button.pack(fill=X)

category_icon =PhotoImage(file='categories.png')
category_button = Button(left_Frame, image=category_icon,compound='left',text='Category',font=('times new roman' , 20, 'bold'),anchor='w',padx=10)
category_button.pack(fill=X)

product_icon =PhotoImage(file='new-product.png')
product_button = Button(left_Frame,image=product_icon,compound='left', text='Product',font=('times new roman' , 20, 'bold'),anchor='w',padx=10)
product_button.pack(fill=X)

sales_icon =PhotoImage(file='packages.png')
sales_button = Button(left_Frame,image=sales_icon,compound='left',text='Sales',font=('times new roman' , 20, 'bold'),anchor='w',padx=10)
sales_button.pack(fill=X)

exit_icon =PhotoImage(file='logout.png')
exit_button = Button(left_Frame,image=exit_icon,compound='left',text='Exit',font=('times new roman' , 20, 'bold'),anchor='w',padx=10)
exit_button.pack(fill=X)


#employee frame
emp_frame = Frame(root,bg='#2c3e50',bd=3,relief=RIDGE)
emp_frame.place(x=600,y=126,height=170,width=280)
total_emp_icon = PhotoImage(file='staff.png') 
total_emp_icon_label = Label(emp_frame,image=total_emp_icon, bg='#2c3e50')
total_emp_icon_label.pack()

total_emp_label =Label(emp_frame,text='Total Employees',bg='#2c3e50' ,fg='white',font=('times new roman',15,'bold'))
total_emp_label.pack()

total_emp_label =Label(emp_frame,text='0',bg='#2c3e50' ,fg='white',font=('times new roman',30,'bold'))
total_emp_label.pack()


#supplier frame
sup_frame = Frame(root,bg='#8e44ad',bd=3,relief=RIDGE)
sup_frame.place(x=300,y=300,height=170,width=280)
sup_emp_icon = PhotoImage(file='sales.png') 
sup_emp_icon_label = Label(sup_frame,image=sup_emp_icon, bg='#8e44ad')
sup_emp_icon_label.pack()

total_sup_label =Label(sup_frame,text='Total Suppliers',bg='#8e44ad' ,fg='white',font=('times new roman',15,'bold'))
total_sup_label.pack()

total_sup_label =Label(sup_frame,text='0',bg='#8e44ad' ,fg='white',font=('times new roman',30,'bold'))
total_sup_label.pack()


#categories frame
cat_frame = Frame(root,bg='#e74c3c',bd=3,relief=RIDGE)
cat_frame.place(x=300,y=125,height=170,width=280)
total_cat_icon = PhotoImage(file='market-segment.png') 
total_cat_icon_label = Label(cat_frame,image=total_cat_icon, bg='#e74c3c')
total_cat_icon_label.pack()

total_cat_label =Label(cat_frame,text='Total Categories',bg= '#e74c3c' ,fg='white',font=('times new roman',15,'bold'))
total_cat_label.pack()

total_cat_label =Label(cat_frame,text='0',bg='#e74c3c' ,fg='white',font=('times new roman',30,'bold'))
total_cat_label.pack()


#products frame
prod_frame = Frame(root,bg='#27ae60',bd=3,relief=RIDGE)
prod_frame.place(x=600,y=300,height=170,width=280)
total_prod_icon = PhotoImage(file='products.png') 
total_prod_icon_label = Label(prod_frame,image=total_prod_icon, bg='#27ae60')
total_prod_icon_label.pack()

total_prod_label =Label(prod_frame,text='Total Products',bg= '#27ae60' ,fg='white',font=('times new roman',15,'bold'))
total_prod_label.pack()

total_prod_label =Label(prod_frame,text='0',bg='#27ae60' ,fg='white',font=('times new roman',30,'bold'))
total_prod_label.pack()


#sales frame
sale_frame = Frame(root,bg='#540627',bd=3,relief=RIDGE)
sale_frame.place(x=410,y=500,height=170,width=280)
total_sale_icon = PhotoImage(file='sales.png') 
total_sale_icon_label = Label(sale_frame,image=total_sale_icon, bg='#540627')
total_sale_icon_label.pack()

total_sale_label =Label(sale_frame,text='Total Sale',bg= '#540627' ,fg='white',font=('times new roman',15,'bold'))
total_sale_label.pack()

total_sale_label =Label(sale_frame,text='0',bg='#540627' ,fg='white',font=('times new roman',30,'bold'))
total_sale_label.pack()


root.mainloop()

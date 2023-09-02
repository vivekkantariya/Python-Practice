from tkinter import *
from tkinter import messagebox
import pymongo

root=Tk()
root.title("Billing Application")
root.geometry('1280x720')
label_fg_color = 'white'
entry_bg_color = '#EAE2B7'  # Choose your desired color
bg_color='#0074D9'
bg_color_main = '#FF6B6B'  # Choose your desired color
bg_color_frames = '#1D3557'  # Choose your desired color

# variable
c_name=StringVar()
c_phone=StringVar()
item=StringVar()
Rate=IntVar()
quantity=IntVar()
bill_no=StringVar()
current_bill_number = 1000  

global l
l=[] 

client = pymongo.MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB URI
db = client["billing_db"]
bills_collection = db["bills"]
settings_collection = db["settings"]

def load_current_bill_number():
    setting = settings_collection.find_one({"name": "current_bill_number"})
    if setting:
        return setting["value"]     
    return 1000

def save_current_bill_number(number):
    settings_collection.update_one(
        {"name": "current_bill_number"},
        {"$set": {"value": number}},
        upsert=True
    )
    
current_bill_number = load_current_bill_number()

# Functions
def additm():
    n = Rate.get()
    m = quantity.get() * n
    l.append(m)
    if item.get() != '':
        textarea.insert((10.0 + float(len(l) - 1)), f"\t{item.get()}\t\t  {quantity.get()}\t\t {m}\n")
    else:
        messagebox.showerror('Error', 'Please enter an item')
        
        
def gbill():
    global current_bill_number
    if c_name.get() == "" or c_phone.get() == "":
        messagebox.showerror("Error", "Customer detail are must")
    else:
        bill_no.set(str(current_bill_number)) 
        textAreaText = textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END, f"\n===============================================")
        textarea.insert(END, f"\nTotal Paybill Amount :\t\t      {sum(l)}")
        textarea.insert(END, f"\n\n===============================================")
        save_bill()

        current_bill_number += 1
        save_current_bill_number(current_bill_number)  

        
def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0)
    quantity.set(0)
    welcome()
    
def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()
        
def save_bill():
    save = messagebox.askyesno("Save bill", "Do you want to save the Bill?")
    if save:
        bill_details = textarea.get('1.0', END)
        try:
            bill_data = {
                "bill_number": bill_no.get(),
                "customer_name": c_name.get(),
                "phone_number": c_phone.get(),
                "bill_details": bill_details,
                "total_amount": sum(l)
            }
            bills_collection.insert_one(bill_data)
            messagebox.showinfo("Saved", f"Bill no. :{bill_no.get()} Saved Successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            

def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\n\t\t  Jay Gurudev General Store ") # Replace with your shop name 
    textarea.insert(END,f"\n\n  Bill Number:\t\t{bill_no.get()}")
    textarea.insert(END,f"\n  Customer Name:\t\t{c_name.get()}")
    textarea.insert(END,f"\n  Phone Number:\t\t{c_phone.get()}")
    textarea.insert(END,f"\n\n===============================================")
    textarea.insert(END,"\n\tProduct\t\tQTY\t\tPrice")
    textarea.insert(END,f"\n===============================================\n")
    textarea.configure(font='arial 15 bold')

title=Label(root,pady=10,text="Billing Software",bg=bg_color,fg='white',font=('times new roman', 30 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

# Product Frames
F1=LabelFrame(root,relief=GROOVE,text='Customer Details',font=('verdana',15,'bold'),fg='gold',bg= bg_color, padx=20, pady=20, borderwidth=5, border='2')
F1.place(x=10,y=90,relwidth=0.97)

cname_lbl = Label(F1, text='Customer Name', font=('Cambria', 18, 'bold'), bg=bg_color_frames, fg=label_fg_color)
cname_lbl.grid(row=0, column=0, padx=20, pady=5)
cname_txt = Entry(F1, width=15, textvariable=c_name, font='Cambria 15 bold', relief=SUNKEN, bg=entry_bg_color)
cname_txt.grid(row=0, column=1, padx=10, pady=5)

cphone_lbl = Label(F1, text='Phone No. ', font=('Cambria', 18, 'bold'), bg=bg_color_frames, fg=label_fg_color)
cphone_lbl.grid(row=0, column=2, padx=20, pady=5)
cphone_txt = Entry(F1, width=15, font='Cambria 15 bold', textvariable=c_phone, relief=SUNKEN, bg=entry_bg_color)
cphone_txt.grid(row=0, column=3, padx=10, pady=5)

F2 = LabelFrame(root, text='Product Details', font=('Cambria', 18, 'bold'), fg='gold', bg=bg_color_frames)
F2.place(x=10, y=220, width=630, height=500)

itm = Label(F2, text='Product Name', font=('Cambria', 18, 'bold'), bg=bg_color_frames, fg=label_fg_color)
itm.grid(row=0, column=0, padx=30, pady=20)
itm_txt = Entry(F2, width=20, textvariable=item, font='Cambria 15 bold', relief=RIDGE, bg=entry_bg_color)
itm_txt.grid(row=0, column=1, padx=10, pady=20)

rate = Label(F2, text='Product Rate', font=('Cambria', 18, 'bold'), bg=bg_color_frames, fg=label_fg_color)
rate.grid(row=1, column=0, padx=30, pady=20)
rate_txt = Entry(F2, width=20, textvariable=Rate, font='Cambria', relief=RIDGE, bg=entry_bg_color)
rate_txt.grid(row=1, column=1, padx=10, pady=20)

n = Label(F2, text='Product Quantity', font=('Cambria', 18, 'bold'), bg=bg_color_frames, fg=label_fg_color)
n.grid(row=2, column=0, padx=30, pady=20)
n_txt = Entry(F2, width=20, textvariable=quantity, font='Cambria', relief=RIDGE , bg=entry_bg_color)
n_txt.grid(row=2, column=1, padx=10, pady=20)

# Bill Area
F3 = Frame(root, relief=GROOVE, borderwidth=5, border='2')
F3.place(x=655, y=220, width=600, height=500)
bill_title = Label(F3, text='Bill Area', font='Helvetica 15 bold', bd=7, relief=GROOVE).pack(fill=X)
scrol_y = Scrollbar(F3, orient=VERTICAL)
textarea = Text(F3, yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()

root.configure(bg=bg_color_main)
F1.configure(bg=bg_color_frames)
F2.configure(bg=bg_color_frames)
F3.configure(bg='white')
title.configure(bg=bg_color_main)

# Buttons styling
btn_styles = {
    'font': 'Cambria 15 bold',
    'bg': '#D35400',
    'fg': 'white',   # White text color
    'width': 15,
    'bd': 3,
    'relief': 'raised'
}

# Buttons
btn1 = Button(F2, text='Add Item', command=additm, **btn_styles)
btn2 = Button(F2, text='Generate Bill', command=gbill, **btn_styles)
btn3 = Button(F2, text='Clear', command=clear, **btn_styles)
btn1.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")
btn2.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")
btn3.grid(row=5, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

root.mainloop()
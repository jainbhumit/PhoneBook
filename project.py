from tkinter import *
import pywhatkit
from PIL import ImageTk, Image

# Create Object
app = Tk()

# Set geometry
app.title('Phone Book')
app.geometry('1920x3840')
# app.iconbitmap('favicon.ico')

img = Image.open('D:\\python\\project\\project_phonebook\\black-spectacles-otop-an-open-book.jpg')
img1=img.resize((2000,2000))
img2 = ImageTk.PhotoImage(img1)
Image_label=Label(app, image=img2)
Image_label.place(x=0,y=-300)


photo=PhotoImage(file=r"D:\python\project\project_phonebook\images.png")



# Information List
datas = []

# Add Information
def add():
	global datas
	datas.append([Name.get(),Number.get(),address.get(1.0, "end-1c")])
	update_book()


# View Information
def view():
	
	Name.set(datas[int(select.curselection()[0])][0])
	Number.set(datas[int(select.curselection()[0])][1])
	address.delete(1.0,"end")
	address.insert(1.0, datas[int(select.curselection()[0])][2])

def whatApp():

	num = datas[int(select.curselection()[0])][1]
	print(num)
	pywhatkit.sendwhatmsg_instantly(str(num),str(YourMessage.get()))
    

# Delete Information
def delete():
	del datas[int(select.curselection()[0])]
	update_book()

def reset():
	Name.set('')
	Number.set('')
	address.delete(1.0,"end")
    
    


# Update Information
def update_book():
	select.delete(0,END)
	for n,p,a in datas:
		select.insert(END, n)



# Add Buttons, Label, ListBox
Name = StringVar()
Number = StringVar()
YourMessage=StringVar()

frame = Frame()
frame.pack(pady=10)

frame1 = Frame()
frame1.pack()

frame2 = Frame()
frame2.pack(pady=10)

frame3=Frame()
frame3.pack(pady=5)


Label(frame3,text="Your Message",font='arial 12 bold',fg="black").pack(side=LEFT)
Entry(frame3,textvariable=YourMessage,width=50).pack()

Label(frame, text = 'Name', font='arial 12 bold',fg="black").pack(side=LEFT)
Entry(frame, textvariable = Name,width=55).pack()

Label(frame1, text = 'Phone No.(with code)', font='arial 12 bold',fg="black").pack(side=LEFT)
Entry(frame1, textvariable = Number,width=50).pack()

Label(frame2, text = 'Address', font='arial 12 bold',fg="black").pack(side=LEFT)
address = Text(frame2,width=45,height=10)
address.pack()

Button(app,text="Add",font="arial 12 bold",command=add,fg="black").place(x= 100, y=270)

Button(app,text="View",font="arial 12 bold",command=view,fg="black").place(x= 100, y=310)
Button(app,text="whatsappMessage",font=("arial 12 bold"),command=whatApp,bg="green",fg="white",width=100,height=100,image=photo).pack(pady=5)

Button(app,text="Delete",font="arial 12 bold",command=delete,fg="black").place(x= 100, y=350)
Button(app,text="Reset",font="arial 12 bold",command=reset,fg="black").place(x= 100, y=390)

scroll_bar = Scrollbar(app, orient=VERTICAL)
select = Listbox(app, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200,y=260)

# Execute Tkinter
app.mainloop()
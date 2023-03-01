from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('บันทึกการปฏิบัติงาน')
GUI.geometry('600x500')

L1 = Label(GUI,text='บันทึกการปฏิบัติงาน',font=('Angsana New',30),fg='red')
L1.place(x=170,y=30)

############################

L2 = Label(GUI,text='วันที่',font=('Angsana New',20),fg='black')
L2.place(x=30,y=100)
E2 =ttk.Entry()
E2.place(x=110,y=110)

L3 = Label(GUI,text='เวลา',font=('Angsana New',20),fg='black')
L3.place(x=300,y=100)
E3 =ttk.Entry()
E3.place(x=400,y=110)

L4 = Label(GUI,text='เครื่องจักร',font=('Angsana New',20),fg='black')
L4.place(x=30,y=140)
E4 =ttk.Entry()
E4.place(x=110,y=150)

L5 = Label(GUI,text='สถานะ',font=('Angsana New',20),fg='black')
L5.place(x=300,y=140)
combol = ttk.Combobox(value=["รออะไหล่","รอ COP","แก้ไขแล้ว"])
combol.place(x=400,y=150)

L6 = Label(GUI,text='อาการเสีย',font=('Angsana New',20),fg='black')
L6.place(x=30,y=180)
E6 =ttk.Entry()
E6.place(x=110,y=190)

L7 = Label(GUI,text='การแก้ไข',font=('Angsana New',20),fg='black')
L7.place(x=30,y=220)
E7 =ttk.Entry()
E7.place(x=110,y=230)

###################################

def Button1():
    text = 'บันทึกสำเร็จ'
    messagebox.showinfo('บันทึก',text)

FB1 = Frame(GUI)
FB1.place(x=250,y=400)
B1 = ttk.Button(text='บันทึก',command=Button1)
B1.pack(ipadx=25,ipady=4e0)

GUI.mainloop()

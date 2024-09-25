from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
def exit():
    hostl.destroy()
    import main
hostl=Tk()
hostl.title("HOSTEL STUDENTS")
width= hostl.winfo_screenwidth()
height= hostl.winfo_screenheight()
hostl.geometry("%dx%d" % (width, height))
back_icon=PhotoImage(file="back_icon.png")
back=Button(hostl,image=back_icon,bd=0,bg="white",fg="orange red",text="Back",cursor="hand2",width=70,compound="left",font=("Times New Roman",15,"bold"),command=exit)
back.place(x=50,y=20)
label=Label(hostl,text="Hostel Students",font=("Times New Roman",35,"bold"))
label.place(x=600,y=100)


column=["Id","Name","Inter College","Inter Marks","Phone No","Gender","Email","Place","Degree","Branch","State"]
table=ttk.Treeview(hostl,columns=column,show="headings")
s=ttk.Style(hostl)
s.theme_use("clam")
s.configure(".",font=("Times New Roman",15),rowheight=50)
s.map("Treeview",background=[("selected","midnight blue")])
s.configure("Treeview.Heading",background="SteelBlue1",font=("Helvetica",15,"bold"))
for i in column:
    table.heading(i,text=i)
table.column("Id",width=15,anchor="center") 
table.column("Name",width=150)
table.column("Inter College",width=80)
table.column("Inter Marks",width=80,anchor="center")
table.column("Phone No",width=70)
table.column("Gender",width=25,minwidth=50,anchor="center")
table.column("Email",width=130)
table.column("Place",width=50)
table.column("Degree",width=30,anchor="center")
table.column("Branch",width=25,minwidth=50,anchor="center")
table.column("State",width=50)      

# Horizontal scrollbar
hsb = ttk.Scrollbar(hostl, orient="horizontal", command=table.xview)
table.configure(xscrollcommand=hsb.set)
hsb.pack(side="bottom", fill="x")
table.pack(padx=100,pady=200,side="left", fill="both", expand=True)

#Connect Database
con=pymysql.connect(host="localhost",user="root",password="1234",database="student_dtbase")
mycursor=con.cursor()
query="use student_dtbase"
mycursor.execute(query)
query="select id,concat(fname,%s,mname,%s,lname),inter_clgname,inter_marks,mobile_no,gender,email_id,place,degree,branch,state from student_details where hostel=%s"
mycursor.execute(query,(" "," ","yes"))
row=mycursor.fetchall()
for j in row:
    table.insert("","end",values=(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10]))
query="select count(hostel) from student_details where hostel=%s"
mycursor.execute(query,"yes")
row=mycursor.fetchone()

con.commit()
con.close()
a=row[0]
count=Label(hostl,text=f"Total Count :  {a}",font=("Times New Roman",20,"bold"))
count.place(x=1200,y=150)
hostl.mainloop()

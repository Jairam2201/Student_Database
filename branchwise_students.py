from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
def exit():
    total.destroy()
    import main

def details():
    for row in table.get_children():
        table.delete(row)
    con=pymysql.connect(host="localhost",user="root",password="1234",database="student_dtbase")
    mycursor=con.cursor()
    query="use student_dtbase"
    mycursor.execute(query)
    branch_list = ['CSE', 'ECE', 'EEE', 'CIVIL', 'DS', 'AI', 'AI-ML']
    input_branch = branch.get()
    if input_branch not in branch_list:
        messagebox.showerror("ERROR", "Invalid branch name.")
        return
    else:
        query="select id,concat(fname,%s,mname,%s,lname),inter_clgname,inter_marks,mobile_no,gender,email_id,place,degree,branch,state,hostel from student_details where branch=%s"
        mycursor.execute(query,(" "," ",branch.get()))
        row=mycursor.fetchall()
        for j in row:
            table.insert("","end",values=(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10],j[11]))  
    query="select count(id) from student_details where branch=%s"
    mycursor.execute(query,branch.get())
    row=mycursor.fetchone()
    a=row[0]
    count=Label(total,text=f"Total Count :  {a}",font=("Times New Roman",20,"bold"))
    count.place(x=1210,y=200)
    con.commit()
    con.close()
   

total=Tk()
total.title("BRANCHWISE STUDENTS LIST")
width= total.winfo_screenwidth()
height= total.winfo_screenheight()
total.geometry("%dx%d" % (width, height))

back_icon=PhotoImage(file="back_icon.png")
back=Button(total,image=back_icon,text="Back",bd=0,bg="white",fg="orange red",cursor="hand2",width=70,compound=LEFT,font=("Times New Roman",15,"bold"),command=exit)
back.place(x=50,y=20)
label=Label(total,text="Branch name : ",font=("Times New Roman",20,"bold"))
label.place(x=500,y=80)
frame=Frame(total,highlightbackground="gray55",highlightthickness=1,highlightcolor="orange red")
frame.place(x=700,y=84)
string=StringVar()
branch=Entry(frame,bd=0,bg="gray87",font=("Times New Roman",18,"bold"),textvariable=string)
branch.grid()
submit=Button(total,text="Submit",bg="blue",fg="white",activebackground="blue4",activeforeground="white",cursor="hand2",font=("Times New Roman",15,"bold"),command=details)
submit.place(x=650,y=150)

column=["Id","Name","Inter College","Inter Marks","Phone No","Gender","Email","Place","Degree","Branch","State","Hostel"]
table=ttk.Treeview(total,columns=column,show="headings")
s=ttk.Style(total)
s.theme_use("clam")
s.configure(".",font=("Times New Roman",15))
s.map("Treeview",background=[("selected","midnight blue")])
s.configure("Treeview", rowheight=50)
s.configure("Treeview.Heading",background="SteelBlue1",font=("Helvetica",15,"bold"))
for i in column:
    table.heading(i,text=i)
table.column("Id",width=15,anchor="center") 
table.column("Name",width=150)
table.column("Inter College",width=80)
table.column("Inter Marks",width=80,anchor="center")
table.column("Phone No",width=70)
table.column("Gender",width=40,anchor="center")
table.column("Email",width=130)
table.column("Place",width=50)
table.column("Degree",width=40,anchor="center")
table.column("Branch",width=40,anchor="center")
table.column("State",width=50)
table.column("Hostel",width=25,anchor="center")

# Horizontal scrollbar
hsb = ttk.Scrollbar(total, orient="horizontal", command=table.xview)
table.configure(xscrollcommand=hsb.set)
hsb.pack(side="bottom", fill="x")
table.pack(padx=100,pady=250,side="left", fill="both", expand=True)



total.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import cryptography
#import pywhatkit
#import datetime
#functionality part
def scratch():
    l=[firstname,mname,lname,inter_clgname,inter_marks,phno,email,place]
    for i in l:
        i.delete(0,"end")
    sel_degree.set("Select Degree")
    sel_branch.set("Select Branch")
    sel_states.set("Select state")
    hostel.set("Select yes or no")
    bus.set("Select yes or no")
    radio.set(None)
def exit():
    add.destroy()
    import main
def submit():
     
     l=[firstname,lname,inter_clgname,inter_marks,phno,email,place]
     for i in l:
          if i.get() == '':
               messagebox.showerror("ERROR","All details are required.")
               return
     value=radio.get()
     if value!="Male" and value!="Female" and value!="Others":
          messagebox.showerror("ERROR","Please select your gender.")
          return
     elif sel_degree.get()=="Select Degree" or sel_branch.get()=="Select Branch" or sel_states.get()=="Select state" or hostel.get()=="Select yes or no" or bus.get()=="Select yes or no":
          messagebox.showerror("ERROR","Missing Selections.")
          return
     try:
        inter_marks_value = int(inter_marks.get())
        
     except ValueError:
        messagebox.showerror("ERROR", "Please enter valid marks.")
        return
     try:
         phno_value = int(phno.get())
     except ValueError:
        messagebox.showerror("ERROR", "Please enter valid phone number.")
        return
    
     con=pymysql.connect(host="localhost",user="root",password="1234")
     mycursor=con.cursor()
     try:
               query="create database student_dtbase"
               mycursor.execute(query)
               query="use student_dtbase"
               mycursor.execute(query)
               query="create table student_details(id int not null auto_increment primary key,fname varchar(50),mname varchar(50),lname varchar(50),inter_clgname varchar(100),inter_marks bigint,mobile_no bigint,gender varchar(10),email_id varchar(100),place varchar(100),degree varchar(100),branch varchar(50),state varchar(100),hostel varchar(50),bus varchar(50))"
               mycursor.execute(query)
     except:
               query="use student_dtbase"
               mycursor.execute(query)
     finally:
               query="insert into student_details(fname,mname,lname,inter_clgname,inter_marks,mobile_no,gender,email_id,place,degree,branch,state,hostel,bus) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
               mycursor.execute(query,(firstname.get(),mname.get(),lname.get(),inter_clgname.get(),inter_marks.get(),phno.get(),radio.get(),email.get(),place.get(),sel_degree.get(),sel_branch.get(),sel_states.get(),hostel.get(),bus.get()))
               messagebox.showinfo("SUCCESS","Student Details Added.")
               con.commit()
               rollno=Toplevel(add)
               rollno.resizable(0,0)
               rollno.title("ROLLNO")
               label=Label(rollno,text="Your Roll No is:",font=("Times New Roman",25,"bold"))
               label.grid(row=0,column=0,padx=(10,10),pady=(15,15))
               query="select id from student_details where fname=%s and lname=%s and email_id=%s"
               mycursor.execute(query,(firstname.get(),lname.get(),email.get()))
               row=mycursor.fetchone()
               rollno_labl=Label(rollno,text=row,font=("Times New Roman",25,"bold"))
               rollno_labl.grid(row=1,column=0,padx=(25,10),pady=(0,15))
               rollno.mainloop()
               '''
               num=str(phno.get())
               cntry_code="+91"
               moble_no=cntry_code+num
               time=datetime.datetime.now()
               hour=time.hour
               minutes=time.minute+1
               
               msg=pywhatkit.sendwhatmsg(moble_no,f"Your Roll Number is:\n {row}",hour,minutes)
               '''
               con.close()


add=Tk()
width= add.winfo_screenwidth() 
height= add.winfo_screenheight()
add.geometry("%dx%d" % (width, height))
add.title("ADD A STUDENT")
back_icon=PhotoImage(file="back_icon.png")
back=Button(add,text="Back",image=back_icon,bd=0,bg="white",fg="orange red",compound="left",width=70,cursor="hand2",font=("Times New Roman",15,"bold"),command=exit)
back.place(x=50,y=20)
label=Label(add,text="Enter the details...",font=("Times New Roman",60,"bold"))
label.place(x=400,y=80)
frame=Frame(add,bg="CadetBlue1")
frame.place(x=250,y=220)
#row 1
fname_label=Label(frame,text="First Name",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
fname_label.grid(row=0,column=0,padx=20,pady=(15,0),sticky="w")
firstname=Entry(frame,font=("Times New Roman",18,"bold"),width=22,bd=0)
firstname.grid(row=1,column=0,padx=20)
mname_label=Label(frame,text="Middle Name",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
mname_label.grid(row=0,column=1,padx=25,pady=(15,0),sticky="w")
mname=Entry(frame,font=("Times New Roman",18,"bold"),width=22,bd=0)
mname.grid(row=1,column=1,padx=25)
lname_label=Label(frame,text="Last Name",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
lname_label.grid(row=0,column=2,padx=25,pady=(15,0),sticky="w")
lname=Entry(frame,font=("Times New Roman",18,"bold"),width=22,bd=0)
lname.grid(row=1,column=2,padx=25)

#row 2
clgname_label=Label(frame,text="College Name(INTER)",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
clgname_label.grid(row=2,column=0,padx=20,pady=(25,0),sticky="w")
inter_clgname=Entry(frame,font=("Times New Roman",18,"bold"),width=22,bd=0)
inter_clgname.grid(row=3,column=0,padx=20)
marks_label=Label(frame,text="Marks(INTER)",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
marks_label.grid(row=2,column=1,padx=25,pady=(25,0),sticky="w")
inter_marks=Entry(frame,font=("Times New Roman",18,"bold"),width=22,bd=0)
inter_marks.grid(row=3,column=1,padx=25)
phno_label=Label(frame,text="Mobile no.",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
phno_label.grid(row=2,column=2,padx=25,pady=(25,0),sticky="w")
phno=Entry(frame,font=("Times New Roman",18,"bold"),width=22,bd=0)
phno.grid(row=3,column=2,padx=25)

#row 3
gender=Label(frame,text="Gender : ",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
gender.grid(row=4,column=0,padx=20,pady=(25,0),sticky="w")
radio=StringVar()
r1=Radiobutton(frame,text="Male",variable=radio,value="Male",bg="CadetBlue1",activebackground="CadetBlue1",font=("Times New Roman",12,"bold"))
r1.grid(row=5,column=0,padx=20,sticky="w")
r2=Radiobutton(frame,text="Female",variable=radio,value="Female",bg="CadetBlue1",activebackground="CadetBlue1",font=("Times New Roman",12,"bold"))
r2.grid(row=5,column=0,padx=10)
r3=Radiobutton(frame,text="Other",variable=radio,value="Other",bg="CadetBlue1",activebackground="CadetBlue1",font=("Times New Roman",12,"bold"))
r3.grid(row=5,column=0,sticky="e",padx=(0,20))
radio.set(None)
email_label=Label(frame,text="Email Id",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
email_label.grid(row=4,column=1,padx=25,pady=(25,0),sticky="w")
email=Entry(frame,font=("Times New Roman",18,"bold"),width=22,bd=0)
email.grid(row=5,column=1,padx=25)
place_label=Label(frame,text="City",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
place_label.grid(row=4,column=2,padx=25,pady=(25,0),sticky="w")
place=Entry(frame,font=("Times New Roman",18,"bold"),width=22,bd=0)
place.grid(row=5,column=2,padx=25)

#row 4
degree_label=Label(frame,text="Degree",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
degree_label.grid(row=6,column=0,padx=20,pady=(25,0),sticky="w")
degree=['B.Tech','BSC','M.Tech']
sel_degree=ttk.Combobox(frame,values=degree,font=("Times New Roman",15),width=25)
sel_degree.set("Select Degree")
sel_degree.grid(row=7,column=0,padx=20)
branch_label=Label(frame,text="Branch",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
branch_label.grid(row=6,column=1,padx=25,pady=(25,0),sticky="w")
branch=['CSE','ECE','EEE','CIVIL','DS','AI','AI-ML']
sel_branch=ttk.Combobox(frame,values=branch,font=("Times New Roman",15),width=25)
sel_branch.set("Select Branch")
sel_branch.grid(row=7,column=1,padx=25)
state_label=Label(frame,text="State",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
state_label.grid(row=6,column=2,padx=25,pady=(25,0),sticky="w")
states=['Andhra Pradesh','Tamilnadu','Telangana','Punjab','Gujarat','Kerala']
sel_states=ttk.Combobox(frame,values=states,font=("Times New Roman",15),width=25)
sel_states.set("Select state")
sel_states.grid(row=7,column=2,padx=25)
sel_degree.config(state='readonly')
sel_branch.config(state='readonly')
sel_states.config(state='readonly')

#row 5
hostel_label=Label(frame,text="Hostel",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
hostel_label.grid(row=8,column=0,padx=20,pady=(25,0),sticky="w")
options=["Yes","No"]
hostel=ttk.Combobox(frame,values=options,font=("Times New Roman",15),width=25)
hostel.set("Select yes or no")
hostel.grid(row=9,column=0,padx=20,pady=(0,15))
bus_label=Label(frame,text="Bus Transport",font=("Times New Roman",15,"bold"),bg="CadetBlue1")
bus_label.grid(row=8,column=1,padx=25,pady=(25,0),sticky="w")
options=["Yes","No"]
bus=ttk.Combobox(frame,values=options,font=("Times New Roman",15),width=25)
bus.set("Select yes or no")
bus.grid(row=9,column=1,padx=25,pady=(0,15))
button=Button(add,text="ADD",font=("Times New Roman",18,"bold"),cursor="hand2",width=22,bg="DeepSkyBlue2",command=submit)
button.place(x=550,y=670)
hostel.config(state="readonly")
bus.config(state='readonly')
add.mainloop()



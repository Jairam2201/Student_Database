from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
def exit():
    search.destroy()
    import main
def details():
    con=pymysql.connect(host="localhost",user="root",password="1234",database="student_dtbase")
    mycursor=con.cursor()
    query="use student_dtbase"
    mycursor.execute(query)
    query="select * from student_details where id=%s"
    mycursor.execute(query,rollno.get())
    row=mycursor.fetchone()
    if row==None:
        messagebox.showerror("ERROR", "Invalid Rollno.")
    else:
        frame=Frame(search,bg="CadetBlue1")
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
        gen=["Male","Female","Other"]
        sel_gender=ttk.Combobox(frame,values=gen,font=("Times New Roman",15),width=25)
        sel_gender.set("Select gender")
        sel_gender.grid(row=5,column=0,padx=25)
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
        degree=['btech','bsc','mtech']
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
        states=['AP','tamilnadu','telangana','punjab','gujarat']
        sel_states=ttk.Combobox(frame,values=states,font=("Times New Roman",15),width=25)
        sel_states.set("Select state")
        sel_states.grid(row=7,column=2,padx=25)

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
        #insertion
        query="select * from student_details where id=%s"
        mycursor.execute(query,rollno.get())
        row=mycursor.fetchone()
        l=[firstname,mname,lname,inter_clgname,inter_marks,phno,sel_gender,email,place,sel_degree,sel_branch,sel_states,hostel,bus]
        for index, entry in enumerate(l):
            index+=1
            if entry==sel_gender or entry==hostel or entry==bus  or entry==sel_degree or entry==sel_branch or entry==sel_states:
                entry.set(row[index])
                entry.config(state="disabled")
            else:
                entry.insert(0, row[index])
                entry.config(state="disabled")
        
  
    con.commit()
    con.close()




search=Tk()
search.title("STUDENT DETAILS")
width= search.winfo_screenwidth()
height= search.winfo_screenheight()
search.geometry("%dx%d" % (width, height))
back_icon=PhotoImage(file="back_icon.png")
back=Button(search,image=back_icon,text="Back",bd=0,bg="white",fg="orange red",cursor="hand2",width=70,compound=LEFT,font=("Times New Roman",15,"bold"),command=exit)
back.place(x=50,y=20)
label=Label(search,text="Student Rollno : ",font=("Times New Roman",20,"bold"))
label.place(x=500,y=80)
frame=Frame(search,highlightbackground="gray55",highlightthickness=1,highlightcolor="orange red")
frame.place(x=700,y=84)
rollno=Entry(frame,font=("Times New Roman",18,"bold"),bd=0,bg="gray87")
rollno.grid()
submit=Button(search,text="Search",bg="blue",fg="white",activebackground="blue4",activeforeground="white",cursor="hand2",font=("Times New Roman",15,"bold"),command=details)
submit.place(x=650,y=150)



search.mainloop()

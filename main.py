from tkinter import *
from PIL import Image, ImageTk
def exit():
    root.destroy()
    import login
def add():
    root.destroy()
    import add
def change():
    root.destroy()
    import update
def search():
    root.destroy()
    import rollno_search
def delete():
    root.destroy()
    import delete
def info():
    root.destroy()
    import branchwise_students
def hostel():
    root.destroy()
    import hostel

root = Tk()
root.title("Database")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
logout=Button(root,text="LOGOUT",fg="white",bg="orange red",
              bd=0,font=("Times New Roman",15,"bold"),cursor="hand2",command=exit)
logout.place(x=1400,y=25)
heading=Label(root,text="Student Database",fg="blue4",font=("Times New Roman",80,"bold"))
heading.place(x=350 ,y=100)
fr1=Frame(root,highlightbackground="orange red",highlightthickness=1)
fr1.place(x=300,y=320)
add=Button(fr1,text="Add a Student",bg="dodger blue2",activebackground="blue2",activeforeground="white",font=("Times New Roman",22,"bold"),width=18,cursor="hand2",command=add)
add.grid()

fr1=Frame(root,highlightbackground="orange red",highlightthickness=1)
fr1.place(x=300,y=430)
change=Button(fr1,text="Update Details",bg="dodger blue2",activebackground="blue2",activeforeground="white",font=("Times New Roman",22,"bold"),width=18,cursor="hand2",command=change)
change.grid()
fr1=Frame(root,highlightbackground="orange red",highlightthickness=1)
fr1.place(x=300,y=535)
search=Button(fr1,text="Student Details",bg="dodger blue2",activebackground="blue2",activeforeground="white",font=("Times New Roman",22,"bold"),width=18,cursor="hand2",command=search)
search.grid()
fr1=Frame(root,highlightbackground="orange red",highlightthickness=1)
fr1.place(x=850,y=320)
delete=Button(fr1,text="Remove Student",bg="dodger blue2",activebackground="blue2",activeforeground="white",font=("Times New Roman",22,"bold"),width=18,cursor="hand2",command=delete)
delete.grid()
fr1=Frame(root,highlightbackground="orange red",highlightthickness=1)
fr1.place(x=850,y=430)
inf=Button(fr1,text="Branchwise List",bg="dodger blue2",activebackground="blue2",activeforeground="white",font=("Times New Roman",22,"bold"),width=18,cursor="hand2",command=info)
inf.grid()
fr1=Frame(root,highlightbackground="orange red",highlightthickness=1)
fr1.place(x=850,y=535)
hostl=Button(fr1,text="Hostel Students",bg="dodger blue2",activebackground="blue2",activeforeground="white",font=("Times New Roman",22,"bold"),width=18,cursor="hand2",command=hostel)
hostl.grid()
root.mainloop()

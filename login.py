from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def for_signup():
    login.destroy()
    from signup import signup
def reset_pswd():   
    login.destroy()
    from resetpswd import reset
def change():
    closeeye_img.config(file="open.png")
    pswd_entry.config(show="")
    closeeye.config(command=real)
def real():
    closeeye_img.config(file="close.png")
    pswd_entry.config(show="*")
    closeeye.config(command=change)
def login_user():
    if user_entry.get()=='' or pswd_entry.get()=='':
        messagebox.showerror("ERROR","Enter your Username and Password.")
    else:
        con=pymysql.connect(host="localhost",user="root",password="1234")
        mycursor=con.cursor()
        query="use userregistration"
        mycursor.execute(query)
        '''query="select * from userdetails where username=%s and password=%s"
        mycursor.execute(query,(user_entry.get(),pswd_entry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("ERROR","Username doesnot exist.")
        else:
            messagebox.showinfo("SUCCESS","Login Success.")'''
        query="select password from userdetails where username=%s"
        mycursor.execute(query,user_entry.get())
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("ERROR","Username doesnot exist.")
        elif row[0]==pswd_entry.get():
            messagebox.showinfo("SUCCESS","Login Success.")
            login.destroy()
            import main
        elif row[0]!=pswd_entry.get():
            messagebox.showerror("ERROR","Password Incorrect.")
login=Tk()
login.title("LOGIN")
width= login.winfo_screenwidth() 
height= login.winfo_screenheight()
login.geometry("%dx%d" % (width, height))
frame=Frame(login,bg="white",highlightcolor="orange red",highlightbackground="orange red",highlightthickness=5)
frame.place(x=570,y=250)
login_label=Label(frame,text="Login",fg="orange red",font=("Times New Roman",25,"bold"),bg="white")
login_label.grid(row=0,column=0,pady=(10,0))
user_label=Label(frame,text="Username",font=("Times New Roman",15,"bold"),bg="white")
user_label.grid(row=1,column=0,sticky="w",padx="25",pady=(25,0))
user_entry=Entry(frame,width="30",font=("Times New Roman",15,"bold"),fg="orange red",highlightbackground="orange red",highlightthickness=0.5,bd=0)
user_entry.grid(row=2,column=0,sticky="w",padx="25")

pswd_label=Label(frame,text="Password",font=("Times New Roman",15,"bold"),bg="white")
pswd_label.grid(row=3,column=0,sticky="w",padx="25",pady=(20,0))
pswd_entry=Entry(frame,width="30",fg="orange red",font=("Times New Roman",15,"bold"),show="*",highlightbackground="orange red",highlightthickness=0.5,bd=0)
pswd_entry.grid(row=4,column=0,sticky="w",padx="25")
closeeye_img=PhotoImage(file="close.png")
closeeye=Button(frame,image=closeeye_img,bg="white",cursor="hand2",activebackground="white",bd=0,command=change)
closeeye.grid(row=4,column=0,sticky="e",padx=(0,25))
forget_pswd=Button(frame,text="Forgot Password",bg="white",
                   activebackground="white",activeforeground="blue2",
                   fg="dodger blue",bd=0,font=("Times New Roman",10),cursor="hand2",command=reset_pswd)
forget_pswd.grid(row=5,column=0,sticky="e",padx=(0,25),pady=(10,0))
login_button=Button(frame,text="Login",width="30",font=("Times New Roman",12,"bold"),cursor="hand2",command=login_user)
login_button.grid(row=6,column=0,padx="25",pady=(15,0))
dontaccnt=Label(frame,text="Don't have an account?",font=("Times New Roman",10,"bold"),bg="white")
dontaccnt.grid(row=7,column=0,pady="10")
signup=Button(login,text="Signup",bg="white",bd=0,
              activebackground="white",activeforeground="blue4",fg="dodger blue",font=("Times New Roman",12,"bold"),cursor="hand2",command=for_signup)
signup.place(x=815,y=550)
login.mainloop()

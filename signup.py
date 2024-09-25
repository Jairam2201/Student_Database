from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import cryptography
import pymysql
def for_login():
    signup.destroy()
    import login
def success():
    if user_entry.get()!='' and email_entry.get()!='' and pswd_entry.get()!='' and cnpswd_entry.get()!='':
        messagebox.showinfo("SUCCESS","Registration Successfull.")
        signup.destroy()
        import login
    

def signup_user():
    if user_entry.get()=='' or email_entry.get()=='' or pswd_entry.get()=='' or cnpswd_entry.get()=='':        
        messagebox.showerror("ERROR","All Fields Are Required")
    elif pswd_entry.get()!=cnpswd_entry.get():
        messagebox.showerror("ERROR","Password didnot match")
    elif checkmark.get()==0:
        messagebox.showerror("ERROR","Please accept the terms & conditions.")
    else:
            con=pymysql.connect(host="localhost",user="root",password="1234")
            mycursor=con.cursor()
            try:
                query="create database userregistration"
                mycursor.execute(query)
                query="use userregistration"
                mycursor.execute(query)
                query="create table userdetails(scno int not null auto_increment primary key,username varchar(100),email varchar(100),password varchar(100),confirmpswd varchar(100))"
                mycursor.execute(query)
            except:
                query="use userregistration"
                mycursor.execute(query)
            finally:
                query1="select username from userdetails where username=%s"
                mycursor.execute(query1,(user_entry.get()))
                row=mycursor.fetchone()
                if row==None:
                    query2="insert into userdetails(username,email,password,confirmpswd) values(%s,%s,%s,%s)"
                    mycursor.execute(query2,(user_entry.get(),email_entry.get(),pswd_entry.get(),cnpswd_entry.get()))
                    con.commit()
                    con.close()
                    success()
                else:
                    messagebox.showerror("ERROR","Username already exists.\nPlease try another one.")
                    con.commit()
                    con.close()
            
    
signup=Tk()
signup.title("SIGNUP")
width= signup.winfo_screenwidth() 
height= signup.winfo_screenheight()
signup.geometry("%dx%d" % (width, height))
label=Label(signup,text="Sign Up...",fg="OrangeRed2",font=("Times New Roman",150,"bold"))
label.place(x=120,y=250)
frame=Frame(signup,bg="white",highlightcolor="orange red",highlightbackground="orange red",highlightthickness=5)
frame.place(x=1020,y=180)
user_label=Label(frame,text="Username",font=("Times New Roman",15,"bold"),bg="white")
user_label.grid(row=1,column=0,sticky="w",padx="25",pady=(25,0))
user_entry=Entry(frame,width="35",highlightbackground="orange red",highlightthickness=0.5,bd=0,font=("Times New Roman",15,"bold"))
user_entry.grid(row=2,column=0,sticky="w",padx="25")
email_label=Label(frame,text="Email",font=("Times New Roman",15,"bold"),bg="white")
email_label.grid(row=3,column=0,sticky="w",padx="25",pady=(20,0))
email_entry=Entry(frame,width="35",highlightbackground="orange red",highlightthickness=0.5,bd=0,font=("Times New Roman",15,"bold"))
email_entry.grid(row=4,column=0,sticky="w",padx="25")
pswd_label=Label(frame,text="Password",font=("Times New Roman",15,"bold"),bg="white")
pswd_label.grid(row=5,column=0,sticky="w",padx="25",pady=(20,0))
pswd_entry=Entry(frame,width="35",highlightbackground="orange red",highlightthickness=0.5,bd=0,font=("Times New Roman",15,"bold"),show="*")
pswd_entry.grid(row=6,column=0,sticky="w",padx="25")
cnpswd_label=Label(frame,text="Confirm Password",font=("Times New Roman",15,"bold"),bg="white")
cnpswd_label.grid(row=7,column=0,sticky="w",padx="25",pady=(20,0))
cnpswd_entry=Entry(frame,width="35",highlightbackground="orange red",highlightthickness=0.5,bd=0,font=("Times New Roman",15,"bold"),show="*")
cnpswd_entry.grid(row=8,column=0,sticky="w",padx="25")
checkmark=IntVar()
check=Checkbutton(frame,text="I agree to the terms & conditions.",bg="white",
                  activebackground="white",activeforeground="orange red",fg="orange red",variable=checkmark,cursor="hand2")
check.grid(row=9,column=0,sticky="w",padx="25",pady="10")
button=Button(frame,text="Signup",width="30",font=("Times New Roman",15,"bold"),command=signup_user,cursor="hand2")
button.grid(row=10,column=0,padx="25",pady=(10,0))
alreadyaccnt=Label(frame,text="Already have an account?",font=("Times New Roman",10,"bold"),bg="white")
alreadyaccnt.grid(row=11,column=0,pady="5")
login=Button(signup,text="Login",fg="dodger blue",font=("Times New Roman",12,"bold"),
             bg="white",bd=0,activebackground="white",activeforeground="blue4",command=for_login,cursor="hand2")
login.place(x=1308,y=590)
signup.mainloop()

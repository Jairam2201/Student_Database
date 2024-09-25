from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
def signin():
    reset.destroy()
    import login
def update():
    if email_entry.get()=='' or newpswd_entry.get()=='' or cnpswd_entry.get()=='':
        messagebox.showerror("ERROR","All details are required.")
    elif newpswd_entry.get()!=cnpswd_entry.get():
        messagebox.showerror("ERROR","Password Mismatch.")
    else:
        try:
            
            con=pymysql.connect(host="localhost",user="root",password="1234")
            mycursor=con.cursor()
            query="use userregistration"
            mycursor.execute(query)
        except:
            messagebox.showerror("ERROR","Connection failed.Please try again.")
            return
        query="select email from userdetails where email=%s"
        mycursor.execute(query,email_entry.get())
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("ERROR","You have entered wrong email.")
        else:
            query="update userdetails set password=%s,confirmpswd=%s where email=%s"
            mycursor.execute(query,(newpswd_entry.get(),cnpswd_entry.get(),email_entry.get()))
            messagebox.showinfo("SUCCESS","Password changed.")
        con.commit()
        con.close()
    
reset=Tk()
reset.title("RESET PASSWORD")
width= reset.winfo_screenwidth() 
height= reset.winfo_screenheight()
reset.geometry("%dx%d" % (width, height))
label=Label(reset,bg="white")
label.grid()
reset_label=Label(reset,text="RESET  YOUR",bg="red",fg="white",font=("Times New Roman",65,"bold"))
reset_label.place(x=85,y=300)
pswd_label=Label(reset,text="PASSWORD",font=("Times New Roman",60,"bold"))
pswd_label.place(x=85,y=400)
frame=Frame(reset,bg="white")
frame.place(x=900,y=250)
email_label=Label(frame,text="Email",bg="white",font=("Times New Roman",15,"bold"))
email_label.grid(row=1,column=0,sticky="w",padx="35",pady=(25,0))
email_entry=Entry(frame,width="30",font=("Times New Roman",15,"bold"),highlightbackground="orange red",highlightthickness=0.5,bd=0)
email_entry.grid(row=2,column=0,sticky="w",padx="35")
newpswd_label=Label(frame,text="New Password",bg="white",font=("Times New Roman",15,"bold"))
newpswd_label.grid(row=3,column=0,sticky="w",padx="35",pady=(20,0))
newpswd_entry=Entry(frame,width="30",font=("Times New Roman",15,"bold"),show="*",highlightbackground="orange red",highlightthickness=0.5,bd=0)
newpswd_entry.grid(row=4,column=0,sticky="w",padx="35")
cnpswd_label=Label(frame,text="Confirm New Password",bg="white",font=("Times New Roman",15,"bold"))
cnpswd_label.grid(row=5,column=0,sticky="w",padx="35",pady=(20,0))
cnpswd_entry=Entry(frame,width="30",font=("Times New Roman",15,"bold"),show="*",highlightbackground="orange red",highlightthickness=0.5,bd=0)
cnpswd_entry.grid(row=6,column=0,sticky="w",padx="35")
button=Button(frame,text="Change Password",cursor="hand2",font=("Times New Roman",15,"bold"),command=update)
button.grid(row=7,column=0,padx="25",pady=(20,0))
login=Button(frame,text="Signin",bg="white",bd=0,
             activebackground="white",activeforeground="blue4",
             fg="orange red",cursor="hand2",font=("Times New Roman",13,"bold"),command=signin)
login.grid(row=8,column=0,pady=(0,10))
reset.mainloop()

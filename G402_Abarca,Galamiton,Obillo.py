from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

root = Tk()
root.title("Employee Performance Tracker Management System")

width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(True, True)
root.config(bg="white")

#========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
SEARCH = StringVar()
EMPID = IntVar()
FULLNAME = StringVar()
DEPARTMENT = StringVar()                                        #This block of code holds a string data
POSTDESIGNATION = StringVar()                                   #where we can set text values and can retrieve it later
WORKQUALITY = StringVar()
PRODUCTIVITY = StringVar()
JOBKNOWLEDGE = StringVar()
CLIENTSERVICE = StringVar()
TEAMWORK = StringVar()
SAFETY = StringVar()
RELIABILITY = StringVar()
INITIATIVE = StringVar()


#========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut2.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS 'cfpproject' (employee INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,EMP_ID INTEGER, FULLNAME TEXT, DEPARTMENT TEXT, POSTDESIGNATION TEXT, WORKQUALITY INTEGER, PRODUCTIVITY INTEGER, JOBKNOWLEDGE INTEGER, CLIENTSERVICE INTEGER, TEAMWORK INTEGER, SAFETY INTEGER, RELIABILITY INTEGER, INITIATIVE INTEGER)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    cursor.execute("SELECT * FROM `cfpproject` ORDER BY `fullname` ASC")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Exit():
    result = tkMessageBox.askquestion('Program', 'Do you want to close the program?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('Program', 'Do you want to close the program?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()

def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Account Login")
    width = 600
    height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()
    
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm,  bg="sky blue", text="Administrator Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Enter Username:", font=('arial', 16), bd=25)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Enter Password:", font=('arial', 16), bd=25)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 16), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 16), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login, bg="sky blue")
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)
    
def Home():
    global Home
    Home = Tk()
    Home.title("Employee Performance Tracker Management System")
    width = 1000
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=8, relief=RIDGE)
    Title.place(x=150, y=170)
    lbl_display = Label(Title, text="Welcome to Employee Performance \n Tracker Management System", font=('arial', 30))
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add new", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Options", menu=filemenu2)
    Home.config(menu=menubar)
    Home.config(bg="white")

def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add New Record")
    width = 500
    height = 600
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(True, True)
    AddNewForm()

def AddNewForm():
    TopAddNew = Frame(addnewform, width=200, height=200, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew,bg="skyblue", text="Adding New Performance Record", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=100)
    MidAddNew.pack(side=TOP)
    lbl_emp_id = Label(MidAddNew, text="Employee ID:", font=('arial', 16), bd=5)
    lbl_emp_id.grid(row=0, sticky=W)
    lbl_fullname = Label(MidAddNew, text="Full Name:", font=('arial', 16), bd=5)
    lbl_fullname.grid(row=1, sticky=W)
    lbl_department = Label(MidAddNew, text="Department:", font=('arial', 16),  bd=5)
    lbl_department.grid(row=2, sticky=W)
    lbl_post = Label(MidAddNew, text="Post Designation:", font=('arial', 16), bd=5)
    lbl_post.grid(row=3, sticky=W)
    lbl_quality = Label(MidAddNew, text="Work Quality:", font=('arial', 16),  bd=5)
    lbl_quality.grid(row=4, sticky=W)
    lbl_productivity = Label(MidAddNew, text="Productivity:", font=('arial', 16),  bd=5)
    lbl_productivity.grid(row=5, sticky=W)
    lbl_knowledge = Label(MidAddNew, text="Job Knowledge:", font=('arial', 16),  bd=5)
    lbl_knowledge.grid(row=6, sticky=W)
    lbl_service = Label(MidAddNew, text="Client Service:", font=('arial', 16),  bd=5)
    lbl_service.grid(row=7, sticky=W)
    lbl_teamwork = Label(MidAddNew, text="Teamwork:", font=('arial', 16),  bd=5)
    lbl_teamwork.grid(row=8, sticky=W)
    lbl_safety = Label(MidAddNew, text="Safety:", font=('arial', 16), bd=5)
    lbl_safety.grid(row=9, sticky=W)
    lbl_reliability = Label(MidAddNew, text="Reliability:", font=('arial', 16),  bd=5)
    lbl_reliability.grid(row=10, sticky=W)
    lbl_initiative = Label(MidAddNew, text="Initiative:", font=('arial', 16),  bd=5)
    lbl_initiative.grid(row=11, sticky=W)

    emp_id = Entry(MidAddNew, textvariable=EMPID, font=('arial', 16), width=15)
    emp_id.grid(row=0, column=1)
    fullname = Entry(MidAddNew, textvariable=FULLNAME, font=('arial', 16), width=15)
    fullname.grid(row=1, column=1)
    department = Entry(MidAddNew, textvariable=DEPARTMENT, font=('arial', 16), width=15)
    department.grid(row=2, column=1)
    post = Entry(MidAddNew, textvariable=POSTDESIGNATION, font=('arial', 16), width=15)
    post.grid(row=3, column=1)
    quality = Entry(MidAddNew, textvariable=WORKQUALITY, font=('arial', 16), width=15)
    quality.grid(row=4, column=1)
    productivity = Entry(MidAddNew, textvariable=PRODUCTIVITY, font=('arial', 16), width=15)
    productivity.grid(row=5, column=1)
    knowledge = Entry(MidAddNew, textvariable=JOBKNOWLEDGE, font=('arial', 16), width=15)
    knowledge.grid(row=6, column=1)
    service = Entry(MidAddNew, textvariable=CLIENTSERVICE, font=('arial', 16), width=15)
    service.grid(row=7, column=1)
    teamwork = Entry(MidAddNew, textvariable=TEAMWORK, font=('arial', 16), width=15)
    teamwork.grid(row=8, column=1)
    safety = Entry(MidAddNew, textvariable=SAFETY, font=('arial', 16), width=15)
    safety.grid(row=9, column=1)
    reliability = Entry(MidAddNew, textvariable=RELIABILITY, font=('arial', 16), width=15)
    reliability.grid(row=10, column=1)
    initiative = Entry(MidAddNew, textvariable=INITIATIVE, font=('arial', 16), width=15)
    initiative.grid(row=11, column=1)
    btn_addcon = Button(MidAddNew, text="Save", width=50, bg="sky blue", command=AddNew)
    btn_addcon.grid(row=12, columnspan=2, pady=10)

def AddNew():
    Database()
    cursor.execute("INSERT INTO `cfpproject` (emp_id, fullname, department, postdesignation, workquality, productivity, jobknowledge, clientservice, teamwork, safety, reliability, initiative) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (int(EMPID.get()), str(FULLNAME.get()), str(DEPARTMENT.get()), str(POSTDESIGNATION.get()), str(WORKQUALITY.get()), str(PRODUCTIVITY.get()), str(JOBKNOWLEDGE.get()), str(CLIENTSERVICE.get()), str(TEAMWORK.get()), str(SAFETY.get()), str(RELIABILITY.get()), str(INITIATIVE.get())))
    conn.commit()
    EMPID.set("")
    FULLNAME.set("")
    DEPARTMENT.set("")
    POSTDESIGNATION.set("")
    WORKQUALITY.set("")
    PRODUCTIVITY.set("")
    JOBKNOWLEDGE.set("")
    CLIENTSERVICE.set("")
    TEAMWORK.set("")
    SAFETY.set("")
    RELIABILITY.set("")
    INITIATIVE.set("")
    cursor.close()
    conn.close()
def Exit2():
    result = tkMessageBox.askquestion('Program', 'Are All Fields Complete?', icon="warning")
    if result == 'yes':
        ShowAddNew.destroy()
        exit()
def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=600, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X, pady=20, padx=10)
    LeftViewForm = Frame(viewform, width=500)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Employee Records", font=('Verdana', 18), bg="sky blue", width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search Employee ID", font=('Verdana', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('Verdana', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)

    tree = ttk.Treeview(MidViewForm, columns=("employee", "emp_id", "Fullname", "Department", "Post Designation", "Work Quality", "Productivity", "Job Knowledge", "Client Service", "Teamwork", "Safety", "Reliability", "Initiative"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('employee', text="employee", anchor=CENTER,)
    tree.heading('emp_id', text="Employee ID", anchor=CENTER)
    tree.heading('Fullname', text="Fullname", anchor=CENTER)
    tree.heading('Department', text="Department", anchor=CENTER)
    tree.heading('Post Designation', text="Post Designation", anchor=CENTER)
    tree.heading('Work Quality', text="Work Quality", anchor=CENTER)
    tree.heading('Productivity', text="Productivity", anchor=CENTER)
    tree.heading('Job Knowledge', text="Job Knowledge", anchor=CENTER)
    tree.heading('Client Service', text="Client Service", anchor=CENTER)
    tree.heading('Teamwork', text="Team Work", anchor=CENTER)
    tree.heading('Safety', text="Safety", anchor=CENTER)
    tree.heading('Reliability', text="Reliability", anchor=CENTER)
    tree.heading('Initiative', text="Initiative", anchor=CENTER)
    tree.column('#0', stretch=FALSE, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=150)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)
    tree.column('#8', stretch=NO, minwidth=0, width=120)
    tree.column('#9', stretch=NO, minwidth=0, width=100)
    tree.column('#10', stretch=NO, minwidth=0, width=80)
    tree.column('#11', stretch=NO, minwidth=0, width=100)
    tree.column('#12', stretch=NO, minwidth=0, width=100)
    tree.pack()
    DisplayData()

def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `cfpproject`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `cfpproject` WHERE `emp_id` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")

def Delete():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('Program', 'Are you sure you want to delete employee record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            employee = selecteditem[0]
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `cfpproject` WHERE `employee` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Employee Records")
    width = 700
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(True, True)
    ViewForm()

def Logout():
    result = tkMessageBox.askquestion('Program', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes': 
        admin_id = ""
        root.deiconify()
        Home.destroy()
  
def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field", fg="red", font=("verdana, 14"))
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close() 

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()


#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="Acess", menu=filemenu)
root.config(menu=menubar)

#========================================FRAME============================================
Title1 = Frame(root,bg="white")
Title1.place(y=130, x=55)
Title2 = Frame(root, bg="white")
Title2.place(y=310, x=300)
TableMargin = Frame(root,height=5, width=700, padx=40, pady=10, bg="black")
TableMargin.place(x=150, y=100)
TableMargin2 = Frame(root,height=5, width=700, padx=40, pady=10, bg="black")
TableMargin2.place(x=150, y=400)
#========================================LABEL WIDGET=====================================
lbl_display1 = Label(Title1, bg="white", text="Employee Performance\n Tracker Management System", font=('verdana', 45))
lbl_display1.pack()
lbl_display2 = Label(Title2, bg="white", text="Presented by:\n Abarca,E. Galamiton, G. Obillo, C.", font=('verdana', 16))
lbl_display2.pack()

#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()

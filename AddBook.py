# in this we will add a form so that user will able to add a book and register to database.
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql

# function register book
def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    #insertBooks = "insert into"+bookTable+"values('"+bid+"', '"+title+"', '"+author+"', '"+status+"')"
    insertBooks = "insert into "+bookTable+" values ('"+bid+"','"+title+"','"+author+"','"+status+"')"

    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo('Error', "Can't add book to database")

    print(bid)
    print(title)
    print(author)
    print(status)

    root.destroy()


# Now, we will make a func name add_book -> which will display form to add details
# it will connect to server and fetch details, after call bookRegister to commit in dbs
def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, cur, con, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    root.configure(background="#575fcf")


    mypass="123"
    mydatabase = "books_db"

    con = pymysql.connect(host="localhost", user="gui", password=mypass, database=mydatabase)
    cur = con.cursor()

    #enter the table name here
    bookTable = "book" #book table



    #add a heading Frame
    headingFrame1 = Frame(root, bg="#3c40c6", bd=5)
    headingFrame1.place(x=190, y=50)

    headingLabel = Label(headingFrame1,width=20, text="Add Books", bg="white", fg="#575fcf", font=('rubik',15))
    headingLabel.pack(ipady=10)

    #Frame of entries 
    LabelFrame = Frame(root, bg="#3c40c6",width=500,height=230)
    LabelFrame.place(x=48, y=140)

    #book ID
    id_label = Label(LabelFrame, text="Book Id: ", bg="#3c40c6", fg="white")
    id_label.place(x=30, y=40)
    #entry label for book Id
    bookInfo1 = Entry(LabelFrame,width=50)
    bookInfo1.place(x=150, y=40)

    #title
    title_label = Label(LabelFrame, text="Title: ", bg="#3c40c6", fg="white")
    title_label.place(x=30,y=80)
    #entry for title
    bookInfo2 = Entry(LabelFrame,width=50)
    bookInfo2.place(x=150, y=80)

    #author
    author_label = Label(LabelFrame, text="Author: ", bg="#3c40c6", fg="white")
    author_label.place(x=30,y=120)
    #entry for title
    bookInfo3 = Entry(LabelFrame,width=50)
    bookInfo3.place(x=150, y=120)

    #Status
    status_label = Label(LabelFrame, text="Status: ", bg="#3c40c6", fg="white")
    status_label.place(x=30,y=160)
    #entry for title
    bookInfo4 = Entry(LabelFrame,width=50)
    bookInfo4.place(x=150, y=160)

    #submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg="#3c40c6", fg="white", command=bookRegister)
    SubmitBtn.place(x=200,y=430,width=100,height=50)

    #Quit button
    QuitBtn = Button(root, text="Quit", bg="#ff3f34", fg="white", command=root.destroy)
    QuitBtn.place(x=330,y=430,width=100,height=50)

    root.mainloop()
# in this we will add a form so that user will able to add a book and update to database.
from tkinter import *
from tkinter import messagebox
import pymysql


# function register book
def getBook():
    bid = bookInfo1.get()
    try:
             # check input is integer or not
            try:
                sql_select_query = """select * from book where bid = %s"""
                # set variable in query
                cur.execute(sql_select_query, (bid,))
                # fetch result
                record = cur.fetchone()

                print(record[1])
                bookInfo2.config(text = record[1])
                bookInfo3.config(text = record[2])
                bookInfo4.config(text = record[3])
                #for row in records:
                #        bookInfo2.setvar(row["title"])

            except : 
                print("Database error")         
                messagebox.showinfo('Error', "You Entered Wrong ID")

    except:
            print("Check input")
    



def searchBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, cur, con, bookTable, root

    root = Tk()
    root.title("Search Book")
    root.minsize(width=400, height=400)
    root.geometry("600x600")
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

    headingLabel = Label(headingFrame1,width=20, text="Search Book", bg="white", fg="#575fcf", font=('rubik',15))
    headingLabel.pack(ipady=10)

    #Frame of entries 
    LabelFrame = Frame(root, bg="#3c40c6",width=500,height=280)
    LabelFrame.place(x=48, y=140)

    #book ID
    id_label = Label(LabelFrame, text="Book Id: ", bg="#3c40c6", fg="white")
    id_label.place(x=30, y=40)
    #entry label for book Id
    bookInfo1 = Entry(LabelFrame,width=50)
    bookInfo1.place(x=150, y=40)

    update = Button(LabelFrame, text="Search", bg="#575fcf", bd=0 , width=20 ,fg="white",command=getBook)
    update.place(x=309,y=80)

    #title
    title_label = Label(LabelFrame, text="Title: ", bg="#3c40c6", fg="white")
    title_label.place(x=30,y=120)
    #entry for title
    bookInfo2 = Label(LabelFrame,fg='white',text='',bg='#3c40c6',font=('rubik',10))
    bookInfo2.place(x=150, y=120)

    #author
    author_label = Label(LabelFrame, text="Author: ", bg="#3c40c6", fg="white")
    author_label.place(x=30,y=160)
    #entry for title
    bookInfo3 = Label(LabelFrame,fg='white',text='',bg='#3c40c6',font=('rubik',10))
    bookInfo3.place(x=150, y=160)

    #Status
    status_label = Label(LabelFrame, text="Status: ", bg="#3c40c6", fg="white")
    status_label.place(x=30,y=200)
    #entry for title
    bookInfo4 = Label(LabelFrame,fg='white',text='',bg='#3c40c6',font=('rubik',10))
    bookInfo4.place(x=150, y=200)



    #Quit button
    QuitBtn = Button(root, text="Quit", bg="#ff3f34", fg="white", command=root.destroy)
    QuitBtn.place(x=250,y=530,width=100,height=50)

    root.mainloop()
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql

mypass="123"
mydatabase="books_db"

con = pymysql.connect(host="localhost", user="gui", password=mypass, database=mydatabase)
cur = con.cursor()

#declare the name of tables
bookTable = "book"
issue_Table = "books_issued"

def deleteBook():
    bid = bookInfo1.get()

    deleteSql = "delete from "+ bookTable+ "where bid = '" +bid+"'"
    deleteIssue = "delete from "+issue_Table+ " where bid = '" +bid+"' "

    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo("Success", "Book Deleted Successfully")

    except:
        messagebox.showinfo("Error", "Please check Book Id")

    # print(bid)

    bookInfo1.delete(0, END)
    root.destroy()

def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, bookTable, cur, con, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#575fcf")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#3c40c6", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="Delete Book", bg="white", fg="#575fcf", font=('rubik',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="#3c40c6")
    LabelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    #take a book ID to delete
    lb2 = Label(LabelFrame, text="Book Id: ", bg="#3c40c6", fg="white")
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(LabelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Submit", bg="lightblue", fg="black", command=deleteBook)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

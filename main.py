from tkinter import *
from turtle import width
import pymysql
from AddBook import *
from ViewBooks import *
from UpdateBook import updateBook
from DeleteBook import *


#connect to mySQL server
mypass="123"
mydatabase = "books_db"   #name of database

con = pymysql.connect(host="localhost", user="gui", password=mypass, database=mydatabase)

cur = con.cursor()

# designing the window
root = Tk()
root.title("Library  Management System")
root.minsize(width=400, height=400)
root.geometry("600x600")
root.configure(background="#575fcf")


#adding a heading Frame to library
headingFrame1 = Frame(root, bg="#3c40c6", bd=5)
headingFrame1.pack(pady=44)
headingLabel = Label(headingFrame1, text="Welcome to \n Library Management System", bg="white", 
                fg="#3c40c6", font=('rubik',15),width=40)
headingLabel.pack(fill='both',ipady=12)

#Add the buttons
add_frame = Frame(root, bg="#3c40c6", bd=5)
add_frame.pack(pady=10)
add = Button(add_frame, text="Add Book Details", bg="white", bd=0 , width=35 ,fg="#3c40c6", command=addBook)
add.pack(fill='both',ipady=12)

view_frame = Frame(root, bg="#3c40c6", bd=5)
view_frame.pack(pady=10)
view = Button(view_frame, text="View book list", bg="white", bd=0 , width=35 ,fg="#3c40c6", command=View)
view.pack(fill='both',ipady=12)

update_frame = Frame(root, bg="#3c40c6", bd=5)
update_frame.pack(pady=10)
update = Button(update_frame, text="Update Book", bg="white", bd=0 , width=35 ,fg="#3c40c6",command=updateBook)
update.pack(fill='both',ipady=12)
search_frame = Frame(root, bg="#3c40c6", bd=5)
search_frame.pack(pady=10)
search = Button(search_frame, text="Search Book", bg="white", bd=0 , width=35 ,fg="#3c40c6")
search.pack(fill='both',ipady=12)
delete_frame = Frame(root, bg="#ff3f34", bd=5)
delete_frame.pack(pady=10)
delete = Button(delete_frame, text="Delete Book", bg="white", bd=0 , width=35 ,fg="#ff3f34", command=delete)
delete.pack(fill='both',ipady=12)

root.mainloop() #call the mainloop to run the application

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import pymysql



def fetch_all():
                mypass="123"
                mydatabase="books_db"

                con = pymysql.connect(host="localhost", user="gui", password=mypass, database=mydatabase)
                cur = con.cursor()

                #enter table names here
                bookTable = "book"
                getBooks = "select * from "+ bookTable
                curs = con.cursor()
                curs.execute(getBooks)
                rows = curs.fetchall()
                if len(rows) !=0:
                        book.delete(*book.get_children())
                        for row in rows:
                                book.insert("",END,value=row)
                                print('-->',row)
                        con.commit()
                con.close()

def View():
    global book

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#575fcf")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#3c40c6", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg="white", fg="#575fcf", font=('rubik',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    
    book = ttk.Treeview(root,
    columns=('id','title','author','status'),
    )
    scroll_x = Scrollbar(book,orient=HORIZONTAL)
    scroll_y = Scrollbar(book,orient=VERTICAL)

    book.place(x=1,y=140,width=600,height=300)

    scroll_x.pack(side=BOTTOM,fill='x')
    scroll_y.pack(side=LEFT,fill='y')
    book.config(xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.config(command=book.xview)
    scroll_y.config(command=book.yview)
    book['show']='headings'
    book.heading('id',text='id')
    book.heading('title',text='title')
    book.heading('author',text='author')
    book.heading('status',text='status')
    book.column('id',anchor=CENTER, stretch=NO)
    book.column('title',anchor=CENTER, stretch=NO)
    book.column('author',anchor=CENTER, stretch=NO)
    book.column('status',anchor=CENTER, stretch=NO)
    fetch_all()


    quitBtn = Button(root, text="QUIT", bg='lightblue', fg="black", command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()

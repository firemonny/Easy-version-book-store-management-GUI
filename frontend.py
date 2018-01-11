from tkinter import *
import backend
def get_selected_row(event):  #need to review
    global selected_tuple
    index = listbox1.curselection()[0]
    selected_tuple=listbox1.get(index)
    titleentry.delete(0,END)
    titleentry.insert(0,selected_tuple[1])
    authorentry.delete(0,END)
    authorentry.insert(0,selected_tuple[2])
    Yearentry.delete(0,END)
    Yearentry.insert(0,selected_tuple[3])
    ISBNentry.delete(0,END)
    ISBNentry.insert(0,selected_tuple[4])

def viewall_command():
    listbox1.delete(0,END)
    for row in backend.view():
        listbox1.insert(END,row)
def serach_command():
    listbox1.delete(0,END)
    for row in backend.search(title=titlevar.get(),author=authorvar.get(),year=Yearvar.get(),isbn=ISBNvar.get()):
        listbox1.insert(END,row)
def add_command():
    backend.insert(title=titlevar.get(),author=authorvar.get(),year=int(Yearvar.get()),isbn=int(ISBNvar.get()))
    listbox1.delete(0,END)
    listbox1.insert(END,(titlevar.get(),authorvar.get(),Yearvar.get(),ISBNvar.get()))
def delete_command():
    backend.delete(selected_tuple[0])
    for row in backend.view():
        listbox1.insert(END,row)
def update_command():
    backend.update(selected_tuple[0],titlevar.get(),authorvar.get(),Yearvar.get(),ISBNvar.get())
    listbox1.delete(0,END)
    for row in backend.view():
        listbox1.insert(END,row)



window = Tk()
window.wm_title("BookStore")
#Buttonpart
ViewAllButton = Button(window,text="View All",height=1,width=10,command=viewall_command)
ViewAllButton.grid(row=2,column=3)
SearchButton = Button(window,text="Search Entry",height=1,width=10,command=serach_command)
SearchButton.grid(row=3,column=3)
AddEntryButton = Button(window,text="Add Entry",height=1,width=10,command=add_command)
AddEntryButton.grid(row=4,column=3)
UpdateButton = Button(window,text="Update",height=1,width=10,command=update_command)
UpdateButton.grid(row=5,column=3)
DeleteButton = Button(window,text="Delete",height=1,width=10,command=delete_command)
DeleteButton.grid(row=6,column=3)
CloseButton = Button(window,text="Close",height=1,width=10,comman=window.destroy)
CloseButton.grid(row=7,column=3)
#Lable part#
titlelabel = Label(window,text="Title")
titlelabel.grid(row=0,column=0)
authorlabel = Label(window, text="Author")
authorlabel.grid(row=0,column=2)
yearlabel = Label(window, text="Year")
yearlabel.grid(row=1,column=0)
ISBNlabel = Label(window, text="ISBN")
ISBNlabel.grid(row=1,column=2)
#entryvariable
titlevar=StringVar()
authorvar=StringVar()
Yearvar=StringVar()
ISBNvar=StringVar()
#entrypart
titleentry = Entry(window,textvariable=titlevar)
titleentry.grid(row=0,column=1)
authorentry = Entry(window,textvariable=authorvar)
authorentry.grid(row=0,column=3)
Yearentry=Entry(window,textvariable=Yearvar)
Yearentry.grid(row=1,column=1)
ISBNentry = Entry(window,textvariable=ISBNvar)
ISBNentry.grid(row=1,column=3)
#listbox
listbox1 = Listbox(window, height=6,width=35)
listbox1.grid(row=2,column=0,rowspan=6,columnspan=2) #but need to expand it so the format will match
#scroll bar
scrollbar1= Scrollbar(window)
scrollbar1.grid(row=2,column=2)

listbox1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=listbox1.yview)
listbox1.bind('<<ListboxSelect>>',get_selected_row)


window.mainloop()

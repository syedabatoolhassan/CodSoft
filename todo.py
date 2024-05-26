from tkinter import *
root = Tk()
root.title("to do list ")
root.geometry("500x500")

#define our font
from tkinter import font


my_font = font.Font(
    family="brush script MT",
    size = 30,
    weight = "bold"
)

#create frame
my_frame = Frame(root) 
my_frame.pack(pady=10)

#list box 
my_list = Listbox(my_frame, 
                  font=my_font,
                  width=25,
                  height=5,
                  bg="SystemButtonFace",
                  bd=0,
                  fg="#464646",
                  )

my_list.pack() 

#creat dumy list
stuff=["complete report", "meet with team" , "finish coding task", "attend meeting","respond to email"]

#add dumy list to list box
for item in stuff:
    my_list.insert(END,item)

#scroll bar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT , fill=BOTH)

#add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#creat entry box to add items in list
my_entry=Entry(root,font=("helvetica",24))
my_entry.pack(pady=20)

#create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#functions
def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0,END)
def update_item():
    selected_index = my_list.curselection()
    if selected_index:
        updated_text = my_entry.get()
        my_list.delete(selected_index)
        my_list.insert(selected_index, updated_text)
        my_entry.delete(0, END)

def track_item():
    selected_index = my_list.curselection()
    if selected_index:
        tracked_item = my_list.get(selected_index)
        tracked_label.config(text="Currently tracking: " + tracked_item)

#add some buttons
delete_button = Button(button_frame,text="delete item", command = delete_item)
add_button = Button(button_frame,text="add item", command = add_item)
update_button = Button(button_frame, text="Update Item", command=update_item)
track_button = Button(button_frame, text="Track Item", command=track_item)

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1, padx=20)
update_button.grid(row=1, column=0)
track_button.grid(row=1, column=1)

# Tracked item label
tracked_label = Label(root, text="")
tracked_label.pack(pady=10)


root.mainloop()

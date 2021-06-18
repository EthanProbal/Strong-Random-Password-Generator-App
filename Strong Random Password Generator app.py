from tkinter import *
from random import randint

root = Tk()
root.title("Frustrated Learner - Strong Password Generator")
root.geometry("500x300")

l_frame = LabelFrame(root, text = "How many characters ?")
l_frame.pack(pady = 20)

character_len_entry = Entry(l_frame, font =("Helvetika", 24))
character_len_entry.insert(0, 25)
character_len_entry.pack(padx = 20, pady = 20)

def generator():
    global message_label
    global pw_len
    password_entry.delete(0, END)
    message_label.grid_forget()
    try :
        pw_len = int(character_len_entry.get())
        message_label.grid_forget()
        message_label = Label(button_frame, text = "Random Password Generated !", font =("Helvetica", 15))
        message_label.grid(row = 0, column = 0, columnspan =3, pady = 3)
        
        generated_pass = ""
        for x in range(pw_len):
            generated_pass += chr(randint(33,126))
        
        password_entry.insert(0, generated_pass)
        
        if pw_len <= 0:
            message_label.grid_forget()
            message_label = Label(button_frame, text = "Password Length can't be 0 or Negative", font =("Helvetica", 15), fg = "red")
            message_label.grid(row = 0, column = 0, columnspan =3, pady = 3)
            
    except ValueError:
        message_label.grid_forget()
        message_label = Label(button_frame, text = "Invalid Value Entered !", fg = "red", font =("Helvetica", 15))
        message_label.grid(row = 0, column = 0, columnspan =3)
        
def copy():
    global message_label
    
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    
    message_label.grid_forget()
    message_label = Label(button_frame, text = "Password Copied to Clipboard", font =("Helvetica", 15))  
    message_label.grid(row = 0, column = 0, columnspan =3, pady = 3)
        
password_entry = Entry(root, font =("Helvetica", 21), text = "", width = 25, bd =0, bg = "systembuttonface")
password_entry.pack(pady = 10)

button_frame = Frame(root)
button_frame.pack(pady = 20)

button_generate = Button(button_frame, text = "Generate Random Password", command = generator)
button_generate.grid(row = 1, column = 0, padx = 10)

button_copy = Button(button_frame, text = "Copy To Clipboard", command = copy)
button_copy.grid(row = 1, column = 1, padx = 10)

button_exit = Button(button_frame, text = "Exit Application", command = root.quit)
button_exit.grid(row = 1, column = 2, padx = 10)

message_label = Label(root, text = "")

root.mainloop()

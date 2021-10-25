from tkinter.filedialog import *
import tkinter as tk

# Save file method
def saveFile():
    new_file = asksaveasfile(mode = 'w', filetypes = [('text files', '.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

# Open file method
def openFile():
    file = askopenfile(mode = 'r', filetypes = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.insert(INSERT, content)

# Clear file method
def clearFile():
    entry.delete(1.0, END)


# Create the canvas
canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "white")
top = Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'nw')


# Buttons
b1 = Button(canvas, text="Open", bg="white", command = openFile)
b1.pack(in_ = top, side=LEFT)

b2 = Button(canvas, text="Save", bg="white", command = saveFile)
b2.pack(in_ = top, side=LEFT)

b3 = Button(canvas, text="Clear", bg="white", command = clearFile)
b3.pack(in_ = top, side=LEFT)

b4 = Button(canvas, text="Exit", bg="white", command = exit)
b4.pack(in_ = top, side=LEFT)


# canvas settings
entry = Text(canvas, wrap = WORD, bg = "#F9DDA4", font = ("tahoma", 16))
entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)


canvas.mainloop()
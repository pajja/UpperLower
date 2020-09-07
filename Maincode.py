from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("UpperLower")

canvas = Canvas(root, height=450, width=450, bg='#e8ffff')
canvas.pack()

frameInput = Frame(root, bg='#e8ffff').place(relx=0, rely=0, width=450, height=225)
frameOutput = Frame(root, bg='#e8ffff').place(relx=0, rely=0.5, width=450, height=225)

wInput = Scrollbar(frameInput)
wInput.place(relx=0.95, rely=0.02, width=15, height=195)

wOutput = Scrollbar(frameOutput)
wOutput.place(relx=0.95, rely=0.55, width=15, height=195)

textInput = Text(frameInput, wrap=WORD, yscrollcommand=wInput.set)
textInput.place(relx=0.02, rely=0.02, width=420, height=195)

textOutput = Text(frameOutput, wrap=WORD, yscrollcommand=wOutput.set)
textOutput.place(relx=0.02, rely=0.55, widt=420, height=195)

def makeUpper():
    try:
        textOutput.delete(1.0, END)
        ansUpper = textInput.get(1.0, END).upper()
        textOutput.insert(END, ansUpper)
    except:
        messagebox.showerror("Error", "Unkown Error")

def makeLower():
    try:
        textOutput.delete(1.0, END)
        ansLower = textInput.get(1.0, END).lower()
        textOutput.insert(END, ansLower)
    except:
        messagebox.showerror("Error", "Unknown Error")

upperButton = Button(root, text='Upper', bg='#d0efff', relief=GROOVE, command=makeUpper)
upperButton.place(relx=0.45, rely=0.5, anchor=CENTER)

lowerButton = Button(root, text='Lower', bg='#d0efff', relief=GROOVE, command=makeLower)
lowerButton.place(relx=0.55, rely=0.5, anchor=CENTER)

root.mainloop()

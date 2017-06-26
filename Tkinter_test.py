from Tkinter import *
import webbrowser

window = Tk()

window.title("My First Tkinter")
window.geometry('400x400')

print webbrowser._browserss # fuck

counter = 0
def increment_counter():
    global counter
    counter += 1

def btn_handler():
    increment_counter()

    txt = Text(window)
    txt.pack()
    txt.insert(END, "Text added... %d" % counter)

    btn.state = DISABLED

    webbrowser.open('https://www.google.com/', new=0, autoraise=True)

btn = Button(window, text="Click", width=25, height=4, command=btn_handler)
btn.pack()

window.mainloop()

import os, sys, random, json
from tkinter import *

with open('kana.json', encoding='utf-8') as kana_array:
    kana = json.load(kana_array)

def verify(entry):
    if entry==kana[num][1]:
        reply= "Correct."
    else:
        reply = "Incorrect, it's " + str(kana[num][1])
    result['text']=reply
    random_kana()

def random_kana():
    global num; num=random.randint(0,len(kana)-1)
    #print("kana: ", kana[num][0])
    display['text']=kana[num][0]
    entry.delete(0, END)


def exit_program():
    window.destroy()
    exit()

window = Tk()
window.title("Learning Japanese")

hgt = 800
wdt = 600
canvas= Canvas(window, height=hgt, width=wdt)
canvas.pack()
frame = Frame (window, bg ="gray10", bd= 5)
frame.place(relwidth=1, relheight=1)

window.configure(background="gray10")
intro = Label (frame, text = "Guess the Kana", bg= "gray10", fg = "white", font = "none 18 bold")
intro.place(relx=0.5,rely=0.1,relwidth=1,relheight=0.1, anchor="n")

display = Label (frame, bg= "gray10", fg = "white", font = "none 30 bold")
display.place(relx=0.5, rely=0.3, relwidth= 1,relheight=0.1, anchor="n")

generate = Button(frame,font=16, bg= "gray", fg="white", text = "New character", command= lambda:random_kana())
generate.place(relx=0.3, rely= 0.8, relwidth=0.1,relheight=0.1)

entry = Entry(frame, font=14) 
entry.place(relx= 0.5, rely=0.7, relwidth=0.1,relheight=0.1,anchor="n")

test = Button(frame, text= "Verify",bg ="gray", fg="white",font="18", command = lambda: verify(entry.get()))  
test.place(relx=0.5,rely=0.8,relwidth=0.1,relheight=0.1,anchor="n")

result = Label(frame,font=18, bg= "gray10", fg="white")
result.place(relx=0.5,rely=0.6,relwidth=1,relheight=0.1,anchor="n")

exit_button = Button(frame, text = "Exit", bg="gray",fg="white", font = 18, command = exit_program)
exit_button.place(relx=0.8, rely=0.8,relwidth=0.1,relheight=0.1,anchor="n" )


random_kana()
window.mainloop()
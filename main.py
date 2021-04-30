import os
import sys
import tkinter
import random

def press():
    text.delete(1.0, tkinter.END)
    text.insert(1.0, random.choice(lines))
    text.tag_add('title', 1.0, '1.end')
    text.tag_config('title', font=("Times", 18, 'bold', 'italic'), justify=tkinter.CENTER)

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

path = resource_path("citates.txt")

window = tkinter.Tk()
window.title("Мотивация на каждый день")

with open(path, 'r', encoding='utf-8') as citates:
    lines = citates.readlines()
    today_citate = random.choice(lines)

text = tkinter.Text(width=80, height=8, wrap=tkinter.WORD)
text.grid(row=0, columnspan=4, sticky=tkinter.W + tkinter.E)

scroll = tkinter.Scrollbar(command=text.yview)
scroll.grid(row=0, column=5, sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)
text.config(yscrollcommand=scroll.set)
text.insert(1.0, today_citate)

text.tag_add('title', 1.0, '1.end')
text.tag_config('title', font=("Times", 18, 'bold', 'italic'), justify=tkinter.CENTER)

btn = tkinter.Button(text="Следующая", command=lambda:press())
btn.grid(row=1, columnspan=5)

window.mainloop()

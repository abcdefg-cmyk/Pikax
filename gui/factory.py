from tkinter import *

# image = None
from tkinter import ttk


def make_button(master, text=''):
    # global image
    # image = PhotoImage(file='neurons.gif')
    return Button(master=master,
                  text=text,
                  relief=RAISED,
                  state=DISABLED,
                  padx=10,
                  pady=2,
                  )


def make_label(master, text=''):
    return ttk.Label(master=master,
                     text=text)


def make_entry(master):
    return ttk.Entry(master=master)


def make_frame(master):
    return ttk.Frame(master=master)


def make_dropdown(master, default, choices):
    dropdown = ttk.Combobox(master, values=choices, state='readonly')
    dropdown.configure(width=17)
    dropdown.set(default)
    return dropdown


def make_text(master):
    return Text(master, wrap=WORD, height=2, width=60, state=DISABLED)


def grid(component):
    component.grid(padx=5, pady=5)


def pack(component):
    component.pack(padx=5, pady=5)
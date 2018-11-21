from tkinter import filedialog
from tkinter import *

def read_from_file():
    root = Tk()
    filename = filedialog.askopenfile(mode="r", initialdir="/", title="select file",
                                      filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    root.destroy()
    return filename.readline()

def save_to_file(text):
    filename = input('Enter filename: ')
    f = open(filename+'.txt','w')
    f.write(text)
    f.close()
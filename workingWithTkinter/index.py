# from tkinter.messagebox import *
from tkinter.filedialog import *
from workingWithPdf import mergePDFs as merger

# name = askquestion('What is your name?', 'Enter your name')
# print(name) type = str

# name = askokcancel('What is your name?', 'Enter your name')
# print(name) type = boolean

# name = askretrycancel('What is your name?', 'Enter your name')
# print(name) type = boolean: to continue after an error

# name = askyesno('What is your name?', 'Enter your name')
# print(name) type boolean

# name = askyesnocancel('What is your name?', 'Enter your name')
# print(name) yes: 1, no: 0, cancel: null


def op():
    name = askdirectory()
    if len(name) < 1:
        print('Go back and select a folder')
        op()
    else:
        print(type(name))
        print(name)

def openFile():
    file = askopenfilenames()
    print(len(file))

fileOpen = merger.Merger()
#
# fileOpen.save()
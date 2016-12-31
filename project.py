import datetime
from tkinter import *


class Employee:
    def __init__(self, name, address, salary, date):
        self.name = name
        self.address = address
        self.salary = salary
        self.date = date

    def vypis(self):
        print(self.name, self.address, self.salary, self.date)

    pass


def load_file(file_name):
    array = []

    with open(file_name) as f:
        for line in f:
            array.append(line)

    return array


def make_list(temp_array, final_array):
    def make_employee_from_file():
        nonlocal temp_array
        e = Employee(temp_array[0][:-1], temp_array[1][:-1], temp_array[2][:-1], temp_array[3][:-1])
        return e

    for f in temp_array:
        x = make_employee_from_file()
        final_array.append(x)
        temp_array = temp_array[5:]
        if len(temp_array) < 1:
            break

    return final_array


def print_all(list_employees):
    for n in list_employees:
        print(n.name, n.address, n.salary, n.date)
    pass


array = load_file("dan.txt")
list_employees = []
list_employees = make_list(array, list_employees)


def do_nothing():
    pass


def menu(root):
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=do_nothing)
    filemenu.add_command(label="Open", command=do_nothing)
    filemenu.add_command(label="Save", command=do_nothing)
    filemenu.add_command(label="Save as...", command=do_nothing)
    filemenu.add_command(label="Close", command=do_nothing)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=do_nothing)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=do_nothing)
    editmenu.add_command(label="Copy", command=do_nothing)
    editmenu.add_command(label="Paste", command=do_nothing)
    editmenu.add_command(label="Delete", command=do_nothing)
    editmenu.add_command(label="Select All", command=do_nothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=do_nothing)
    helpmenu.add_command(label="About...", command=do_nothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    return menubar


def text_writer(root,employees):
    text = Text(root)
    for n in employees:
        text.insert(INSERT, n.name, INSERT, "\n")
        text.insert(INSERT, n.address, INSERT, "\n")
        text.insert(INSERT, n.salary, INSERT, "\n")
        text.insert(INSERT, n.date, INSERT, "\n", INSERT, "\n")
    text.pack()
    return text


def gui(employees):
    root = Tk()
    frame = Frame(root)
    frame.pack()
    menu_bar = menu(root)
    text = text_writer(root,employees)
    root.config(menu=menu_bar)

    root.mainloop()

gui(list_employees)

"""
-------------WITHOUT GUI-------------------

key = 'k' #input("Press any key: ")


while key != 'k' and key != 'K':
    if key == 'v':
        print("You chose add eployee: ")
        name = input("Type name: ")
        address = input("Type address: ")
        salary = input("Type salary: ")
        now = datetime.datetime.now()
        date = str(now.day) + str(now.month) + str(now.year)
        list_employees.append(Employee(name,address,salary,date))
    elif key == 'p':
        print_all(list_employees)

    key = input("Press any key: ")
"""
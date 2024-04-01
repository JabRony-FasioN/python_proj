import tkinter as tk
from tkinter import ttk
import openpyxl

def load_data(path):
    goal = []
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    list_values = list(sheet.values)
    for i in list_values:
        goal.append(i[0])
        

    return goal
    



from openpyxl import Workbook, load_workbook
# If you need to get the column letter, also import this
from openpyxl.utils import get_column_letter 
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import os
from datetime import datetime
import pandas as pd
past=['20230110000035','455']

def csv():
    global ProdutoCSV, LocalCSV, RuaCSV
    # reading CSV file
    data = pd.read_csv("workbook.csv")

    # converting column data to list
    try:
        ProdutoCSV = data['Produto'].tolist()
        LocalCSV = data['Local'].tolist()
        RuaCSV = data['Rua'].tolist()

        
    except:
        ProdutoCSV=[]
        LocalCSV=[]
        RuaCSV=[]

        print(ProdutoCSV)
        print(LocalCSV)

    return ProdutoCSV, LocalCSV, RuaCSV


def appendPast():

    if (ProdutoCSV != []) and (LocalCSV != []):
        for prods in ProdutoCSV:
            if str(prods) not in str(past):
                print(prods)
                past.append(prods)

        for locs in LocalCSV:
            if str(locs) not in str(past):
                print(locs)
                past.append(locs)


csv()
appendPast()

print(past)
'''
專案在學習grid的編排
'''

import tkinter as tk
from tkinter import ttk

class Windows(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        ttkStyle =ttk.Style()
        ttkStyle.theme_use("default")
        ttkStyle.configure("1.TFrame",background = "#008080")
        ttkStyle.configure("2.TFrame",background= "#ff7f50") 
        ttkStyle.configure("3.TFrame",background= "#ffffff")
        ttkStyle.configure("1.TLabel",background= "#3cb371")
        
        mainFrame = ttk.Frame(self)
        mainFrame.pack(expand = True, fill=tk.BOTH)

        '''
        ttk.Label(mainFrame,text="BMI試算").pack()
        '''

        topFrame = ttk.Frame(mainFrame,style="1.TFrame",height=100)
        topFrame.pack(fill=tk.X)

        ttk.Label(topFrame,text="BMI calculate", style="1.TLabel").pack(pady=25)

        bottomFrame = ttk.Frame(mainFrame,style="2.TFrame")
        bottomFrame.pack(expand=True,fill=tk.BOTH)
        '''
        --新增這個以後我的style=1.TLabel會失效
        bottomFrame.pack(expand=True,fill=tk.BOTH)
        bottomFrame.columnconfigure(0,weight=3)
        bottomFrame.columnconfigure(1,weight=5)
        bottomFrame.rowconfigure(0, weight=1)
        '''
        
        

        ttk.Label(bottomFrame,text="name",style="gridLabel.TLabel").grid(column=0,row=0,sticky=tk.E)
        ttk.Entry(bottomFrame).grid(column=1,row=0, sticky=tk.W)

        



def main():
    '''
    This is the program exacuative point
    這是程式的執行點
    '''

    window = Windows()
    window.title("BMI calculator")
    window.geometry("400x500") 
    window.mainloop()

if __name__=="__main__":
    main()
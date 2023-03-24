'''
專案在學習grid的編排
'''

import tkinter as tk
from tkinter import ttk

class Windows(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        ttkStyle =ttk.Style()
        print(ttkStyle.theme_names())
        ttkStyle.theme_use("default")
        ttkStyle.configure("1.TFrame",background = "#008080")
        ttkStyle.configure("2.TFrame",background= "#ff7f50") 
        ttkStyle.configure("3.TFrame",background="#ffffff")
        
        mainFrame = ttk.Frame(self,style="1.TFrame")
        mainFrame.pack(expand = True, fill=tk.BOTH)

        '''
        ttk.Label(mainFrame,text="BMI試算").pack()
        '''

        topFrame = ttk.Frame(mainFrame, style="1.TFrame",height=100)
        topFrame.pack(fill=tk.X)

        bottomFrame = ttk.Frame(mainFrame,style="2.TFrame")
        bottomFrame.pack(expand=True,fill=tk.BOTH)



def main():
    '''
    This is the program exacuative point
    這是程式的執行點
    '''

    window = Windows()
    window.title("BMI calculator")
    window.geometry("400x500") 
    window.mainloop()


    pass

if __name__=="__main__":
    main()
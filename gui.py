from tkinter import *
from tkinter import ttk
from config import *
import requests

'''
API EXCHANGE RATE SOFTWARE
'''

class GUI(CONFIG):
    def __init__(self,root):
        super().__init__()
        self.win = root
        self.settings()
        self.data = requests.get("https://api.exchangerate.host/latest").json()
        self.keys = list(self.data["rates"].keys())
        #Frames
        self.main_f = Frame(self.win)

    def settings(self):
        self.win.title(self.title)
        self.win.geometry("{}x{}".format(self.width,self.height))

    def start(self):
        self.main()
        self.win.mainloop()

    def main(self):
        #data/list
        basic = ["EUR","USD","JPY","GBP","AUD","CAD","CNY","HKD","NZD","RUB"] #addable currencies
        #Widgets/Frontend
        self.main_f.pack(fill="both",expand=1)
        Label(self.main_f,text="EXCHANGE RATE API\nhttps://exchangerate.host/#/",font=self.font).place(relx=0.5,rely=0.1,anchor="center")
        
        cc_input = ttk.Combobox(self.main_f,values=basic,state="readonly",font=self.font)
        cc_input.current(0)
        cc_input.place(relx=0.3,rely=0.4,anchor="center",relwidth=0.2)

        cc_output = ttk.Combobox(self.main_f,values=basic,state="readonly",font=self.font)
        cc_output.current(1)
        cc_output.place(relx=0.7,rely=0.4,anchor="center",relwidth=0.2)

        cc_in_entry = Entry(self.main_f,font=self.font)
        cc_in_entry.place(relx=0.3,rely=0.5,anchor="center",relwidth=0.25)

        cc_out_entry = Entry(self.main_f,font=self.font)
        cc_out_entry.insert(0,"sdasd")
        cc_out_entry["state"] = "disabled"
        cc_out_entry.place(relx=0.7,rely=0.5,anchor="center",relwidth=0.25)
        
        Button(self.main_f,text="------->",font=self.font,command=lambda:self.convert(cc_input.get(),float(cc_in_entry.get()),cc_output.get(),cc_out_entry)).place(relx=0.5,rely=0.65,anchor="center")

    def convert(self,cc_input,cc_in_entry,cc_output,cc_out_entry):
        cc_out_entry["state"] = "normal"
        cc_out_entry.delete(0,END)
        if cc_input == "EUR":
            multi = self.data["rates"][cc_output] #multiplicator
        else:
            multi = self.data["rates"][cc_output]/self.data["rates"][cc_input] #reference document formula
        total = round(multi * cc_in_entry,2)
        cc_out_entry.insert(0,total)
        cc_out_entry["state"] = "disabled"

root = Tk()
app = GUI(root)
app.start()
from tkinter import *
import json

with open('times.json','r+') as file:
    data = json.load(file)
    start = data['start']
    end = data['end']

class Window(object):
    def __init__(self,window):
        global new
        self.window=window
        self.window.wm_title('website blocker')

        self.v1=StringVar()
        l1=Label(window,text='Name of website',width=12,font=('Times', 13))
        l1.grid(row=1,column=0)
        self.e1=Entry(window,textvariable=self.v1, width=60)
        self.e1.grid(row=1,column=1,columnspan=5)

        self.v2=IntVar()
        l2=Label(window,text='Start time',width=12)
        l2.grid(row=3,column=4)
        self.e2=Entry(window,textvariable=self.v2, width=12)
        self.e2.grid(row=4,column=4)

        self.v3=IntVar()
        l3=Label(window,text='End time',width=12)
        l3.grid(row=5,column=4)
        self.e3=Entry(window,textvariable=self.v3, width=12)
        self.e3.grid(row=6,column=4)

        b1=Button(window,text='Add Entry',width=12,command=self.add_command)
        b1.grid(row=2,column=0)
        b2=Button(window,text='View All',width=12,command=self.view_command)
        b2.grid(row=2,column=1)
        b4=Button(window,text='Update',width=12,command=self.update_command)
        b4.grid(row=2,column=2)
        b5=Button(window,text='Delete',width=12,command=self.delete_command)
        b5.grid(row=2,column=3)
        b6=Button(window,text='Close',width=12,command=window.destroy)
        b6.grid(row=2,column=4)
        b7=Button(window,text='Submit',width=12,command=self.update_json)
        b7.grid(row=7,column=4)

        self.list1 = Listbox(window, height=15,width=45)
        self.list1.grid(row=3,column=0,rowspan=6,columnspan=3)

        sb1 = Scrollbar(window)
        sb1.grid(row=1,column=3,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

    def get_selected_row(self,event):
        x=self.list1.curselection()
        self.selected=self.list1.get(x)
        self.e1.delete(0,END)
        self.e1.insert(END, self.selected)
    
    def add_command(self):
        with open('websites.txt','a') as file:
            file.write(self.v1.get()+'\n')
        self.list1.delete(0,END)
        self.list1.insert(END,self.v1.get())

       
    def view_command(self):
        with open('websites.txt','r+') as file:
            website_list = file.readlines()
            self.list1.delete(0,END)
            for site in website_list:
                self.list1.insert(END,site)
            
    
    def update_command(self):
        with(open('websites.txt', 'r+')) as file:
            contents = file.readlines()
            x = contents.index(self.selected)
            contents[x] = self.v1.get()
            file.seek(0)
            file.truncate()
            for site in contents:
                file.write(site)
 
    def delete_command(self):
            with(open('websites.txt', 'r+')) as file:
                contents = file.readlines()
                contents.remove(self.selected)
                file.seek(0)
                file.truncate()
                for site in contents:
                    file.write(site)

    def update_json(self):
        with open('times.json','r+') as file:
            data = json.load(file)
            data['start'] = self.v2.get()
            data['end'] = self.v3.get()
            file.seek(0)
            file.truncate()
            json.dump(data, file)
        

    
window=Tk()
Window(window)
window.geometry("500x300+200+200")
window.mainloop()

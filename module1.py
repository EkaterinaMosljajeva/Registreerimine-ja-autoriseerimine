from tkinter import *
from random import *

ur_aken=Tk()
ur_aken.geometry("400x400")
ur_aken.iconbitmap("kot.ico")
canv=Canvas(ur_aken,width=200,height=200)
ur_img=PhotoImage(file="kot1.png")
canv.create_image(2,2,image=ur_img)
canv.grid(row=0,column=0)
ur_aken.mainloop()

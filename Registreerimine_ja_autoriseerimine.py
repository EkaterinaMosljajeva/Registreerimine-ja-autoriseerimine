from tkinter import *
k=0

def zv(event):
    global k
    k+=1
    if k%2==0:
        password.configure(show="*")
    else:
        password.configure(show="")

aken=Tk()
aken.title("Minu aken")
aken.geometry("450x300")
aken.iconbitmap("kot.ico")
f=Frame(aken)
lbl=Label(f,text="Autoriseerimine",bg="pink",fg="#AA4A44",font="Arial 20",width=28)
log=Label(f,text="Login",font="Arial 20")
login=Entry(f,fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
pas=Label(f,text="Password",font="Arial 20")
password=Entry(f,fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10,show="*")
ent=Button(f,text="Enter", font="Arial 24", relief=GROOVE, width=11)
pas_btn=Button(f,text="Näita parool", font="Arial 10", relief=GROOVE, width=10)


pas_btn.bind("<Button-1>",zv)

lbl.pack()
log.pack()
login.pack()
pas.pack()
password.pack()
pas_btn.pack()
ent.pack()
f.grid(row=0,column=0)



aken.mainloop()

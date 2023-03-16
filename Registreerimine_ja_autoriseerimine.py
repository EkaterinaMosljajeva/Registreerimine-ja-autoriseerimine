from tkinter import *
from random import *
import string
k=0

def zv(event):
    global k
    k+=1
    if k%2==0:
        password.configure(show="*")
    else:
        password.configure(show="")

def spisok(f):
    log_pas={}
    pas_log={}
    file=open(f,'r',encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split("-")
        log_pas[v]=k
        pas_log[k]=v
        print(k,v)
    return log_pas

def pswrd(event):
    sala=""
    for i in range(12):
        t=choice(string.ascii_letters)
        num=choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        sala+=choice(t_num)
    password.configure(text=sala)




def proverka(event):
    pas_list=list(log_pas.keys())
    log_list=list(log_pas.values())
    l=login.get()
    p=password.get()
    if l=="":
        login.configure(bg="red")
    else:
        login.configure(bg="lightblue")
    if p=="":
        password.configure(bg="red")
    else:
        password.configure(bg="lightblue")
    if l in log_list:
        ind=log_list.index(l)
        if p in pas_list[ind]:
            ur_aken=Toplevel()
            ur_aken.geometry("400x400")
            ur_aken.iconbitmap("kot.ico")
            canv=Canvas(ur_aken,width=200,height=200)
            ur_img=PhotoImage(file="kot1.png")
            canv.create_image(2,2,image=ur_img)
            canv.grid(row=0,column=0)
            ur_aken.mainloop()
        else:
            pass

log_pas=spisok("log_pas.txt")
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
pas_btn=Button(f,text="Näita parool",font="Arial 10",relief=GROOVE, width=10)
r=Button(f,text="Genereeritud parool",font="Arial 10",relief=GROOVE, width=15)


pas_btn.bind("<Button-1>",zv)
r.bind("<Button-1>",pswrd)
ent.bind("<Button-1>",proverka)


lbl.pack()
log.pack()
login.pack()
pas.pack()
password.pack()
pas_btn.pack()
r.pack()
ent.pack()
f.grid(row=0,column=0)



aken.mainloop()


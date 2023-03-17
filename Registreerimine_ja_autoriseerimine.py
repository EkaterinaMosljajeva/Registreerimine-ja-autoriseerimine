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
    password.delete(0, END)
    password.insert(0,sala)

def salvesta(event):
    pas_list=list(log_pas.keys())
    log_list=list(log_pas.values())
    y=[]
    for i in range(len(log_pas)):
        y.append(pas_list[i]+"-"+log_list[i]+"\n")
    file=open("log_pas.txt",'w', encoding="utf-8-sig")
    file.writelines(y)

def registratsia(event):
    register=Toplevel()
    register.iconbitmap("kot.ico")
    register.geometry("450x350")
    register.title("Registreerimine")
    register["bg"] = "Gainsboro"
    reg_log=Entry(register, fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
    rl=Label(register,text="Login",font="Arial 20",bg="Gainsboro")
    rp=Label(register,text="Password",font="Arial 20",bg="Gainsboro")
    reg_pas=Entry(register,fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
    lbr=Label(register,text="Registreerimine",bg="pink",fg="#AA4A44",font="Arial 20",width=28)
    entr=Button(register,text="Enter", font="Arial 24", relief=GROOVE, width=11)
    ent.bind("<Button-1>",salvesta)
    lbr.pack()
    rl.pack()
    reg_log.pack()
    rp.pack()
    reg_pas.pack()
    entr.pack()
    
    register.mainloop()

def muutmine(event):
    muuta=Toplevel()
    muuta.iconbitmap("kot.ico")
    muuta.geometry("450x350")
    muuta.title("Registreerimine")
    muuta["bg"] = "Gainsboro"
    muu_log=Entry(muuta, fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
    ml=Label(muuta,text="Login",font="Arial 20",bg="Gainsboro")
    mp=Label(muuta,text="Password",font="Arial 20",bg="Gainsboro")
    muu_pas=Entry(muuta,fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
    lbm=Label(muuta,text="Muutmine",bg="pink",fg="#AA4A44",font="Arial 20",width=28)
    entm=Button(f,text="Enter", font="Arial 24", relief=GROOVE, width=11)
    lbm.pack()
    ml.pack()
    muu_log.pack() 
    mp.pack() 
    muu_pas.pack()
    entm.pack()
    muuta.mainloop()



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
            incor.configure(text="",bg="Gainsboro")
            ur_aken=Toplevel()
            ur_aken.iconbitmap("kot.ico")
            aken.geometry("600x600")
            fur=Frame(ur_aken)
            canv=Canvas(ur_aken,width=200,height=200)
            muu=Button(fur,text="Nime või parooli muutmine",font="Arial 10",relief=GROOVE)
            ur_img=PhotoImage(file="kot1.png").subsample(9)
            canv.create_image(100,110,image=ur_img)
            canv.grid(row=0,column=0)
            muu.pack()
            fur.grid()
            muu.bind("<Button-1>",muutmine)
            ur_aken.mainloop()
        else:
            incor.configure(text="Vale parool",bg="#F08080")
    else:
        incor.configure(text="Vale login",bg="#F08080")

log_pas=spisok("log_pas.txt")
aken=Tk()
aken.title("Autoriseeriminen")
aken.geometry("450x350")
aken.iconbitmap("kot.ico")
aken["bg"] = "Gainsboro"
f=Frame(aken,bg="Gainsboro")
lbl=Label(f,text="Autoriseerimine",bg="pink",fg="#AA4A44",font="Arial 20",width=28)
log=Label(f,text="Login",font="Arial 20",bg="Gainsboro")
login=Entry(f,fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
pas=Label(f,text="Password",font="Arial 20",bg="Gainsboro")
password=Entry(f,fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10,show="*")
ent=Button(f,text="Enter", font="Arial 24", relief=GROOVE, width=11)
pas_btn=Button(f,text="Näita parool",font="Arial 10",relief=GROOVE, width=10)
r=Button(f,text="Genereeritud parool",font="Arial 10",relief=GROOVE, width=15)
reg=Button(f,text="Registreerimine",font="Arial 10",relief=GROOVE, width=15,bg="lightgreen")

incor=Label(f,font="Arial 20",width=28,bg="Gainsboro")


pas_btn.bind("<Button-1>",zv)
r.bind("<Button-1>",pswrd)
ent.bind("<Button-1>",proverka)
reg.bind("<Button-1>",registratsia)


lbl.pack()
log.pack()
login.pack()
pas.pack()
password.pack()
pas_btn.pack()
r.pack()
ent.pack()
f.grid(row=0,column=0)
incor.pack(side=BOTTOM)
reg.pack(side=BOTTOM)



aken.mainloop()

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
    return log_pas,pas_log

def pswrd(event):
    sala=""
    for i in range(12):
        t=choice(string.ascii_letters)
        num=choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        sala+=choice(t_num)
    password.delete(0, END)
    password.insert(0,sala)

def mut():
    lines=[]
    with open("log_pas.txt",'r') as fp:
        lines=fp.readline()
    with open("log_pas.txt",'w') as fp:
        for line in enumerate(lines):
            fp.write(line)



def salvesta(event):
        l=reg_log.get()
        p=reg_pas.get()
        f=open("log_pas.txt",'a',encoding="utf-8-sig")
        f.write("\n"+l+"-"+p)
        register.destroy()


def registratsia(event):
    global reg_log,reg_pas,register
    register=Toplevel()
    register.iconbitmap("kot.ico")
    register.geometry("450x350")
    register.title("Registreerimine")
    register["bg"] = "Gainsboro"
    reg_log=Entry(register, fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
    login=Label(register,text="Login",font="Arial 20",bg="Gainsboro")
    password=Label(register,text="Password",font="Arial 20",bg="Gainsboro")
    reg_pas=Entry(register,fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
    lbr=Label(register,text="Registreerimine",bg="pink",fg="#AA4A44",font="Arial 20",width=28)
    entr=Button(register,text="Enter", font="Arial 24", relief=GROOVE, width=11)
    r=Button(register,text="Genereeritud parool",font="Arial 10",relief=GROOVE, width=15)

    entr.bind("<Button-1>",salvesta)
    r.bind("<Button-1>",pswrd)
 
    lbr.pack()
    login.pack()
    reg_log.pack()
    password.pack()
    reg_pas.pack()
    r.pack()
    entr.pack()
    
    register.mainloop()



def muutmine1(y):
    muuta=Toplevel()
    muuta.geometry("450x350")
    muuta.iconbitmap("kot.ico")
    muuta.title("Muuda parool") 
    lblt=Label(muuta,text="Autoriseerimine",bg="pink",fg="#AA4A44",font="Arial 20",width=28)
    lbln=Label(muuta,text="Parool",font="Arial 20")
    entn=Entry(muuta,fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
    lblnn=Label(muuta,text="Uus parool",font="Arial 20")
    entnn=Entry(muuta,fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
    btnv=Button(muuta,text="Muuda",font="Arial 20",relief=GROOVE)
    lblt.pack()
    lbln.pack()
    entn.pack()
    lblnn.pack()
    entnn.pack()
    btnv.pack()
    muuta.mainloop()

def muutmine2(x):
    muuta=Toplevel()
    muuta.geometry("450x350")
    muuta.iconbitmap("kot.ico")
    muuta.title("Muuda login") 
    lblt=Label(muuta,text="Muuda login",bg="pink",fg="#AA4A44",font="Arial 20",width=28)
    lbln=Label(muuta,text="Login",font="Arial 20")
    entn=Entry(muuta,fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
    lblnn=Label(muuta,text="Uus login",font="Arial 20")
    entnn=Entry(muuta,fg="blue",bg="lightblue",font="Arial 20",justify=CENTER,width=10)
    btnv=Button(muuta,text="Muuda",font="Arial 20",relief=GROOVE) 
    lblt.pack()
    lbln.pack()
    entn.pack()
    lblnn.pack()
    entnn.pack()
    btnv.pack()
    muuta.mainloop()




def proverka(event):
    global l1,p1
    pas_list=list(log_pas.keys())
    log_list=list(log_pas.values())
    l1=login.get()
    p1=password.get()
    if l1=="":
        login.configure(bg="red")
    else:
        login.configure(bg="lightblue")
    if p1=="":
        password.configure(bg="red")
    else:
        password.configure(bg="lightblue")
    if l1 in log_list:
        ind=log_list.index(l1)
        if p1 in pas_list[ind]:
            incor.configure(text="",bg="Gainsboro")
            ur_aken=Toplevel()
            ur_aken.iconbitmap("kot.ico")
            aken.geometry("600x600")
            fur=Frame(ur_aken)
            canv=Canvas(ur_aken,width=200,height=200)
            muu1=Button(fur,text="Parooli muutmine",font="Arial 10",relief=GROOVE)
            muu2=Button(fur,text="Login muutmine",font="Arial 10",relief=GROOVE)
            ur_img=PhotoImage(file="kot1.png").subsample(9)
            canv.create_image(100,110,image=ur_img)
            canv.grid(row=0,column=0)
            muu1.pack(side=LEFT)
            muu2.pack(side=LEFT)
            fur.grid()
            muu1.bind("<Button-1>",muutmine1)
            muu2.bind("<Button-1>",muutmine2)

            ur_aken.mainloop()
        else:
            incor.configure(text="Vale parool",bg="#F08080")
    else:
        incor.configure(text="Vale login",bg="#F08080")

log_pas,pas_log=spisok("log_pas.txt")
aken=Tk()
aken.title("Autoriseerimine")
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
reg=Button(f,text="Registreerimine",font="Arial 10",relief=GROOVE, width=15,bg="lightgreen")

incor=Label(f,font="Arial 20",width=28,bg="Gainsboro")


pas_btn.bind("<Button-1>",zv)
ent.bind("<Button-1>",proverka)
reg.bind("<Button-1>",registratsia)


lbl.pack()
log.pack()
login.pack()
pas.pack()
password.pack()
pas_btn.pack()
ent.pack()
f.grid(row=0,column=0)
incor.pack(side=BOTTOM)
reg.pack(side=BOTTOM)

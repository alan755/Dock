from tkinter import*
import pickle
import os

                                                               #DATA MANAGEMENT SYSTEM
class file:
    def  enter(self,name,password,string):
       self.name=name
       self.password=password
       self.string=string
    def stringfun(self):
        return self.string
    def update(self,string,password):
        self.string=string
        self.password=password
    def compare(self,namec,passw):
          if namec==self.name and passw==self.password:
                      return  '1'
          else:
                      return '0'
        

def have():
    qp=Tk()
    qp.title("DOCK:Data Security Software")
    qp.geometry("300x53")

    Label(qp,text="          Number of users                   ",fg="white",bg="midnightblue",font=("Arial Rounded MT Bold",15)).grid(row=0,column=0,sticky=W)
    ou=Text(qp,width=2,bg="white",fg="black",font=("ariel",15))
    ou.grid(row=10,column=0,sticky=W)
    with open("login.txt","r") as t:
        n=10
        y=t.read(n)
        y=int(y)-10
    
    ou.insert(END,y)
    
def shall():
    sh=Tk()
    sh.title("DOCK: Data Management System")
    sh.geometry("300x400")
    sh.configure(background="lightsteelblue")

    Label(sh,text="             DETAILS                       ",font=("ALgerian",20),fg="white",bg="midnightblue").grid(row=0,column=0,sticky=W)
    Label(sh,text="                    Members                     ",bg="steelblue",fg="white",font=("Arial Rounded MT Bold",15)).grid(row=10,column=0,sticky=W)
    Label(sh,text="Alan Mathew\n Ashish Prakash\n Akhil Anand\n Akash James\n Anchu Babu",fg="snow",bg="lightsteelblue",font=("Arial Rounded MT Bold",14)).grid(row=20,column=0,sticky=W)
    Label(sh,text="\n\n\n",bg="lightsteelblue",).grid(row=30,column=0,sticky=W)
    Label(sh,text="                      Guide                                 ",bg="steelblue",fg="white",font=("Arial Rounded MT Bold",15)).grid(row=50,column=0,sticky=W)
    Label(sh,text="Mrs. Tintu Alphonsa Thomas",bg="lightsteelblue",fg="snow",font=("Arial Rounded MT Bold",14)).grid(row=70,column=0,sticky=W)
    Label(sh,text="\n\n\n",bg="lightsteelblue",).grid(row=75,column=0,sticky=W)
    Label(sh,text="             Group Number 3                  ",bg="steelblue",fg="white",font=("Arial Rounded MT Bold",15)).grid(row=80,column=0,sticky=W)
    #Label(sh,text="3",bg="lightsteelblue",fg="black",font=("Arial Rounded MT Bold",14)).grid(row=83,column=0,sticky=W)
    sh.mainloop()


                    
#signup
def does():

       def done():
           o1=inpo.get()
           o2=inpu.get()
           o3=inpa.get()
           o=file()
           o.enter(o1,o2,o3)
           ou=open("logged","ab")
           pickle.dump(o,ou)
           ou.close()
           a="Accoount created successfully"
           outo.insert(END,a)
           with open("login.txt","r")as f:
                  n=10
                  r=f.read(n)
           r=int(r)
           r+=1
           f.close()
           with open("login.txt","w+")as g:
                  g.write(str(r))
           g.close()

       #signing up..
       al=Tk()
       al.title("DOCK:The Data Management System")
       al.geometry("500x350")
       al.configure(background="lightsteelblue")
       Label(al,text="                       Sign Up Here                                                                                          ",bg="midnightblue",fg="white",font=("ALgerian",20)).grid(row=0,column=0,sticky=W)
       Label(al,bg="lightsteelblue",text="Username",fg="black",font=("Arial Rounded MT Bold",15)).grid(row=10,column=0,sticky=W)
       inpu=Entry(al,width=30,bg="white",fg="black",font=("Arial Rounded MT Bold",15))
       inpu.grid(row=25,column=0,sticky=W)
       Label(al,bg="lightsteelblue",text="Password",fg="black",font=("Arial Rounded MT Bold",15)).grid(row=30,column=0,sticky=W)
       inpo=Entry(al,width=30,bg="white",fg="black",font=("Arial Rounded MT Bold",15),show="*")
       inpo.grid(row=50,column=0,sticky=W)
       Label(al,bg="lightsteelblue",text="Data",fg="black",font=("Arial Rounded MT Bold",15)).grid(row=60,column=0,sticky=W)
       inpa=Entry(al,width=100,bg="white",fg="black",font=("Arial Rounded MT Bold",15))
       inpa.grid(row=80,column=0,sticky=W)

       Button(al,text="Enter",fg="white",bg="midnightblue",command=done,font=("Arial Rounded MT Bold",15),width=8).grid(row=90,column=0,sticky=W)

       #Label(al,bg="lightcyan",text="Output",fg="black",font=("Arial Rounded MT Bold",15),).grid(row=100,column=0,sticky=W)
       outo=Text(al,width=40,height=1,bg="lightsteelblue",fg="black",font=("Arial Rounded MT Bold",15))
       outo.grid(row=110,column=0,sticky=W)

       al.mainloop()
#signin
def do():
    
    def did():
         #profile page
         global inp
         q=inp.get()
         global inpp
         p=inpp.get()
         d="loading......"
         global out
         out.insert(END,d)
         with open("login.txt","r") as  f:
                n=10
                u=f.read(n)
         u=int(u)        
         i=10
         flag=1
         inpute=open("logged","rb")
         while i<u:
               o=file()
               o=pickle.load(inpute)
               w=o.compare(q,p)
               if w=='1':

                   def had():

                       def been():
                             global d
                             e=d.get()
                             global nam
                             na=nam.get()
                             k="Account updated successfully"
                             global ow
                             ow.insert(END,k)

                             o.update(e,na)
                             rt=open("logged","ab")
                             pickle.dump(o,rt)
                             rt.close()
                             with open("login.txt","r")as h:
                                        n=40
                                        r=h.read(n)
                             r=int(r)
                             r+=1
                             h.close()
                             with open("login.txt","w+")as v:
                                     v.write(str(r))
                             v.close()
                             
                             
                           

                       y=Tk()
                       y.title("DOCK: Data Management System")
                       y.geometry("700x300")
                       y.configure(background="lightsteelblue")

                       Label(y,text="                              Update Data                                                  ",bg="midnightblue",fg="white",font=("ALgerian",20)).grid(row=0,column=0,sticky=W)
                       Label(y,text="Enter new Data",fg="black",bg="lightsteelblue",font=("Arial Rounded MT Bold",15)).grid(row=10,column=0,sticky=W)
                       global d
                       d=Entry(y,width=100,font=("Arial Rounded MT Bold",15),bg="white",fg="black")
                       d.grid(row=20,column=0,sticky=W)
                       Label(y,text="Enter the new password(to enhance the security of your account)",bg="lightsteelblue",fg="black",font=("Arial Rounded MT Bold",15)).grid(row=30,column=0,sticky=W)
                       global nam
                       nam=Entry(y,width=100,show="*",font=("Arial Rounded MT Bold",15),bg="white",fg="black")
                       nam.grid(row=40,column=0,sticky=W)

                       Button(y,text="Enter",command=been,bg="midnightblue",fg="white").grid(row=50,column=0,sticky=W)
                       #Label(y,text="Output",font=("Arial Rounded MT Bold",15),fg="black").grid(row=60,column=0,sticky=W)
                       global ow
                       ow=Text(y,width=100,bg="lightsteelblue",fg="black",font=("Arial Rounded MT Bold",15))
                       ow.grid(row=70,column=0,sticky=W)
                       y.mainloop()
                   
                   
                   flag=0
                   ini=Tk()
                   ini.title("DOCK:Data Management System")
                   ini.geometry("500x300")
                   ini.configure(background="lightsteelblue")
                  
                   Label(ini,text="                     HOME PAGE                                     ",bg="midnightblue",fg="white",font=("ALgerian",20)).grid(row=0,column=0,sticky=W)
                   Label(ini,text="Data",fg="black",bg="lightsteelblue",font=("Arial Rounded MT Bold",15)).grid(row=10,column=0,sticky=W)
                   Button(ini,text="Update",command=had,bg="midnightblue",fg="white",width=16).grid(row=20,column=0,sticky=W)
                   outa=Text(ini,width=80,bg="white",fg="black",font=("Arial Rounded MT Bold",15))
                   outa.grid(row=60,column=0,sticky=W)
                   qr=o.stringfun()
                   outa.insert(END,qr)
                   ini.mainloop()
               i+=1    
         if flag==1:
                w=Tk()
                w.title("DOCK:Data Management System")
                w.geometry("200x200")
                Label(w,text="SORRY\nTRY AGAIN",font=("Arial Rounded MT Bold",15),fg="white",bg="black").grid(row=0,column=0,sticky=W)
                w.mainloop()
         inpute.close()     
                     
                     
 #signing in........
    a=Tk()
    a.title("DOCK  :  Sign In Page  ")
    a.geometry("500x350")
    a.configure(background="lightsteelblue")
    Label(a,text="                     Access Your Dock                                  ",fg="white",bg="midnightblue",font=("ALgerian",20)).grid(row=0,column=0,sticky=W)
    Label(a,bg="lightsteelblue",text="Username",fg="black",font=("Arial Rounded MT Bold",13)).grid(row=10,column=0,sticky=W)
    Label(a,bg="lightsteelblue",text="Password",fg="black",font=("Arial Rounded MT Bold",13)).grid(row=40,column=0,sticky=W)
    global inp
    inp=Entry(a,width=21,bg="white",fg="black",font=("Arial Rounded MT Bold",17))
    inp.grid(row=30,column=0,sticky=W)
    global inpp
    inpp=Entry(a,width=24,bg="white",fg="black",font=("symbol",17),show="*")
    inpp.grid(row=50,column=0,sticky=W)

   # Label(a,width=40,bg="lightsteelblue",text="Output",fg="black",font=("Arial Rounded MT Bold",13)).grid(row=280,column=0,sticky=W)
    global out
    out=Text(a,width=30,height=1,bg="lightsteelblue",fg="black",font=("Arial Rounded MT Bold",17))
    out.grid(row=300,column=0,sticky =W)
    
    Button(a,text="Sign In",width=8,command=did,fg="white",bg="midnightblue",font=("Arial Rounded MT Bold",13)).grid(row=100,column=0,sticky=W)
    a.mainloop()


def function() : 
   r=Tk()
   r.title("DOCK:The Data Management System")
   r.geometry("600x300")
   #r.configure(background="red")
   r["bg"]="lightsteelblue" 
   Label(r,text="                                D O C K                                                                    ",bg="midnightblue",fg="white",font=("ALgerian",23)).grid(row=0,column=0,sticky=W)
   Label(r,text=" -----------------------------------------{   We Secure  }-------------------------------------------------------",fg="white",bg="lightsteelblue",font=("Rockwell",12)).grid(row=4,column=0,sticky=W)
   Label(r,text="                                                          Welcome to DOCK                                                                  ",fg="black",font=("Arial Rounded MT Bold",13),bg="white").grid(row=20,column=0,sticky=W)
   Button(r,text="                    Sign In                                           ",width=55,bg="forestgreen",fg="snow",command=do,font=("Arial Rounded MT Bold",15)).grid(row=30,column=0,sticky=W)
   Button(r,text="                    Sign Up                                           ",width=55,bg="forestgreen",fg="snow",command=does,font=("Arial Rounded MT Bold",15)).grid(row=35,column=0,sticky=W)
   #Label(r,text="                             Number of users                                                              ",fg="black",bg="white",font=("Century Gothic",12)).grid(row=40,column=0,sticky=W)
   Button(r,text="Number of users",width=15,bg="cornsilk",fg="midnightblue",font=("Arial Rounded MT Bold",12),command=have,).grid(row=70,column=0,sticky=W)
   #Label(r,text="                                                      About us                                                                              ",fg="black",bg="white",font=("Century Gothic",12)).grid(row=60,column=0,sticky=W)
   Button(r,text="  About Us",fg="midnightblue",font=("Arial Rounded MT Bold",12),command=shall,bg="cornsilk").grid(row=90,column=0,sticky=W)
   
   r.mainloop()
im=open("logged","ab")
if  os.stat("logged").st_size == 0:
     n=10
     with open('login.txt', 'w') as f:
           f.write(str(n))

im.close()
function()


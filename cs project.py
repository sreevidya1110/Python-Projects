from tkinter import*
import mysql.connector as sql
from tkinter import ttk
from functools import partial
import os.path
import csv
from PIL import Image, ImageTk

mycon=sql.connect(host="localhost",user="root",passwd="Suma1974",database="sreevidyaproj")
if mycon.is_connected():
    print("success")
c=mycon.cursor()

def register1_details():
    global firstname_nfo
    global lastname_info
    global phone_no_info
    
    firstname_info=firstname1.get()
    lastname_info=lastname1.get()
    
    phone_no_info=phone_no1.get()
    q7="update registration_details set firstname='%s' where UserId='%s'"%(firstname_info,UserID_info)
    c.execute(q7)
    q8="update registration_details set lastname='%s'where UserId='%s'"%(lastname_info,UserID_info)
    c.execute(q8)
    q9="update registration_details set phone_no= %s where UserId='%s'"%(phone_no_info,UserID_info)
    c.execute(q9)
    mycon.commit()
    

def editprofile():
    global screen102
    screen102=Toplevel(screen101)
    screen102.geometry("500x500")
    screen102.title("Edit Profile")
    global firstname1
    global lastname1
    global phone_no1
    firstname1=StringVar()
    lastname1=StringVar()
    phone_no1=IntVar()
    firstnamel1=Label(screen102,text="Firstname*",font=("Verdana"),fg="#212121")
    firstnamel1.place(x=70,y=70)
    firstname1_entry=Entry(screen102,textvariable=firstname1)
    firstname1_entry.place(x=70,y=110)
    lastnamel1=Label(screen102,text="Lastname*",font=("Verdana"),fg="#212121")
    lastnamel1.place(x=70,y=170)
    lastname1_entry=Entry(screen102,textvariable=lastname1)
    lastname1_entry.place(x=70,y=210)
    phone_nol=Label(screen102,text="Phone no*",font=("Verdana"),fg="#212121")
    phone_nol.place(x=70,y=270)
    phone_no_entry=Entry(screen102,textvariable=phone_no1)
    phone_no_entry.place(x=70,y=310)
    submit1_button=Button(screen102,text="Submit",font=("Verdana"), bg="#303F9F",fg="#FFFFFF",command=register1_details)
    submit1_button.place(x=70,y=370)

def profile():
    global screen101
    screen101=Toplevel(win)
    screen101.geometry("600x400")
    screen101.title("Profile")
        
    Labelname=Label(screen101,text="Name:",font=("Verdana",12,"bold"))
    Labelname.place(x=50,y=100)
    LabelUserID=Label(screen101,text="UserID:",font=("Verdana",12,"bold"))
    LabelUserID.place(x=50,y=150)
    Labelphoneno=Label(screen101,text="Phone no:",font=("Verdana",12,"bold"))
    Labelphoneno.place(x=50,y=200)
    q3="select UserID from registration_details where UserID='%s'"%UserID_info
    c.execute(q3)
    data10=c.fetchall()
    i=data10[0][0]
    q4="select firstname from registration_details where UserID ='%s'"%UserID_info
    c.execute(q4)
    data11=c.fetchall()
    j=data11[0][0]
    q5="select lastname from registration_details where UserID='%s'"%UserID_info
    c.execute(q5)
    data12=c.fetchall()
    k=data12[0][0]
    q6="select phone_no from registration_details where UserID='%s'"%UserID_info
    c.execute(q6)
    data13=c.fetchall()
    m=data13[0][0]
    n=j+" "+k
    Labelname1=Label(screen101,text=n,font=("Verdana",12,"bold"))
    Labelname1.place(x=200,y=100)
    LabelUserID1=Label(screen101,text=i,font=("Verdana",12,"bold"))
    LabelUserID1.place(x=200,y=150)
    Labelphoneno1=Label(screen101,text=m,font=("Verdana",12,"bold"))
    Labelphoneno1.place(x=200,y=200)
    editbutton=Button(screen101,text="Edit Profile",bg="#303F9F",fg="#FFFFFF",command=editprofile)
    editbutton.place(x=200,y=300)

def ok1():
    screen99.destroy()

def buynow1():
    if len(t)==0:
        def emptybuynow1():
    
            global screen99
            screen99=Toplevel(addtocartscreen)
            screen99.title("empty cart")
            screen99.geometry("250x150")
            labelle=Label(screen99,text="CART IS EMPTY!!",font=("Verdana",15))
            labelle.pack()
            button28=Button(screen99,text="OK",bg="#303F9F",fg="#FFFFFF",command=ok1)
            button28.place(x=125,y=80)
        emptybuynow1()
    else:
        s=0
        d=""
        for i in t:
            f=""
            for j in i[3]:
                if j=="₹" or j==" ":
                    continue
                else:
                    f=f+j
            s=s+int(f)
            q=i[1]
            d=d+q+" "+","
                
        global screen9
        screen9=Toplevel(addtocartscreen)
        screen9.title("Payment Details")
        screen9.geometry("600x600")
        
        global cardname
        global cardnumber
        global expirydate
        global cvv
        global shipmentadd
        cardname=StringVar()
        cardnumber=StringVar()
        expirydate=StringVar()
        cvv=StringVar()
        shipmentadd=StringVar()
        
        cardname_label=Label(screen9,text="Name on card:",font=("Verdana",12,"bold"))
        cardname_label.place(x=50,y=100)
        cardnumber_label=Label(screen9,text="Card number:",font=("Verdana",12,"bold"))
        cardnumber_label.place(x=50,y=150)
        expirydate_label=Label(screen9,text="Expiry date:",font=("Verdana",12,"bold"))
        expirydate_label.place(x=50,y=200)
        cvv_label=Label(screen9,text="cvv:",font=("Verdana",12,"bold"))
        cvv_label.place(x=50,y=250)
        shipmentadd_label=Label(screen9,text="Shipping Address:",font=("Verdana",12,"bold"))
        shipmentadd_label.place(x=50,y=400)
        cardname_entry=Entry(screen9,textvariable=cardname)
        cardname_entry.place(x=300,y=100)
        cardnumber_entry=Entry(screen9,textvariable=cardnumber)
        cardnumber_entry.place(x=300,y=150)
        expirydate_entry=Entry(screen9,textvariable=expirydate)
        expirydate_entry.place(x=300,y=200)
        cvv_entry=Entry(screen9,textvariable=cvv,show="*")
        cvv_entry.place(x=300,y=250)
        amount_label=Label(screen9,text="Amount:",font=("Verdana",12,"bold"))
        amount_label.place(x=50,y=300)
        watchname_label=Label(screen9,text="Watch Name:",font=("Verdana",12,"bold"))
        watchname_label.place(x=50,y=350)
        price_label=Label(screen9,text=s,font=(12))
        price_label.place(x=300,y=300)
        name_label=Label(screen9,text=d,font=(12))
        name_label.place(x=300,y=350)
        shipmentadd_entry=Entry(screen9,textvariable=shipmentadd,width=50)
        shipmentadd_entry.place(x=300,y=400)
        
        confirmpayment_button=Button(screen9,text="Confirm Payment",command=shoppingconfirm,bg="#303F9F",fg="#FFFFFF")
        confirmpayment_button.place(x=300,y=500)
        f=open(user_infofile,'r',encoding='utf-8', newline='')
        d=csv.reader(f)
        
        for i in d:
            if len(t)!=0:
                t.pop()
            else:
                break
        f.close()
        f=open(user_infofile,'w',encoding='utf-8', newline='')
        e=csv.writer(f)
        e.writerows(t)
        f.close()

def removefromcart(b):
    global t
    t=[]
    imagelabels[b].destroy()
    watchNames[b].destroy()
    watchDetails[b].destroy()
    watchPrices[b].destroy()
    removefromcartbutton[b].destroy()
    f=open(user_infofile,'r',encoding='utf-8', newline='')
    d=csv.reader(f)
    
    for i in q:
        if i==q[b]:
            continue
        else:
            t.append(i)
    f.close()
    f=open(user_infofile,'w',encoding='utf-8', newline='')
    u=csv.writer(f)
    u.writerows(t)
    f.close()

def viewcart(k):
        global addtocartscreen
        addtocartscreen=Toplevel(win)
        s=open(user_infofile,'r',encoding='utf-8')
        wrapper1=Frame(addtocartscreen,width=1300,height=250,bg="#bbbfca")
        mycanvas=Canvas(wrapper1,height=400,width=1300,bg="#bbbfca")
        mycanvas.pack(side=LEFT)
        yscrollbar=ttk.Scrollbar(wrapper1,orient="vertical",command=mycanvas.yview)
        yscrollbar.pack(side=LEFT,fill="y")

        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")))
        global myframe
        myframe=Frame(mycanvas,bg="#bbbfca")
        mycanvas.create_window((0,0),window=myframe,anchor="nw")
        wrapper1.grid()

        j=5
        b=0
        global t
        t=[]
        m=csv.reader(s)
        global imagelabels
        global watchNames
        global watchDetails
        global watchPrices
        global removefromcartbutton
        imagelabels=list(range(100))
        watchNames=list(range(100))
        watchDetails=list(range(100))
        watchPrices=list(range(100))
        removefromcartbutton=list(range(100))
        
        for o in m:
            t.append(o)
            imagef1=ImageTk.PhotoImage(Image.open(o[0]).resize((300,300),Image.BILINEAR))
            imagelabels[b]=Label(myframe,image=imagef1,height=300,width=300)
            imagelabels[b].image=imagef1
            imagelabels[b].grid(column=2,row=j)
            
            global detailsFrame
            detailsFrame = Frame(myframe)
            detailsFrame.grid(column=3, row=j)
            watchName1 = o[1]
            watchNames[b]=Label(detailsFrame,text=watchName1,font=("calibri",25, 'bold'), wraplength=450,justify=LEFT)
            watchNames[b].text = watchName1
            watchNames[b].grid(column=0,row=0)

            watchDetail1 =o[2]
            watchDetails[b]=Label(detailsFrame,text=watchDetail1,font=("Verdana",15),fg="#3F51B5", wraplength=450,justify=LEFT)
            watchDetails[b].detail = watchDetail1
            watchDetails[b].grid(column=0,row=1)

            watchPrice1 =str(o[3])
            watchPrices[b]=Label(detailsFrame,text=watchPrice1,font=("Verdana",15), wraplength=350,justify=LEFT)
            watchPrices[b].price = watchPrice1
            watchPrices[b].grid(column=0,row=2)

            removefromcarttext="Remove from cart"
            removefromcartbutton[b]=Button(myframe,text=removefromcarttext,font=("AR BERKLEY",20),bg="#303F9F",fg="#FFFFFF",relief=RAISED,command=partial(removefromcart,b))
            removefromcartbutton[b].button=removefromcarttext
            removefromcartbutton[b].grid(column=7,row=j)

            j=j+5
            b=b+1
            
        s.close()
        global q
        global length
        q=t
        length=len(q)
        buynow1button=Button(addtocartscreen,text="Buy now",font=("AR BERKLEY",20),bg="#303F9F",fg="#FFFFFF",relief=RAISED,command=buynow1)
        buynow1button.place(x=600,y=500)
        addtocartscreen.geometry("1000x2500")
        addtocartscreen.configure(bg="#bbbfca")
        addtocartscreen.title("Watches")
        addtocartscreen.state("zoomed")
        addtocartscreen.mainloop()   

def addtocart(k):
    if os.path.isfile(user_infofile):
        t=[]
        f=open(user_infofile,'a',encoding='utf-8', newline='')
        w=csv.writer(f)
        l=[watchImageslist[k],watchNameslist[k],watchDetailslist[k],watchPriceslist[k]]
        t.append(l)
        w.writerows(t)
        f.close()
    else:
        t=[]
        f=open(user_infofile,'w',encoding='utf-8', newline='')
        w=csv.writer(f)
        l=[watchImageslist[k],watchNameslist[k],watchDetailslist[k],watchPriceslist[k]]
        t.append(l)
        w.writerows(t)
        f.close()
     
    
def digital():
    global digitalwin
    digitalwin=Toplevel(win)
    
    global wrapper2
    wrapper2=Frame(digitalwin,width=1300,height=250,bg="#bbbfca")
    wrapper2.grid()

    menu1=Button(wrapper2,text="Womens Watches",font=("AR BERKLEY",15,"bold"),bg="#303F9F",fg="#FFFFFF",bd=4,relief=RAISED,activeforeground="#FF5722",command=women)
    menu1.grid(column=0,row=0)
    menu2=Button(wrapper2,text="Men's Watches",font=("AR BERKLEY",15,"bold"),relief=RAISED,bg="#303F9F",fg="#FFFFFF",bd=4,activeforeground="#FF5722",command=men)
    menu2.grid(column=1,row=0)

    menu3=Button(wrapper2,text="Luxury Watches",font=("AR BERKLEY",15,"bold"),relief=RAISED,bg="#303F9F",fg="#FFFFFF",bd=4,activeforeground="#FF5722",command=mainscreen)
    menu3.grid(column=2,row=0)

    wrapper1=Frame(digitalwin,height=400,width=1400,bg="#bbbfca")

    mycanvas=Canvas(wrapper1,height=400,width=1300,bg="#bbbfca")
    mycanvas.pack(side=LEFT)
    yscrollbar=ttk.Scrollbar(wrapper1,orient="vertical",command=mycanvas.yview)
    yscrollbar.pack(side=LEFT,fill="y")

    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")))

    myframe=Frame(mycanvas,bg="#bbbfca")
    mycanvas.create_window((0,0),window=myframe,anchor="nw")
    wrapper1.grid()
    image1=ImageTk.PhotoImage(Image.open("project images/digitalwatches/open screen-1.jpg").resize((600,200),Image.BILINEAR))
    Label(wrapper2,image=image1,width=600,height=200).grid(column=0,row=2,columnspan=3)
    query="select image_path,watch_name,price,description from digital"
    c.execute(query)
    data1=c.fetchall()
    j=4
    k=0
    global watchPriceslist
    global watchNameslist
    global watchDetailslist
    global watchImageslist
    
    imagelabels=list(range(len(data1)))
    watchNames=list(range(len(data1)))
    watchDetails=list(range(len(data1)))
    watchPrices=list(range(len(data1)))
    buynowbutton=list(range(len(data1)))
    addtocartbutton=list(range(len(data1)))
    watchPriceslist=[]
    watchNameslist=[]
    watchDetailslist=[]
    watchImageslist=[]

    start = "\033[1m"
    end = "\033[0;0m"
    for  i in data1:
        global v
        v=i[0]
        global watchName
        global watchDetail
        global watchPrice
        
        imagef=ImageTk.PhotoImage(Image.open(i[0]).resize((300,300),Image.BILINEAR))
        imagelabels[k]=Label(myframe,image=imagef,height=300,width=300)
        imagelabels[k].image=imagef
        watchImageslist.append(i[0])
        imagelabels[k].grid(column=2,row=j)

        detailsFrame = Frame(myframe)
        detailsFrame.grid(column=3, row=j)
        watchName = i[1]
        watchNames[k]=Label(detailsFrame,text=watchName,font=("calibri",25, 'bold'), wraplength=350,justify=LEFT)
        watchNames[k].text = watchName
        watchNameslist.append(watchName)
        watchNames[k].grid(column=0,row=0)

        watchDetail =i[3]
        watchDetails[k]=Label(detailsFrame,text=watchDetail,font=("Verdana",15),fg="#3F51B5", wraplength=450,justify=LEFT)
        watchDetails[k].detail = watchDetail
        watchDetailslist.append(watchDetail)
        watchDetails[k].grid(column=0,row=1)

        watchPrice ="₹"+" " +str(i[2])
        watchPrices[k]=Label(detailsFrame,text=watchPrice,font=("Verdana",15), wraplength=350,justify=LEFT)
        watchPrices[k].price = watchPrice
        watchPriceslist.append(watchPrice)
        watchPrices[k].grid(column=0,row=2)
        buynowtext="Buy now"
        addtocarttext="Add to cart"

        buynowbutton[k]=Button(myframe,text=buynowtext,font=("AR BERKLEY",20),bg="#303F9F",fg="#FFFFFF",relief=RAISED,command= partial(buynow,k))
        buynowbutton[k].button=buynowtext
        buynowbutton[k].grid(column=7,row=j)

        addtocartbutton[k]=Button(myframe,text=addtocarttext,font=("AR BERKLEY",20),bg="#FFFFFF",fg="#303F9F",relief=RAISED,command=partial(addtocart,k))
        addtocartbutton[k].button=addtocarttext
        addtocartbutton[k].grid(column=11,row=j)
        j=j+1
        k=k+1
        
    global user_infofile
    user_infofile=UserID_info+'.txt'
    global g
    g=[]
    addtocartbutton1=Button(wrapper2,text="Cart",font=("AR BERKLEY",20),bg="#303F9F",fg="#FFFFFF",relief=RAISED,command=partial(viewcart,k))
    addtocartbutton1.grid(column=3,row=0)
       
    digitalwin.geometry("1000x2500")
    digitalwin.configure(bg="#bbbfca")
    digitalwin.title("Watches")
    digitalwin.state("zoomed")
    digitalwin.mainloop()        
   
    
def men():
    global menwin
    menwin=Toplevel(win)
    
    global wrapper2
    wrapper2=Frame(menwin,width=1400,height=250,bg="#bbbfca")
    wrapper2.grid()

    menu1=Button(wrapper2,text="Womens Watches",font=("AR BERKLEY",15,"bold"),bg="#303F9F",fg="#FFFFFF",bd=4,relief=RAISED,activeforeground="#FF5722",command=women)
    menu1.grid(column=0,row=0)
    menu2=Button(wrapper2,text="Luxury Watches",font=("AR BERKLEY",15,"bold"),relief=RAISED,bg="#303F9F",fg="#FFFFFF",bd=4,activeforeground="#FF5722",command=mainscreen)
    menu2.grid(column=1,row=0)

    menu3=Button(wrapper2,text="Digital Watches",font=("AR BERKLEY",15,"bold"),relief=RAISED,bg="#303F9F",fg="#FFFFFF",bd=4,activeforeground="#FF5722",command=digital)
    menu3.grid(column=2,row=0)

    wrapper1=Frame(menwin,height=400,width=1300,bg="#bbbfca")

    mycanvas=Canvas(wrapper1,height=400,width=1300,bg="#bbbfca")
    mycanvas.pack(side=LEFT)
    yscrollbar=ttk.Scrollbar(wrapper1,orient="vertical",command=mycanvas.yview)
    yscrollbar.pack(side=LEFT,fill="y")
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")))

    myframe=Frame(mycanvas,bg="#bbbfca")
    mycanvas.create_window((0,0),window=myframe,anchor="nw")
    wrapper1.grid()
    image1=ImageTk.PhotoImage(Image.open("project images/men's watches final/open screen 1.jpg").resize((600,200),Image.BILINEAR))
    Label(wrapper2,image=image1,width=600,height=200).grid(column=0,row=2,columnspan=3)
    query="select image_path,watch_name,price,description from men"
    c.execute(query)
    data1=c.fetchall()
    j=4
    k=0
    global watchPriceslist
    global watchNameslist
    global watchDetailslist
    global watchImageslist
    
    imagelabels=list(range(len(data1)))
    watchNames=list(range(len(data1)))
    watchDetails=list(range(len(data1)))
    watchPrices=list(range(len(data1)))
    buynowbutton=list(range(len(data1)))
    addtocartbutton=list(range(len(data1)))
    watchPriceslist=[]
    watchNameslist=[]
    watchDetailslist=[]
    watchImageslist=[]

    start = "\033[1m"
    end = "\033[0;0m"
    for  i in data1:
        
        global v
        v=i[0]
        global watchName
        global watchDetail
        global watchPrice
        
        imagef=ImageTk.PhotoImage(Image.open(i[0]).resize((300,300),Image.BILINEAR))
        imagelabels[k]=Label(myframe,image=imagef,height=300,width=300)
        imagelabels[k].image=imagef
        watchImageslist.append(i[0])
        imagelabels[k].grid(column=2,row=j)

        detailsFrame = Frame(myframe)
        detailsFrame.grid(column=3, row=j)
        watchName = i[1]
        watchNames[k]=Label(detailsFrame,text=watchName,font=("calibri",25, 'bold'), wraplength=350,justify=LEFT)
        watchNames[k].text = watchName
        watchNameslist.append(watchName)
        watchNames[k].grid(column=0,row=0)

        watchDetail =i[3]
        watchDetails[k]=Label(detailsFrame,text=watchDetail,font=("Verdana",15),fg="#3F51B5", wraplength=450,justify=LEFT)
        watchDetails[k].detail = watchDetail
        watchDetailslist.append(watchDetail)
        watchDetails[k].grid(column=0,row=1)

        watchPrice ="₹"+" " +str(i[2])
        watchPrices[k]=Label(detailsFrame,text=watchPrice,font=("Verdana",15), wraplength=350,justify=LEFT)
        watchPrices[k].price = watchPrice
        watchPriceslist.append(watchPrice)
        watchPrices[k].grid(column=0,row=2)
        buynowtext="Buy now"
        addtocarttext="Add to cart"

        buynowbutton[k]=Button(myframe,text=buynowtext,font=("AR BERKLEY",20),bg="#303F9F",fg="#FFFFFF",relief=RAISED,command= partial(buynow,k))
        buynowbutton[k].button=buynowtext
        buynowbutton[k].grid(column=7,row=j)

        addtocartbutton[k]=Button(myframe,text=addtocarttext,font=("AR BERKLEY",20),bg="#FFFFFF",fg="#303F9F",relief=RAISED,command=partial(addtocart,k))
        addtocartbutton[k].button=addtocarttext
        addtocartbutton[k].grid(column=11,row=j)
        
        j=j+1
        k=k+1
        
    global user_infofile
    user_infofile=UserID_info+'.txt'
    global g
    g=[]
    addtocartbutton1=Button(wrapper2,text="Cart",font=("AR BERKLEY",20),bg="#303F9F",fg="#FFFFFF",relief=RAISED,command=partial(viewcart,k))
    addtocartbutton1.grid(column=3,row=0)
          
    menwin.geometry("1000x2500")
    menwin.configure(bg="#bbbfca")
    menwin.title("Watches")
    menwin.state("zoomed")
    menwin.mainloop()        
   
    
def women():
    global womenwin
    womenwin=Toplevel(win)
    
    global wrapper2
    wrapper2=Frame(womenwin,width=1300,height=250,bg="#bbbfca")
    wrapper2.grid()

    menu1=Button(wrapper2,text="Luxury Watches",font=("AR BERKLEY",15,"bold"),bg="#303F9F",fg="#FFFFFF",bd=4,relief=RAISED,activeforeground="#FF5722",command=mainscreen)
    menu1.grid(column=0,row=0)
    menu2=Button(wrapper2,text="Men's Watches",font=("AR BERKLEY",15,"bold"),relief=RAISED,bg="#303F9F",fg="#FFFFFF",bd=4,activeforeground="#FF5722",command=men)
    menu2.grid(column=1,row=0)
    menu3=Button(wrapper2,text="Digital Watches",font=("AR BERKLEY",15,"bold"),relief=RAISED,bg="#303F9F",fg="#FFFFFF",bd=4,activeforeground="#FF5722",command=digital)
    menu3.grid(column=2,row=0)

    wrapper1=Frame(womenwin,height=400,width=1300,bg="#bbbfca")

    mycanvas=Canvas(wrapper1,height=400,width=1300,bg="#bbbfca")
    mycanvas.pack(side=LEFT)
    yscrollbar=ttk.Scrollbar(wrapper1,orient="vertical",command=mycanvas.yview)
    yscrollbar.pack(side=LEFT,fill="y")

    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")))

    myframe=Frame(mycanvas,bg="#bbbfca")
    mycanvas.create_window((0,0),window=myframe,anchor="nw")
    wrapper1.grid()
    image1=ImageTk.PhotoImage(Image.open("project images/womenwatches/open screen-2.jpg").resize((600,200),Image.BILINEAR))
    Label(wrapper2,image=image1,width=600,height=200).grid(column=0,row=2,columnspan=3)
    query="select image_path,watch_name,price,description from women"
    c.execute(query)
    data1=c.fetchall()
    j=4
    k=0
    global watchPriceslist
    global watchNameslist
    global watchDetailslist
    global watchImageslist
    
    imagelabels=list(range(len(data1)))
    watchNames=list(range(len(data1)))
    watchDetails=list(range(len(data1)))
    watchPrices=list(range(len(data1)))
    buynowbutton=list(range(len(data1)))
    addtocartbutton=list(range(len(data1)))
    watchPriceslist=[]
    watchNameslist=[]
    watchDetailslist=[]
    watchImageslist=[]
    start = "\033[1m"
    end = "\033[0;0m"
    for  i in data1:
        global v
        v=i[0]
        global watchName
        global watchDetail
        global watchPrice
        
        imagef=ImageTk.PhotoImage(Image.open(i[0]).resize((300,300),Image.BILINEAR))
        imagelabels[k]=Label(myframe,image=imagef,height=300,width=300)
        imagelabels[k].image=imagef
        watchImageslist.append(i[0])
        imagelabels[k].grid(column=2,row=j)

        detailsFrame = Frame(myframe)
        detailsFrame.grid(column=3, row=j)
        watchName = i[1]
        watchNames[k]=Label(detailsFrame,text=watchName,font=("calibri",25, 'bold'), wraplength=350,justify=LEFT)
        watchNames[k].text = watchName
        watchNameslist.append(watchName)
        watchNames[k].grid(column=0,row=0)

        watchDetail =i[3]
        watchDetails[k]=Label(detailsFrame,text=watchDetail,font=("Verdana",15),fg="#3F51B5", wraplength=450,justify=LEFT)
        watchDetails[k].detail = watchDetail
        watchDetailslist.append(watchDetail)
        watchDetails[k].grid(column=0,row=1)

        watchPrice ="₹"+" " +str(i[2])
        watchPrices[k]=Label(detailsFrame,text=watchPrice,font=("Verdana",15), wraplength=350,justify=LEFT)
        watchPrices[k].price = watchPrice
        watchPriceslist.append(watchPrice)
        watchPrices[k].grid(column=0,row=2)
        buynowtext="Buy now"
        addtocarttext="Add to cart"

        buynowbutton[k]=Button(myframe,text=buynowtext,font=("AR BERKLEY",20),bg="#303F9F",fg="#FFFFFF",relief=RAISED,command= partial(buynow,k))
        buynowbutton[k].button=buynowtext
        buynowbutton[k].grid(column=7,row=j)

        addtocartbutton[k]=Button(myframe,text=addtocarttext,font=("AR BERKLEY",20),bg="#FFFFFF",fg="#303F9F",relief=RAISED,command=partial(addtocart,k))
        addtocartbutton[k].button=addtocarttext
        addtocartbutton[k].grid(column=11,row=j)
        j=j+1
        k=k+1
        
    global user_infofile
    user_infofile=UserID_info+'.txt'
    global g
    g=[]
    addtocartbutton1=Button(wrapper2,text="Cart",font=("AR BERKLEY",20),bg="#303F9F",fg="#FFFFFF",relief=RAISED,command=partial(viewcart,k))
    addtocartbutton1.grid(column=3,row=0)
          
    womenwin.geometry("1000x2500")
    womenwin.configure(bg="#bbbfca")
    womenwin.title("Watches")
    womenwin.state("zoomed")
    womenwin.mainloop()        
 
def delete10():
    screen10.destroy()
def shoppingconfirm():
    global screen10
    cardnameinfo=cardname.get()
    cardnumberinfo=cardnumber.get()
    expirydateinfo=expirydate.get()
    cvvinfo=cvv.get()
    shipmentaddinfo=shipmentadd.get()
    screen10=Toplevel(screen9)
    screen10.title("Payment")
    screen10.geometry("600x300")
    if len(cardnameinfo)==0 or len(cardnumberinfo)==0 or len(expirydateinfo)==0 or len(cvvinfo)==0 or len(shipmentaddinfo)==0:
        label2=Label(screen10,text="Please enter all fields to proceed to payment",font=("Verdana",12,"bold"))
        label2.place(x=50,y=30)
        ok_button=Button(screen10,text="OK",bg="#303F9F",fg="#FFFFFF",command=delete10)
        ok_button.place(x=150,y=100)
    else:
        confirm_label1=Label(screen10,text='''Payment Successful!!
                                          Your watch will be shipped to your address within the next 5 business days
                                          Thanks for shopping with HAVI!!!''',font=("Verdana",15,"bold"),fg="green")
        confirm_label1.place(x=0,y=50)
        screen10.state("zoomed")
        #timespan()
        
def buynow(k):
    global screen9
    screen9=Toplevel(win)
    screen9.title("Payment Details")
    screen9.geometry("600x600")
    
    global cardname
    global cardnumber
    global expirydate
    global cvv
    global shipmentadd
    cardname=StringVar()
    cardnumber=StringVar()
    expirydate=StringVar()
    cvv=StringVar()
    shipmentadd=StringVar()
    print(watchPriceslist[k])
    cardname_label=Label(screen9,text="Name on card:",font=("Verdana",12,"bold"))
    cardname_label.place(x=50,y=100)
    cardnumber_label=Label(screen9,text="Card number:",font=("Verdana",12,"bold"))
    cardnumber_label.place(x=50,y=150)
    expirydate_label=Label(screen9,text="Expiry date:",font=("Verdana",12,"bold"))
    expirydate_label.place(x=50,y=200)
    cvv_label=Label(screen9,text="cvv:",font=("Verdana",12,"bold"))
    cvv_label.place(x=50,y=250)
    shipmentadd_label=Label(screen9,text="Shipping Address:",font=("Verdana",12,"bold"))
    shipmentadd_label.place(x=50,y=400)
    cardname_entry=Entry(screen9,textvariable=cardname)
    cardname_entry.place(x=300,y=100)
    cardnumber_entry=Entry(screen9,textvariable=cardnumber)
    cardnumber_entry.place(x=300,y=150)
    expirydate_entry=Entry(screen9,textvariable=expirydate)
    expirydate_entry.place(x=300,y=200)
    cvv_entry=Entry(screen9,textvariable=cvv,show="*")
    cvv_entry.place(x=300,y=250)
    amount_label=Label(screen9,text="Amount:",font=("Verdana",12,"bold"))
    amount_label.place(x=50,y=300)
    watchname_label=Label(screen9,text="Watch Name:",font=("Verdana",12,"bold"))
    watchname_label.place(x=50,y=350)
    price_label=Label(screen9,text=watchPriceslist[k],font=(12))
    price_label.place(x=300,y=300)
    name_label=Label(screen9,text=watchNameslist[k],font=(12))
    name_label.place(x=300,y=350)
    shipmentadd_entry=Entry(screen9,textvariable=shipmentadd,width=50)
    shipmentadd_entry.place(x=300,y=400)
    confirmpayment_button=Button(screen9,text="Confirm Payment",command=shoppingconfirm,bg="#303F9F",fg="#FFFFFF")
    confirmpayment_button.place(x=300,y=500)

    
def delete6():
    screen6.destroy()
def delete7():
    screen7.destroy()
def delete8():
    screen8.destroy()
def useridexists():
    global screen6
    screen6=Toplevel(screen1)
    screen6.geometry("250x150")
    screen6.title("UserID  exists")
    duplicate_UserID=Label(screen6,text="UserID already exists",font=("calibri",12))
    duplicate_UserID.pack()
    empty=Label(screen6,text="")
    empty.pack()
    user_button=Button(screen6,text="OK",font=("calibri",13),command=delete6)
    user_button.pack()
def passwordexists():
    global screen7
    screen7=Toplevel(screen1)
    screen7.geometry("250x150")
    screen7.title("Password exists")
    duplicate_Password=Label(screen7,text="Password already exists please create a new one!!",font=("calibri",12))
    duplicate_Password.pack()
    empty=Label(screen7,text="")
    empty.pack()
    password_button=Button(screen7,text="OK",font=("calibri",13),command=delete7)
    password_button.pack()
def greaterlength():
    global screen8
    screen8=Toplevel(screen1)
    screen8.geometry("250x150")
    screen8.title("Invalid Phone no")
    greaterlength_label=Label(screen8,text="Invalid Phone no!!!",font=("calibri",9))
    greaterlength_label.pack()
    empty=Label(screen8,text="")
    empty.pack()
    greaterlength_button=Button(screen8,text="OK",font=("calibri",13),command=delete8)
    greaterlength_button.pack()
    
def delete5():
    screen1.destroy()
    mainscreen()

def delete4():
    screen6.destroy()

def delete3():
    screen5.destroy()

def delete2():
    screen4.destroy()

def mainscreen():
    #screen2.destroy()
    global win
    win=Toplevel(screen)
    
    global wrapper2
    wrapper2=Frame(win,width=1300,height=250,bg="#bbbfca")
    wrapper2.grid()

    menu1=Button(wrapper2,text="Womens Watches",font=("AR BERKLEY",15,"bold"),bg="#303F9F",fg="#FFFFFF",bd=4,relief=RAISED,activeforeground="#FF5722",command=women)
    menu1.grid(column=0,row=0)
    menu2=Button(wrapper2,text="Men's Watches",font=("AR BERKLEY",15,"bold"),relief=RAISED,bg="#303F9F",fg="#FFFFFF",bd=4,activeforeground="#FF5722",command=men)
    menu2.grid(column=1,row=0)
    menu3=Button(wrapper2,text="Digital Watches",font=("AR BERKLEY",15,"bold"),relief=RAISED,bg="#303F9F",fg="#FFFFFF",bd=4,activeforeground="#FF5722",command=digital)
    menu3.grid(column=2,row=0)

    profile_button=Button(wrapper2,text="Profile",font=("AR BERKLEY",15,"bold"),relief=RAISED,bg="#303F9F",fg="#FFFFFF",bd=4,activeforeground="#FF5722",command=profile)
    profile_button.grid(column=3,row=0)

    wrapper1=Frame(win,height=400,width=1300,bg="#bbbfca")

    mycanvas=Canvas(wrapper1,height=400,width=1300,bg="#bbbfca")
    mycanvas.pack(side=LEFT)
    yscrollbar=ttk.Scrollbar(wrapper1,orient="vertical",command=mycanvas.yview)
    yscrollbar.pack(side=LEFT,fill="y")

    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")))

    myframe=Frame(mycanvas,bg="#bbbfca")
    mycanvas.create_window((0,0),window=myframe,anchor="nw")
    wrapper1.grid()
    image1=ImageTk.PhotoImage(Image.open("project images/open screen-1.jpg").resize((900,200),Image.BILINEAR))
    Label(wrapper2,image=image1,width=900,height=200).grid(column=0,row=2,columnspan=3)
    query="select image_path,watch_name,price,description from general"
    c.execute(query)
    data1=c.fetchall()
    j=4
    k=0
    global watchPriceslist
    global watchNameslist
    global watchDetailslist
    global watchImageslist
    
    imagelabels=list(range(len(data1)))
    watchNames=list(range(len(data1)))
    watchDetails=list(range(len(data1)))
    watchPrices=list(range(len(data1)))
    buynowbutton=list(range(len(data1)))
    addtocartbutton=list(range(len(data1)))
    watchPriceslist=[]
    watchNameslist=[]
    watchDetailslist=[]
    watchImageslist=[]
    start = "\033[1m"
    end = "\033[0;0m"
    for i in data1:
        global v
        v=i[0]
        global watchName
        global watchDetail
        global watchPrice
        
        imagef=ImageTk.PhotoImage(Image.open(i[0]).resize((300,300),Image.BILINEAR))
        imagelabels[k]=Label(myframe,image=imagef,height=300,width=300)
        imagelabels[k].image=imagef
        watchImageslist.append(i[0])
        imagelabels[k].grid(column=2,row=j)

        detailsFrame = Frame(myframe)
        detailsFrame.grid(column=3, row=j)
        watchName = i[1]
        watchNames[k]=Label(detailsFrame,text=watchName,font=("calibri",25, 'bold'), wraplength=350,justify=LEFT)
        watchNames[k].text = watchName
        watchNameslist.append(watchName)
        watchNames[k].grid(column=0,row=0)

        watchDetail =i[3]
        
        watchDetails[k]=Label(detailsFrame,text=watchDetail,font=("Verdana",15),fg="#3F51B5", wraplength=450,justify=LEFT)
        watchDetails[k].detail = watchDetail
        watchDetailslist.append(watchDetail)
        watchDetails[k].grid(column=0,row=1)

        watchPrice ="₹"+" " +str(i[2])
        watchPrices[k]=Label(detailsFrame,text=watchPrice,font=("Verdana",15), wraplength=350,justify=LEFT)
        watchPrices[k].price = watchPrice
        watchPriceslist.append(watchPrice)
        watchPrices[k].grid(column=0,row=2)
        buynowtext="Buy now"
        addtocarttext="Add to cart"

        buynowbutton[k]=Button(myframe,text=buynowtext,font=("AR BERKLEY",20),bg="#303F9F",fg="#FFFFFF",relief=RAISED,command= partial(buynow,k))
        buynowbutton[k].button=buynowtext
        buynowbutton[k].grid(column=7,row=j)

        addtocartbutton[k]=Button(myframe,text=addtocarttext,font=("AR BERKLEY",20),bg="#FFFFFF",fg="#303F9F",relief=RAISED,command=partial(addtocart,k))
        addtocartbutton[k].button=addtocarttext
        addtocartbutton[k].grid(column=11,row=j)
        
        j=j+1
        k=k+1
        
    global user_infofile
    user_infofile=UserID_info+'.txt'
    global g
    g=[]
    addtocartbutton1=Button(wrapper2,text="Cart",font=("AR BERKLEY",20),bg="#303F9F",fg="#FFFFFF",relief=RAISED,command=partial(viewcart,k))
    addtocartbutton1.grid(column=4,row=0)
          
    win.geometry("1000x2500")
    win.configure(bg="#bbbfca")
    win.title("Watches")
    win.state("zoomed")
    win.mainloop()        
   
def password_not():
    global screen4
    screen4=Toplevel(screen2)
    screen4.geometry("250x150")
    screen4.title("Password not found")
    password_not1=Label(screen4,text="INCORRECT PASSWORD!!",font=("calibri"))
    password_not1.pack()
    empty=Label(screen4,text="")
    empty.pack()
    password_not1_button=Button(screen4,text="OK",font=("calibri",13),command=delete2)
    password_not1_button.pack()

def user_not():
    global screen5
    screen5=Toplevel(screen2)
    screen5.geometry("250x150")
    screen5.title("Username not found")
    user_not1=Label(screen5,text="UserId Not Found!!",font=("calibri",13))
    user_not1.pack()
    empty=Label(screen5,text="")
    empty.pack()
    user_not1_button=Button(screen5,text="OK",font=("calibri",13),command=delete3)
    user_not1_button.pack()

def login_success():
    
    global UserID_info
    UserID2_info=UserID1.get()
    UserID_info=UserID1.get()
    password2_info=password1.get()
    q1="select UserID from registration_details where UserID='%s' ;"%(UserID2_info)
    c.execute(q1)
    data1=c.fetchall()
    q2="select password from registration_details where UserID='%s'and password='%s';"%(UserID2_info,password2_info)
    c.execute(q2)
    data2=c.fetchall()
    if len(data1)==1 and len(data2)==1:
        mainscreen()
    elif len(data1)==1 and len(data2)==0:
        password_not()
    elif len(data1)==0 and len(data2)==0:
        user_not()
   
def register_details():
    global UserID_info
    global firstname_nfo
    global lastname_info
    global phone_no_info
    
    firstname_info=firstname.get()
    lastname_info=lastname.get()
    UserID_info=UserID.get()
    phone_no_info=phone_no.get()
    password_info=password.get()
    l=[firstname_info,lastname_info,UserID_info,phone_no_info,password_info]
    t=tuple(l)
    q3="select UserID from registration_details where UserID='%s'"%UserID_info
    c.execute(q3)
    data3=c.fetchall()
    q4="select password from registration_details where password='%s'"%password_info
    c.execute(q4)
    data4=c.fetchall()
    
    if len(data3)>=1:
        useridexists()
    elif len(data4)>=1:
        passwordexists()
    else:
        if len(str(phone_no_info))!=10:
            greaterlength()
        else:
            q="insert into registration_details values('%s','%s','%s',%s,'%s')"%t
            c.execute(q)
            mycon.commit()
            
            acknowledgement=Label(screen1,text="REGISTRATION SUCCESSFUL!!!")
        
            acknowledgement.place(x=120,y=540)
            acknowledgement_button=Button(screen1,text="OK",font=("calibri",13),command=delete5)
            acknowledgement_button.place(x=70,y=610)
    
def register_run():
    
    global screen1
    screen1=Toplevel(screen)
    
    screen1.geometry("500x700")
    screen1.title("Signup")
    
    heading1=Label(screen1,text="PLEASE FILL THE DETAILS BELOW",font=("calibri"))
    heading1.place(x=100,y=30)
    
    global firstname
    global lastname
    global phone_no
    global password
    global UserID
    firstname=StringVar()
    lastname=StringVar()
    phone_no=IntVar()
    password=StringVar()
    UserID=StringVar()
    firstnamel=Label(screen1,text="Firstname*",font=("Verdana"),fg="#212121")
    firstnamel.place(x=70,y=70)
    firstname_entry=Entry(screen1,textvariable=firstname)
    firstname_entry.place(x=70,y=110)
    lastnamel=Label(screen1,text="Lastname*",font=("Verdana"),fg="#212121")
    lastnamel.place(x=70,y=170)
    lastname_entry=Entry(screen1,textvariable=lastname)
    lastname_entry.place(x=70,y=210)
    UserID1=Label(screen1,text="UserID*",font=("Verdana"),fg="#212121")
    UserID1.place(x=70,y=270)
    UserID_entry=Entry(screen1,textvariable=UserID)
    UserID_entry.place(x=70,y=310)
    phone_nol=Label(screen1,text="Phone no*",font=("Verdana"),fg="#212121")
    phone_nol.place(x=70,y=370)
    phone_no_entry=Entry(screen1,textvariable=phone_no)
    phone_no_entry.place(x=70,y=410)
    passwordl=Label(screen1,text="Password*",font=("Verdana"),fg="#212121")
    passwordl.place(x=70,y=470)
    password_entry=Entry(screen1,textvariable=password,show="*")
    password_entry.place(x=70,y=510)
    submit_button=Button(screen1,text="Submit",font=("Verdana"), bg="#303F9F",fg="#FFFFFF",command=register_details)
    submit_button.place(x=70,y=570)
    
    
def login_run():
    global screen2
    screen2=Toplevel(screen)
    screen2.geometry("500x300")
    screen2.title("Signin")
    
    global UserID1
    global password1
    UserID1=StringVar()
    password1=StringVar()
    UserID2=Label(screen2,text="UserID*",font=("Verdana"),fg="#212121")
    UserID2.place(x=70,y=30)
    UserID2_entry=Entry(screen2,textvariable=UserID1)
    UserID2_entry.place(x=70,y=70)
    password2=Label(screen2,text="Password*",font=("Verdana"),fg="#212121")
    password2.place(x=70,y=140)
    password2_entry=Entry(screen2,textvariable=password1,show="*")
    password2_entry.place(x=70,y=180)
    login_button=Button(screen2,text="Signin",font=("calibri"),bg="#303F9F",fg="#FFFFFF", command=login_success)
    login_button.place(x=70,y=220)
    global UserID_info
    UserID_info=UserID1.get()
    
    
    
screen=Tk()
screen.geometry("700x500")

screen.title("signup or signin page")
login_image=ImageTk.PhotoImage(file="project images/login screen.jpg")
background_label=Label(image=login_image)
background_label.pack()
heading=Label(text="HAVI",font=("AR BERKLEY",30,"bold"))
heading.place(x=550,y=200)
watchintro_label=Label(text="-The world of watches",font=("AR BERKLEY",25,"bold"))
watchintro_label.place(x=500,y=290)
signinlabel=Label(text="Already have an account?",font=("AR BLANCA",13,"bold"))
signinlabel.place(x=300,y=360)
                  
register_button=Button(text="Sign up",font=("times new roman",15,"bold"),fg="#303F9F",command=register_run)
register_button.place(x=1200,y=100)

login_button=Button(text="Sign in",font=("times new roman",15,"bold"),fg="#303F9F",command=login_run)
login_button.place(x=510,y=360)
screen.state("zoomed")










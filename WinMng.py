from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, Text
import os
import pickle as pk
import csv
from tkinter import messagebox
from Swiss import Swiss
class WinMng:
    window=0
    widgets=[]
    widgets1=[]
    swiss=Swiss
    rounds=0
    id=0
    listrnd=9
    rndNO=0
    tournName=''

    def init(window,widgets):
        WinMng.window=window
        WinMng.widgets=widgets
    def getId():
        fh=open('MngFiles\\id.txt','r')
        x=fh.read(1)
        fh.close()
        fh=open('MngFiles\\id.txt','w')
        fh.write(str(int(x)+1))

        return x

    def importing():
        id=WinMng.getId()

        print('importing')
        print(WinMng.widgets1[1])
        entry=WinMng.widgets1[1].get()
        print(entry)

        

        path='TournamentFIles\\{}'.format(entry)
        print(path)
        os.makedirs(path)
        filename=filedialog.askopenfilename(initialdir="/",title="Select File")
        filetypes=(("executables","*.txt"))
        
        
        fh=open(filename,'r')
        path2='TournamentFIles\\{}\\importedPlayers.txt'.format(entry)
        
        fhw=open(path2,'w')
        x=fh.readlines()
        print(x,'debug1')
        fhw.writelines(x)
        fh.close()
        fhw.close()
        tournDetails=[str(id),entry,path]
        path='MngFiles\\TournData.txt' 
        fh=open(path,'a')
        data='{},{},{}\n'.format(tournDetails[0],tournDetails[1],tournDetails[2])
        fh.write(data)
        fh.close()
        for widget1 in WinMng.window.winfo_children():
            widget1.destroy()
            
        WinMng.widgets1=[]
        WinMng.widgets=[]
        WinMng.tab1()

        WinMng.swiss.swiss_init(entry)
        WinMng.swiss.swiss_startingRank()

        path2='TournamentFIles\\{}\\stats.txt'.format(entry)
        fh=open(path2,'w')
        fh.write('1')
        fh.close()
        print('hi')

    def on_entry_change():
        print('entrty change')
        WinMng.importing()

    def createTourn():
        print('create tourn ')
        window=WinMng.window
        widgets=WinMng.widgets1
        print(widgets,'rectify')
        popup=tk.Frame(window,width=300,height=200,bg='grey').place(x=50,y=50)
        
        #Mng.tourn=copy.copy(tourn)

        Name=Label(popup,text='Name',
        font=('Arial,20,bold'),
        fg='white',
        bg='#2f2f30')
        Name.place(x=83,y=60)

        entry=Entry(popup,font=('Arial',15))
        entry.place(x=83,y=80)

        importButton=Button(popup,text='Import',font=('Arial',22),fg='white',bg='#33339c',command=WinMng.importing).place(x=143,y=120)
        entry.bind("<Return>", lambda event: WinMng.on_entry_change())
        widgets.append(Name)
        widgets.append(entry)
        widgets.append(importButton)

    def Listclick(l):
        x=WinMng.widgets[0].curselection()[0]
        print('tournament list clicked',x)
        for widget1 in WinMng.window.winfo_children():
            widget1.destroy()
        WinMng.widgets=[]        
        WinMng.tab2(x)
        
    def back():
        WinMng.widgets=[]
        WinMng.widgets1=[]
        for widget1 in WinMng.window.winfo_children():
            widget1.destroy()
        WinMng.tab1()

    def back2():
        WinMng.widgets=[]
        WinMng.widgets1=[]
        for widget1 in WinMng.window.winfo_children():
            widget1.destroy()
        WinMng.tab2(WinMng.id)

    def resultUpdate():
        WinMng.swiss.updateResult(WinMng.tournName,WinMng.rndNO)
        print('updated result')

    def pairNxt():
        print('pair next pressed')
        pairing,roundNo=WinMng.swiss.pair()
        WinMng.widgets=[]
        WinMng.widgets1=[]
        for widget1 in WinMng.window.winfo_children():
            widget1.destroy()
        WinMng.tab2(WinMng.id)

    def Listroundclick(event):
        
        x=WinMng.listrnd.curselection()[0]
        print('list rnd clicked=>',x)
        WinMng.widgets=[]
        WinMng.widgets1=[]
        for widget1 in WinMng.window.winfo_children():
            widget1.destroy()
        WinMng.tab3(x)

    def resultentry():
        file_path = 'TournamentFIles\\{}\\Round{}Pairing.csv'.format(WinMng.tournName,str(WinMng.rndNO+1))
        if os.name == 'nt':  # Check if the operating system is Windows
            os.system('start notepad.exe ' + file_path)
        else:
            os.system('notepad ' + file_path)
    def refreshtab3():
        WinMng.widgets=[]
        WinMng.widgets1=[]
        for widget1 in WinMng.window.winfo_children():
            widget1.destroy()
        WinMng.tab3(WinMng.rndNO)
    def tab1():
        win=WinMng.window
        widg=WinMng.widgets
        fh=open('MngFiles\\TournData.txt','r')
        
        tournament=[]
        y=fh.readlines()
        for i in y:
            z=i.split(',')
            print(z)

            tournament.append('   {}'.format(z[1]))
        print(tournament)
        


        win.title('Tournament Scheduling')
        header=Frame(win,bg='#181a18',cursor='dot')
        header.place(x=0,y=0,relwidth=1,relheight=0.085)
        createTournament=Button(header,text='Create Tournament',
                            font=('Arial',10),command=WinMng.createTourn).place(x=25,rely=0.25)


        
        lbg='#3b3a3a'
        body=Frame(win,bg=lbg)
        body.place(relwidth=1,relheight=1-0.085,rely=0.085,relx=0)


        listTournaments=Listbox(body,bg=lbg,fg='white',font=('Arial',23),relief='flat',highlightthickness=1)
        listTournaments.place(relheight=1,relwidth=0.8,relx=0.1)
        j=0
        for i in tournament:
            print(i)
            listTournaments.insert(j,i)
            j+=1
            listTournaments.place(relheight=1,relwidth=0.8,relx=0.1)
        listTournaments.bind("<<ListboxSelect>>", WinMng.Listclick)
        print('1')
        
        WinMng.widgets.append(listTournaments)
        print(WinMng.widgets)

    def tab2(id):
        WinMng.id=id
        window=WinMng.window
        print(id)
        fh=open('MngFiles\\TournData.txt','r')
        y=fh.readlines()
        y=y[id].split(',')
        print(y)
        WinMng.swiss.opened_init(y[1])
        WinMng.tournName=y[1]
        #WinMng.swiss.swiss_init(y[1])


        path='TournamentFIles\\{}\\'
        window.title('Tournament Scheduling')

        header=Frame(window,bg='#181a18',cursor='dot')
        header.place(x=0,y=0,relwidth=1,relheight=0.085)
        createTournament=Button(header,text='Back',
                        font=('Arial',10),command=WinMng.back).place(x=25,rely=0.25)

        lgb='#3b3a3a'
        rbg='#211e1e'
        body=Frame(window,bg=lgb)
        body.place(relwidth=1,relheight=1-0.085,rely=0.085,relx=0)

        leftBody=Frame(body,bg=rbg)
        leftBody.place(relheight=1,relwidth=0.5)

        rightBody=Frame(body,bg=lgb)
        rightBody.place(relheight=1,relwidth=0.5,relx=0.5)

        
        sno=Label(leftBody,text='S.No',bg=rbg,anchor='w',font=('Arial',18),fg='white')
        sno.place(relwidth=0.16,relheight=0.04,relx=0,rely=0)
        nme=Label(leftBody,text='Name',bg=rbg,anchor='w',font=('Arial',18),fg='white')
        nme.place(relwidth=0.425,relheight=0.04,relx=0.06+0.1,rely=0)
        rtg=Label(leftBody,text='Rating',bg=rbg,anchor='w',font=('Arial',18),fg='white')
        rtg.place(relwidth=0.2125,relheight=0.04,relx=0.435+0.1,rely=0)
        pts=Label(leftBody,text='Point',bg=rbg,anchor='w',font=('Arial',18),fg='white')
        pts.place(relwidth=0.3526,relheight=0.04,relx=0.6475+0.1,rely=0)

        listsno=Listbox(leftBody,bg=rbg,fg='white',font=('Arial',18),relief='flat',borderwidth=0,highlightthickness=0)
        listsno.place(relwidth=0.16,relheight=0.9,relx=0,rely=0.05)

        listplayers=Listbox(leftBody,bg=rbg,font=('Arial',18),relief='flat',borderwidth=0,highlightthickness=0,fg='white')
        listplayers.place(relheight=0.9,relwidth=0.425,relx=0.06+0.1,rely=0.05)

        listratings=Listbox(leftBody,bg=rbg,font=('Arial',18),relief='flat',borderwidth=0,highlightthickness=0,fg='white')
        listratings.place(relheight=0.9,relwidth=0.2125,relx=0.435+0.1,rely=0.05)
        
        listpts=Listbox(leftBody,bg=rbg,font=('Arial',18),relief='flat',borderwidth=0,highlightthickness=0,fg='white')
        listpts.place(relheight=0.9,relwidth=0.2125,relx=0.6475+0.1,rely=0.05)

        nextRoundbutton=Button(rightBody,text='Pair Next Round',font=('Arial',16),command=WinMng.pairNxt)
        nextRoundbutton.place(relx=0.6,rely=0.03)


        container=LabelFrame(rightBody,bg=lgb,fg='white')
        container.place(relx=0.1,rely=0.1,relheight=1,relwidth=0.8)
        listrnd=Listbox(container,bg=lgb,fg='white',font=('Arial',18),relief='flat',borderwidth=0,highlightthickness=0)
        listrnd.place(relwidth=1,relheight=1)
        WinMng.swiss.Read_LatestRank()
        Players=WinMng.swiss.latestRank
        print(Players,'LOL')
        j=0
        for i in Players:
            print(i)
            listplayers.insert(j,' '+i[0])
            j+=1
        j=0
        for i in Players:

            listratings.insert(j,i[2])
            j+=1
        j=0
        for i in Players:
  
            listpts.insert(j,str(float(i[3])))
            j+=1
        for i in range(len(Players)):
            
            listsno.insert(i,str(i+1))
        path='TournamentFIles\\{}\\stats.txt'.format(y[1])
        fh=open(path,'r')
        rounds=int(fh.read(1))-1
        for i in range(rounds):
            listrnd.insert(i,' Round - '+str(i+1) )
        WinMng.listrnd=listrnd
        listrnd.bind("<<ListboxSelect>>", WinMng.Listroundclick)
    
    def tab3(rndNO):
        WinMng.rndNO=rndNO
        print(WinMng.tournName)
        print('Tab3')
        window=WinMng.window
        file_path = 'TournamentFIles\\{}\\Round{}Pairing.csv'.format(WinMng.tournName,str(rndNO+1))
        



        header=Frame(window,bg='#181a18',cursor='dot')
        header.place(x=0,y=0,relwidth=1,relheight=0.085)
        createTournament=Button(header,text='Back',
                        font=('Arial',10),command=WinMng.back2).place(x=25,rely=0.25)
        updateResult=Button(header,text='Update Result',
                        font=('Arial',10),command=WinMng.resultUpdate).place(relx=0.9,rely=0.25)
        resultUpdatingSRC=Button(header,text='Enter Result',
                        font=('Arial',10),command=WinMng.resultentry).place(relx=0.4,rely=0.25)
        refresh=Button(header,text='Refresh',
                        font=('Arial',10),command=WinMng.refreshtab3).place(x=105,rely=0.25)
        lbg='white'
        body=Frame(window,bg=lbg)
        body.place(relwidth=1,relheight=1-0.085,rely=0.085,relx=0)
        
        
        tree = ttk.Treeview(body)
        tree.pack(side='top')
        if file_path:
            with open(file_path, newline='') as csv_file:
                reader = csv.reader(csv_file)
                z=next(reader)
                print(z)
                headers = z  # Get the headers from the first row
                tree.delete(*tree.get_children())  # Clear existing data

                # Insert headers into the treeview
                tree["columns"] = headers
                tree['show'] = 'headings'
                #tree.heading("#0", text="Row")
                j=0
                for header in headers:
                    tree.heading('{}'.format(j), text=header)
                    tree.column('{}'.format(j), width=80,anchor ='c')
                    j+=1

                # Insert data into the treeview
                j=1
                print('hoi')
                for rec in reader:
                    print(rec)
                    tree.insert("", 'end', text ="L{}".format(j), values=rec)
                    j+=1
                '''
                for i, row in enumerate(reader, start=1):
                    tree.insert(parent='', index='end', iid=i, text=str(i), values=row)
                '''
        messageBoxDisplayText='Open\n {}\n And Edit Result Or \n Click Enter Result Button \n Then Click Update Result Button'.format(file_path)
        messagebox.showinfo('Steps to Update Result',messageBoxDisplayText)


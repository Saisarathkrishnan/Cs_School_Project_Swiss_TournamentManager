import copy
from tabulate import tabulate

import csv

class Swiss:
    tournName=''
    playersDetails=[]
    startingRank=[]
    latestRank=[]
    def swiss_init(name):
        Swiss.tournName=name
        print('swiss initialized')
        path='TournamentFIles\\{}\\importedPlayers.txt'.format(name)
        
        fh=open(path,'r')
        players=fh.readlines()
        playersDetails=[]
        print(players)
        for i in players:

            z=i.split(',')
            
            #dob=dob[0:len]
            plydic={
                'NAME':z[0],
                'DOB':z[2][0:len(z[2])-2],
                'RATING':int(z[1]),
                'PTS':0.0
            }
            playersDetails.append(plydic)

        for i in playersDetails:
            print(i)
        Swiss.playersDetails=playersDetails

    def swiss_startingRank():
        players=Swiss.playersDetails
        sorted_data = sorted(players, key=lambda x: (-x["RATING"], x["NAME"]))
        print('LOLOLOLOLOLOLOLO')
        for i in sorted_data:
            print(i)
        path='TournamentFIles\\{}\\startingRank.txt'.format(Swiss.tournName)
        fh=open(path,'w')
        starting_Rank_dump=[]
        for i in sorted_data:
            x='{},{},{},{}\n'.format(i['NAME'],i['DOB'],i['RATING'],i['PTS'])
            starting_Rank_dump.append(x)
        fh.writelines(starting_Rank_dump)
        Swiss.startingRank=starting_Rank_dump
        Swiss.latestRank=copy.deepcopy(Swiss.startingRank)
        print(Swiss.latestRank)
        Swiss.Update_LatestRank()

    def opened_init(name):
        Swiss.tournName=name

    def Update_LatestRank():
        path='TournamentFIles\\{}\\LatestRank.txt'.format(Swiss.tournName)
        fh=open(path,'w')
        fh.writelines(Swiss.latestRank)

    def Read_LatestRank():
        path='TournamentFIles\\{}\\LatestRank.txt'.format(Swiss.tournName)
        fh=open(path,'r')
        x=fh.readlines()
        print(x,'LOLOL')
        Swiss.latestRank=[]
        for i in x:
            y=i.split(',')
            Swiss.latestRank.append(y)
        for i in Swiss.latestRank:
            i[3]=i[3][0:3]
        
    def pair():
        print()
        f=[]
        k=[]
        h=[]
        path='TournamentFIles\\{}\\stats.txt'.format(Swiss.tournName)
        fh=open(path,'r')
        roundNO=int(fh.read(1))
        print(roundNO)
        fh.close()
        fh=open(path,'w')
        x=roundNO+1
        fh.write(str(x))
        print(Swiss.latestRank)
        ranking=Swiss.latestRank
        minpoint=0
        minpoint=ranking[len(ranking)-1][3]
        print(minpoint,"minPt")
        #f=copy.deepcopy(ranking)
        p=0
        for j in range(((roundNO-1)*2)+1):
            #print('hi')
            o=0
            for i in ranking:
                print(i,j,'debug')
                if(j/2 == float(i[3])):
                    if(o==0):
                        o+=1
                        p+=1
                        print('hi')
                        f.append([])                  
                    f[p-1].append(i) 
            if(len(f)==len(ranking)):
                print(len(f))
                break

        print('complete')  
        f.reverse()
        for i in f:
            header=['name','elo','DOB','point']
            table=tabulate(i,headers=header,tablefmt="grid")
            print(i)
            print('\n\n')
        noIteration=0
        print(f)
        
        for i in f:
            k=[]
            noOfTopPt=len(i)-1            
            l=len(i)   
            if(l%2==0):
                split=l/2
                for j in range(int(split)):
                    k.append(list([i[j]]+[i[int(split+j)]]))
                #Swiss.Swiss_log(k)
                print('even')

            else:
                if(i[1][3]!=minpoint):
                    print(i,'ref')
                    print(f[noIteration+1],'ref')
                    f[noIteration+1].insert(0,i[len(i)-1])
                    i.pop(len(i)-1)   
                    print(i,'ref')               
                    print(f[noIteration+1],'ref')  
                    split=(l-1)/2
                else:
                    split=(l+1)/2
                    i.append(['BYE',0,'0',0.0])
                for j in range(int(split)):
                    k.append(list([i[j]]+[i[int(split+j)]]))
                print(end='')
            noIteration+=1
            for y in k: 
                #print(i)
                h.append(y)
        header=['name','name']
        table=tabulate(h,headers=header,tablefmt="grid")
        lmno=[]
        print(table)
        for i in h:
            lq='{},{},{},{}|{},{},{},{}\n'.format(i[0][0],i[0][1],i[0][2],i[0][3],i[1][0],i[1][1],i[1][2],i[1][3])
            lmno.append(lq)

        path='TournamentFIles\\{}\\Round{}Pairing.txt'.format(Swiss.tournName,roundNO)
        fh=open(path,'w')
        fh.writelines(lmno)
        fh.close()
        
        path='TournamentFIles\\{}\\Round{}Pairing.csv'.format(Swiss.tournName,roundNO)
        fh=open(path,'w',newline='')
        cwriter=csv.writer(fh)
        data=[]
        j=1
        data.append(['BrdNO','Name','Rating','Pts','Left Result','Right Result','Pts','Rating','Name'])
        for i in h:
            lq=[]
            print(type(i[0][3]),type(i[1][3]),'DEBUG')
            lq.append(j)
            lq.append(i[0][0])
            lq.append(i[0][2])
            lq.append(i[0][3])
            lq.append('')
            lq.append('')
            lq.append(i[1][3])
            lq.append(i[1][2])
            lq.append(i[1][0])
            data.append(lq)
            j+=1
        cwriter.writerows(data)
        print(data,'hiii')


        fh.close()

        return lmno,roundNO
    
    def custom_sort_key(item):
        parts = item.split()
        
        print( -int(parts[2],parts[0]))
        return (-float(parts[3][0:3]), -int(parts[2],parts[0]))
    def updateResult(name,no):
        no=str(int(no)+1)
        print(name,no,'yes')
        path='TournamentFIles\\{}\\Round{}Pairing.csv'.format(name,no)
        with open(path, newline='') as csv_file:
                reader = csv.reader(csv_file)
                z=next(reader)
                print(z)
                playlist=[]
                for i in reader:
                    x=[]
                    name1=i[1]
                    rtg1=i[2]
                    pts1=str(float(i[3])+float(i[4]))
                    DOB1=''
                    name2=i[8]
                    rtg2=i[7]
                    pts2=str(float(i[6])+float(i[5]))
                    DOB2=''
                    path='TournamentFIles\\{}\\LatestRank.txt'.format(name)
                    fh=open(path,'r')
                    oldrank=fh.readlines()
                    for o in oldrank:
                        ply=o.split(',')
                        
                        if( name1 in ply ):
                            DOB1=ply[1]
                            print(ply,DOB1)
                        elif(name2 in ply):
                            DOB2=ply[1]
                            print(ply,DOB2)
                    fh.close()
                    if(name1 !='BYE'):
                        y='{},{},{},{}\n'.format(name1,DOB1,rtg1,pts1)
                        playlist.append(y)
                        print(y)
                    if(name1 !='BYE'):
                        y='{},{},{},{}\n'.format(name2,DOB2,rtg2,pts2)
                        playlist.append(y)
                        print(y)
                    #print(i)
                print(playlist)
                path='TournamentFIles\\{}\\RankAfterRound{}.txt'.format(name,no)
                fh=open(path,'w')
                fh.writelines(playlist)
                fh.close()
                sorted_list=[]
                for i in playlist:
                    lol=i.split(',')
                    stringInp=[]
                    lol[3]=float(lol[3][0:3])
                    sorted_list.append(lol)
                    print(lol,'help')
                
                sorted_list = sorted(sorted_list, key=lambda item: (-item[3], -int(item[2]),item[0]))
                #sorted_list = sorted(playlist, key=Swiss.custom_sort_key)
                playlist=[]
                for i in sorted_list:
                    print(i)
                    x='{},{},{},{}\n'.format(i[0],i[1],i[2],i[3])
                    playlist.append(x)
                print('hola')
                
                
                Swiss.latestRank=playlist
                Swiss.Update_LatestRank()


                
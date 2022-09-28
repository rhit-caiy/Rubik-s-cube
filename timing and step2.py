import random,time
import compress
corner=[i for i in range(8)]#0,1,2,3,4,5,6,7,lub,rub,luf,ruf,ldf,rdf,ldb,rdb
cornerd=[0,0,0,0,5,5,5,5]#white or yellow face direction
edge=[i for i in range(12)]#0,1,2,3,4,5,6,7,8,9,10,11,ub,ul,uf,ur,lb,lf,rf,rb,db,dl,df,dr
edged=[0,0,0,0,1,2,3,4,5,5,5,5]#white or yellow, then right color on equator edge
center=[0,1,2,3,4,5]#center

#paste cube data here

facecorner=[[0,2,3,1],[0,6,4,2],[2,4,5,3],[3,5,7,1],[1,7,6,0],[4,6,7,5]]
faceedge=[[0,1,2,3],[1,4,9,5],[2,5,10,6],[3,6,11,7],[0,7,8,4],[10,9,8,11]]
adj=[[4,3,2,1],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[1,2,3,4]]#adjacent face of each
cornerposition=[[[0,0],[1,0],[4,2]],[[0,2],[4,0],[3,2]],[[0,6],[2,0],[1,2]],[[0,8],[3,0],[2,2]],
                [[5,0],[1,8],[2,6]],[[5,2],[2,8],[3,6]],[[5,6],[4,8],[1,6]],[[5,8],[3,8],[4,6]]]#corner face map to position
edgeposition=[[[0,1],[4,1]],[[0,3],[1,1]],[[0,7],[2,1]],[[0,5],[3,1]],
              [[1,3],[4,5]],[[2,3],[1,5]],[[3,3],[2,5]],[[4,3],[3,5]],
              [[5,7],[4,7]],[[5,3],[1,7]],[[5,1],[2,7]],[[5,5],[3,7]]]#edge face map to position

centeredge=[[0,2,10,8],[4,5,6,7],[1,3,11,9]]#middle rotation block
color=["#FFFF00","#0000FF","#FF0000","#00FF00","#FF8000","#FFFFFF"]
rotates=["U","L","F","R","B","D","M","E","S","x","y","z"]
def rotate(a):
    rotateedge(a)
    rotatecorner(a)
    
def rotateedge(a):
    global edge,edged
    r=faceedge[a]
    ne=[i for i in edge]
    ned=[i for i in edged]
    for i in range(4):
        ne[r[i]]=edge[r[(i+1)%4]]
    for i in r:
        i=edge[i]
        if edged[i]!=a:
            ned[i]=adj[a][(adj[a].index(edged[i])+1)%4]
    edge=ne
    edged=ned
    
def rotatecorner(a):
    global corner,cornerd
    r=facecorner[a]
    nc=[i for i in corner]
    ncd=[i for i in cornerd]
    for i in range(4):
        nc[r[i]]=corner[r[(i+1)%4]]
    for i in r:
        i=corner[i]
        if cornerd[i]!=a:
            ncd[i]=adj[a][(adj[a].index(cornerd[i])+1)%4]
    corner=nc
    cornerd=ncd
    
def rotatemiddle(a):
    global center,edge,edged
    #LDF for MES
    ne=[i for i in edge]
    ned=[i for i in edged]
    nc=[i for i in center]
    facenum=0
    if a==0:
        facenum=1
    elif a==1:
        facenum=5
    else:
        facenum=2
    for i in range(4):
        nc[adj[facenum][i]]=center[adj[facenum][(i-1)%4]]
    for i in range(4):
        ne[centeredge[a][i]]=edge[centeredge[a][(i-1)%4]]
    for i in range(4):
        ned[edge[centeredge[a][i]]]=adj[facenum][(adj[facenum].index(edged[edge[centeredge[a][i]]])+1)%4]
    center=nc
    edge=ne
    edged=ned
    
def rotatecube(a):
    if a==0:
        rotatemiddle(0)
        rotatemiddle(0)
        rotatemiddle(0)
        rotate(3)
        rotate(1)
        rotate(1)
        rotate(1)
    elif a==1:
        rotatemiddle(1)
        rotatemiddle(1)
        rotatemiddle(1)
        rotate(0)
        rotate(5)
        rotate(5)
        rotate(5)
    elif a==2:
        rotatemiddle(2)
        rotate(2)
        rotate(4)
        rotate(4)
        rotate(4)

def randomcube():
    a=random.randrange(80,120)
    for i in range(a):
        r=random.randrange(0,9)
        if r<6:
            rotate(r)
        else:
            rotatemiddle(r-6)
        
totalstep=0
solutionstring=""
#letters to action
def do(s):
    global totalstep,solutionstring
    l=len(s)
    solutionstring+=s
    rotates=["U","L","F","R","B","D","M","E","S","x","y","z"]
    i=0
    while i<l:
        a=rotates.index(s[i])
        if 0<=a<=5:
            rotate(a)
            totalstep+=1
        elif 6<=a<=8:
            rotatemiddle(a-6)
            totalstep+=1
        elif 9<=a<=11:
            rotatecube(a-9)
        i+=1
        if i<l:
            if s[i]=="'":
                i+=1
                if 0<=a<=5:
                    rotate(a)
                    rotate(a)
                elif 6<=a<=8:
                    rotatemiddle(a-6)
                    rotatemiddle(a-6)
                elif 9<=a<=11:
                    rotatecube(a-9)
                    rotatecube(a-9)
            elif s[i]=='2':
                i+=1
                if 0<=a<=5:
                    rotate(a)
                elif 6<=a<=8:
                    rotatemiddle(a-6)
                elif 9<=a<=11:
                    rotatecube(a-9)

def solve():
    global totalstep,totalsteps
    c()
    totalsteps[0]=totalstep
    f()
    totalsteps[1]=totalstep-sum(totalsteps)
    o()
    totalsteps[2]=totalstep-sum(totalsteps)
    p()
    totalsteps[3]=totalstep-sum(totalsteps)
    
#cross
def c():
    direction()
    if edge[8:]==[8,9,10,11] and edged[8:]==[5,5,5,5]:
        return
    rotation=cross(edge,edged)
    allrotation=[["U","U2","U'"],["L","L2","L'"],["F","F2","F'"],["R","R2","R'"],["B","B2","B'"],["D","D2","D'"]]
    string=""
    for i in rotation:
        string+=allrotation[i[0]][i[1]]
    do(string)
    
onestepcube=[]#store cubes that only 1 step from correct one, reduce last step
correctedge=[8,9,10,11]
correctedged=[5,5,5,5]
for i in range(1,6):#up doesn't count
    r=faceedge[i]
    newedge=correctedge.copy()
    newedged=correctedged.copy()
    for j in range(3):#totally 15 possible bottom cube
        for l in range(4):
            if newedge[l] in r:
                newedge[l]=r[(r.index(newedge[l])-1)%4]
                if newedged[l]!=i:
                    newedged[l]=adj[i][(adj[i].index(newedged[l])+1)%4]
        onestepcube.append([newedge.copy(),newedged.copy()])
#exhaustively get optimize cross, return format [[0,0],[6,1]],[face number, rotation time-1]
def cross(edge,edged):
    queue=[]
    newqueue=[]
    #check face that have no 8,9,10,11 block
    helpless=[]
    for i in range(6):
        j=faceedge[i]
        if edge[j[0]]<8 and edge[j[1]]<8 and edge[j[2]]<8 and edge[j[3]]<8:
            helpless.append(i)
    #edge,edge direction,current rotation,face without white block or repeated rotate face
    edge=[edge.index(i) for i in range(8,12)]
    edged=edged[8:]
    queue.append([edge.copy(),edged.copy(),[],helpless.copy()])
    
    
    #require only 1 step to solve
    if [edge,edged] in onestepcube:
        index=onestepcube.index([edge,edged])
        return [[index//3+1,2-index%3]]
        
    #[edge,edged,current steps,useless next step]
    for c in range(1,9):
        #dequeue
        for i in queue:
            istep=i[2]
            helpless=i[3]
            #turn 6 faces
            for j in range(6):
                if j not in helpless:
                    #rotation time in one face
                    newedge=i[0].copy()
                    newedged=i[1].copy()
                    #3 angles
                    r=faceedge[j]
                    for k in range(3):
                        #rotate and change edge and edge direction
                        for l in range(4):
                            if newedge[l] in r:
                                newedge[l]=r[(r.index(newedge[l])-1)%4]
                                if newedged[l]!=j:
                                    newedged[l]=adj[j][(adj[j].index(newedged[l])+1)%4]
                        newstep=istep+[[j,k]]
                        newhelpless=[j]
                        #face without white edge
                        for l in range(6):
                            m=faceedge[l]
                            if m[0] not in newedge and m[1] not in newedge and m[2] not in newedge and m[3] not in newedge:
                                newhelpless.append(l)
                        #return
                        #if newedge==[8,9,10,11] and newedged==[5,5,5,5]:
                        #    return newstep
                        if [newedge,newedged] in onestepcube:
                            index=onestepcube.index([newedge,newedged])
                            return newstep+[[index//3+1,2-index%3]]
                        #enqueue
                        elif c<5:
                            newqueue.append([newedge.copy(),newedged.copy(),newstep.copy(),newhelpless.copy()])
                        else:
                            m=0
                            for l in newedged:
                                if l==5:
                                    m+=1
                            if c==5 and m>=1 or c==6 and m>=2 or c==7 and m>=3:
                                newqueue.append([newedge.copy(),newedged.copy(),newstep.copy(),newhelpless.copy()])
        queue=newqueue.copy()
        newqueue=[]
    
#f2l
pce=[[5,6],[7,7],[6,4],[4,5]]#paired corner edge, pce[i][0] is corner, pce[i][1] is edge
def f():
    #both blocks are on top
    for i in range(8):
        solvedce=solvedf2l()#0,1,2,3 to represent lb,lf,rf,rb corner ede block pairs correct locations
        n=len(solvedce)#number of solved pairs
        if n==4:
            return
        bothtop(n)
        cornertop(n)
        cornerbottom(n)
        solvedce=solvedf2l()#0,1,2,3 to represent lb,lf,rf,rb corner ede block pairs correct locations
        newn=len(solvedce)#number of solved pairs
        if newn==4:
            return
        if n==newn:
            removeother()
        

#solved f2l index, length=4 if finished
def solvedf2l():
    solvedce=[]#0,1,2,3 to represent lb,lf,rf,rb corner ede block pairs correct locations
    for i in range(4):
        if corner[pce[i][0]]==pce[i][0] and cornerd[pce[i][0]]==5 and edge[pce[i][1]]==pce[i][1] and edged[pce[i][1]]==pce[i][1]-3:
            solvedce.append(i)
    return solvedce

#both corner and edge on top
def bothtop(n):
    s=[[],[],[]]
    #white up
    s[0]=[["F'UFU2F'U'F","URU2R'URU'R'"],#22 19
       ["U'F'U2FU'F'UF","U2RUR'URU'R'"],#20 21
       ["F'U2FUF'U'F","RUR'U2RUR'U'RUR'"],#18 23
       ["FURU'R'F'RU'R'","RU2R'U'RUR'"]]#24 17
    #white front
    s[1]=[["U'RU'R'UF'U'F","U'RUR'U2RU'R'"],#9 5
          ["F'U'F","U'RU2R'U2RU'R'"],#3 7
          ["UF'UFU'F'U'F","RUR'U2RU'R'URU'R'"],#13 15
          ["U'RU2R'UF'U'F","URU'R'"]]#11 1
    #white right
    s[2]=[["UF'U2FU2F'UF","RUR'"],#8 4
          ["UF'U'FU2F'UF","U'RUR'URUR'U'"],#6 10
          ["U'F'UF","RU'R'URU'R'UURU'R'"],#2 12
          ["RU'R'U2F'U'F","U'RU'R'URUR'"]]#16 14
    for j in range(4-n):
        c=0
        for i in range(4):
            if pce[i][0] in corner[:4] and pce[i][1] in edge[:4]:
                c+=1
                if corner[1]==pce[i][0]:
                    do("U")
                elif corner[0]==pce[i][0]:
                    do("U2")
                elif corner[2]==pce[i][0]:
                    do("U'")
                
                cd=cornerd[pce[i][0]]#corner direction, 0 is up, 1 is front, 2 is right
                if cd!=0:
                    cd-=1
                ep=edge.index(pce[i][1])#edge position
                ed=edged[pce[i][1]]#edge direction
                if ed!=0:
                    ed=1
                do(s[cd][ep][ed])
            do("y")
        if c==0:
            break
#only corner on top and edge not
def cornertop(n):
    s=[["RU'R'UF'UF","RUR'U'RUR'U'RUR'"],["U'RUR'UF'UF","U'RU'R'U2RU'R'"],["UF'U'FU'RUR'","U'RU2R'URUR'"]]#31 32 35 33 36 34
    for j in range(4-n):
        c=0
        for i in range(4):
            if pce[i][0] in corner[:4] and pce[i][1] not in edge[:4]:
                #c+=1
                #up-down condition
                if pce[i][1]==edge[6]:
                    if corner[1]==pce[i][0]:
                        do("U")
                    elif corner[0]==pce[i][0]:
                        do("U2")
                    elif corner[2]==pce[i][0]:
                        do("U'")
                    cd=cornerd[pce[i][0]]#corner direction, 0 is up, 1 is front, 2 is right
                    if cd!=0:
                        cd-=1
                    ed=edged[pce[i][1]]-2#edge direction
                    c+=1
                    do(s[cd][ed])
                #edge in another edge position
            do("y")
        if c==0:
            break
    
def cornerbottom(n):
    s=[["","RU'R'UF'U2FU2F'UF"],["LF'L'U2LFL'RUR'","RUR'U'RU2R'U'RUR'"],["RU'R'LF'L'U2LFL'","RU'R'URU2R'URU'R'"]]#0 37 40 38 41 39
    s1=[["FRF'U'F'UFR'","R'F'RURU'R'F"],["F'U'FUF'U'F","RU'R'URU'R'"],["F'UFU'F'UF","RUR'U'RUR'"]]#26 25 29 27 28 30
    for j in range(4-n):
        c=0
        for i in range(4):
            if pce[i][0]==corner[5] and pce[i][1]==edge[6]:
                #corner and button align in correct position
                cd=cornerd[pce[i][0]]
                ed=3-edged[pce[i][1]]
                if cd==5:
                    cd=0
                else:
                    cd-=1
                if cd!=0 or ed!=0:
                    c+=1
                    do(s[cd][ed])
            elif pce[i][0]==corner[5] and pce[i][1] in edge[:4]:
                c+=1
                #conner correct and edge on top
                cd=cornerd[pce[i][0]]
                ed=edged[pce[i][1]]
                ep=edge.index(pce[i][1])
                if cd==5:
                    cd=0
                else:
                    cd-=1
                if ed!=0:
                    ed=1
                if ep==0:
                    if ed==0:
                        do("U2")
                    else:
                        do("U")
                elif ep==1:
                    if ed==0:
                        do("U'")
                    else:
                        do("U2")
                elif ep==2 and ed!=0:
                    do("U'")
                elif ep==3 and ed==0:
                    do("U")
                do(s1[cd][ed])
            do("y")
        if c==0:
            break
#remove edge and corner that not belong to its position
def removeother():
    c=0
    for i in range(4):
        if c==0 and ((edge[6]!=pce[i][1] and edge[6]>=4) or (corner[5]!=(pce[i][0]) and corner[5]>=4)):
            c=1
            do("RUR'")
        do("y")
        
#oll             
def o():
    e=0#correct edge
    c=0#correct corner
    for i in range(4):
        if edged[i]==0:
            e+=1
        if cornerd[i]==0:
            c+=1
    if e==4:#0 21 22 23 24 25 26 27
        if c==4:#0
            return
        elif c==2:#23 24 25
            d=[]
            for i in range(4):
                if cornerd[i]!=0:
                    d.append(cornerd[i])
            if abs(d[1]-d[0])==2:
                while cornerd[corner[2]]!=1:
                    do("y")
                do("RBR'FRB'R'F'")#24
            elif d[0]==d[1]:
                while cornerd[corner[0]]!=4:
                    do("y")
                do("R2D'RU2R'DRU2R")#23
            else:
                while cornerd[corner[0]]!=1:
                    do("y")
                do("F'LFR'F'L'FR")#25
        elif c==1:#26 27
            while cornerd[corner[2]]!=0:
                do("y")
            if cornerd[corner[0]]==1:
                do("y'")
                do("L'U'LU'L'U2L")#26
            else:
                do("RUR'URU2R'")#27
        elif c==0:#21 22
            for i in range(4):
                if cornerd[corner[0]]==4 and cornerd[corner[1]]==4 and cornerd[corner[2]]==2:
                    do("RU2R'U'RUR'U'RU'R'")#21
                    break
                elif cornerd[corner[0]]==1 and cornerd[corner[1]]==4:
                    do("RU2R2U'R2U'R2U2R")#22
                do("y")
    elif e==2:
        if c==4:#28 57
            while edged[edge[2]]==0:
                do("y")
            if edged[edge[1]]!=0:
                do("y'")
            if edged[edge[0]]==0:
                do("MUM'U2MUM'")#28
            else:
                do("RUR'U'M'URU'L'")#57
        elif c==2:
            while edged[edge[1]]!=0:
                do("y")
            if edged[edge[3]]==0:#33 45 34 39 40 46
                if cornerd[corner[0]]==0 and cornerd[corner[2]]==0 or cornerd[corner[1]]==0 and cornerd[corner[3]]==0:
                    if cornerd[corner[1]]!=0:
                        do("y2")
                    if cornerd[corner[0]]==1:
                        do("FRUR'U'F'")#45
                    else:
                        do("RUR'U'R'FRF'")#33
                elif cornerd[corner[0]]==0 and cornerd[corner[3]]==0 or cornerd[corner[1]]==0 and cornerd[corner[2]]==0:
                    if cornerd[corner[0]]==0:
                        if cornerd[corner[2]]!=1:
                            do("y2")
                        do("R'FRUR'U'F'UR")#40
                    else:
                        if cornerd[corner[0]]!=4:
                            do("y2")
                        do("LF'L'U'LUFU'L'")#39
                else:
                    if cornerd[corner[0]]==0:
                        do("y2")
                    if cornerd[corner[0]]==1:
                        do("RUR'U'B'R'FRS")#34
                    else:
                        do("y")
                        do("R'U'R'FRF'UR")#46
            else:#31 32 43 44 35 37 29 30 41 42 36 38
                if edged[edge[0]]!=0:
                    do("y")
                if cornerd[corner[0]]==0 and cornerd[corner[3]]==0:
                    if cornerd[corner[2]]==2:
                        do("FRU'R'U'RUR'F'")#37
                    else:
                        do("y2")
                        do("RU2R2FRF'RU2R'")#35
                elif cornerd[corner[1]]==0 and cornerd[corner[2]]==0:
                    if cornerd[corner[0]]==4:
                        do("RUR'URU'R'U'R'FRF'")#38
                    else:
                        do("y")
                        do("L'U'LU'L'ULULF'L'F")#36
                elif cornerd[corner[0]]==0:
                    if cornerd[corner[2]]==0:
                        if cornerd[corner[1]]==3:
                            do("FURU'R'F'")#44
                        else:
                            do("y2")
                            do("SRUR'U'R'FRB'")#32
                    else:
                        if cornerd[corner[2]]==2:
                            do("y")
                            do("F'U'L'ULF")#43
                        else:
                            do("y")
                            do("R'U'FURU'R'F'R")#31
                else:
                    while cornerd[corner[0]]!=0 or cornerd[corner[1]]!=0:
                        do("y")
                    s=[["L2U'LBL'UL2U'L'B'L","R'U'RU'R'U2RFRUR'U'F'"],["R2UR'B'RU'R2URBR'","LUL'ULU2L'F'L'U'LUF"]]#29 42 30 41
                    ed=edged[edge[1]]
                    cd=cornerd[corner[2]]-1
                    do(s[ed][cd])#29 42 30 41
        elif c==1:
            while edged[edge[1]]!=0:
                do("y")
            if edged[edge[3]]==0:#13 14 15 16
                if cornerd[corner[2]]==0 or cornerd[corner[3]]==0:
                    do("y2")
                s=[["R'F'RL'U'LUR'FR","B'U'R'U2RUR'U'RB"],["BULU2L'U'LUL'B'","LFL'RUR'U'LF'L'"]]#15 14 13 16
                cd1=cornerd[corner[0]]
                if cd1!=0:
                    cd1=1
                cd2=cornerd[corner[2]]-1
                do(s[cd1][cd2])#13 14 15 16
            else:#5 6 9 10 7 8 11 12
                if edged[edge[0]]!=0:
                    do("y")
                if cornerd[corner[0]]==0:#5 6
                    if cornerd[corner[1]]==4:
                        do("y")
                        do("LF2R'F'RF'L'")#6
                    else:
                        do("R'F2LFL'FR")#5
                elif cornerd[corner[3]]==0:#9 10
                    if cornerd[corner[0]]==1:
                        do("RUR'U'R'FR2UR'U'F'")#9
                    else:
                        do("y'")
                        do("RUR'UR'FRF'RU2R'")#10
                else:
                    if cornerd[corner[1]]==0:
                        if cornerd[corner[0]]==4:
                            do("y'")
                            do("F'L'U'LUFUFRUR'U'F'")#11
                        else:
                            do("y")
                            do("R'F'LF'L'F2R")#8
                    else:
                        if cornerd[corner[0]]==4:
                            do("LFR'FRF2L'")#7
                        else:
                            do("y2")
                            do("FRUR'U'F'UFRUR'U'F'")#12
        elif c==0:
            if edged[edge[0]]==0 and edged[edge[2]]==0 or edged[edge[1]]==0 and edged[edge[3]]==0:#51 52 55 56
                if edged[edge[0]]==0:
                    do("y")
                if cornerd[corner[0]]==1 and cornerd[corner[3]]==3:
                    do("LFL'URU'R'URU'R'LF'L'")#56
                elif cornerd[corner[0]]==0 and cornerd[corner[1]]==4:
                    do("BULU'L'ULU'L'B'")#51
                elif cornerd[corner[0]]==4 and cornerd[corner[1]]==3:
                    do("FURU'R'URU'R'F'")#51
                elif cornerd[corner[0]]==4 and cornerd[corner[2]]==2:
                    do("y")
                    do("RU2R2U'RU'R'U2FRF'")#55
                else:
                    while cornerd[corner[0]]!=4 or cornerd[corner[2]]!=2:
                        do("y")
                    do("RUR'URU'BU'B'R'")#52
            else:#47 48 49 50 53 54
                while edged[edge[0]]!=0 or edged[edge[1]]!=0:
                    do("y")
                if cornerd[corner[0]]==4 and cornerd[corner[1]]==4:
                    if cornerd[corner[2]]==1:
                        do("y")
                        do("F'L'U'LUL'U'LUF")#47
                    else:
                        do("y")
                        do("LFR'FRF'R'FRF2L'")#54
                elif cornerd[corner[0]]==1 and cornerd[corner[2]]==1:
                    if cornerd[corner[1]]==4:
                        do("FRUR'U'RUR'U'F'")#48
                    else:
                        do("R'F'LF'L'FLF'L'F2R")#53
                elif cornerd[corner[0]]==4:
                    do("R'FR2B'R2F'R2BR'")#50
                else:
                    do("y'")
                    do("RB'R2FR2BR2F'R")#49
    elif e==0:#1 2 3 4 17 18 19
        if c==0:#1 2
            while cornerd[corner[0]]!=1 or cornerd[corner[2]]!=1:
                do("y")
            if cornerd[corner[1]]==3:
                do("RU2R2FRF'U2R'FRF'")#1
            else:
                do("FRUR'U'SRUR'U'B'")#2
        elif c==1:#3 4
            while cornerd[corner[1]]==4 or cornerd[corner[3]]==2:
                do("y")
            do("BULU'L'B'")
            while cornerd[corner[0]]!=1 or cornerd[corner[2]]!=1:
                do("y")
            do("FRUR'U'F'")
        elif c==2:#17 18 19
            while cornerd[corner[2]]==0:
                do("y")
            if cornerd[corner[1]]!=0:
                if cornerd[corner[2]]==2:
                    do("yy")
                do("RUR'UR'FRF'U2R'FRF'")#17
            else:
                if cornerd[corner[3]]==0:
                    do("y'")
                if cornerd[corner[2]]==2:
                    do("LFR'FRF2L2B'RB'R'B2L")#18
                else:
                    do("MURUR'U'M'R'FRF'")#19
        elif c==4:
            do("MURUR'U'M2URU'L'")
    direction()
    
def direction():
    if center[0]==5:
        do("x2")
    elif center[1]==5:
        do("z'")
    elif center[2]==5:
        do("x'")
    elif center[3]==5:
        do("z")
    elif center[4]==5:
        do("x")
    while center[1]!=1:
        do("y")
    
def p():
    if corner[:4] in [[0,1,2,3],[2,0,3,1],[3,2,1,0],[1,3,0,2]]:#1 2 3 4
        while corner[0]!=0:
            do("y")
        if edge[:4]==[0,1,2,3]:
            pass
        elif edge[:4]==[2,3,0,1]:
            do("M2UM2U2M2UM2")#3
        elif edge[:4]==[1,0,3,2] or edge[:4]==[3,2,1,0]:
            if edge[0]==3:
                do("y")
            do("M2UM2UM'U2M2U2M'")#4
        else:
            while cornerposition[corner[0]][2][0]!=edgeposition[edge[0]][1][0]:
                do("y")
            if cornerposition[corner[2]][1][0]==edgeposition[edge[1]][1][0]:
                do("M2UMU2M'UM2")#1
            else:
                do("M2U'MU2M'U'M2")#2
    elif edge[:4] in [[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]]:
        if edge[1]==0:
            do("U")
        elif edge[2]==0:
            do("U2")
        elif edge[3]==0:
            do("U'")
        if corner[:4]==[2,3,0,1] or corner[:4]==[1,0,3,2]:
            if corner[0]==1:
                do("y")
            do("x'RU'R'DRUR'D'RUR'DRU'R'D'")#7
        else:
            while cornerposition[corner[0]][2][0]!=cornerposition[corner[1]][1][0]:
                do("y")
            if cornerposition[corner[2]][1][0]==edgeposition[edge[2]][1][0]:
                do("y")
                do("x'R2D2R'U'RD2R'UR'")#5
            else:
                do("y'")
                do("x'L2D2LUL'D2LU'L")#6
    elif cornerposition[corner[0]][1][0]==edgeposition[edge[1]][1][0] and cornerposition[corner[1]][1][0]==edgeposition[edge[0]][1][0] and cornerposition[corner[2]][1][0]==edgeposition[edge[2]][1][0] and cornerposition[corner[3]][1][0]==edgeposition[edge[3]][1][0]:
        if not (cornerposition[corner[0]][2][0]==edgeposition[edge[0]][1][0] or cornerposition[corner[2]][2][0]==edgeposition[edge[1]][1][0] or cornerposition[corner[1]][2][0]==edgeposition[edge[3]][1][0] or cornerposition[corner[3]][2][0]==edgeposition[edge[2]][1][0]):
            do("R'UL'U2RU'LR'UL'U2RU'L")#21
        else:
            while cornerposition[corner[3]][2][0]!=edgeposition[edge[2]][1][0]:
                do("y")
            do("R'UL'U2RU'R'U2LR")#12
    elif cornerposition[corner[0]][2][0]==edgeposition[edge[0]][1][0] and cornerposition[corner[2]][2][0]==edgeposition[edge[1]][1][0] and cornerposition[corner[1]][2][0]==edgeposition[edge[3]][1][0] and cornerposition[corner[3]][2][0]==edgeposition[edge[2]][1][0]:
        if not (cornerposition[corner[0]][1][0]==edgeposition[edge[1]][1][0] or cornerposition[corner[1]][1][0]==edgeposition[edge[0]][1][0] or cornerposition[corner[2]][1][0]==edgeposition[edge[2]][1][0] or cornerposition[corner[3]][1][0]==edgeposition[edge[3]][1][0]):
            do("LU'RU2L'UR'LU'RU2L'UR'")#20
        else:
            while cornerposition[corner[2]][1][0]!=edgeposition[edge[2]][1][0]:
                do("y")
            do("LU'RU2L'ULU2L'R'")#13
    else:
        for i in range(4):
            if cornerposition[corner[0]][1][0]==edgeposition[edge[1]][1][0]==cornerposition[corner[2]][2][0]:
                do("U'R'URU'R2F'U'FURFR'F'R2")#9
            elif cornerposition[corner[0]][1][0]==cornerposition[corner[2]][2][0]:
                if cornerposition[corner[0]][2][0]==edgeposition[edge[0]][1][0] and cornerposition[corner[2]][1][0]==edgeposition[edge[2]][1][0]:
                    do("RUR'U'R'FR2U'R'U'RUR'F'")#8
                elif cornerposition[corner[0]][2][0]==edgeposition[edge[0]][1][0]:
                    do("y'")
                    do("R'U2RU2R'FRUR'U'R'F'R2U'")#14
                elif cornerposition[corner[2]][1][0]==edgeposition[edge[2]][1][0]:
                    do("y'")
                    do("LU2L'U2LF'L'U'LULFL2U")#15
                elif cornerposition[corner[1]][1][0]==edgeposition[edge[0]][1][0]:
                    do("R2D'y'RU'RUR'DyR2BU'B'")#16
                elif cornerposition[corner[3]][2][0]==edgeposition[edge[2]][1][0]:
                    do("R2DyR'UR'U'RD'y'R2F'UF")#18
                elif cornerposition[corner[3]][1][0]==edgeposition[edge[3]][1][0]:
                    do("RUR'y'R2D'y'RU'R'UR'DyR2")#17
                elif cornerposition[corner[1]][2][0]==edgeposition[edge[3]][1][0]:
                    do("R'U'yFR2DyR'URU'RD'y'R2")#19
            elif cornerposition[corner[2]][1][0]==edgeposition[edge[2]][1][0] and cornerposition[corner[2]][2][0]==edgeposition[edge[1]][1][0]:
                do("R'UR'U'yR'F'R2U'R'UR'FRF")#10
            elif cornerposition[corner[2]][1][0]==edgeposition[edge[2]][1][0] and cornerposition[corner[1]][2][0]==edgeposition[edge[3]][1][0]:
                do("FRU'R'U'RUR'F'RUR'U'R'FRF'")#11
            if corner[:4] in [[0,1,2,3],[2,0,3,1],[3,2,1,0],[1,3,0,2]] and edge[:4] in [[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]]:
                break
            do("y")
    direction()
    if corner[1]==0:
        do("U'")
    elif corner[2]==0:
        do("U")
    elif corner[3]==0:
        do("U2")

import numpy as np
import matplotlib.pyplot as plt

start=time.time()
grosstotalsteps=[0,0,0,0]
compressedsteps=[]
number=1000
cs=[]
fs=[]
os=[]
ps=[]
totals=[]
ts=[]

for cubes in range(number):
    if cubes%100==0 and cubes!=0:
        print(cubes,sum(totals)/cubes,[i/cubes for i in grosstotalsteps],sum(compressedsteps)/cubes)
    totalstep=0
    totalsteps=[0,0,0,0]
    randomcube()
    solutionstring=""
    t1=time.time()
    solve()
    t2=round(time.time()-t1,3)
    ts.append(t2)
    
    compress.compress(solutionstring)
    compressedsteps.append(compress.compressedstep)
    
    cs.append(totalsteps[0])
    fs.append(totalsteps[1])
    os.append(totalsteps[2])
    ps.append(totalsteps[3])
    totals.append(totalstep)
    for i in range(4):
        grosstotalsteps[i]+=totalsteps[i]
    
end=time.time()
for i in range(4):
    grosstotalsteps[i]/=number
print("total cube solved",number)
print("average steps:",sum(totals)/number)
print("average compressed steps:",sum(compressedsteps)/number)
print("cfop average steps",grosstotalsteps)
print("total time:",end-start,"s")
print("average time:",(end-start)/number,"s")


cs=np.array(cs)
fs=np.array(fs)
os=np.array(os)
ps=np.array(ps)
totals=np.array(totals)
ts=np.array(ts)
compressedsteps=np.array(compressedsteps)

fig=plt.figure(figsize=(20,10))
#fig, axs = plt.subplots(nrows=2, ncols=4, constrained_layout=True)

plt.subplot(2,4,1)
plt.hist(cs,color='r')
plt.title("c")
plt.xlabel("steps")
plt.ylabel("number")
plt.grid()

plt.subplot(2,4,2)
plt.hist(fs,color='g')
plt.title("f")
plt.xlabel("steps")
plt.ylabel("number")
plt.grid()

plt.subplot(2,4,3)
plt.hist(os,color='orange')
plt.title("o")
plt.xlabel("steps")
plt.ylabel("number")
plt.grid()

plt.subplot(2,4,4)
plt.hist(ps,color='b')
plt.title("p")
plt.xlabel("steps")
plt.ylabel("number")
plt.grid()

plt.subplot(2,4,5)
plt.hist(totals,color='y')
plt.title("total")
plt.xlabel("steps")
plt.ylabel("number")
plt.grid()

plt.subplot(2,4,6)
plt.hist(compressedsteps,color='y')
plt.title("compressed STM")
plt.xlabel("steps")
plt.ylabel("number")
plt.grid()

plt.subplot(2,4,7)
plt.scatter(ts,cs,color='k')
plt.title("time")
plt.xlabel("second")
plt.ylabel("C step")
plt.grid()

plt.subplot(2,4,8)
plt.plot(ts,'r-')
plt.title("time")
plt.xlabel("cube")
plt.ylabel("time")
plt.grid()

plt.show()
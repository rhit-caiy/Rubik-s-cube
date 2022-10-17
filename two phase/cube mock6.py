from tkinter import Tk,Canvas
import random,time
import threading

window=Tk()
canvas=Canvas(window,bg="#808080",width=1440,height=810)
window.title("cube")

corner=[i for i in range(8)]#0,1,2,3,4,5,6,7,lub,rub,luf,ruf,ldf,rdf,ldb,rdb
cornerd=[0,0,0,0,5,5,5,5]#white or yellow face direction
edge=[i for i in range(12)]#0,1,2,3,4,5,6,7,8,9,10,11,ub,ul,uf,ur,lb,lf,rf,rb,db,dl,df,dr
edged=[0,0,0,0,1,1,3,3,5,5,5,5]#white or yellow, then blue or green
center=[0,1,2,3,4,5]#center
cc=corner.copy()
ccd=cornerd.copy()
ce=edge.copy()
ced=edged.copy()
cmed=[1,1,3,3]

#paste cube data here


cube=[[i]*9 for i in range(6)]#color representation
facecorner=[[0,2,3,1],[0,6,4,2],[2,4,5,3],[3,5,7,1],[1,7,6,0],[4,6,7,5]]
faceedge=[[0,1,2,3],[1,4,9,5],[2,5,10,6],[3,6,11,7],[0,7,8,4],[10,9,8,11]]
adj=[[4,3,2,1],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[1,2,3,4]]#adjacent face of each
cornerposition=[[[0,0],[1,0],[4,2]],[[0,2],[4,0],[3,2]],[[0,6],[2,0],[1,2]],[[0,8],[3,0],[2,2]],
                [[5,0],[1,8],[2,6]],[[5,2],[2,8],[3,6]],[[5,6],[4,8],[1,6]],[[5,8],[3,8],[4,6]]]#corner face map to position
edgeposition=[[[0,1],[4,1]],[[0,3],[1,1]],[[0,7],[2,1]],[[0,5],[3,1]],
              [[1,3],[4,5]],[[1,5],[2,3]],[[3,3],[2,5]],[[3,5],[4,3]],
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
    ne=edge.copy()
    ned=edged.copy()
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
    nc=corner.copy()
    ncd=cornerd.copy()
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
    ne=edge.copy()
    ned=edged.copy()
    nc=center.copy()
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
    
def rotatec(a):
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
        
def rotatecube(f,t,oc,ocd,oe,oed):
    re=faceedge[f]
    rc=facecorner[f]
    adjf=adj[f]
    ne=oe.copy()
    ned=oed.copy()
    nc=oc.copy()
    ncd=ocd.copy()
    for n in range(4):
        ne[re[n]]=oe[re[n+t-4]]
        nc[rc[n]]=oc[rc[n+t-4]]
        en=oe[re[n]]
        if oed[en]!=f:
            ned[en]=adjf[adjf.index(oed[en])+t-4]
        cn=oc[rc[n]]
        if ocd[cn]!=f:
            ncd[cn]=adjf[adjf.index(ocd[cn])+t-4]
    return [nc,ncd,ne,ned]

def start():
    draw()
    display()
    
def draw():
    canvas.create_rectangle(50,500,150,550,fill="#C0C0C0")
    canvas.create_text(100,525,text="reset")
    canvas.create_rectangle(200,500,300,550,fill="#C0C0C0")
    canvas.create_text(250,525,text="random")
    canvas.create_rectangle(50,560,150,610,fill="#C0C0C0")
    canvas.create_text(100,585,text="solve")
    canvas.create_rectangle(200,560,300,610,fill="#C0C0C0")
    canvas.create_text(250,585,text="random and solve")
    canvas.create_rectangle(900,500,1000,550,fill="#C0C0C0")
    canvas.create_text(950,525,text="input")
    for i in range(12):
        canvas.create_rectangle(100*i+110,650,100*i+190,690,fill="#C0C0C0")
        canvas.create_text(100*i+140,670,text=rotates[i])
    for i in range(12):
        canvas.create_rectangle(100*i+110,700,100*i+190,740,fill="#C0C0C0")
        canvas.create_text(100*i+140,720,text=rotates[i]+"'")
        
def click(coordinate):
    global cube,corner,cornerd,edge,edged,center
    x=coordinate.x
    y=coordinate.y
    if 650<y<690:
        a=(x-100)//100
        if 0<=a<=5:
            rotate(a)
        elif 6<=a<=8:
            rotatemiddle(a-6)
        elif 9<=a<=11:
            rotatec(a-9)
    elif 700<y<740:
        a=(x-100)//100
        if 0<=a<=5:
            rotate(a)
            rotate(a)
            rotate(a)
        elif 6<=a<=8:
            rotatemiddle(a-6)
            rotatemiddle(a-6)
            rotatemiddle(a-6)
        elif 9<=a<=11:
            rotatec(a-9)
            rotatec(a-9)
            rotatec(a-9)
    elif 50<x<150 and 500<y<550:
        cube=[[i+1]*9 for i in range(6)]
        corner=[i for i in range(8)]
        cornerd=[0,0,0,0,5,5,5,5]
        edge=[i for i in range(12)]
        edged=[0,0,0,0,1,1,3,3,5,5,5,5]
        center=[0,1,2,3,4,5]
    elif 200<x<300 and 500<y<550:
        randomcube()
        print("random")
        print("cube =",cube)
        print("corner =",corner)
        print("cornerd =",cornerd)
        print("edge =",edge)
        print("edged =",edged)
        print("center =",center)
    elif 50<x<150 and 560<y<610:
        print("solve")
        print("cube =",cube)
        print("corner =",corner)
        print("cornerd =",cornerd)
        print("edge =",edge)
        print("edged =",edged)
        print("center =",center)
        solve()
    elif 200<x<300 and 560<y<610:
        randomcube()
        print("random and solve")
        print("cube =",cube)
        print("corner =",corner)
        print("cornerd =",cornerd)
        print("edge =",edge)
        print("edged =",edged)
        print("center =",center)
        solve()
    elif 900<x<1000 and 500<y<550:
        i=input("input:")
        if i.isdigit():
            i=rotatenumbertostring(i)
        do(i)
    display()
    
def keypress(key):
    k=key.keysym
    print(k)
    if k=='U':
        rotate(0)
    elif k=='L':
        rotate(1)
    elif k=='F':
        rotate(2)
    elif k=='R':
        rotate(3)
    elif k=='B':
        rotate(4)
    elif k=='D':
        rotate(5)
    elif k=="M":
        rotatemiddle(0)
    elif k=="E":
        rotatemiddle(1)
    elif k=="S":
        rotatemiddle(2)
    elif k=='x':
        rotatec(0)
    elif k=='y':
        rotatec(1)
    elif k=='z':
        rotatec(2)
    display()
    
def display():
    updatecube()
    canvas.delete("all")
    draw()
    for i in range(6):
        x=0
        y=0
        if i==0:
            x=500
            y=0
        elif i==5:
            x=500
            y=400
        else:
            x=i*200+100
            y=200
        for j in range(3):
            for k in range(3):
                canvas.create_rectangle(x+60*k,y+60*j+20,x+60*k+60,y+60*j+80,fill=color[cube[i][3*j+k]])
    canvas.update()
    time.sleep(0.5)
    
def updatecube():
    global cube
    #center
    for i in range(6):
        cube[i][4]=center[i]
    #edge
    for i in range(12):
        b=edge[i]#block number
        if edged[b]==edgeposition[i][0][0]:
            cube[edgeposition[i][0][0]][edgeposition[i][0][1]]=edgeposition[edge[i]][0][0]
            cube[edgeposition[i][1][0]][edgeposition[i][1][1]]=edgeposition[edge[i]][1][0]
        else:
            cube[edgeposition[i][0][0]][edgeposition[i][0][1]]=edgeposition[edge[i]][1][0]
            cube[edgeposition[i][1][0]][edgeposition[i][1][1]]=edgeposition[edge[i]][0][0]
    #corner
    for i in range(8):
        b=corner[i]
        if cornerd[b]==cornerposition[i][0][0]:
            cube[cornerposition[i][0][0]][cornerposition[i][0][1]]=cornerposition[corner[i]][0][0]
            cube[cornerposition[i][1][0]][cornerposition[i][1][1]]=cornerposition[corner[i]][1][0]
            cube[cornerposition[i][2][0]][cornerposition[i][2][1]]=cornerposition[corner[i]][2][0]
        elif cornerd[b]==cornerposition[i][1][0]:
            cube[cornerposition[i][0][0]][cornerposition[i][0][1]]=cornerposition[corner[i]][2][0]
            cube[cornerposition[i][1][0]][cornerposition[i][1][1]]=cornerposition[corner[i]][0][0]
            cube[cornerposition[i][2][0]][cornerposition[i][2][1]]=cornerposition[corner[i]][1][0]
        else:
            cube[cornerposition[i][0][0]][cornerposition[i][0][1]]=cornerposition[corner[i]][1][0]
            cube[cornerposition[i][1][0]][cornerposition[i][1][1]]=cornerposition[corner[i]][2][0]
            cube[cornerposition[i][2][0]][cornerposition[i][2][1]]=cornerposition[corner[i]][0][0]

def randomcube():
    a=random.randrange(64,128)
    randomstring=""
    for i in range(a):
        r=random.randrange(0,9)
        if r<6:
            rotate(r)
        else:
            rotatemiddle(r-6)
        randomstring+=rotates[r]
    print("mix up steps:",randomstring)
        
#letters to action
def do(s):
    l=len(s)
    rotates=["U","L","F","R","B","D","M","E","S","x","y","z"]
    i=0
    while i<l:
        a=rotates.index(s[i])
        if 0<=a<=5:
            rotate(a)
        elif 6<=a<=8:
            rotatemiddle(a-6)
        elif 9<=a<=11:
            rotatec(a-9)
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
                    rotatec(a-9)
                    rotatec(a-9)
            elif s[i]=='2':
                i+=1
                if 0<=a<=5:
                    rotate(a)
                elif 6<=a<=8:
                    rotatemiddle(a-6)
                elif 9<=a<=11:
                    rotatec(a-9)
        display()

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
        
def solve():
    global totalstep,solutionstring,minstep
    minstep=stepshouldbelow
    direction()
    solutionstring=phase1(corner,cornerd,edge,edged,0)
    print("solution string",solutionstring)
    solutionstring=rotatenumbertostring(solutionstring)
    print(solutionstring)
    do(solutionstring)
    result=compressstep(solutionstring)
    print("compressed steps",result[3])
    print("STM step:",result[0])
    print("HTM step:",result[1])
    print("QTM step:",result[2])
    
allrotation=[["U","U2","U'"],["L","L2","L'"],["F","F2","F'"],["R","R2","R'"],["B","B2","B'"],["D","D2","D'"]]
def rotatenumbertostring(s):
    r=""
    for i in range(steplen(s)):
        r+=allrotation[int(s[2*i])][int(s[2*i+1])-1]
    return r

phase2rotations=["01","02","03","12","22","32","42","51","52","53"]
medchange=[0,3,4,1,2]

def getdict1(dict1step):
    global dict1
    predictstate=[[cc,ccd,ce,ced,""]]
    newpredictstate=[]
    key=getkey(cc,ccd,ce,ced)
    dict1[key]=""
    print("phase 1 dict")
    print("{:<8}{:<8}{:<16}{:<16}{:<16}".format("dict","step","cubes left","dict 1 length","time"))
    t0=time.time()
    for step in range(1,dict1step+1):
        t1=time.time()
        for cube in predictstate:
            oc=cube[0]
            ocd=cube[1]
            oe=cube[2]
            oed=cube[3]
            oldstep=cube[4]
            for f in range(6):
                if step>2 and (str(f)==oldstep[0] or (str(f)==oldstep[2] and oldstep[0]+oldstep[2] in ["05","50","13","31","24","42"])):
                    continue
                re=faceedge[f]
                rc=facecorner[f]
                adjf=adj[f]
                for t in range(1,4):
                    ne=oe.copy()
                    ned=oed.copy()
                    nc=oc.copy()
                    ncd=ocd.copy()
                    for n in range(4):
                        ne[re[n]]=oe[re[n+t-4]]
                        nc[rc[n]]=oc[rc[n+t-4]]
                        en=oe[re[n]]
                        if oed[en]!=f:
                            ned[en]=adjf[adjf.index(oed[en])+t-4]
                        cn=oc[rc[n]]
                        if ocd[cn]!=f:
                            ncd[cn]=adjf[adjf.index(ocd[cn])+t-4]
                    key=getkey(nc,ncd,ne,ned)
                    if key not in dict1:
                        if step==1:
                            newstep=str(f)
                        else:
                            newstep=str(f)+str(4-t)+oldstep
                        dict1[key]=newstep
                        if step!=dict1step:
                            newpredictstate.append([nc,ncd,ne,ned,newstep])
        
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}".format(1,step,len(newpredictstate),len(dict1),time.time()-t1))
        predictstate=newpredictstate.copy()
        newpredictstate.clear()
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}".format(1,"total",len(newpredictstate),len(dict1),time.time()-t0))
positionsimplify=[0,1,2,1,2,0]
def getkey(c,cd,e,ed):
    cpd=[positionsimplify[cd[c[i]]] for i in range(7)]
    epd=[positionsimplify[ed[e[i]]] for i in range(11)]
    cepd=cpd+epd#18 0-2
    k1=0
    t=1
    for i in cepd:
        k1+=i*t
        t*=3
    mep=sorted([e.index(i) for i in range(4,8)])
    k2=str(mep[0])+str(mep[1]-mep[0]-1)+str(mep[2]-mep[1]-1)+str(mep[3]-mep[2]-1)
    key=str(k1)+k2
    return key

def getdict2(dict2step):
    global dict2
    predictstate=[[cc,ce,cmed,""]]
    newpredictstate=[]
    dict2[str(cc+ce+cmed)]=""
    print("phase 2 dict")
    print("{:<8}{:<8}{:<16}{:<16}{:<16}".format("dict","step","cubes left","dict 2 length","time"))
    t0=time.time()
    for step in range(1,dict2step+1):
        t1=time.time()
        for cube in predictstate:
            oc=cube[0]
            oe=cube[1]
            omed=cube[2]
            oldstep=cube[3]
            for j in phase2rotations:
                if step==1 or oldstep[0]!=j[0] and not (step>2 and j[0]==oldstep[-4] and oldstep[-4]+oldstep[-2] in ["05","50","13","31","24","42"]):
                    f=int(j[0])
                    t=int(j[1])
                    nc=oc.copy()
                    ne=oe.copy()
                    nmed=omed.copy()
                    fe=faceedge[f]
                    fc=facecorner[f]
                    if f==0 or f==5:
                        for k in range(4):
                            ne[fe[k]]=oe[fe[(k+t)-4]]
                            nc[fc[k]]=oc[fc[(k+t)-4]]
                    else:
                        for k in range(4):
                            ne[fe[k]]=oe[fe[k-2]]
                            nc[fc[k]]=oc[fc[k-2]]
                        for e in [fe[1],fe[3]]:
                            en=oe[e]-4
                            if omed[en]!=f:
                                nmed[en]=medchange[omed[en]]
                    key=str(nc+ne+nmed)
                    if key not in dict2:
                        newstep=j[0]+str(4-int(j[1]))+oldstep
                        dict2[key]=newstep
                        if step!=dict2step:
                            newpredictstate.append([nc,ne,nmed,newstep])
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}".format(2,step,len(newpredictstate),len(dict2),time.time()-t1))
        predictstate=newpredictstate.copy()
        newpredictstate.clear()
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}".format(2,"total",len(newpredictstate),len(dict1),time.time()-t0))
    


def phase1(c,cd,e,ed,threadid):
    global minstep
    tstart=time.time()
    cubes=[[c,cd,e,ed,""]]
    newcubes=[]
    solutionnum=0
    minstr="6"*2*minstep
    
    #check first
    key=getkey(c,cd,e,ed)
    if key in dict1:
        solutionnum+=1
        furtherstep=dict1[key]
        if furtherstep=="":
            solution=phase2([c,cd,e,ed],"")
            if solution and steplen(solution)<minstep:
                minstr=solution
                minstep=steplen(solution)
                print("already satisfy for thread {}, step {} {}\n".format(threadid,minstep,solution),end="")
        else:
            phase2cube=[c,cd,e,ed]
            for i in range(int(len(furtherstep)/2)):
                phase2cube=rotatecube(int(furtherstep[2*i]),int(furtherstep[2*i+1]),*phase2cube)
            solution=phase2(rotatecube(int(furtherstep[-1]),1,*phase2cube),furtherstep+"1")
            if solution and steplen(solution)<minstep:
                minstep=steplen(solution)
                minstr=solution
                print("directly in dict, thread {} {} {}\n".format(threadid,minstep,solution),end="")
            solution=phase2(rotatecube(int(furtherstep[-1]),3,*phase2cube),furtherstep+"3")
            if solution and steplen(solution)<minstep:
                minstep=steplen(solution)
                minstr=solution
                print("directly in dict, thread {} {} {}\n".format(threadid,minstep,solution),end="")
            
    for step in range(1,phase1maxstep+1):
        tloop=time.time()
        for cubepack in cubes:
            previousstep=cubepack[4]
            for f in range(6):
                if step==1 or str(f)!=previousstep[-2] and not (step>2 and str(f)==previousstep[-4] and previousstep[-4]+previousstep[-2] in ["05","50","13","31","24","42"]):
                    for t in range(1,4):
                        newcubepack=rotatecube(f,t,*cubepack[:4])
                        nc=newcubepack[0]
                        ncd=newcubepack[1]
                        ne=newcubepack[2]
                        ned=newcubepack[3]
                        newstep=previousstep+str(f)+str(t)
                        key=getkey(nc,ncd,ne,ned)
                        if key in dict1:
                            solutionnum+=1
                            furtherstep=dict1[key]+"1"
                            for i in range(int(len(furtherstep)/2)):
                                #phase2cube=rotatecube(int(furtherstep[2*i]),int(furtherstep[2*i+1]),*phase2cube)
                                oc=nc.copy()
                                ocd=ncd.copy()
                                oe=ne.copy()
                                oed=ned.copy()
                                f1=int(furtherstep[2*i])
                                t1=int(furtherstep[2*i+1])
                                re=faceedge[f1]
                                rc=facecorner[f1]
                                adjf=adj[f1]
                                for n in range(4):
                                    ne[re[n]]=oe[re[n+t1-4]]
                                    nc[rc[n]]=oc[rc[n+t1-4]]
                                    en=oe[re[n]]
                                    if oed[en]!=f1:
                                        ned[en]=adjf[adjf.index(oed[en])+t1-4]
                                    cn=oc[rc[n]]
                                    if ocd[cn]!=f1:
                                        ncd[cn]=adjf[adjf.index(ocd[cn])+t1-4]
                            phase2cube=[nc,ncd,ne,ned]
                            solution=phase2(phase2cube,newstep+furtherstep)
                            if solution and steplen(solution)<minstep:
                                minstep=steplen(solution)
                                minstr=solution
                                print("thread {} find {} {}/{}  verified complete number {} {}\n".format(threadid,minstep,step,phase1maxstep,solutionnum,solution),end="")
                            solution=phase2(rotatecube(int(furtherstep[-1]),2,*phase2cube),newstep+furtherstep[:-1]+"3")
                            if solution and steplen(solution)<minstep:
                                minstep=steplen(solution)
                                minstr=solution
                                print("thread {} find {} {}/{}  verified complete number {} {}\n".format(threadid,minstep,step,phase1maxstep,solutionnum,solution),end="")
                                # print(threadid,minstep,step,"/",phase1maxstep,"verified complete number",solutionnum,solution)
                        elif step!=phase1maxstep:
                            newcubepack.append(newstep)
                            newcubes.append(newcubepack)
        cubes=newcubes.copy()
        newcubes.clear()
        print("{}-{} cubes in list {} thread min {} time {:f}s\n".format(threadid,step,len(cubes),steplen(minstr),time.time()-tloop),end="")
    print("finish thread {}, thread min {} verified complete phase one number {} time {:f}s\n".format(threadid,steplen(minstr),solutionnum,time.time()-tstart),end="")
    return minstr

def phase2(cubepack,s):
    c=cubepack[0]
    cd=cubepack[1]
    e=cubepack[2]
    ed=cubepack[3]
    phase1len=steplen(s)
    #check first
    if str(c+e+ed[4:8]) in dict2:
        return s+dict2[str(c+e+ed[4:8])]
    elif phase1len+dict2step+1>=minstep:
        return False
    maxstep=min(minstep-phase1len-dict2step-1,phase2maxstep)
    cubes=[[c,cd,e,ed,s]]
    newcubes=[]
    for step in range(1,maxstep+1):
        if phase1len+step+dict2step>=minstep:
            break
        for cube in cubes:
            previousstep=cube[4]
            for r in phase2rotations:
                f=r[0]
                t=r[1]
                if len(previousstep)==0 or f!=previousstep[-2] and not (step>2 and f==previousstep[-4] and previousstep[-4]+previousstep[-2] in ["05","50","13","31","24","42"]):
                    newcubepack=rotatecube(int(f),int(t),*cube[:4])
                    newcorner=newcubepack[0]
                    newcornerd=newcubepack[1]
                    newedge=newcubepack[2]
                    newedged=newcubepack[3]
                    key=str(newcorner+newedge+newedged[4:8])
                    if key in dict2:
                        return previousstep+r+dict2[key]
                    newcubes.append([newcorner,newcornerd,newedge,newedged,previousstep+r])
        cubes=newcubes.copy()
        newcubes.clear()
    return False

def steplen(s):
    return int(len(s)/2)

def initialcube():
    return [cc,ccd,ce,ced]

changebasetable=[[1,5,2,0,4,3],[2,1,5,3,0,4],[0,1,2,3,4,5]]
def getcubewithbase(randomstring,base):
    l=steplen(randomstring)
    cubepack=initialcube()
    for i in range(l):
        f=changebasetable[base][int(randomstring[2*i])]
        t=int(randomstring[2*i+1])
        cubepack=rotatecube(f,t,*cubepack)
    return cubepack

dict1={}
dict2={}
dict1step=6#6
dict2step=7#7
dict1thread=threading.Thread(target=getdict1,args=(dict1step,))
dict2thread=threading.Thread(target=getdict2,args=(dict2step,))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("takes about 20s to finish computing")
tdict=time.time()
dict1thread.start()
dict2thread.start()
dict2thread.join()
dict1thread.join()
print("time",time.time()-tdict,"s")
print("finish dicts",len(dict1),len(dict2))

phase1maxstep=5#6
phase2maxstep=7#5
stepshouldbelow=phase1maxstep+dict1step+phase2maxstep+dict2step
minstep=stepshouldbelow
    
def compressstep(s):
    s=s.replace("2","-")
    s=s.replace("'","--")
    s2=""
    for i in range(len(s)):
        if s[i]=="-":
            s2=s2+s2[-1]
        else:
            s2=s2+s[i]
    s=s2.replace("M","RLLLxxx").replace("E","UDDDyyy").replace("S","BFFFz")
    center=[0,1,2,3,4,5]
    s2=""
    newcenter=center.copy()
    for i in s:
        n=rotates.index(i)
        if n<6:
            s2+=str(center[n])
        elif n>=9:
            #RUF
            rotatecube=[3,0,2]
            n-=9
            for j in range(4):
                newcenter[adj[rotatecube[n]][(j+1)%4]]=center[adj[rotatecube[n]][j]]
            center=newcenter.copy()
    anti=[[0,5],[1,3],[2,4]]
    g=[]
    m=0
    n=0
    for i in s2:
        i=int(i)
        if i in anti[0]:
            n=0
        elif i in anti[1]:
            n=1
        elif i in anti[2]:
            n=2
        m=anti[n].index(i)
        if g==[]:
            g=[[n,0,0]]
        if g[-1][0]!=n:
            g.append([n,0,0])
        g[-1][m+1]+=1
    for i in g:
        i[1]%=4
        i[2]%=4
    g=[i for i in g if not (i[1]==0 and i[2]==0)]
    middlerotation=[["Ey","E2y2","E'y'"],["M'x'","M2x2","Mx"],["S'z","S2z2","Sz'"]]
    #stm<=htm<=qtm
    stm=0
    htm=0
    qtm=0
    s=""
    for i in g:
        a=i[1]
        b=i[2]
        if a==4-b:
            s+=middlerotation[i[0]][a-1]
            stm+=1
        elif a==0:
            s+=allrotation[anti[i[0]][1]][b-1]
            stm+=1
        elif b==0:
            s+=allrotation[anti[i[0]][0]][a-1]
            stm+=1
        else:
            s+=allrotation[anti[i[0]][0]][a-1]+allrotation[anti[i[0]][1]][b-1]
            stm+=2
        if a!=0:
            htm+=1
            qtm+=1
            if a==2:
                qtm+=1
        if b!=0:
            htm+=1
            qtm+=1
            if b==2:
                qtm+=1
    return [stm,htm,qtm,s]


canvas.bind("<Button-1>",click)
canvas.bind_all("<KeyPress>",keypress)
start()
canvas.pack()
window.mainloop()
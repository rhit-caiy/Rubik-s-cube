from time import time,strftime,localtime,sleep
from random import randint
from math import log
from itertools import permutations,product,combinations
from tkinter import Tk,Canvas
#based on two phase algorithm version 27 and 28
print(strftime("%Y-%m-%d %H:%M:%S",localtime()))

cc,cco,ce,ceo=(0,1,2,3,4,5,6,7),(0,0,0,0,3,3,3,3),(0,1,2,3,4,5,6,7,8,9,10,11),(0,0,0,0,1,1,4,4,3,3,3,3)
facecorner=((0,2,3,1),(0,6,4,2),(2,4,5,3),(4,6,7,5),(3,5,7,1),(1,7,6,0))
faceedge=((0,1,2,3),(1,4,9,5),(2,5,10,6),(10,9,8,11),(3,6,11,7),(0,7,8,4))
facetimedirection=(((0,5,1,3,2,4),(0,4,5,3,1,2)),((2,1,3,5,4,0),(3,1,5,0,4,2)),((4,0,2,1,3,5),(3,4,2,0,1,5)),((0,2,4,3,5,1),(0,4,5,3,1,2)),((5,1,0,2,4,3),(3,1,5,0,4,2)),((1,3,2,4,0,5),(3,4,2,0,1,5)))
cornerdirection=((0,5,1),(0,4,5),(0,1,2),(0,2,4),(3,2,1),(3,4,2),(3,1,5),(3,5,4))
edgedirection=((0,5),(0,1),(0,2),(0,4),(1,5),(1,2),(4,2),(4,5),(3,5),(3,1),(3,2),(3,4))
adj=((5,4,2,1),(0,2,3,5),(0,4,3,1),(1,2,4,5),(0,5,3,2),(0,1,3,4))
#the position of each face of each block
cornerposition=(((0,0),(5,2),(1,0)),((0,2),(4,2),(5,0)),((0,6),(1,2),(2,0)),((0,8),(2,2),(4,0)),
                ((3,0),(2,6),(1,8)),((3,2),(4,6),(2,8)),((3,6),(1,6),(5,8)),((3,8),(5,6),(4,8)))
edgeposition=(((0,1),(5,1)),((0,3),(1,1)),((0,7),(2,1)),((0,5),(4,1)),
              ((1,3),(5,5)),((1,5),(2,3)),((4,3),(2,5)),((4,5),(5,3)),
              ((3,7),(5,7)),((3,3),(1,7)),((3,1),(2,7)),((3,5),(4,7)))
centeredge=((0,2,10,8),(4,5,6,7),(1,3,11,9))
color=("#FFFF00","#0000FF","#FF0000","#FFFFFF","#00FF00","#FF8000")
allrotation=("U","U2","U'","L","L2","L'","F","F2","F'","D","D2","D'","R","R2","R'","B","B2","B'","M","M2","M'","E","E2","E'","S","S2","S'","x","x2","x'","y","y2","y'","z","z2","z'")
eighteen=tuple([18**i for i in range(28)])

#initialize
t0=time()
#dicts: contains number presentations of all corner and edge positions
#tuple->index
#corner 40320 8!
cdict={i:n for n,i in enumerate(permutations(cc))}
#corner orientation 2187 3**7
codict={i:n for n,i in enumerate((i for i in product(range(3),repeat=8) if not sum(i)%3))}
#edge orientation 2048 2**11
eodict={i:n for n,i in enumerate([i for i in product(range(2),repeat=12) if not i.count(1)%2])}
#4 edge position 495 C(12,4)
ep4dict={j:n for n,j in enumerate(j for i in combinations(ce,r=4) for j in permutations(i))}
#index->tuple
rcdict={cdict[key]:key for key in cdict}
rcodict={codict[key]:key for key in codict}
rep4dict={ep4dict[key]:key for key in ep4dict}
reodict={eodict[key]:key for key in eodict}
#list contains length of 0, rotation list
cl,col,eol,ep4l,cr,cor,eor,ep4r=[0]*len(cdict),[0]*len(codict),[0]*len(eodict),[0]*len(ep4dict),[],[],[],[]
add1,add2=[1,2,0],[2,0,1]
for f in 0,1,2,3,4,5:
    c1,c2,c3,c4=facecorner[f]
    e1,e2,e3,e4=fe=faceedge[f]
    sfe=set(fe)
    fte=e2,e3,e4,e1
    d0,d1,d2=cl.copy(),cl.copy(),cl.copy()
    for a,dc in enumerate(cdict):
        c=list(dc)
        c[c1],c[c2],c[c3],c[c4]=c[c2],c[c3],c[c4],c[c1]
        b=cdict[tuple(c)]
        d0[a],d2[b]=b,a
        if not d1[a]:
            c[c1],c[c2],c[c3],c[c4]=c[c2],c[c3],c[c4],c[c1]
            b=cdict[tuple(c)]
            d1[a],d1[b]=b,a
    cr.append((tuple(d0),tuple(d1),tuple(d2)))
    d0,d1,d2=col.copy(),col.copy(),col.copy()
    if f!=0 and f!=3:
        for a,dco in enumerate(codict):
            co=list(dco)
            co[c1],co[c2],co[c3],co[c4]=add1[co[c2]],add2[co[c3]],add1[co[c4]],add2[co[c1]]
            b=codict[tuple(co)]
            d0[a],d2[b]=b,a
            if not d1[a]:
                co[c1],co[c2],co[c3],co[c4]=add1[co[c2]],add2[co[c3]],add1[co[c4]],add2[co[c1]]
                b=codict[tuple(co)]
                d1[a],d1[b]=b,a
    else:
        for a,dco in enumerate(codict):
            co=list(dco)
            co[c1],co[c2],co[c3],co[c4]=co[c2],co[c3],co[c4],co[c1]
            b=codict[tuple(co)]
            d0[a],d2[b]=b,a
            if not d1[a]:
                co[c1],co[c2],co[c3],co[c4]=co[c2],co[c3],co[c4],co[c1]
                b=codict[tuple(co)]
                d1[a],d1[b]=b,a
    cor.append((tuple(d0),tuple(d1),tuple(d2)))
    d0,d1,d2=eol.copy(),eol.copy(),eol.copy()
    if f==1 or f==4:
        for a,deo in enumerate(eodict):
            eo=list(deo)
            eo[e1],eo[e2],eo[e3],eo[e4]=1-eo[e2],1-eo[e3],1-eo[e4],1-eo[e1]
            b=eodict[tuple(eo)]
            d0[a],d2[b]=b,a
            if not d1[a]:
                eo[e1],eo[e2],eo[e3],eo[e4]=1-eo[e2],1-eo[e3],1-eo[e4],1-eo[e1]
                b=eodict[tuple(eo)]
                d1[a],d1[b]=b,a
    else:
        for a,deo in enumerate(eodict):
            eo=list(deo)
            eo[e1],eo[e2],eo[e3],eo[e4]=eo[e2],eo[e3],eo[e4],eo[e1]
            b=eodict[tuple(eo)]
            d0[a],d2[b]=b,a
            if not d1[a]:
                eo[e1],eo[e2],eo[e3],eo[e4]=eo[e2],eo[e3],eo[e4],eo[e1]
                b=eodict[tuple(eo)]
                d1[a],d1[b]=b,a
    eor.append((tuple(d0),tuple(d1),tuple(d2)))
    d0,d1,d2=ep4l.copy(),ep4l.copy(),ep4l.copy()
    for a,dep in enumerate(ep4dict):
        ep=list(dep)
        for i in 0,1,2,3:
            if (x:=ep[i]) in sfe:
                ep[i]=fe[fte.index(x)]
        b=ep4dict[tuple(ep)]
        d0[a],d2[b]=b,a
        if not d1[a]:
            for i in 0,1,2,3:
                if (x:=ep[i]) is not dep[i]:
                    ep[i]=fe[fte.index(x)]
            b=ep4dict[tuple(ep)]
            d1[a],d1[b]=b,a
    ep4r.append((tuple(d0),tuple(d1),tuple(d2)))
cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1=tuple(cr),tuple(cor),tuple(ep4r),tuple(eor),cdict[(0,1,2,3,4,5,6,7)],codict[(0,0,0,0,0,0,0,0)],ep4dict[(0,1,2,3)],ep4dict[(4,5,6,7)],ep4dict[(8,9,10,11)],eodict[(0,0,0,0,0,0,0,0,0,0,0,0)],tuple([i[0] for i in cr]),tuple([i[0] for i in cor]),tuple([i[0] for i in eor]),tuple([i[0] for i in ep4r]),tuple([i[1] for i in cr]),tuple([i[1] for i in ep4r])

#dict for directly complete cube
#1 19
#2 262
#3 3502
#4 46741
#5 621649
#6 8240087
#7 109043123
def getdict0(dict0step):
    print("\ndict0\n{:<8}{:<16}{:<16}{:<16}".format("step","cubes left","dict length","time/s"))
    dict0={ccn+40320*(ccon+2187*(ceon+2048*(cen3+11880*(cen2+11880*cen1)))):1}
    predictstate,newpredictstate=[(ccn,ccon,ceon,cen1,cen2,cen3,0,-1)],[]
    t0=time()
    for step in range(1,dict0step+1):
        t1=time()
        eighteen0,eighteen1=eighteen[step-1],eighteen[step]
        for cube in predictstate:
            oc,oco,oeo,oe1,oe2,oe3,oldstep,f1=cube
            for f in 0,1,2,3,4,5:
                if f1 is not f:
                    crf0,ep4rf0=cr0[f],ep4r0[f]
                    corf0,eorf0=cor0[f],eor0[f]
                    nc,nco,neo,ne1,ne2,ne3=oc,oco,oeo,oe1,oe2,oe3
                    for t in 2,1,0:
                        nc,nco,neo,ne1,ne2,ne3=crf0[nc],corf0[nco],eorf0[neo],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                        if (key0:=nc+40320*(nco+2187*(neo+2048*(ne3+11880*(ne2+11880*ne1))))) not in dict0:
                            newstep=oldstep+(3*f+t)*eighteen0
                            dict0[key0]=newstep+eighteen1
                            if step is not dict0step:
                                newpredictstate.append((nc,nco,neo,ne1,ne2,ne3,newstep,f))
        print("{:<8}{:<16}{:<16}{:<16f}".format(step,len(newpredictstate),len(dict0),time()-t1))
        predictstate,newpredictstate=newpredictstate,[]
    return dict0,round(time()-t0,6)

#dict for complete phase 1, remove correct one
#1 4
#2 54
#3 647
#4 7802
#5 95038
#6 1138855
#7 13209133
#8 138155501
def getdict1(dict1step,cor0,eor0,ep4r0):
    print("\ndict1\n{:<8}{:<16}{:<16}{:<16}".format("step","cubes left","dict length","time/s"))
    dict1={425:1}#cen2//24+495*(ceon+2048*ccon)
    predictstate,newpredictstate=[(0,0,10200,1,-1)],[]
    t0=time()
    for step in range(1,dict1step+1):
        t1=time()
        for cube in predictstate:
            oco,oeo,oe2,oldstep,f1=cube
            oldstep=18*oldstep
            for f in 0,1,2:
                if f1 is not f and f1-f!=3:
                    newstep=oldstep+3*f
                    nco,neo,ne2=oco,oeo,oe2
                    corf0,eorf0,ep4rf0=cor0[f],eor0[f],ep4r0[f]
                    for newstep in [newstep+2,newstep+1,newstep]:
                        nco,neo,ne2=corf0[nco],eorf0[neo],ep4rf0[ne2]
                        if (key1:=ne2//24+495*(neo+2048*nco)) not in dict1:
                            dict1[key1]=newstep
                            if step is not dict1step:
                                newpredictstate.append((nco,neo,ne2,newstep,f))
            for f in 3,4,5:
                if f1 is not f:
                    newstep=oldstep+3*f
                    nco,neo,ne2=oco,oeo,oe2
                    corf0,eorf0,ep4rf0=cor0[f],eor0[f],ep4r0[f]
                    for newstep in [newstep+2,newstep+1,newstep]:
                        nco,neo,ne2=corf0[nco],eorf0[neo],ep4rf0[ne2]
                        if (key1:=ne2//24+495*(neo+2048*nco)) not in dict1:
                            dict1[key1]=newstep
                            if step is not dict1step:
                                newpredictstate.append((nco,neo,ne2,newstep,f))
        print("{:<8}{:<16}{:<16}{:<16f}".format(step,len(newpredictstate),len(dict1),time()-t1))
        predictstate,newpredictstate=newpredictstate,[]
    dict1.pop(425)
    return dict1,round(time()-t0,6)

#dict for complete phase 2
#1 11
#2 78
#3 534
#4 3613
#5 23561
#6 146635
#7 883485
#8 5068603
#9 27699336
def getdict2(dict2step,eighteen,cr0,ep4r0,cr1,ep4r1):
    print("\ndict2\n{:<8}{:<16}{:<16}{:<16}".format("step","cubes left","dict length","time/s"))
    dict2={121187856:1}#cen3+11880*(cen2+11880*(cen1+11880*ccn))
    predictstate,newpredictstate=[(0,0,10200,11856,0,-1)],[]
    t0=time()
    for step in range(1,dict2step+1):
        t1=time()
        eighteen0,eighteen1=eighteen[step-1],eighteen[step]
        for cube in predictstate:
            oc,oe1,oe2,oe3,oldstep,f1=cube
            for f in 4,5:
                if f1 is not f:
                    ep4rf1=ep4r1[f]
                    nc,ne1,ne2,ne3=cr1[f][oc],ep4rf1[oe1],ep4rf1[oe2],ep4rf1[oe3]
                    if (key2:=ne3+11880*(ne2+11880*(ne1+11880*nc))) not in dict2:
                        newstep=oldstep+(3*f+1)*eighteen0
                        dict2[key2]=newstep+eighteen1
                        if step is not dict2step:
                            newpredictstate.append((nc,ne1,ne2,ne3,newstep,f))
            for f in 1,2:
                if f1 is not f and f1-f!=3:
                    ep4rf1=ep4r1[f]
                    nc,ne1,ne2,ne3=cr1[f][oc],ep4rf1[oe1],ep4rf1[oe2],ep4rf1[oe3]
                    if (key2:=ne3+11880*(ne2+11880*(ne1+11880*nc))) not in dict2:
                        newstep=oldstep+(3*f+1)*eighteen0
                        dict2[key2]=newstep+eighteen1
                        if step is not dict2step:
                            newpredictstate.append((nc,ne1,ne2,ne3,newstep,f))
            if f1!=3:
                crf0,ep4rf0=cr0[3],ep4r0[3]
                nc,ne1,ne2,ne3=oc,oe1,oe2,oe3
                for t in 2,1,0:
                    nc,ne1,ne2,ne3=crf0[nc],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                    if (key2:=ne3+11880*(ne2+11880*(ne1+11880*nc))) not in dict2:
                        newstep=oldstep+(9+t)*eighteen0
                        dict2[key2]=newstep+eighteen1
                        if step is not dict2step:
                            newpredictstate.append((nc,ne1,ne2,ne3,newstep,3))
                if f1!=0:
                    crf0,ep4rf0=cr0[0],ep4r0[0]
                    nc,ne1,ne2,ne3=oc,oe1,oe2,oe3
                    for t in 2,1,0:
                        nc,ne1,ne2,ne3=crf0[nc],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                        if (key2:=ne3+11880*(ne2+11880*(ne1+11880*nc))) not in dict2:
                            newstep=oldstep+t*eighteen0
                            dict2[key2]=newstep+eighteen1
                            if step is not dict2step:
                                newpredictstate.append((nc,ne1,ne2,ne3,newstep,0))
        print("{:<8}{:<16}{:<16}{:<16f}".format(step,len(newpredictstate),len(dict2),time()-t1))
        predictstate,newpredictstate=newpredictstate,[]
    return dict2,round(time()-t0,6)

window=Tk()
canvas=Canvas(window,bg="#808080",width=1440,height=810)
window.title("cube")

def rotatemiddle(a):
    global e1,e2,e3,eo,center
    #LDF for MES
    edge=[(rep4dict[e1]+rep4dict[e2]+rep4dict[e3]).index(i) for i in range(12)]
    edged=[edgedirection[n][i] for n,i in enumerate(reodict[eo])]
    ne=list(edge)
    ned=list(edged)
    nc=center.copy()
    facenum=0
    if a==0:
        facenum=1
    elif a==1:
        facenum=3
    else:
        facenum=2
    for i in range(4):
        nc[adj[facenum][i]]=center[adj[facenum][i-1]]
    for i in range(4):
        ne[centeredge[a][i]]=edge[centeredge[a][i-1]]
    me1,me2,me3,me4=centeredge[a]
    for i in range(4):
        ned[centeredge[a][i-1]]=edgedirection[centeredge[a][i-1]][edged[centeredge[a][i]]==edgedirection[centeredge[a][i]][0]]
    
    center=nc
    ned=[edgedirection[i].index(ned[i]) for i in range(12)]
    eo=eodict[tuple(ned)]
    e1=ep4dict[tuple([ne.index(i) for i in range(0,4)])]
    e2=ep4dict[tuple([ne.index(i) for i in range(4,8)])]
    e3=ep4dict[tuple([ne.index(i) for i in range(8,12)])]

def rotatecube(a):
    if a==0:
        rotatemiddle(0)
        rotatemiddle(0)
        rotatemiddle(0)
        rotate(4,0)
        rotate(1,2)
    elif a==1:
        rotatemiddle(1)
        rotatemiddle(1)
        rotatemiddle(1)
        rotate(0,0)
        rotate(3,2)
    elif a==2:
        rotatemiddle(2)
        rotate(2,0)
        rotate(5,2)

def rotate(f,t):
    global c,co,e1,e2,e3,eo
    c=cr[f][t][c]
    co=cor[f][t][co]
    eo=eor[f][t][eo]
    ep4rft=ep4r[f][t]
    e1,e2,e3=ep4rft[e1],ep4rft[e2],ep4rft[e3]

def start():
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
    canvas.create_rectangle(900,560,1000,610,fill="#C0C0C0")
    canvas.create_text(950,585,text="replay")
    canvas.create_rectangle(1050,500,1150,550,fill="#C0C0C0")
    canvas.create_text(1100,525,text="?")
    canvas.create_rectangle(1050,560,1150,610,fill="#C0C0C0")
    canvas.create_text(1100,585,text="back")
    for i in range(12):
        for j in range(3):
            canvas.create_rectangle(100*i+110,650+50*j,100*i+190,690+50*j,fill="#C0C0C0")
            canvas.create_text(100*i+140,670+50*j,text=allrotation[3*i+j])
    if solving==1:
        for i in range(threadn):
            x=200
            y=20+100*i
            w=1000
            y1=80+100*i
            canvas.create_rectangle(x,y,x+w,y1)
            canvas.create_text(x-20,(y+y1)/2,text=str(i))
        
def click(coordinate):
    global cubecolor,c,co,eo,e1,e2,e3,center
    if solving:
        return
    x=coordinate.x
    y=coordinate.y
    a=(x-100)//100
    if 650<y<690:
        if 0<=a<=5:
            rotate(a,0)
        elif 6<=a<=8:
            rotatemiddle(a-6)
        elif 9<=a<=11:
            rotatecube(a-9)
    elif 700<y<740:
        if 0<=a<=5:
            rotate(a,1)
        elif 6<=a<=8:
            rotatemiddle(a-6)
            rotatemiddle(a-6)
        elif 9<=a<=11:
            rotatecube(a-9)
            rotatecube(a-9)
    elif 750<y<790:
        if 0<=a<=5:
            rotate(a,2)
        elif 6<=a<=8:
            rotatemiddle(a-6)
            rotatemiddle(a-6)
            rotatemiddle(a-6)
        elif 9<=a<=11:
            rotatecube(a-9)
            rotatecube(a-9)
            rotatecube(a-9)
    elif 50<x<150 and 500<y<550:
        c=ccn
        co=ccon
        e1=cen1
        e2=cen2
        e3=cen3
        eo=ceon
        center=[0,1,2,3,4,5]
        cubecolor=[[i]*9 for i in range(6)]
    elif 200<x<300 and 500<y<550:
        randomcube()
        print("random")
        print("cube =",cubecolor)
        print(f"c = {c} ; co = {co} ; eo = {eo} ; e1 = {e1} ; e2 = {e2} ; e3 = {e3}")
    elif 50<x<150 and 560<y<610:
        print("solve")
        print("cube =",cubecolor)
        print(f"c = {c} ; co = {co} ; eo = {eo} ; e1 = {e1} ; e2 = {e2} ; e3 = {e3}")
        solvecube()
    elif 200<x<300 and 560<y<610:
        randomcube()
        display()
        print("random and solve")
        print("cube =",cubecolor)
        print(f"c = {c} ; co = {co} ; eo = {eo} ; e1 = {e1} ; e2 = {e2} ; e3 = {e3}")
        solvecube()
    elif 900<x<1000 and 500<y<550:
        print("\ninput input mode:\n1: rotation notation, ULFDRB\n2: rotation in number from 0 to 17\n3: in 18decimal\n4: number of c,co,eo,e1,e2,e3, split by comma")
        i=input("input type:")
        v=input("input value:")
        if i=="1":
            v=rotatestringtonumber(v)
        elif i=="2":
            pass
        elif i=="3":
            v=decodevalue(int(v))
        if i in "123" and len(i)==1:
            for j in range(len(v)//2):
                rotate(int(v[2*j]),int(v[2*j+1]))
        elif i=="4":
            c,co,eo,e1,e2,e3=[int(value) for value in v.split(",")]

    elif 900<x<1000 and 560<y<610:
        replay()
    elif 1050<x<1150 and 500<y<550:
        pass
    elif 1050<x<1150 and 560<y<610:
        loadhistory()
    display()
    addhistory()

keydict={'W':(1,2),'A':(0,0),'S':(1,0),'D':(0,2),'R':(2,0),'F':(2,2),'I':(4,0),'J':(0,0),'K':(4,2),'L':(0,2),'Y':(2,2),'H':(2,0),'Z':(3,2),'M':(3,0),'X':(3,0),'N':(3,2)}
def keypress(key):
    if solving:
        return
    k=key.keysym
    print(k)
    if len(k)==1:
        if k in "012345":
            rotate(int(k),0)
        elif k in "ulfdrb":
            rotate("ulfdrb".index(k),0)
        elif k in "mes":
            rotatemiddle("mes".index(k))
        elif k in "xyz":
            rotatecube("xyz".index(k))
        elif k in keydict:
            f,t=keydict[k]
            rotate(f,t)
        elif k=="G":
            rotatemiddle(0)
        elif k=="T":
            for i in range(3):
                rotatemiddle(0)
        elif k=="[":
            rotatecube(1)
        elif k=="]":
            for i in range(3):
                rotatecube(1)
    elif k in ("Up","Down","Left","Right","Next","Prior"):
        v=("Up","Down","Left","Right","Next","Prior").index(k)
        for i in range(v%2*2+1):
            rotatecube(v//2)
    elif k=="Return":
        solvecube()
    elif k=="space":
        randomcube()
        solvecube()
    elif k=="BackSpace":
        loadhistory()
    display()
    addhistory()

def display():
    updatecubecolor()
    canvas.delete("all")
    draw()
    xy=((500,0),(300,200),(500,200),(500,400),(700,200),(900,200))
    for i in range(6):
        x,y=xy[i]
        for j in range(3):
            for k in range(3):
                canvas.create_rectangle(x+60*k,y+60*j+20,x+60*k+60,y+60*j+80,fill=color[cubecolor[i][3*j+k]])
    canvas.update()
    
def updatecubecolor():
    global cubecolor
    #center
    for i in range(6):
        cubecolor[i][4]=center[i]
    #edge
    edge=[0]*12
    for n,i in enumerate(rep4dict[e1]+rep4dict[e2]+rep4dict[e3]):
        edge[i]=n
    edged=reodict[eo]
    for i in range(12):
        n=edged[i]
        for j in 0,1:
            a,b=edgeposition[i][j]
            cubecolor[a][b]=edgedirection[edge[i]][n-j]
    #corner
    corner=rcdict[c]
    cornerd=rcodict[co]
    for i in range(8):
        n=cornerd[i]
        for j in 0,1,2:
            a,b=cornerposition[i][j]
            cubecolor[a][b]=cornerdirection[corner[i]][j-n]

def addhistory():
    global history
    if (c,co,eo,e1,e2,e3,center)!=history[-1]:
        history.append((c,co,eo,e1,e2,e3,center))

def loadhistory():
    global history,c,co,eo,e1,e2,e3,center
    if len(history)>1:
        history.pop()
        c,co,eo,e1,e2,e3,center=history[-1]
        display()

def randomcube():
    for i in range(randint(1024,2048)):
        rotate(randint(0,5),randint(0,2))
    addhistory()
    
def randomcolor():
    c="#"
    for i in range(6):
        c+=hex(randint(0,15))[2:]
    return c

#solve the cube with c,co,eo,e1,e2,e3 numbers
def solve(c,co,eo,e1,e2,e3,threadid,htm,qtm,stm,minmove,phase1step,cr0,cor0,eor0,ep4r0,cr1,ep4r1,cr,ep4r,dict1,dict2,eighteen):
    tstart=time()
    cubes=[(c,co,eo,e1,e2,e3,1,0,-1)]
    n=0
    total=totalnums[phase1step-1]
    x=200
    y=20+100*threadid
    w=1000
    y1=80+100*threadid
    cl=randomcolor()
    drawnum=total//1000
    if threadid:
        while cubes:
            n=1+n
            if not n%drawnum:
                p=n/total
                canvas.create_line(x+w*p,y,x+w*p,y1,fill=cl)
                canvas.update()
                
            oc,oco,oeo,oe1,oe2,oe3,oldstep,step,f1=cubes.pop()
            step,oldstep=1+step,18*oldstep
            for f in 0,1,2,3,4,5:
                if f is not f1 and f1-f!=3:
                    m1_1=oldstep+3*f
                    crf0,corf0,eorf0,ep4rf0=cr0[f],cor0[f],eor0[f],ep4r0[f]
                    nc,nco,neo,ne1,ne2,ne3=oc,oco,oeo,oe1,oe2,oe3
                    for m1 in m1_1,m1_1+1,m1_1+2:
                        nc,nco,neo,ne1,ne2,ne3=crf0[nc],corf0[nco],eorf0[neo],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                        if step is not phase1step:
                            cubes.append((nc,nco,neo,ne1,ne2,ne3,m1,step,f))
                        if ne2//24+495*(neo+2048*nco) in dict1:
                            m1_2,f0,nc1,ne11,ne21,ne31=18*dict1[ne2//24+495*(neo+2048*nco)],f,nc,ne1,ne2,ne3
                            while (m1_2:=m1_2//18)>=18:
                                f0,t0,m1=m1_2//3%6,m1_2%3,18*m1+m1_2%18
                                ep4rf0t0=ep4r[f0][t0]
                                nc1,ne11,ne21,ne31=cr[f0][t0][nc1],ep4rf0t0[ne11],ep4rf0t0[ne21],ep4rf0t0[ne31]
                            if ne31+11880*(ne21+11880*(ne11+11880*nc1)) in dict2:
                                m2=dict2[ne31+11880*(ne21+11880*(ne11+11880*nc1))]
                                if (l:=int(log(m1,18))+int(log(m2,18)))<=htm:
                                    cl=randomcolor()
                                    htm,qtm,stm,minmove=solved(m1,m2,minmove,l,qtm,stm,step,tstart,1)
                                    ep4rf01=ep4r1[f0]
                                    nc1,ne11,ne21,ne31=cr1[f0][nc1],ep4rf01[ne11],ep4rf01[ne21],ep4rf01[ne31]
                                    if (key2:=ne31+11880*(ne21+11880*(ne11+11880*nc1))) in dict2:
                                        m2=dict2[key2]
                                        if (l:=int(log(m1,18))+int(log(m2,18)))<=htm:
                                            htm,qtm,stm,minmove=solved(m1-2,m2,minmove,l,qtm,stm,step,tstart,2)
    else:#threadid==0
        while cubes:
            n=1+n
            if not n%drawnum:
                p=n/total
                canvas.create_line(x+w*p,y,x+w*p,y1,fill=cl)
                canvas.update()
            oc,oco,oeo,oe1,oe2,oe3,oldstep,step,f1=cubes.pop()
            step,oldstep=1+step,18*oldstep
            for f in 0,1,2,3,4,5:
                if f is not f1 and f1-f!=3:
                    m1_1=oldstep+3*f
                    crf0,corf0,eorf0,ep4rf0=cr0[f],cor0[f],eor0[f],ep4r0[f]
                    nc,nco,neo,ne1,ne2,ne3=oc,oco,oeo,oe1,oe2,oe3
                    for m1 in m1_1,m1_1+1,m1_1+2:
                        nc,nco,neo,ne1,ne2,ne3=crf0[nc],corf0[nco],eorf0[neo],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                        if step is not phase1step:
                            cubes.append((nc,nco,neo,ne1,ne2,ne3,m1,step,f))
                        if nc+40320*(nco+2187*(neo+2048*(ne3+11880*(ne2+11880*ne1)))) in dict0:
                            m2=dict0[nc+40320*(nco+2187*(neo+2048*(ne3+11880*(ne2+11880*ne1))))]
                            l=int(log(m1,18))+int(log(m2,18))
                            if l<=htm:
                                htm,qtm,stm,minmove=solved(m1,m2,minmove,l,qtm,stm,step,tstart,0)
                                cl=randomcolor()
                        elif ne2//24+495*(neo+2048*nco) in dict1:
                            m1_2,f0,nc1,ne11,ne21,ne31=18*dict1[ne2//24+495*(neo+2048*nco)],f,nc,ne1,ne2,ne3
                            while (m1_2:=m1_2//18)>=18:
                                f0,t0,m1=m1_2//3%6,m1_2%3,18*m1+m1_2%18
                                ep4rf0t0=ep4r[f0][t0]
                                nc1,ne11,ne21,ne31=cr[f0][t0][nc1],ep4rf0t0[ne11],ep4rf0t0[ne21],ep4rf0t0[ne31]
                            if ne31+11880*(ne21+11880*(ne11+11880*nc1)) in dict2:
                                m2=dict2[ne31+11880*(ne21+11880*(ne11+11880*nc1))]
                                if (l:=int(log(m1,18))+int(log(m2,18)))<=htm:
                                    cl=randomcolor()
                                    htm,qtm,stm,minmove=solved(m1,m2,minmove,l,qtm,stm,step,tstart,1)
                                    ep4rf01=ep4r1[f0]
                                    nc1,ne11,ne21,ne31=cr1[f0][nc1],ep4rf01[ne11],ep4rf01[ne21],ep4rf01[ne31]
                                    if (key2:=ne31+11880*(ne21+11880*(ne11+11880*nc1))) in dict2:
                                        m2=dict2[key2]
                                        if (l:=int(log(m1,18))+int(log(m2,18)))<=htm:
                                            htm,qtm,stm,minmove=solved(m1-2,m2,minmove,l,qtm,stm,step,tstart,2)
    
    return htm,qtm,stm,minmove,time()-tstart

#print the solved form solve, solution must be <= current htm
def solved(m1,m2,minmove,l,qtm,stm,step,tstart,rtype):
    n=solution=(m1-1)*eighteen[int(log(m2,18))]+m2
    if solution<minmove:
        minmove=solution
    qtmvalue=stmvalue=l
    n,numstr=18*n,""
    while (n:=n//18)>=18:
        numstr=str(n//3%6)+str(n%3)+numstr
        if numstr[1]=="1":
            qtmvalue+=1
    for i in range(0,len(numstr)-2,2):
        if abs(int(numstr[i])-int(numstr[i+2]))==3 and int(numstr[i+1])+int(numstr[i+3])==2:
            stmvalue-=1
    if qtmvalue<qtm:
        qtm=qtmvalue
    if stmvalue<stm:
        stm=stmvalue
    print("{:<18}{:<6}{:<6}{:<14f}{:<6}{:<36}{}".format(f"{l} = {step} + {l-step-int(log(m2,18))} + {int(log(m2,18))}",qtmvalue,stmvalue,time()-tstart,rtype,solution,numstr))
    return l,qtm,stm,minmove

def rotatenumbertostring(s):
    r=""
    for i in range(len(s)//2):
        r+=allrotation[3*int(s[2*i])+int(s[2*i+1])]
    return r

def rotatestringtonumber(s):
    r=""
    for c in s:
        if c=="2":
            r=r[:-1]+"1"
        elif c=="'" or c=="3":
            r=r[:-1]+"2"
        elif c in allrotation:
            i=allrotation.index(c)
            r+=str(i//3)+"0"
    return r

def decodevalue(num):
    s=""
    num=18*num
    while (num:=num//18)>=18:
        s=str(num//3%6)+str(num%3)+s
    return s

def reverserotation(s):
    r=""
    for i in range(len(s)//2):
        r=s[2*i]+str(2-int(s[2*i+1]))+r
    return r

total=[round((-(6-3*6**0.5)**n*(-3+6**0.5)+(3*(2+6**0.5))**n*(3+6**0.5))/4) for n in range(1,12)]#correct for n<=12, from sum of series OEIS A333298, real should be sum of A080583 from A080601
totalnums=[sum(total[:n])+1 for n in range(len(total))]

replaycube=(ccn,ccon,ceon,cen1,cen2,cen3)
replaystring=""
def replay():
    global c,co,eo,e1,e2,e3
    c,co,eo,e1,e2,e3=replaycube
    display()
    sleep(1)
    for i in range(len(replaystring)//2):
        f,t=int(replaystring[2*i]),int(replaystring[2*i+1])
        rotate(f,t)
        display()
        sleep(0.5)

#change corner 2 7 034 156
changecorner=(4,6,2,0,3,1,5,7)
#change edge 125 069 3a4 7b8
changeedge=(9,5,1,4,
            10,2,0,8,
            11,6,3,7)
addc=(1,2,2,1,1,2,2,1)
adde=(1,0,1,0,1,1,1,1,1,0,1,0)
#directions
changedirections=((0,1,2,3,4,5),(1,2,0,4,5,3),(2,0,1,5,3,4))

def diagonalrotation(c,co,e,eo):
    nc=c.copy()
    nco=co.copy()
    ne=e.copy()
    neo=eo.copy()
    for i in range(8):
        nc[i]=c[changecorner[i]]
    for i in range(12):
        ne[i]=e[changeedge[i]]
    for i in range(8):
        nco[i]=(co[changecorner[i]]+addc[i])%3
    for i in range(12):
        neo[i]=(eo[changeedge[i]]+adde[i])%2
    return nc,nco,ne,neo

#reverse
def changebase(c,co,eo,e1,e2,e3,index):
    for t in range(index%3):
        c=rcdict[c]
        co=rcodict[co]
        eo=reodict[eo]
        e=rep4dict[e1]+rep4dict[e2]+rep4dict[e3]
        e=[e.index(i) for i in range(12)]
        
        nc=list(c)
        nco=list(co)
        neo=list(eo)
        ne=list(e)
        
        for i in range(8):
            nc[i]=changecorner[c[i]]
        for i in range(12):
            ne[i]=changeedge[e[i]]
        
        
        for i in range(8):
            n=c.index(i)
            nco[n]=(co[n]+addc[i])%3
        
        for i in range(12):
            n=e.index(i)
            neo[n]=(eo[n]+adde[i])%2
        
        #adjust direction
        for i in range(2):
            nc,nco,ne,neo=diagonalrotation(nc,nco,ne,neo)
        
        c=cdict[tuple(nc)]
        co=codict[tuple(nco)]
        eo=eodict[tuple(neo)]
        e1=ep4dict[tuple([ne.index(i) for i in range(0,4)])]
        e2=ep4dict[tuple([ne.index(i) for i in range(4,8)])]
        e3=ep4dict[tuple([ne.index(i) for i in range(8,12)])]
    return c,co,eo,e1,e2,e3

def reversecube(c,co,eo,e1,e2,e3):
    #jump back to original place, see where the previous occupied block jump to
    c=rcdict[c]
    co=rcodict[co]
    eo=reodict[eo]
    e=rep4dict[e1]+rep4dict[e2]+rep4dict[e3]
    e=[e.index(i) for i in range(12)]
    
    nc=list(c)
    nco=list(co)
    neo=list(eo)
    ne=list(e)
    
    for i in range(8):
        nc[c[i]]=i
        nco[c[i]]=(3-co[i])%3
    
    for i in range(12):
        ne[e[i]]=i
        neo[e[i]]=eo[i]
    
    c=cdict[tuple(nc)]
    co=codict[tuple(nco)]
    eo=eodict[tuple(neo)]
    e1=ep4dict[tuple([ne.index(i) for i in range(0,4)])]
    e2=ep4dict[tuple([ne.index(i) for i in range(4,8)])]
    e3=ep4dict[tuple([ne.index(i) for i in range(8,12)])]
    return c,co,eo,e1,e2,e3

def solvecube():
    global replaycube,replaystring,solving,c,co,eo,e1,e2,e3,center
    print()
    solving=1
    #adjust direction
    adjust1=[[0,0],[2,2,2],[0,0,0],[],[2],[0]]
    for a in adjust1[center.index(3)]:#put white to bottom
        rotatecube(a)
    adjust2=[[],[],[1],[],[1,1],[1,1,1]]
    for a in adjust2[center.index(1)]:#put blue to left
        rotatecube(a)
    
    if (c,co,eo,e1,e2,e3)==(ccn,ccon,ceon,cen1,cen2,cen3):
        print("unmixed")
        solving=0
        return
    
    display()
    print(f"c = {c} ; co = {co} ; eo = {eo} ; e1 = {e1} ; e2 = {e2} ; e3 = {e3}")
    replaycube=(c,co,eo,e1,e2,e3)
    
    print("search depth",phase1step,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
    htm=qtm=stm=2*stepshouldbelow
    currentminmove=minmove=eighteen[-1]
    bestid=0
    cubepacks=[]
    for i in range(3):
        cubepacks.append(changebase(c,co,eo,e1,e2,e3,i))
    for i in range(3):
        cubepacks.append(reversecube(*cubepacks[i]))
    print("cube packs:",cubepacks)
    
    for i in range(threadn):
        print("{}\nc = {} ; co = {} ; eo = {} ; e1 = {} ; e2 = {} ; e3 = {}\n{:<18}{:<6}{:<6}{:<14}{:<6}{:<36}".format("thread "+str(i),*cubepacks[i],"htm","qtm","stm","time/s","type","solution"))
        htm,qtm,stm,minmove,threadtime=solve(*cubepacks[i],i,htm,qtm,stm,minmove,phase1step,cr0,cor0,eor0,ep4r0,cr1,ep4r1,cr,ep4r,dict1,dict2,eighteen)
        print("finish thread {}    htm {}  qtm {}  stm {}    time {:f}s    {}\n".format(i,htm,qtm,stm,threadtime,strftime("%Y-%m-%d %H:%M:%S",localtime())))
        canvas.create_text(1250,50+100*i,text=str(round(threadtime,3))+"s")
        canvas.update()
        if currentminmove!=minmove:
            currentminmove=minmove
            bestid=i
        if htm<=phase1step+dict0step+1:
            break
    sleep(1)
    solving=2
    if htm>=stepshouldbelow:
        print("fail to solve")
        canvas.create_text(50,50,text="no solution")
        canvas.update()
    else:
        numstr=decodevalue(minmove)
        rotatenotation=rotatenumbertostring(numstr)
        print("best solution in thread",bestid)
        print("\nmin htm",htm,"qtm",qtm,"stm",stm,"\nsolution\n"+str(minmove)+"\n"+numstr+"\n"+rotatenotation)
        
        replaystring=""
        direction=changedirections[(-bestid)%3]
        for i in range(htm):
            replaystring+=str(direction[int(numstr[2*i])])+numstr[2*i+1]
        if bestid>2:
            replaystring=reverserotation(replaystring)
        display()
        sleep(1)
        for i in range(htm):
            f,t=int(replaystring[2*i]),int(replaystring[2*i+1])
            rotate(f,t)
            display()
            canvas.create_text(1000,30,text=str(minmove))
            canvas.create_text(1000,60,text=numstr)
            canvas.create_text(1000,90,text=rotatenotation)
            canvas.create_text(1000,120,text="htm "+str(htm))
            canvas.create_text(50,50,text="thread "+str(bestid))
            canvas.update()
            sleep(0.5)
    sleep(1)
    solving=0

phase1step=6#7
dict0step=6#6
dict1step=7#8
dict2step=8#9
stepshouldbelow=phase1step+dict1step+dict2step+1
print(phase1step,"+",dict1step,"+",dict2step)
dict0,tdict0=getdict0(dict0step)
print("{:<8}{:<16}{:<16}{:<16f}".format("total","",len(dict0),tdict0))
dict1,tdict1=getdict1(dict1step,cor0,eor0,ep4r0)
print("{:<8}{:<16}{:<16}{:<16f}".format("total","",len(dict1),tdict1))
dict2,tdict2=getdict2(dict2step,eighteen,cr0,ep4r0,cr1,ep4r1)
print("{:<8}{:<16}{:<16}{:<16f}".format("total","",len(dict2),tdict2))
print(f"dicts time {round(tdict0+tdict1+tdict2,6)}s = {tdict0}s + {tdict1}s + {tdict2}s")

threadn=6
print(threadn,"threads")

c=ccn
co=ccon
e1=cen1
e2=cen2
e3=cen3
eo=ceon

center=[0,1,2,3,4,5]
cubecolor=[[i]*9 for i in range(6)]
history=[(c,co,eo,e1,e2,e3,center)]
solving=0

canvas.bind("<Button-1>",click)
canvas.bind_all("<KeyPress>",keypress)
start()
canvas.after(1, lambda: window.focus_force())
canvas.pack()
window.mainloop()
from time import time,strftime,localtime,sleep
from random import randint
from math import log
from itertools import permutations,product,combinations
from tkinter import Tk,Canvas

cc,cco,ce,ceo=(0,1,2,3,4,5,6,7),(0,0,0,0,3,3,3,3),(0,1,2,3,4,5,6,7,8,9,10,11),(0,0,0,0,1,1,4,4,3,3,3,3)
facecorner=((0,2,3,1),(0,6,4,2),(2,4,5,3),(4,6,7,5),(3,5,7,1),(1,7,6,0))
faceedge=((0,1,2,3),(1,4,9,5),(2,5,10,6),(10,9,8,11),(3,6,11,7),(0,7,8,4))
facetimedirection=(((0,5,1,3,2,4),(0,4,5,3,1,2)),((2,1,3,5,4,0),(3,1,5,0,4,2)),((4,0,2,1,3,5),(3,4,2,0,1,5)),((0,2,4,3,5,1),(0,4,5,3,1,2)),((5,1,0,2,4,3),(3,1,5,0,4,2)),((1,3,2,4,0,5),(3,4,2,0,1,5)))
cornerdirection=((0,5,1),(0,4,5),(0,1,2),(0,2,4),(3,2,1),(3,4,2),(3,1,5),(3,5,4))
edgedirection=((0,5),(0,1),(0,2),(0,4),(1,5),(1,2),(4,2),(4,5),(3,5),(3,1),(3,2),(3,4))
adj=((5,4,2,1),(0,2,3,5),(0,4,3,1),(1,2,4,5),(0,5,3,2),(0,1,3,4))

#the position of each face of each block
cornerposition=(((0,0),(1,0),(5,2)),((0,2),(5,0),(4,2)),((0,6),(2,0),(1,2)),((0,8),(4,0),(2,2)),
                ((3,0),(1,8),(2,6)),((3,2),(2,8),(4,6)),((3,6),(5,8),(1,6)),((3,8),(4,8),(5,6)))
edgeposition=(((0,1),(5,1)),((0,3),(1,1)),((0,7),(2,1)),((0,5),(4,1)),
              ((1,3),(5,5)),((1,5),(2,3)),((4,3),(2,5)),((4,5),(5,3)),
              ((3,7),(5,7)),((3,3),(1,7)),((3,1),(2,7)),((3,5),(4,7)))
#centeredge=((0,2,10,8),(4,5,6,7),(1,3,11,9))
color=("#FFFF00","#0000FF","#FF0000","#FFFFFF","#00FF00","#FF8000")
allrotation=("U","U2","U'","L","L2","L'","F","F2","F'","D","D2","D'","R","R2","R'","B","B2","B'")
rotates=["U","L","F","R","B","D","M","E","S","x","y","z"]

#init
t0=time()
#dicts: contains number presentations of all corner and edge positions, tuple->index
#corner 40320 8!
cdict={i:n for n,i in enumerate(permutations(cc))}
#corner orientation 2187 3**7
codict={tuple([cornerdirection[j][i[j]] for j in range(8)]):n for n,i in enumerate((i for i in product(range(3),repeat=8) if not sum(i)%3))}
#edge orientation 2048 2**11
eodict={tuple([edgedirection[j][i[j]] for j in range(12)]):n for n,i in enumerate([i for i in product(range(2),repeat=12) if not i.count(1)%2])}
#4 edge position 495 C(12,4)
ep4dict={j:n for n,j in enumerate(j for i in combinations(ce,r=4) for j in permutations(i))}
#index->tuple
rcdict={cdict[key]:key for key in cdict}
rcodict={codict[key]:key for key in codict}
rep4dict={ep4dict[key]:key for key in ep4dict}
reodict={eodict[key]:key for key in eodict}
#list contains length of 0, rotation list
cl,col,eol,ep4l,cr,cor,eor,ep4r=[0]*len(cdict),[0]*len(codict),[0]*len(eodict),[0]*len(ep4dict),[],[],[],[]
for f in 0,1,2,3,4,5:
    c1,c2,c3,c4=facecorner[f]
    e1,e2,e3,e4=fe=faceedge[f]
    sfe=set(fe)
    fte=e2,e3,e4,e1
    ftd0,ftd1=facetimedirection[f]
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
    for a,dco in enumerate(codict):
        co=list(dco)
        co[c1],co[c2],co[c3],co[c4]=ftd0[co[c2]],ftd0[co[c3]],ftd0[co[c4]],ftd0[co[c1]]
        b=codict[tuple(co)]
        d0[a],d2[b]=b,a
        if not d1[a]:
            co[c1],co[c2],co[c3],co[c4]=ftd0[co[c2]],ftd0[co[c3]],ftd0[co[c4]],ftd0[co[c1]]
            b=codict[tuple(co)]
            d1[a],d1[b]=b,a
    cor.append((tuple(d0),tuple(d1),tuple(d2)))
    d0,d1,d2=eol.copy(),eol.copy(),eol.copy()
    for a,deo in enumerate(eodict):
        eo=list(deo)
        eo[e1],eo[e2],eo[e3],eo[e4]=ftd0[eo[e2]],ftd0[eo[e3]],ftd0[eo[e4]],ftd0[eo[e1]]
        b=eodict[tuple(eo)]
        d0[a],d2[b]=b,a
        if not d1[a]:
            eo[e1],eo[e2],eo[e3],eo[e4]=ftd0[eo[e2]],ftd0[eo[e3]],ftd0[eo[e4]],ftd0[eo[e1]]
            b=eodict[tuple(eo)]
            d1[a],d1[b]=b,a
    eor.append((tuple(d0),tuple(d1),tuple(d2)))
    d0,d1,d2=ep4l.copy(),ep4l.copy(),ep4l.copy()
    for a,dep in enumerate(ep4dict):
        ep=list(dep)
        for i in 0,1,2,3:
            if ep[i] in sfe:
                ep[i]=fe[fte.index(ep[i])]
        b=ep4dict[tuple(ep)]
        d0[a],d2[b]=b,a
        if not d1[a]:
            for i in 0,1,2,3:
                if ep[i] is not dep[i]:
                    ep[i]=fe[fte.index(ep[i])]
            b=ep4dict[tuple(ep)]
            d1[a],d1[b]=b,a
    ep4r.append((tuple(d0),tuple(d1),tuple(d2)))
cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1=tuple(cr),tuple(cor),tuple(ep4r),tuple(eor),cdict[cc],codict[cco],ep4dict[ce[0:4]],ep4dict[ce[4:8]],ep4dict[ce[8:12]],eodict[ceo],tuple([i[0] for i in cr]),tuple([i[0] for i in cor]),tuple([i[0] for i in eor]),tuple([i[0] for i in ep4r]),tuple([i[1] for i in cr]),tuple([i[1] for i in ep4r])

#dict for complete phase 1, remove correct one
#1 4
#2 54
#3 647
#4 7802
#5 95038
#6 1138855
#7 
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
                        key1=ne2//24+495*(neo+2048*nco)
                        if key1 not in dict1:
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
                        key1=ne2//24+495*(neo+2048*nco)
                        if key1 not in dict1:
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
#8 
#9 
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
                    key2=ne3+11880*(ne2+11880*(ne1+11880*nc))
                    if key2 not in dict2:
                        newstep=oldstep+(3*f+1)*eighteen0
                        dict2[key2]=newstep+eighteen1
                        if step is not dict2step:
                            newpredictstate.append((nc,ne1,ne2,ne3,newstep,f))
            for f in 1,2:
                if f1 is not f and f1-f!=3:
                    ep4rf1=ep4r1[f]
                    nc,ne1,ne2,ne3=cr1[f][oc],ep4rf1[oe1],ep4rf1[oe2],ep4rf1[oe3]
                    key2=ne3+11880*(ne2+11880*(ne1+11880*nc))
                    if key2 not in dict2:
                        newstep=oldstep+(3*f+1)*eighteen0
                        dict2[key2]=newstep+eighteen1
                        if step is not dict2step:
                            newpredictstate.append((nc,ne1,ne2,ne3,newstep,f))
            if f1!=3:
                crf0,ep4rf0=cr0[3],ep4r0[3]
                nc,ne1,ne2,ne3=oc,oe1,oe2,oe3
                for t in 2,1,0:
                    nc,ne1,ne2,ne3=crf0[nc],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                    key2=ne3+11880*(ne2+11880*(ne1+11880*nc))
                    if key2 not in dict2:
                        newstep=oldstep+(9+t)*eighteen0
                        dict2[key2]=newstep+eighteen1
                        if step is not dict2step:
                            newpredictstate.append((nc,ne1,ne2,ne3,newstep,3))
                if f1!=0:
                    crf0,ep4rf0=cr0[0],ep4r0[0]
                    nc,ne1,ne2,ne3=oc,oe1,oe2,oe3
                    for t in 2,1,0:
                        nc,ne1,ne2,ne3=crf0[nc],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                        key2=ne3+11880*(ne2+11880*(ne1+11880*nc))
                        if key2 not in dict2:
                            newstep=oldstep+t*eighteen0
                            dict2[key2]=newstep+eighteen1
                            if step is not dict2step:
                                newpredictstate.append((nc,ne1,ne2,ne3,newstep,0))
        print("{:<8}{:<16}{:<16}{:<16f}".format(step,len(newpredictstate),len(dict2),time()-t1))
        predictstate,newpredictstate=newpredictstate,[]
    return dict2,round(time()-t0,6)

#solve the cube with c,co,eo,e1,e2,e3 numbers
def solve(c,co,eo,e1,e2,e3,threadid,htm,qtm,stm,minmove,phase1step,cr0,cor0,eor0,ep4r0,cr1,ep4r1,cr,ep4r,dict1,dict2,eighteen):
    tstart=time()
    cubes=[(c,co,eo,e1,e2,e3,1,0,-1)]
    while cubes:
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
                        m1_2,f0,nc1,ne11,ne21,ne31=dict1[ne2//24+495*(neo+2048*nco)],f,nc,ne1,ne2,ne3
                        while m1_2>=18:
                            f0,t0,m1,m1_2=m1_2//3%6,m1_2%3,18*m1+m1_2%18,m1_2//18
                            ep4rf0t0=ep4r[f0][t0]
                            nc1,ne11,ne21,ne31=cr[f0][t0][nc1],ep4rf0t0[ne11],ep4rf0t0[ne21],ep4rf0t0[ne31]
                        if ne31+11880*(ne21+11880*(ne11+11880*nc1)) in dict2:
                            m2=dict2[ne31+11880*(ne21+11880*(ne11+11880*nc1))]
                            l=int(log(m1,18))+int(log(m2,18))
                            if l<=htm:
                                htm,qtm,stm,minmove=solved(m1,m2,minmove,l,htm,qtm,stm,step,tstart,1)
                                ep4rf01=ep4r1[f0]
                                nc1,ne11,ne21,ne31=cr1[f0][nc1],ep4rf01[ne11],ep4rf01[ne21],ep4rf01[ne31]
                                if ne31+11880*(ne21+11880*(ne11+11880*nc1)) in dict2:
                                    m2=dict2[ne31+11880*(ne21+11880*(ne11+11880*nc1))]
                                    l=int(log(m1,18))+int(log(m2,18))
                                    if l<=htm:
                                        htm,qtm,stm,minmove=solved(m1,m2,minmove,l,htm,qtm,stm,step,tstart,2)
    return htm,qtm,stm,minmove,time()-tstart

#print the solved form solve, solution must be <= current htm
def solved(m1,m2,minmove,l,htm,qtm,stm,step,tstart,rtype):
    n=solution=(m1-1)*eighteen[int(log(m2,18))]+m2
    if solution<minmove:
        minmove=solution
    qtmvalue=stmvalue=htm=l
    numstr=""
    while n>=18:
        numstr,n=str(n//3%6)+str(n%3)+numstr,n//18
        if n%3==1:
            qtmvalue+=1
    for i in range(0,len(numstr)-2,2):
        if abs(int(numstr[i])-int(numstr[i+2]))==3 and int(numstr[i+1])+int(numstr[i+3])==2:
            stmvalue-=1
    if qtmvalue<qtm:
        qtm=qtmvalue
    if stmvalue<stm:
        stm=stmvalue
    print("{:<18}{:<6}{:<6}{:<14f}{:<6}{:<36}{}".format(f"{htm} = {step} + {htm-step-int(log(m2,18))} + {int(log(m2,18))}",qtmvalue,stmvalue,time()-tstart,rtype,solution,numstr))
    return htm,qtm,stm,minmove

print(strftime("%Y-%m-%d %H:%M:%S",localtime()))
eighteen=tuple([18**i for i in range(28)])
changedirections=((0,1,2,3,4,5),(1,2,0,4,5,3),(2,0,1,5,3,4))
allrotation=("U","U2","U'","L","L2","L'","F","F2","F'","D","D2","D'","R","R2","R'","B","B2","B'")

phase1step=5#7
dict1step=5#8
dict2step=6#9
stepshouldbelow=phase1step+dict1step+dict2step+1
print(phase1step,"+",dict1step,"+",dict2step)
dict1,tdict1=getdict1(dict1step,cor0,eor0,ep4r0)
print("{:<8}{:<16}{:<16}{:<16f}".format("total","",len(dict1),tdict1))
dict2,tdict2=getdict2(dict2step,eighteen,cr0,ep4r0,cr1,ep4r1)
print("{:<8}{:<16}{:<16}{:<16f}".format("total","",len(dict2),tdict2))
print(f"dicts time {tdict1+tdict2}s = {tdict1}s + {tdict2}s")
n=1
print(n,"threads")



window=Tk()
canvas=Canvas(window,bg="#808080",width=1440,height=810)
window.title("cube")

c=ccn
co=ccon
e1=cen1
e2=cen2
e3=cen3
eo=ceon

center=[0,1,2,3,4,5]
cubecolor=[[i]*9 for i in range(6)]
'''
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
        facenum=3
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
'''
def rotate(f,t):
    global c,co,e1,e2,e3,eo
    c=cr[f][t][c]
    co=cor[f][t][co]
    eo=eor[f][t][eo]
    ep4rft=ep4r[f][t]
    e1,e2,e3=ep4rft[e1],ep4rft[e2],ep4rft[e3]

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
    canvas.create_rectangle(900,560,1000,610,fill="#C0C0C0")
    canvas.create_text(950,585,text="replay")
    for i in range(12):
        canvas.create_rectangle(100*i+110,650,100*i+190,690,fill="#C0C0C0")
        canvas.create_text(100*i+140,670,text=rotates[i])
    for i in range(12):
        canvas.create_rectangle(100*i+110,700,100*i+190,740,fill="#C0C0C0")
        canvas.create_text(100*i+140,720,text=rotates[i]+"'")
        
def click(coordinate):
    global cubecolor,corner,cornerd,edge,edged,center
    x=coordinate.x
    y=coordinate.y
    if 650<y<690:
        a=(x-100)//100
        if 0<=a<=5:
            rotate(a,0)
        '''
        elif 6<=a<=8:
            rotatemiddle(a-6)
        elif 9<=a<=11:
            rotatec(a-9)
            '''
    elif 700<y<740:
        a=(x-100)//100
        if 0<=a<=5:
            rotate(a,2)
            '''
        elif 6<=a<=8:
            rotatemiddle(a-6)
            rotatemiddle(a-6)
            rotatemiddle(a-6)
        elif 9<=a<=11:
            rotatec(a-9)
            rotatec(a-9)
            rotatec(a-9)
            '''
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
        print(f"c = {c}  co = {co}  eo = {eo}  e1 = {e1}  e2 = {e2}  e3 = {e3}")
    elif 50<x<150 and 560<y<610:
        print("solve")
        print("cube =",cubecolor)
        print(f"c = {c}  co = {co}  eo = {eo}  e1 = {e1}  e2 = {e2}  e3 = {e3}")
        solve()
    elif 200<x<300 and 560<y<610:
        randomcube()
        print("random and solve")
        print("cube =",cubecolor)
        print(f"c = {c}  co = {co}  eo = {eo}  e1 = {e1}  e2 = {e2}  e3 = {e3}")
        solve()
        '''
    elif 900<x<1000 and 500<y<550:
        i=input("input:")
        if i.isdigit():
            i=rotatenumbertostring(i)
        do(i)
    elif 900<x<1000 and 560<y<610:
        replay()
        '''
    display()
'''
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
'''
def display():
    updatecube()
    canvas.delete("all")
    draw()
    xy=((500,0),(300,200),(500,200),(500,400),(700,200),(900,200))
    for i in range(6):
        x,y=xy[i]
        for j in range(3):
            for k in range(3):
                canvas.create_rectangle(x+60*k,y+60*j+20,x+60*k+60,y+60*j+80,fill=color[cubecolor[i][3*j+k]])
    canvas.update()
    sleep(0.5)
    
def updatecube():
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
        if edged[i]==ceo[i]:
            cubecolor[edgeposition[i][0][0]][edgeposition[i][0][1]]=edgeposition[edge[i]][0][0]
            cubecolor[edgeposition[i][1][0]][edgeposition[i][1][1]]=edgeposition[edge[i]][1][0]
        else:
            cubecolor[edgeposition[i][0][0]][edgeposition[i][0][1]]=edgeposition[edge[i]][1][0]
            cubecolor[edgeposition[i][1][0]][edgeposition[i][1][1]]=edgeposition[edge[i]][0][0]
    #corner
    corner=rcdict[c]
    cornerd=rcodict[co]
    for i in range(8):
        if cornerd[i]==cornerposition[i][0][0]:
            cubecolor[cornerposition[i][0][0]][cornerposition[i][0][1]]=cornerposition[corner[i]][0][0]
            cubecolor[cornerposition[i][1][0]][cornerposition[i][1][1]]=cornerposition[corner[i]][1][0]
            cubecolor[cornerposition[i][2][0]][cornerposition[i][2][1]]=cornerposition[corner[i]][2][0]
        elif cornerd[i]==cornerposition[i][1][0]:
            cubecolor[cornerposition[i][0][0]][cornerposition[i][0][1]]=cornerposition[corner[i]][2][0]
            cubecolor[cornerposition[i][1][0]][cornerposition[i][1][1]]=cornerposition[corner[i]][0][0]
            cubecolor[cornerposition[i][2][0]][cornerposition[i][2][1]]=cornerposition[corner[i]][1][0]
        else:
            cubecolor[cornerposition[i][0][0]][cornerposition[i][0][1]]=cornerposition[corner[i]][1][0]
            cubecolor[cornerposition[i][1][0]][cornerposition[i][1][1]]=cornerposition[corner[i]][2][0]
            cubecolor[cornerposition[i][2][0]][cornerposition[i][2][1]]=cornerposition[corner[i]][0][0]

def randomcube():
    for i in range(randint(1024,2048)):
        rotate(randint(0,5),randint(0,2))
    '''
    a=randint(16,32)
    randomstring=""
    for i in range(a):
        r=randint(0,9)
        if r<6:
            rotate(r)
        else:
            rotatemiddle(r-6)
        randomstring+=rotates[r]
    print("mix up steps:",randomstring)
    '''
    



canvas.bind("<Button-1>",click)
#canvas.bind_all("<KeyPress>",keypress)
start()
canvas.pack()
window.mainloop()
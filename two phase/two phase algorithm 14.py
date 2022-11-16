import time
from random import randint
from threading import Thread
from math import log
from itertools import permutations,product,combinations
from sys import getsizeof
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
cc=(0,1,2,3,4,5,6,7)
cco=(0,0,0,0,5,5,5,5)
ce=(0,1,2,3,4,5,6,7,8,9,10,11)
ceo=(0,0,0,0,1,1,3,3,5,5,5,5)

facetimecorner=[[(2,3,1,0),(3,1,0,2),(1,0,2,3)],[(6,4,2,0),(4,2,0,6),(2,0,6,4)],[(4,5,3,2),(5,3,2,4),(3,2,4,5)],[(5,7,1,3),(7,1,3,5),(1,3,5,7)],[(7,6,0,1),(6,0,1,7),(0,1,7,6)],[(6,7,5,4),(7,5,4,6),(5,4,6,7)]]
facetimeedge=[[(1,2,3,0),(2,3,0,1),(3,0,1,2)],[(4,9,5,1),(9,5,1,4),(5,1,4,9)],[(5,10,6,2),(10,6,2,5),(6,2,5,10)],[(6,11,7,3),(11,7,3,6),(7,3,6,11)],[(7,8,4,0),(8,4,0,7),(4,0,7,8)],[(9,8,11,10),(8,11,10,9),(11,10,9,8)]]
facecorner=[(0,2,3,1),(0,6,4,2),(2,4,5,3),(3,5,7,1),(1,7,6,0),(4,6,7,5)]
faceedge=[(0,1,2,3),(1,4,9,5),(2,5,10,6),(3,6,11,7),(0,7,8,4),(10,9,8,11)]
facetimedirection=[[[0,4,1,2,3,5],[0,3,4,1,2,5],[0,2,3,4,1,5]],[[2,1,5,3,0,4],[5,1,4,3,2,0],[4,1,0,3,5,2]],[[3,0,2,5,4,1],[5,3,2,1,4,0],[1,5,2,0,4,3]],[[4,1,0,3,5,2],[5,1,4,3,2,0],[2,1,5,3,0,4]],[[1,5,2,0,4,3],[5,3,2,1,4,0],[3,0,2,5,4,1]],[[0,2,3,4,1,5],[0,3,4,1,2,5],[0,4,1,2,3,5]]]
cornerdirection=[(0,4,1),(0,3,4),(0,1,2),(0,2,3),(5,2,1),(5,3,2),(5,1,4),(5,4,3)]
edgedirection=[(0,4),(0,1),(0,2),(0,3),(1,4),(1,2),(3,2),(3,4),(5,4),(5,1),(5,2),(5,3)]

phase2rotations=[0,1,2,4,7,10,13,15,16,17]
eighteen=[18**i for i in range(28)]

def printdictsize(d):
    t=time.time()
    a=getsizeof(d)
    b=0
    for i in d.keys():
        b+=getsizeof(i)
    for i in d.values():
        b+=getsizeof(i)
    print([name for name in globals() if globals()[name] is d][0],len(d),"dict space",a,"B    values and keys space",b,"B    total",(a+b)/2**30,"GB ",(a+b)/2**20,"MB ",time.time()-t,"s")

t1=time.time()
cdict,codict,ep6dict,eodict,reodict,meodict={},{},{},{},{},{}
rcdict,rcodict,rep6dict,mepdict,rmepdict,rmeodict={},{},{},{},{},{}
#cdict, (0,1,2,3,4,5,6,7),(0,1,2,3,4,5,7,6) 40320 8!
n=0
for i in permutations(range(8)):
    cdict[i]=n
    rcdict[n]=i
    n+=1
#codict, (0,0,0,0,5,5,5,5),(0,0,0,0,5,5,4,4) 2187 3**7
n=0
for i in product(range(3),repeat=8):
    if sum(i)%3==0:
        a=()
        for j in range(8):
            a+=(cornerdirection[j][i[j]],)
        codict[a]=n
        rcodict[n]=a
        n+=1
#ep6dict,(0,1,2,3,4,5),(6,7,8,9,10,11) 665280 P(12,6)
n=0
for i in combinations(range(12),r=6):
    for j in permutations(i):
        ep6dict[j]=n
        rep6dict[n]=j
        n+=1
#eodict, (0,0,0,0,1,1,3,3,5,5,5,5),(0,0,0,0,1,1,3,3,5,5,2,3) 2048 2**11
n=0
for i in product(range(2),repeat=12):
    if sum(i)%2==0:
        a=()
        for j in range(12):
            a+=(edgedirection[j][i[j]],)
        eodict[a]=n
        reodict[n]=a
        n+=1
#mepdict, (4,5,6,7) 495 C(12,4)
n=0
for i in combinations(range(12),r=4):
    mepdict[i]=n
    rmepdict[n]=i
    n+=1
#meodict, eo*mep (0,0,0,0,1,1,3,3,5,5,5,5,4,5,6,7),(0,0,0,0,1,1,3,3,5,5,2,3,0,1,2,3) 1013760 2**11*C(12,4)
n=0
j1=[i for i in combinations(range(12),r=4)]
for i in product(range(2),repeat=12):
    if sum(i)%2==0:
        a=()
        for j in range(12):
            a+=(edgedirection[j][i[j]],)
        for j in j1:
            meodict[a+j]=n
            rmeodict[n]=a+j
            n+=1

cr,cor,ep6r,eor,mepr,meor=[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)]
for f in range(6):
    c1,c2,c3,c4=fc=facecorner[f]
    e1,e2,e3,e4=fe=faceedge[f]
    for t in range(3):
        nc1,nc2,nc3,nc4=ftc=facetimecorner[f][t]
        ne1,ne2,ne3,ne4=fte=facetimeedge[f][t]
        ftd=facetimedirection[f][t]
        
        d=cr[f][t]
        for dc in cdict.keys():
            c=list(dc)
            c[c1],c[c2],c[c3],c[c4]=c[nc1],c[nc2],c[nc3],c[nc4]
            d[cdict[dc]]=cdict[tuple(c)]
        d=cor[f][t]
        for dco in codict.keys():
            co=list(dco)
            co[c1],co[c2],co[c3],co[c4]=ftd[co[nc1]],ftd[co[nc2]],ftd[co[nc3]],ftd[co[nc4]]
            d[codict[dco]]=codict[tuple(co)]
        d=ep6r[f][t]
        for dep in ep6dict.keys():
            ep=list(dep)
            for i in range(6):
                if ep[i] in fe:
                    ep[i]=fe[fte.index(ep[i])]
            d[ep6dict[dep]]=ep6dict[tuple(ep)]
            
        d1=eor[f][t]
        for deo in eodict.keys():
            eo=list(deo)
            eo[e1],eo[e2],eo[e3],eo[e4]=ftd[eo[ne1]],ftd[eo[ne2]],ftd[eo[ne3]],ftd[eo[ne4]]
            d1[eodict[deo]]=eodict[tuple(eo)]
        d2=mepr[f][t]
        for dmep in mepdict.keys():
            mep=list(dmep)
            for i in range(4):
                if mep[i] in fe:
                    mep[i]=fe[fte.index(mep[i])]
            mep.sort()
            d2[mepdict[dmep]]=mepdict[tuple(mep)]
        d=meor[f][t]
        for i in eodict.values():
            for j in mepdict.values():
                d[i*495+j]=d1[i]*495+d2[j]

ccn,ccon,cmeon,cen1,cen2=cdict[cc],codict[cco],meodict[ceo+ce[4:8]],ep6dict[ce[0:6]],ep6dict[ce[6:12]]
print(time.time()-t1,"s")

def getdict1(dict1step):
    global dict1
    predictstate=[(ccon,cmeon,1,-1,-1)]
    newpredictstate=[]
    key1=ccon*1013760+cmeon
    dict1[key1]=1
    t0=time.time()
    for step in range(1,dict1step+1):
        t1=time.time()
        for cube in predictstate:
            oco,omeo,oldstep,f1,f2=cube
            for f in range(6):
                if f1!=f and not ((f1==5 and f==0 or f1==4 and f==2 or f1==3 and f==1) or (step>2 and f==f2 and (f==0 and f1==5 or f==1 and f1==3 or f==2 and f1==4))):
                    newstep=oldstep*18+3*f+2
                    for t in range(3):
                        nco,nmeo=cor[f][t][oco],meor[f][t][omeo]
                        key1=nco*1013760+nmeo
                        if key1 not in dict1:
                            dict1[key1]=newstep
                            if step!=dict1step:
                                newpredictstate.append((nco,nmeo,newstep,f,f1))
                        newstep-=1
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,step,len(newpredictstate),len(dict1),time.time()-t1),end="")
        predictstate,newpredictstate=newpredictstate,[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,"total","",len(dict1),time.time()-t0),end="")

def getdict2(dict2step):
    global dict2
    predictstate=[(ccn,cen1,cen2,0,-1,-1)]
    newpredictstate=[]
    key2=(ccn*665280+cen1)*665280+cen2
    dict2[key2]=1
    t0=time.time()
    for step in range(1,dict2step+1):
        t1=time.time()
        for cube in predictstate:
            oc,oe1,oe2,oldstep,f1,f2=cube
            for r in phase2rotations:
                f,t=r//3,r%3
                if f1!=f and not ((f1==5 and f==0 or f1==4 and f==2 or f1==3 and f==1) or (step>2 and f==f2 and (f==0 and f1==5 or f==1 and f1==3 or f==2 and f1==4))):
                    nc,ne1,ne2=cr[f][t][oc],ep6r[f][t][oe1],ep6r[f][t][oe2]
                    key2=(nc*665280+ne1)*665280+ne2
                    if key2 not in dict2:
                        newstep=oldstep+(3*f+2-t)*eighteen[step-1]
                        dict2[key2]=newstep+eighteen[step]
                        if step!=dict2step:
                            newpredictstate.append((nc,ne1,ne2,newstep,f,f1))
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,step,len(newpredictstate),len(dict2),time.time()-t1),end="")
        predictstate,newpredictstate=newpredictstate,[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,"total","",len(dict2),time.time()-t0),end="")

def solve(c,co,meo,e1,e2,threadid):
    global threadsolutions,htm,qtm,minmove,verifiednum
    tstart=time.time()
    cubes=[(c,co,meo,e1,e2,1,0,-1,-1)]
    solutionnum=0
    totalnum=1
    minstr=eighteen[stepshouldbelow]
    #phase 1
    while cubes:
        oc,oco,omeo,oe1,oe2,previousstep,step,f1,f2=cubes.pop()
        step+=1
        for f in range(6):
            if f!=f1 and not ((f1==5 and f==0 or f1==4 and f==2 or f1==3 and f==1) or (step>2 and f==f2 and (f==0 and f1==5 or f==1 and f1==3 or f==2 and f1==4))):
                m1_1=previousstep*18+3*f
                totalnum+=3
                for t in range(3):
                    nc,nco,nmeo,ne1,ne2=cr[f][t][oc],cor[f][t][oco],meor[f][t][omeo],ep6r[f][t][oe1],ep6r[f][t][oe2]
                    if step<phase1maxstep:
                        cubes.append((nc,nco,nmeo,ne1,ne2,m1_1,step,f,f1))
                    key1=nco*1013760+nmeo
                    if key1 in dict1:
                        solutionnum+=1
                        m1_2=dict1[key1]
                        if m1_2!=1:
                            nc1=nc
                            ne11=ne1
                            ne21=ne2
                            m1=m1_1
                            f0=f
                            while m1_2>=18:
                                ft=m1_2%18
                                m1=18*m1+ft
                                m1_2//=18
                                f0,t0=ft//3,ft%3
                                nc1,ne11,ne21=cr[f0][t0][nc1],ep6r[f0][t0][ne11],ep6r[f0][t0][ne21]
                            #phase 2
                            key2=(nc1*665280+ne11)*665280+ne21
                            if key2 in dict2:
                                m2=dict2[key2]
                                solution=(m1-1)*eighteen[int(log(m2,18))]+m2
                                if solution<minmove:
                                    minmove=minstr=solution
                                    htm=int(log(solution,18))
                                    p2=int(log(m2,18))
                                    qtmvalue=htm
                                    numstr=decodevalue(solution)
                                    for i in range(int(len(numstr)/2)):
                                        if numstr[2*i+1]=="1":
                                            qtmvalue+=1
                                    if qtmvalue<qtm:
                                        qtm=qtmvalue
                                    print("{:<8}{:<18}{:<6}{:<24}{:<14f}1     {:<36}{}\n".format(threadid,f"{htm} = {step} + {htm-step-p2} + {p2}",qtmvalue,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution,numstr),end="")
                            if int(log(m1,18))+dict2step<=htm or key2 in dict2 and int(log(solution,18))-1<=htm:
                                nc1,ne11,ne21=cr[f0][1][nc1],ep6r[f0][1][ne11],ep6r[f0][1][ne21]
                                key2=(nc1*665280+ne11)*665280+ne21
                                if key2 in dict2:
                                    m2=dict2[key2]
                                    solution=(m1-3)*eighteen[int(log(m2,18))]+m2
                                    if solution<minmove:
                                        minmove=minstr=solution
                                        htm=int(log(solution,18))
                                        p2=int(log(m2,18))
                                        qtmvalue=htm
                                        numstr=decodevalue(solution)
                                        for i in range(int(len(numstr)/2)):
                                            if numstr[2*i+1]=="1":
                                                qtmvalue+=1
                                        if qtmvalue<qtm:
                                            qtm=qtmvalue
                                        print("{:<8}{:<18}{:<6}{:<24}{:<14f}2     {:<36}{}\n".format(threadid,f"{htm} = {step} + {htm-step-p2} + {p2}",qtmvalue,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution,numstr),end="")
                    m1_1+=1
    threadsolutions[threadid]=minstr
    verifiednum.append(solutionnum)
    print("finish thread {}    thread min htm {}    {}/{}    time {:f}s\n".format(threadid,int(log(minstr,18)),solutionnum,totalnum,time.time()-tstart),end="")

def randomcube():
    a=randint(512,1024)
    randomstring=""
    for i in range(a):
        r=str(randint(0,5))+str(randint(0,2))
        randomstring+=r
    return randomstring

changebasetable=[[0,1,2,3,4,5],[1,5,2,0,4,3],[2,1,5,3,0,4]]
def getcubewithbase(randomstring,base):
    l=int(len(randomstring)/2)
    c,co,meo,e1,e2=ccn,ccon,cmeon,cen1,cen2
    for i in range(l):
        f,t=changebasetable[base][int(randomstring[2*i])],int(randomstring[2*i+1])
        c,co,meo,e1,e2=cr[f][t][c],cor[f][t][co],meor[f][t][meo],ep6r[f][t][e1],ep6r[f][t][e2]
    return c,co,meo,e1,e2
    
def decodevalue(n):
    s=""
    while n>=18:
        ft=n%18
        n//=18
        s=str(ft//3)+str(ft%3)+s
    return s
    
allrotation=["U","U2","U'","L","L2","L'","F","F2","F'","R","R2","R'","B","B2","B'","D","D2","D'"]
def rotatenumbertostring(s):
    r=""
    for i in range(int(len(s)/2)):
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

def reverserotation(s):
    r=""
    for i in range(int(len(s)/2)):
        r=s[2*i]+str(2-int(s[2*i+1]))+r
    return r

dict1,dict2={},{}
dict1step=7#8
dict2step=8#9
dict1thread=Thread(target=getdict1,args=(dict1step,))
dict2thread=Thread(target=getdict2,args=(dict2step,))
print("{:<8}{:<8}{:<16}{:<16}{:<16}\n".format("dict","step","cubes left","dict length","time/s"),end="")
tdictstart=time.time()
dict1thread.start()
dict2thread.start()
dict2thread.join()
dict1thread.join()
tdictend=time.time()
print("time",tdictend-tdictstart,"s")
printdictsize(dict1)
printdictsize(dict2)

htms,qtms=[],[]
verifiednum=[]
starttime=time.time()
phase1maxstep=5#6
stepshouldbelow=phase1maxstep+dict1step+dict2step+1
miss=0
threadn=6
cubenumber=10

for i in range(cubenumber):
    t1=time.time()
    print("\n\ncube",i+1)
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    htm=stepshouldbelow
    qtm=htm*2
    minmove=eighteen[stepshouldbelow]
    
    randomstring=randomcube()
    print("random with",int(len(randomstring)/2),"moves")
    print("search depth",phase1maxstep,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
    unsolvedcubes=[]
    for base in range(3):
        cubepack=getcubewithbase(randomstring,base)
        unsolvedcubes.append(cubepack)
    reverserandomstring=reverserotation(randomstring)
    for base in range(3):
        unsolvedcubes.append(getcubewithbase(reverserandomstring,base))
    threadsolutions=[eighteen[stepshouldbelow]]*threadn
    print("start",threadn,"threads")
    print("{:<8}{:<18}{:<6}{:<24}{:<14}{:<6}{:<36}".format("thread","htm","qtm","in dict1/total","time/s","type","solution"))
    
    threads=[Thread(target=solve,args=(*unsolvedcubes[t],t)) for t in range(threadn)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    #solve(*unsolvedcubes[0],0)
    #for j in range(threadn):
    #    solve(*unsolvedcubes[j],j)
    
    print("\nfinish all threads of cube",i+1)
    print("completed phase one number",verifiednum[-threadn:])
    
    if htm>=stepshouldbelow:
        miss+=1
        print("no solution below",htm,"steps for this cube")
        print("miss rate",miss,"/",i+1)
    else:
        bestthread=0
        print("{:<8}{:<8}{}".format("thread","htm","solution"))
        for j in range(threadn):
            print("{:<8}{:<8}{:<36}{}".format(j,int(log(threadsolutions[j],18)),threadsolutions[j],decodevalue(threadsolutions[j])))
            if minmove==threadsolutions[j]:
                bestthread=j
            elif minmove>threadsolutions[j]:
                minmove=threadsolutions[j]
                htm=int(log(threadsolutions[j],18))
                bestthread=j
        
        bestrotation=decodevalue(minmove)
        htms.append(htm)
        qtms.append(qtm)
        print("\nbest solution in thread",bestthread)
        print("min htm",htm,", qtm",qtm,"solution",minmove,bestrotation,rotatenumbertostring(bestrotation))
        print("current htm results:",htms)
        print("average htm",sum(htms)/len(htms))
        print("average qtm",sum(qtms)/len(qtms))
    t2=time.time()
    print("time:",t2-t1,"s ","average time",(t2-starttime)/(i+1),time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print("estimated time for rest",cubenumber-i-1,"cubes:",(t2-starttime)*(cubenumber-i-1)/(i+1),"s")
endtime=time.time()

print("\n\ntwo phase algorithm version 14")
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("dict time",tdictend-tdictstart,"s")
print("total time",endtime-starttime,"s, average time",(endtime-starttime)/cubenumber,"s")
print("average phase 1 completed number",sum(verifiednum)/len(verifiednum),"max",max(verifiednum),"min",min(verifiednum))
print("search depth",phase1maxstep,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
print("htm",htms)
print("qtm",qtms)
if len(htms)>0:
    print("htm average",sum(htms)/len(htms),"range",min(htms),"-",max(htms))
    print("qtm average",sum(qtms)/len(qtms),"range",min(qtms),"-",max(qtms))
    print("\nmove  number")
    for i in range(min(htms),max(htms)+1):
        print(i,"  ",htms.count(i))
if miss!=0:
    print("there are",miss,"of",cubenumber,"cubes has no solution under this search depth")

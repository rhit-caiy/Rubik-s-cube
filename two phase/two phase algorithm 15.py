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
cdict,codict,ep4dict,eodict={},{},{},{}
rcdict,rcodict,rep4dict,reodict={},{},{},{}
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
#ep4dict,up edge,middle edge,bottom edge, (0,1,2,3),(0,1,2,11),(0,1,3,2) 11880 P(12,4)
n=0
for i in combinations(range(12),r=4):
    for j in permutations(i):
        ep4dict[j]=n
        rep4dict[n]=j
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
cr,cor,ep4r,eor=[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)]
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
        d=ep4r[f][t]
        for dep in ep4dict.keys():
            ep=list(dep)
            for i in range(4):
                if ep[i] in fe:
                    ep[i]=fe[fte.index(ep[i])]
            d[ep4dict[dep]]=ep4dict[tuple(ep)]
        d=eor[f][t]
        for deo in eodict.keys():
            eo=list(deo)
            eo[e1],eo[e2],eo[e3],eo[e4]=ftd[eo[ne1]],ftd[eo[ne2]],ftd[eo[ne3]],ftd[eo[ne4]]
            d[eodict[deo]]=eodict[tuple(eo)]
print(time.time()-t1,"s")
ccn,ccon,cen1,cen2,cen3,ceon=cdict[cc],codict[cco],ep4dict[ce[0:4]],ep4dict[ce[4:8]],ep4dict[ce[8:12]],eodict[ceo]
cr0,cor0,eor0,ep4r0=[i[0] for i in cr],[i[0] for i in cor],[i[0] for i in eor],[i[0] for i in ep4r]
cr1,ep4r1=[i[1] for i in cr],[i[1] for i in ep4r]

def getdict1(dict1step):
    global dict1
    predictstate=[(ccon,ceon,cen2,1,-1,-1)]
    newpredictstate=[]
    key1=(ccon*2048+ceon)*495+cen2//24
    dict1[key1]=1
    t0=time.time()
    for step in range(1,dict1step+1):
        t1=time.time()
        for cube in predictstate:
            oco,oeo,oe2,oldstep,f1,f2=cube
            for f in [0,1,2,3,4,5]:
                if f1!=f and not (f1==5 and f==0 or f1==4 and f==2 or f1==3 and f==1):
                    newstep=oldstep*18+3*f+2
                    nco,neo,ne2=oco,oeo,oe2
                    corf0,eorf0,ep4rf0=cor[f][0],eor[f][0],ep4r[f][0]
                    for t in [0,1,2]:
                        nco,neo,ne2=corf0[nco],eorf0[neo],ep4rf0[ne2]
                        key1=(nco*2048+neo)*495+ne2//24
                        if key1 not in dict1:
                            dict1[key1]=newstep
                            if step!=dict1step:
                                newpredictstate.append((nco,neo,ne2,newstep,f,f1))
                        newstep-=1
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,step,len(newpredictstate),len(dict1),time.time()-t1),end="")
        predictstate,newpredictstate=newpredictstate,[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,"total","",len(dict1),time.time()-t0),end="")

def getdict2(dict2step):
    global dict2
    predictstate=[(ccn,cen1,cen2,cen3,0,-1,-1)]
    newpredictstate=[]
    key2=((ccn*11880+cen1)*11880+cen2)*11880+cen3
    dict2[key2]=1
    t0=time.time()
    for step in range(1,dict2step+1):
        t1=time.time()
        for cube in predictstate:
            oc,oe1,oe2,oe3,oldstep,f1,f2=cube
            for f,t in [(0,0),(0,1),(0,2),(1,1),(2,1),(3,1),(4,1),(5,0),(5,1),(5,2)]:
                if f1!=f and not (f1==5 and f==0 or f1==4 and f==2 or f1==3 and f==1):
                    nc,ne1,ne2,ne3=cr[f][t][oc],ep4r[f][t][oe1],ep4r[f][t][oe2],ep4r[f][t][oe3]
                    key2=((nc*11880+ne1)*11880+ne2)*11880+ne3
                    if key2 not in dict2:
                        newstep=oldstep+(3*f+2-t)*eighteen[step-1]
                        dict2[key2]=newstep+eighteen[step]
                        if step!=dict2step:
                            newpredictstate.append((nc,ne1,ne2,ne3,newstep,f,f1))
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,step,len(newpredictstate),len(dict2),time.time()-t1),end="")
        predictstate,newpredictstate=newpredictstate,[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,"total","",len(dict2),time.time()-t0),end="")

def solve(c,co,eo,e1,e2,e3,threadid):
    global threadsolutions,htm,qtm,minmove,verifiednum
    tstart=time.time()
    cubes=[(c,co,eo,e1,e2,e3,1,0,-1,-1)]
    solutionnum=0
    totalnum=1
    minstr=eighteen[stepshouldbelow]
    #phase 1
    while cubes:
        oc,oco,oeo,oe1,oe2,oe3,previousstep,step,f1,f2=cubes.pop()
        step+=1
        for f in [0,1,2,3,4,5]:
            if f!=f1 and not (f1==5 and f==0 or f1==4 and f==2 or f1==3 and f==1):
                m1_1=previousstep*18+3*f
                totalnum+=3
                crf0,corf0,eorf0,ep4rf0=cr0[f],cor0[f],eor0[f],ep4r0[f]
                nc,nco,neo,ne1,ne2,ne3=oc,oco,oeo,oe1,oe2,oe3
                for t in [0,1,2]:
                    nc,nco,neo,ne1,ne2,ne3=crf0[nc],corf0[nco],eorf0[neo],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                    if step<phase1maxstep:
                        cubes.append((nc,nco,neo,ne1,ne2,ne3,m1_1,step,f,f1))
                    key1=(nco*2048+neo)*495+ne2//24
                    if key1 in dict1:
                        solutionnum+=1
                        m1_2=dict1[key1]
                        if m1_2!=1:
                            nc1,ne11,ne21,ne31=nc,ne1,ne2,ne3
                            m1=m1_1
                            f0=f
                            while m1_2>=18:
                                ft=m1_2%18
                                m1_2//=18
                                m1=18*m1+ft
                                f0,t0=ft//3,ft%3
                                ep4rf0t0=ep4r[f0][t0]
                                nc1,ne11,ne21,ne31=cr[f0][t0][nc1],ep4rf0t0[ne11],ep4rf0t0[ne21],ep4rf0t0[ne31]
                            #phase 2
                            key2=((nc1*11880+ne11)*11880+ne21)*11880+ne31
                            if key2 in dict2:
                                m2=dict2[key2]
                                solution=(m1-1)*eighteen[int(log(m2,18))]+m2
                                if solution<minmove:
                                    minmove=minstr=solution
                                    qtmvalue=htm=int(log(solution,18))
                                    p2=int(log(m2,18))
                                    numstr=decodevalue(solution)
                                    for i in range(int(len(numstr)/2)):
                                        if numstr[2*i+1]=="1":
                                            qtmvalue+=1
                                    if qtmvalue<qtm:
                                        qtm=qtmvalue
                                    print("{:<8}{:<18}{:<6}{:<24}{:<14f}1     {:<36}{}\n".format(threadid,f"{htm} = {step} + {htm-step-p2} + {p2}",qtmvalue,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution,numstr),end="")
                            if int(log(m1,18))+dict2step<=htm or key2 in dict2 and int(log(solution,18))-1<=htm:
                                ep4rf01=ep4r1[f0]
                                nc1,ne11,ne21,ne31=cr1[f0][nc1],ep4rf01[ne11],ep4rf01[ne21],ep4rf01[ne31]
                                key2=((nc1*11880+ne11)*11880+ne21)*11880+ne31
                                if key2 in dict2:
                                    m2=dict2[key2]
                                    solution=(m1-3)*eighteen[int(log(m2,18))]+m2
                                    if solution<minmove:
                                        minmove=minstr=solution
                                        qtmvalue=htm=int(log(solution,18))
                                        p2=int(log(m2,18))
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
    c,co,eo,e1,e2,e3=ccn,ccon,ceon,cen1,cen2,cen3
    for i in range(l):
        f,t=changebasetable[base][int(randomstring[2*i])],int(randomstring[2*i+1])
        c,co,eo,e1,e2,e3=cr[f][t][c],cor[f][t][co],eor[f][t][eo],ep4r[f][t][e1],ep4r[f][t][e2],ep4r[f][t][e3]
    return c,co,eo,e1,e2,e3
    
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
print("{} + {}\n{:<8}{:<8}{:<16}{:<16}{:<16}\n".format(dict1step,dict2step,"dict","step","cubes left","dict length","time/s"),end="")
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
    print("completed phase one number",verifiednum[-threadn:],sum(verifiednum[-threadn:]))
    
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

print("\n\ntwo phase algorithm version 15")
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("dict time",tdictend-tdictstart,"s")
print("total time",endtime-starttime,"s, average time",(endtime-starttime)/cubenumber,"s")
print("average phase 1 completed number per thread",sum(verifiednum)/len(verifiednum),"max",max(verifiednum),"min",min(verifiednum))
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

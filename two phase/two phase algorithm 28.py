from time import time,strftime,localtime
from random import randint
from math import log
from itertools import permutations,product,combinations

def getdicts():
    t0=time()
    cc,cco,ce,ceo=(0,1,2,3,4,5,6,7),(0,0,0,0,0,0,0,0),(0,1,2,3,4,5,6,7,8,9,10,11),(0,0,0,0,0,0,0,0,0,0,0,0)
    facecorner=((0,2,3,1),(0,6,4,2),(2,4,5,3),(4,6,7,5),(3,5,7,1),(1,7,6,0))
    faceedge=((0,1,2,3),(1,4,9,5),(2,5,10,6),(10,9,8,11),(3,6,11,7),(0,7,8,4))
    cdict={i:n for n,i in enumerate(permutations(cc))}
    codict={i:n for n,i in enumerate((i for i in product(range(3),repeat=8) if not sum(i)%3))}
    eodict={i:n for n,i in enumerate([i for i in product(range(2),repeat=12) if not i.count(1)%2])}
    ep4dict={j:n for n,j in enumerate(j for i in combinations(ce,r=4) for j in permutations(i))}
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
    return tuple(cr),tuple(cor),tuple(ep4r),tuple(eor),cdict[cc],codict[cco],ep4dict[ce[0:4]],ep4dict[ce[4:8]],ep4dict[ce[8:12]],eodict[ceo],tuple([i[0] for i in cr]),tuple([i[0] for i in cor]),tuple([i[0] for i in eor]),tuple([i[0] for i in ep4r]),tuple([i[1] for i in cr]),tuple([i[1] for i in ep4r]),round(time()-t0,6)

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
                                        htm,qtm,stm,minmove=solved(m1-2,m2,minmove,l,htm,qtm,stm,step,tstart,2)
    return htm,qtm,stm,minmove,time()-tstart

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
cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1,tinit=getdicts()
print("initialize time",tinit,"s")
phase1step=5#7
dict1step=7#8
dict2step=8#9
stepshouldbelow=phase1step+dict1step+dict2step+1
print(phase1step,"+",dict1step,"+",dict2step)
dict1,tdict1=getdict1(dict1step,cor0,eor0,ep4r0)
print("{:<8}{:<16}{:<16}{:<16f}".format("total","",len(dict1),tdict1))
dict2,tdict2=getdict2(dict2step,eighteen,cr0,ep4r0,cr1,ep4r1)
print("{:<8}{:<16}{:<16}{:<16f}".format("total","",len(dict2),tdict2))
print(f"dicts time {tdict1+tdict2}s = {tdict1}s + {tdict2}s")
#totalnums=sum([round((-(6-3*6**0.5)**n*(-3+6**0.5)+(3*(2+6**0.5))**n*(3+6**0.5))/4) for n in range(phase1step+1)])-1#correct for n<=12, from sum of series OEIS A333298, real should be sum of A080583 from A080601
htms,qtms,stms,times,miss=[],[],[],[],0
n=6
cubenumber=10
print(cubenumber,"cubes",n,"threads")

starttime=time()
for i in range(cubenumber):
    print("\n\ncube",i+1)
    print(strftime("%Y-%m-%d %H:%M:%S",localtime()))
    print("search depth",phase1step,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
    htm,qtm,stm,minmove=stepshouldbelow,stepshouldbelow*2,stepshouldbelow,eighteen[stepshouldbelow]
    l=randint(1024,2048)
    randomlists=[[randint(0,17) for j in range(l)]]
    randomlists.append([(j//3)*6+2-j for j in randomlists[0][::-1]])
    print("random with",l,"moves\n")
    cubetime=0
    for j in range(n):
        randomlist=randomlists[j//3]
        direction=changedirections[j%3]
        c,co,eo,e1,e2,e3=ccn,ccon,ceon,cen1,cen2,cen3
        for k in range(l):
            f,t=direction[randomlist[k]//3],randomlist[k]%3
            ep4rft=ep4r[f][t]
            c,co,eo,e1,e2,e3=cr[f][t][c],cor[f][t][co],eor[f][t][eo],ep4rft[e1],ep4rft[e2],ep4rft[e3]
        print("{}\nc = {}  co = {}  eo = {}  e1 = {}  e2 = {}  e3 = {}\n{:<18}{:<6}{:<6}{:<14}{:<6}{:<36}".format("thread "+str(j),c,co,eo,e1,e2,e3,"htm","qtm","stm","time/s","type","solution"))
        htm,qtm,stm,minmove,threadtime=solve(c,co,eo,e1,e2,e3,j,htm,qtm,stm,minmove,phase1step,cr0,cor0,eor0,ep4r0,cr1,ep4r1,cr,ep4r,dict1,dict2,eighteen)
        print("finish thread {}    htm {}  qtm {}  stm {}    time {:f}s    {}\n".format(j,htm,qtm,stm,threadtime,strftime("%Y-%m-%d %H:%M:%S",localtime())))
        cubetime+=threadtime
    times.append(cubetime)
    print("finish solve cube",i+1)
    if htm>=stepshouldbelow:
        miss+=1
        print("no solution below",htm,"steps for this cube")
    else:
        htms.append(htm)
        qtms.append(qtm)
        stms.append(stm)
        numstr,num="",minmove
        while num>=18:
            numstr,num=str(num//3%6)+str(num%3)+numstr,num//18
        print("\nmin htm",htm,"qtm",qtm,"stm",stm,"\nsolution\n"+str(minmove)+"\n"+numstr)
        for j in range(htm):
            print(allrotation[3*int(numstr[2*j])+int(numstr[2*j+1])],end="")
        if i<100:
            print("\ncurrent htm results:",htms)
        print("\naverage htm",round(sum(htms)/len(htms),6),"\naverage qtm",round(sum(qtms)/len(qtms),6),"\naverage stm",round(sum(stms)/len(stms),6))
    if miss:
        print("miss rate",miss,"/",i+1)
    print("time:",round(cubetime,6),"s ","average time",round(sum(times)/(i+1),6),strftime("%Y-%m-%d %H:%M:%S",localtime()))
    print("estimated time for rest",cubenumber-i-1,"cubes:",round((time()-starttime)*(cubenumber-i-1)/(i+1),6),"s")
endtime=time()

print("\n\ntwo phase algorithm version 28")
print(strftime("%Y-%m-%d %H:%M:%S",localtime()))
print(f"initialize time {tinit}s\ndicts time {tdict1+tdict2}s = {tdict1}s + {tdict2}s")
print(f"total time {round(endtime-starttime,6)}s, actual time {round(sum(times),6)}s, average time {round(sum(times)/cubenumber,6)}s")
print("search depth",phase1step,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
if cubenumber<=100:
    print("htm",htms,"\nqtm",qtms,"\nstm",stms)
print(cubenumber,"cubes")
if len(htms)>0:
    print("\nhtm average",round(sum(htms)/len(htms),6),"range",min(htms),"-",max(htms),"\nhtm     number")
    for i in range(min(htms),max(htms)+1):
        print("{:<8}{:<8}{}".format(i,htms.count(i),"-"*int(100*htms.count(i)/cubenumber)))
    print("\nqtm average",round(sum(qtms)/len(qtms),6),"range",min(qtms),"-",max(qtms),"\nqtm     number")
    for i in range(min(qtms),max(qtms)+1):
        print("{:<8}{:<8}{}".format(i,qtms.count(i),"-"*int(100*qtms.count(i)/cubenumber)))
    print("\nstm average",round(sum(stms)/len(stms),6),"range",min(stms),"-",max(stms),"\nstm     number")
    for i in range(min(stms),max(stms)+1):
        print("{:<8}{:<8}{}".format(i,stms.count(i),"-"*int(100*stms.count(i)/cubenumber)))
if miss!=0:
    print("miss rate",miss,"/",cubenumber)

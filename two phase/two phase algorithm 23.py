import time
from random import randint
from math import log
from itertools import permutations,product,combinations

def getdicts():
    cc,cco,ce,ceo=(0,1,2,3,4,5,6,7),(0,0,0,0,3,3,3,3),(0,1,2,3,4,5,6,7,8,9,10,11),(0,0,0,0,1,1,4,4,3,3,3,3)
    facecorner=[(0,2,3,1),(0,6,4,2),(2,4,5,3),(4,6,7,5),(3,5,7,1),(1,7,6,0)]
    faceedge=[(0,1,2,3),(1,4,9,5),(2,5,10,6),(10,9,8,11),(3,6,11,7),(0,7,8,4)]
    facetimedirection=[[[0,5,1,3,2,4],[0,4,5,3,1,2]],[[2,1,3,5,4,0],[3,1,5,0,4,2]],[[4,0,2,1,3,5],[3,4,2,0,1,5]],[[0,2,4,3,5,1],[0,4,5,3,1,2]],[[5,1,0,2,4,3],[3,1,5,0,4,2]],[[1,3,2,4,0,5],[3,4,2,0,1,5]]]
    cornerdirection=[(0,5,1),(0,4,5),(0,1,2),(0,2,4),(3,2,1),(3,4,2),(3,1,5),(3,5,4)]
    edgedirection=[(0,5),(0,1),(0,2),(0,4),(1,5),(1,2),(4,2),(4,5),(3,5),(3,1),(3,2),(3,4)]
    cdict,codict,ep4dict,eodict={},{},{},{}
    n=0
    for i in permutations(cc):
        cdict[i]=n
        n=1676676672000+n
    n=0
    for i in product(range(3),repeat=8):
        if not sum(i)%3:
            codict[tuple([cornerdirection[j][i[j]] for j in range(8)])]=n
            n=1013760+n
    n=0
    for i in combinations(ce,r=4):
        for j in permutations(i):
            ep4dict[j]=n
            n=1+n
    n=0
    for i in product(range(2),repeat=12):
        if not sum(i)%2:
            eodict[tuple([edgedirection[j][i[j]] for j in range(12)])]=n
            n=495+n
    cr,cor,ep4r,eor=[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)]
    for f in [0,1,2,3,4,5]:
        c1,c2,c3,c4=facecorner[f]
        e1,e2,e3,e4=fe=faceedge[f]
        sfe=set(fe)
        fte=e2,e3,e4,e1
        ftd0,ftd1=facetimedirection[f]
        d0,d1,d2=cr[f]
        for dc in cdict:
            c=list(dc)
            c[c1],c[c2],c[c3],c[c4]=c[c2],c[c3],c[c4],c[c1]
            a,b=cdict[dc],cdict[tuple(c)]
            d0[a],d2[b]=b,a
            if a not in d1:
                c[c1],c[c2],c[c3],c[c4]=c[c2],c[c3],c[c4],c[c1]
                b=cdict[tuple(c)]
                d1[a],d1[b]=b,a
        d0,d1,d2=cor[f]
        for dco in codict:
            co=list(dco)
            co[c1],co[c2],co[c3],co[c4]=ftd0[co[c2]],ftd0[co[c3]],ftd0[co[c4]],ftd0[co[c1]]
            a,b=codict[dco],codict[tuple(co)]
            d0[a],d2[b]=b,a
            if a not in d1:
                co[c1],co[c2],co[c3],co[c4]=ftd0[co[c2]],ftd0[co[c3]],ftd0[co[c4]],ftd0[co[c1]]
                b=codict[tuple(co)]
                d1[a],d1[b]=b,a
        d0,d1,d2=ep4r[f]
        for dep in ep4dict:
            ep=list(dep)
            for i in [0,1,2,3]:
                if ep[i] in sfe:
                    ep[i]=fe[fte.index(ep[i])]
            a,b=ep4dict[dep],ep4dict[tuple(ep)]
            d0[a],d2[b]=b,a
            if a not in d1:
                for i in [0,1,2,3]:
                    if ep[i] is not dep[i]:
                        ep[i]=fe[fte.index(ep[i])]
                b=ep4dict[tuple(ep)]
                d1[a],d1[b]=b,a
        d0,d1,d2=eor[f]
        for deo in eodict:
            eo=list(deo)
            eo[e1],eo[e2],eo[e3],eo[e4]=ftd0[eo[e2]],ftd0[eo[e3]],ftd0[eo[e4]],ftd0[eo[e1]]
            a,b=eodict[deo],eodict[tuple(eo)]
            d0[a],d2[b]=b,a
            if a not in d1:
                eo[e1],eo[e2],eo[e3],eo[e4]=ftd0[eo[e2]],ftd0[eo[e3]],ftd0[eo[e4]],ftd0[eo[e1]]
                b=eodict[tuple(eo)]
                d1[a],d1[b]=b,a
    ccn,ccon,cen1,cen2,cen3,ceon=cdict[cc],codict[cco],ep4dict[ce[0:4]],ep4dict[ce[4:8]],ep4dict[ce[8:12]],eodict[ceo]
    cr0,cor0,eor0,ep4r0,cr1,ep4r1=[i[0] for i in cr],[i[0] for i in cor],[i[0] for i in eor],[i[0] for i in ep4r],[i[1] for i in cr],[i[1] for i in ep4r]
    return cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1

def getdict1(dict1step):
    print("\ndict1\n{:<8}{:<16}{:<16}{:<16}\n".format("step","cubes left","dict length","time/s"),end="")
    dict1={cen2//24+ceon+ccon:1}
    predictstate,newpredictstate=[(ccon,ceon,cen2,1,-1)],[]
    t0=time.time()
    for step in range(1,dict1step+1):
        t1=time.time()
        for cube in predictstate:
            oco,oeo,oe2,oldstep,f1=cube
            oldstep=18*oldstep
            for f in [0,1,2,3,4,5]:
                if f1 is not f and f1-f!=3:
                    newstep=oldstep+3*f
                    nco,neo,ne2=oco,oeo,oe2
                    corf0,eorf0,ep4rf0=cor0[f],eor0[f],ep4r0[f]
                    for newstep in [newstep+2,newstep+1,newstep]:
                        nco,neo,ne2=corf0[nco],eorf0[neo],ep4rf0[ne2]
                        key1=ne2//24+neo+nco
                        if key1 not in dict1:
                            dict1[key1]=newstep
                            if step is not dict1step:
                                newpredictstate.append((nco,neo,ne2,newstep,f))
        print("{:<8}{:<16}{:<16}{:<16f}\n".format(step,len(newpredictstate),len(dict1),time.time()-t1),end="")
        predictstate,newpredictstate=newpredictstate,[]
    dict1.pop(cen2//24+ceon+ccon)
    print("{:<8}{:<16}{:<16}{:<16f}\n".format("total","",len(dict1),time.time()-t0),end="")
    return dict1

def getdict2(dict2step):
    print("\ndict2\n{:<8}{:<16}{:<16}{:<16}\n".format("step","cubes left","dict length","time/s"),end="")
    dict2={ccn+cen3+11880*(cen2+11880*cen1):1}
    predictstate,newpredictstate=[(ccn,cen1,cen2,cen3,0,-1)],[]
    t0=time.time()
    for step in range(1,dict2step+1):
        t1=time.time()
        eighteen0,eighteen1=eighteen[step-1],eighteen[step]
        for cube in predictstate:
            oc,oe1,oe2,oe3,oldstep,f1=cube
            for f in [0,3]:
                if f1 is not f and (f1!=3 or f!=3):
                    crf0,ep4rf0=cr0[f],ep4r0[f]
                    nc,ne1,ne2,ne3=oc,oe1,oe2,oe3
                    for t in [2,1,0]:
                        nc,ne1,ne2,ne3=crf0[nc],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                        key2=nc+ne3+11880*(ne2+11880*ne1)
                        if key2 not in dict2:
                            newstep=oldstep+(3*f+t)*eighteen0
                            dict2[key2]=newstep+eighteen1
                            if step is not dict2step:
                                newpredictstate.append((nc,ne1,ne2,ne3,newstep,f))
            for f in [1,2,4,5]:
                if f1 is not f and f1-f!=3:
                    ep4rf1=ep4r1[f]
                    nc,ne1,ne2,ne3=cr1[f][oc],ep4rf1[oe1],ep4rf1[oe2],ep4rf1[oe3]
                    key2=nc+ne3+11880*(ne2+11880*ne1)
                    if key2 not in dict2:
                        newstep=oldstep+(3*f+1)*eighteen0
                        dict2[key2]=newstep+eighteen1
                        if step is not dict2step:
                            newpredictstate.append((nc,ne1,ne2,ne3,newstep,f))
        print("{:<8}{:<16}{:<16}{:<16f}\n".format(step,len(newpredictstate),len(dict2),time.time()-t1),end="")
        predictstate,newpredictstate=newpredictstate,[]
    print("{:<8}{:<16}{:<16}{:<16f}\n".format("total","",len(dict2),time.time()-t0),end="")
    return dict2

def solve(c,co,eo,e1,e2,e3,threadid,htm,qtm,stm,minmove):
    tstart=time.time()
    print("{}\n{:<18}{:<6}{:<6}{:<24}{:<14}{:<6}{:<36}".format("thread "+str(threadid),"htm","qtm","stm","dict2/dict1/total","time/s","type","solution"))
    cubes,totalnum,phase1num,phase2num=[(c,co,eo,e1,e2,e3,1,0,-1)],1,0,0
    while cubes:
        oc,oco,oeo,oe1,oe2,oe3,oldstep,step,f1=cubes.pop()
        step,oldstep=1+step,18*oldstep
        for f in [0,1,2,3,4,5]:
            if f is not f1 and f1-f!=3:
                m1_1,totalnum=oldstep+3*f,3+totalnum
                crf0,corf0,eorf0,ep4rf0=cr0[f],cor0[f],eor0[f],ep4r0[f]
                nc,nco,neo,ne1,ne2,ne3=oc,oco,oeo,oe1,oe2,oe3
                for m1 in [m1_1,m1_1+1,m1_1+2]:
                    nc,nco,neo,ne1,ne2,ne3=crf0[nc],corf0[nco],eorf0[neo],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                    if step is not phase1step:
                        cubes.append((nc,nco,neo,ne1,ne2,ne3,m1,step,f))
                    if ne2//24+neo+nco in dict1:
                        phase1num,m1_2,f0,nc1,ne11,ne21,ne31=1+phase1num,dict1[ne2//24+neo+nco],f,nc,ne1,ne2,ne3
                        while m1_2>=18:
                            f0,t0,m1,m1_2=(m1_2//3)%6,m1_2%3,18*m1+m1_2%18,m1_2//18
                            ep4rf0t0=ep4r[f0][t0]
                            nc1,ne11,ne21,ne31=cr[f0][t0][nc1],ep4rf0t0[ne11],ep4rf0t0[ne21],ep4rf0t0[ne31]
                        if nc1+ne31+11880*(ne21+11880*ne11) in dict2:
                            phase2num,m2=1+phase2num,dict2[nc1+ne31+11880*(ne21+11880*ne11)]
                            l=int(log(m1,18))+int(log(m2,18))
                            if l<=htm:
                                solution=(m1-1)*eighteen[int(log(m2,18))]+m2
                                if solution<minmove:
                                    minmove=solution
                                qtmvalue=stmvalue=htm=l
                                numstr=decodevalue(solution)
                                for i in range(1,len(numstr),2):
                                    if numstr[i]=="1":
                                        qtmvalue+=1
                                for i in range(0,len(numstr)-2,2):
                                    if abs(int(numstr[i])-int(numstr[i+2]))==3 and int(numstr[i+1])+int(numstr[i+3])==2:
                                        stmvalue-=1
                                if qtmvalue<qtm:
                                    qtm=qtmvalue
                                if stmvalue<stm:
                                    stm=stmvalue
                                print("{:<18}{:<6}{:<6}{:<24}{:<14f}1     {:<36}{}\n".format(f"{htm} = {step} + {htm-step-int(log(m2,18))} + {int(log(m2,18))}",qtmvalue,stmvalue,str(phase2num)+"/"+str(phase1num)+"/"+str(totalnum),time.time()-tstart,solution,numstr),end="")
                                ep4rf01=ep4r1[f0]
                                nc1,ne11,ne21,ne31=cr1[f0][nc1],ep4rf01[ne11],ep4rf01[ne21],ep4rf01[ne31]
                                if nc1+ne31+11880*(ne21+11880*ne11) in dict2:
                                    m2=dict2[nc1+ne31+11880*(ne21+11880*ne11)]
                                    l=int(log(m1,18))+int(log(m2,18))
                                    if l<=htm:
                                        solution=(m1-1)*eighteen[int(log(m2,18))]+m2
                                        if solution<minmove:
                                            minmove=solution
                                        qtmvalue=stmvalue=htm=l
                                        numstr=decodevalue(solution)
                                        for i in range(1,len(numstr),2):
                                            if numstr[i]=="1":
                                                qtmvalue+=1
                                        for i in range(0,len(numstr)-2,2):
                                            if abs(int(numstr[i])-int(numstr[i+2]))==3 and int(numstr[i+1])+int(numstr[i+3])==2:
                                                stmvalue-=1
                                        if qtmvalue<qtm:
                                            qtm=qtmvalue
                                        if stmvalue<stm:
                                            stm=stmvalue
                                        print("{:<18}{:<6}{:<6}{:<24}{:<14f}2     {:<36}{}\n".format(f"{htm} = {step} + {htm-step-int(log(m2,18))} + {int(log(m2,18))}",qtmvalue,stmvalue,str(phase2num)+"/"+str(phase1num)+"/"+str(totalnum),time.time()-tstart,solution,numstr),end="")
    print("finish thread {}    htm {}  qtm {}  stm {}  {}/{}/{}    time {:f}s    {}\n\n".format(threadid,htm,qtm,stm,phase2num,phase1num,totalnum,time.time()-tstart,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())),end="")
    return htm,qtm,stm,minmove,phase1num,phase2num,time.time()-tstart

def randomcube():
    randomstring=reverserandomstring=""
    for i in range(randint(1024,2048)):
        f,t=randint(0,5),randint(0,2)
        randomstring+=str(f)+str(t)
        reverserandomstring=str(f)+str(2-t)+reverserandomstring
    return randomstring,reverserandomstring
def getcubewithbase(randomstring,base,l):
    direction,c,co,eo,e1,e2,e3=[[0,1,2,3,4,5],[1,2,0,4,5,3],[2,0,1,5,3,4]][base],ccn,ccon,ceon,cen1,cen2,cen3
    for i in range(l):
        f,t=direction[int(randomstring[2*i])],int(randomstring[2*i+1])
        ep4rft=ep4r[f][t]
        c,co,eo,e1,e2,e3=cr[f][t][c],cor[f][t][co],eor[f][t][eo],ep4rft[e1],ep4rft[e2],ep4rft[e3]
    return c,co,eo,e1,e2,e3
def decodevalue(n):
    s=""
    while n>=18:
        ft,n=n%18,n//18
        s=str(ft//3)+str(ft%3)+s
    return s
def rotatenumbertostring(s):
    allrotation,r=["U","U2","U'","L","L2","L'","F","F2","F'","D","D2","D'","R","R2","R'","B","B2","B'"],""
    for i in range(len(s)//2):
        r+=allrotation[3*int(s[2*i])+int(s[2*i+1])]
    return r

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
eighteen=[18**i for i in range(28)]
t=time.time()
cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1=getdicts()
tinit=time.time()-t
print("initialize time",tinit,"s")
phase1step=5#7
dict1step=7#8
dict2step=8#9
stepshouldbelow=phase1step+dict1step+dict2step+1
print(phase1step,"+",dict1step,"+",dict2step)
tdict0=time.time()
dict1=getdict1(dict1step)
tdict1=time.time()
dict2=getdict2(dict2step)
tdict2=time.time()
print(f"dicts time {tdict2-tdict0}s = {tdict1-tdict0}s + {tdict2-tdict1}s")

htms,qtms,stms,p1,p2,times,miss=[],[],[],[],[],[],0
totalnums=sum([round((-(6-3*6**0.5)**n*(-3+6**0.5)+(3*(2+6**0.5))**n*(3+6**0.5))/4) for n in range(phase1step+1)])-1#correct for n<=12, from sum of series OEIS A333298, real should be sum of A080583 from A080601
n=6
cubenumber=10

starttime=time.time()
for i in range(cubenumber):
    print("\n\ncube",i+1)
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print("search depth",phase1step,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
    htm,qtm,stm,minmove=stepshouldbelow,stepshouldbelow*2,stepshouldbelow,eighteen[stepshouldbelow]
    randomstrings=randomcube()
    l=len(randomstrings[0])//2
    print("random with",l,"moves\n")
    solutions=[eighteen[stepshouldbelow]]*n
    t=0
    for base in range(n):
        htm,qtm,stm,minmove,phase1num,phase2num,t1=solve(*getcubewithbase(randomstrings[base//3],base%3,l),base,htm,qtm,stm,minmove)
        solutions[base]=minmove
        p1.append(phase1num)
        p2.append(phase2num)
        t+=t1
    times.append(t)
    print("finish solve cube",i+1)
    print("{:<8}{:<8}{:<8}{:<8}{}".format("thread","htm","phase1","phase2","solution"))
    for j in range(n):
        print("{:<8}{:<8}{:<8}{:<8}{:<36}{}".format(j,int(log(solutions[j],18)),p1[-n+j],p2[-n+j],solutions[j],decodevalue(solutions[j])))
    print("phase 1 number",sum(p1[-n:]),"\nphase 2 number",sum(p2[-n:]))
    if sum(p1[-n:]):
        print("phase1/total",sum(p1[-n:])/n/totalnums,"phase2/phase1",sum(p2[-n:])/sum(p1[-n:]))
    if htm>=stepshouldbelow:
        miss+=1
        print("no solution below",htm,"steps for this cube\nmiss rate",miss,"/",i+1)
    else:
        htms.append(htm)
        qtms.append(qtm)
        stms.append(stm)
        print("\nmin htm",htm,", qtm",qtm,"stm",stm,"solution",minmove,decodevalue(minmove),rotatenumbertostring(decodevalue(minmove)))
        if i<100:
            print("current htm results:",htms)
        print("average htm",sum(htms)/len(htms),"\naverage qtm",sum(qtms)/len(qtms),"\naverage stm",sum(stms)/len(stms))
    print("time:",t,"s ","average time",sum(times)/(i+1),time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print("estimated time for rest",cubenumber-i-1,"cubes:",(time.time()-starttime)*(cubenumber-i-1)/(i+1),"s")
endtime=time.time()

print("\n\ntwo phase algorithm version 22")
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("initialize time",tinit,"s")
print(f"dicts time {tdict2-tdict0}s = {tdict1-tdict0}s + {tdict2-tdict1}s")
print(f"total time {endtime-starttime}s, actual time {sum(times)}s, average time {sum(times)/cubenumber}s")
print("average phase 1 completed number per thread",sum(p1)/len(p1),"max",max(p1),"min",min(p1))
print("average phase 2 completed number per thread",sum(p2)/len(p2),"max",max(p2),"min",min(p2))
print("phase1/total",sum(p1)/len(p1)/totalnums,"\nphase2/phase1",(sum(p2)/len(p2))/(sum(p1)/len(p1)))
print("search depth",phase1step,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
if cubenumber<=100:
    print("htm",htms,"\nqtm",qtms,"\nstm",stms)
print(cubenumber,"cubes")
if len(htms)>0:
    print("\nhtm average",sum(htms)/len(htms),"range",min(htms),"-",max(htms),"\nhtm     number")
    for i in range(min(htms),max(htms)+1):
        print("{:<8}{:<8}{}".format(i,htms.count(i),"-"*int(100*htms.count(i)/cubenumber)))
    print("\nqtm average",sum(qtms)/len(qtms),"range",min(qtms),"-",max(qtms),"\nqtm     number")
    for i in range(min(qtms),max(qtms)+1):
        print("{:<8}{:<8}{}".format(i,qtms.count(i),"-"*int(100*qtms.count(i)/cubenumber)))
    print("\nstm average",sum(stms)/len(stms),"range",min(stms),"-",max(stms),"\nstm     number")
    for i in range(min(stms),max(stms)+1):
        print("{:<8}{:<8}{}".format(i,stms.count(i),"-"*int(100*stms.count(i)/cubenumber)))
if miss!=0:
    print("miss rate",miss,"/",cubenumber)

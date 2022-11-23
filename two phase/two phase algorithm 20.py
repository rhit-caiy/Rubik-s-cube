import time
from random import randint
from math import log
from itertools import permutations,product,combinations

def getdicts():
    cc,cco,ce,ceo=(0,1,2,3,4,5,6,7),(0,0,0,0,3,3,3,3),(0,1,2,3,4,5,6,7,8,9,10,11),(0,0,0,0,1,1,4,4,3,3,3,3)
    facetimecorner=[[(2,3,1,0),(3,1,0,2),(1,0,2,3)],[(6,4,2,0),(4,2,0,6),(2,0,6,4)],[(4,5,3,2),(5,3,2,4),(3,2,4,5)],[(6,7,5,4),(7,5,4,6),(5,4,6,7)],[(5,7,1,3),(7,1,3,5),(1,3,5,7)],[(7,6,0,1),(6,0,1,7),(0,1,7,6)]]
    facetimeedge=[[(1,2,3,0),(2,3,0,1),(3,0,1,2)],[(4,9,5,1),(9,5,1,4),(5,1,4,9)],[(5,10,6,2),(10,6,2,5),(6,2,5,10)],[(9,8,11,10),(8,11,10,9),(11,10,9,8)],[(6,11,7,3),(11,7,3,6),(7,3,6,11)],[(7,8,4,0),(8,4,0,7),(4,0,7,8)]]
    facecorner=[(0,2,3,1),(0,6,4,2),(2,4,5,3),(4,6,7,5),(3,5,7,1),(1,7,6,0)]
    faceedge=[(0,1,2,3),(1,4,9,5),(2,5,10,6),(10,9,8,11),(3,6,11,7),(0,7,8,4)]
    facetimedirection=[[[0,5,1,3,2,4],[0,4,5,3,1,2],[0,2,4,3,5,1]],[[2,1,3,5,4,0],[3,1,5,0,4,2],[5,1,0,2,4,3]],[[4,0,2,1,3,5],[3,4,2,0,1,5],[1,3,2,4,0,5]],[[0,2,4,3,5,1],[0,4,5,3,1,2],[0,5,1,3,2,4]],[[5,1,0,2,4,3],[3,1,5,0,4,2],[2,1,3,5,4,0]],[[1,3,2,4,0,5],[3,4,2,0,1,5],[4,0,2,1,3,5]]]
    cornerdirection=[(0,5,1),(0,4,5),(0,1,2),(0,2,4),(3,2,1),(3,4,2),(3,1,5),(3,5,4)]
    edgedirection=[(0,5),(0,1),(0,2),(0,4),(1,5),(1,2),(4,2),(4,5),(3,5),(3,1),(3,2),(3,4)]
    cdict,codict,ep4dict,eodict={},{},{},{}
    for n,i in enumerate(permutations(cc)):
        cdict[i]=n
    n=0
    for i in product(range(3),repeat=8):
        if sum(i)%3==0:
            codict[tuple([cornerdirection[j][i[j]] for j in range(8)])]=n
            n=1+n
    n=0
    for i in combinations(ce,r=4):
        for j in permutations(i):
            ep4dict[j]=n
            n=1+n
    n=0
    for i in product(range(2),repeat=12):
        if sum(i)%2==0:
            eodict[tuple([edgedirection[j][i[j]] for j in range(12)])]=n
            n=1+n
    cr,cor,ep4r,eor=[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)]
    for f in [0,1,2,3,4,5]:
        c1,c2,c3,c4=facecorner[f]
        e1,e2,e3,e4=fe=faceedge[f]
        sfe=set(fe)
        
        nc1,nc2,nc3,nc4=facetimecorner[f][1]
        ne1,ne2,ne3,ne4=fte=facetimeedge[f][1]
        ftd=facetimedirection[f][1]
        d=cr[f][1]
        for dc in cdict:
            a=cdict[dc]
            if a not in d:
                c=list(dc)
                c[c1],c[c2],c[c3],c[c4]=c[nc1],c[nc2],c[nc3],c[nc4]
                b=cdict[tuple(c)]
                d[a],d[b]=b,a
        d=cor[f][1]
        for dco in codict:
            a=codict[dco]
            if a not in d:
                co=list(dco)
                co[c1],co[c2],co[c3],co[c4]=ftd[co[nc1]],ftd[co[nc2]],ftd[co[nc3]],ftd[co[nc4]]
                b=codict[tuple(co)]
                d[a],d[b]=b,a
        d=ep4r[f][1]
        for dep in ep4dict:
            a=ep4dict[dep]
            if a not in d:
                ep=list(dep)
                for i in [0,1,2,3]:
                    if ep[i] in sfe:
                        ep[i]=fe[fte.index(ep[i])]
                b=ep4dict[tuple(ep)]
                d[a],d[b]=b,a
        d=eor[f][1]
        for deo in eodict:
            a=eodict[deo]
            if a not in d:
                eo=list(deo)
                eo[e1],eo[e2],eo[e3],eo[e4]=ftd[eo[ne1]],ftd[eo[ne2]],ftd[eo[ne3]],ftd[eo[ne4]]
                b=eodict[tuple(eo)]
                d[a],d[b]=b,a
        
        nc1,nc2,nc3,nc4=facetimecorner[f][0]
        ne1,ne2,ne3,ne4=fte=facetimeedge[f][0]
        ftd=facetimedirection[f][0]
        d0,d2=cr[f][0],cr[f][2]
        for dc in cdict:
            c=list(dc)
            c[c1],c[c2],c[c3],c[c4]=c[nc1],c[nc2],c[nc3],c[nc4]
            a,b=cdict[dc],cdict[tuple(c)]
            d0[a],d2[b]=b,a
        d0,d2=cor[f][0],cor[f][2]
        for dco in codict:
            co=list(dco)
            co[c1],co[c2],co[c3],co[c4]=ftd[co[nc1]],ftd[co[nc2]],ftd[co[nc3]],ftd[co[nc4]]
            a,b=codict[dco],codict[tuple(co)]
            d0[a],d2[b]=b,a
        d0,d2=ep4r[f][0],ep4r[f][2]
        for dep in ep4dict:
            ep=list(dep)
            for i in [0,1,2,3]:
                if ep[i] in sfe:
                    ep[i]=fe[fte.index(ep[i])]
            a,b=ep4dict[dep],ep4dict[tuple(ep)]
            d0[a],d2[b]=b,a
        d0,d2=eor[f][0],eor[f][2]
        for deo in eodict:
            eo=list(deo)
            eo[e1],eo[e2],eo[e3],eo[e4]=ftd[eo[ne1]],ftd[eo[ne2]],ftd[eo[ne3]],ftd[eo[ne4]]
            a,b=eodict[deo],eodict[tuple(eo)]
            d0[a],d2[b]=b,a
    ccn,ccon,cen1,cen2,cen3,ceon=cdict[cc],codict[cco],ep4dict[ce[0:4]],ep4dict[ce[4:8]],ep4dict[ce[8:12]],eodict[ceo]
    cr0,cor0,eor0,ep4r0,cr1,ep4r1=[i[0] for i in cr],[i[0] for i in cor],[i[0] for i in eor],[i[0] for i in ep4r],[i[1] for i in cr],[i[1] for i in ep4r]
    return cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1

def getdict1(dict1step):
    dict1={(ccon*2048+ceon)*495+cen2//24:1}
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
                        key1=(nco*2048+neo)*495+ne2//24
                        if key1 not in dict1:
                            dict1[key1]=newstep
                            if step is not dict1step:
                                newpredictstate.append((nco,neo,ne2,newstep,f))
        print("{:<8}{:<16}{:<16}{:<16f}\n".format(step,len(newpredictstate),len(dict1),time.time()-t1),end="")
        predictstate,newpredictstate=newpredictstate,[]
    dict1.pop((ccon*2048+ceon)*495+cen2//24)
    print("{:<8}{:<16}{:<16}{:<16f}\n".format("total","",len(dict1),time.time()-t0),end="")
    return dict1

def getdict2(dict2step):
    dict2={((ccn*11880+cen1)*11880+cen2)*11880+cen3:1}
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
                        key2=((nc*11880+ne1)*11880+ne2)*11880+ne3
                        if key2 not in dict2:
                            newstep=oldstep+(3*f+t)*eighteen0
                            dict2[key2]=newstep+eighteen1
                            if step is not dict2step:
                                newpredictstate.append((nc,ne1,ne2,ne3,newstep,f))
            for f in [1,2,4,5]:
                if f1 is not f and f1-f!=3:
                    ep4rf1=ep4r1[f]
                    nc,ne1,ne2,ne3=cr1[f][oc],ep4rf1[oe1],ep4rf1[oe2],ep4rf1[oe3]
                    key2=((nc*11880+ne1)*11880+ne2)*11880+ne3
                    if key2 not in dict2:
                        newstep=oldstep+(3*f+1)*eighteen0
                        dict2[key2]=newstep+eighteen1
                        if step is not dict2step:
                            newpredictstate.append((nc,ne1,ne2,ne3,newstep,f))
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,step,len(newpredictstate),len(dict2),time.time()-t1),end="")
        predictstate,newpredictstate=newpredictstate,[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format("","total","",len(dict2),time.time()-t0),end="")
    return dict2

def solve(c,co,eo,e1,e2,e3,solveid,htm,qtm,minmove):
    tstart=time.time()
    cubes,solutionnum,totalnum=[(c,co,eo,e1,e2,e3,1,0,-1)],0,1
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
                    if step is not phase1maxstep:
                        cubes.append((nc,nco,neo,ne1,ne2,ne3,m1,step,f))
                    key1=(nco*2048+neo)*495+ne2//24
                    if key1 in dict1:
                        solutionnum,m1_2,f0,nc1,ne11,ne21,ne31=1+solutionnum,dict1[key1],f,nc,ne1,ne2,ne3
                        while m1_2>=18:
                            f0,t0,m1,m1_2=(m1_2//3)%6,m1_2%3,18*m1+m1_2%18,m1_2//18
                            ep4rf0t0=ep4r[f0][t0]
                            nc1,ne11,ne21,ne31=cr[f0][t0][nc1],ep4rf0t0[ne11],ep4rf0t0[ne21],ep4rf0t0[ne31]
                        key2=((nc1*11880+ne11)*11880+ne21)*11880+ne31
                        if key2 in dict2:
                            m2=dict2[key2]
                            l=int(log(m1,18))+int(log(m2,18))
                            if l<=htm:
                                solution=(m1-1)*eighteen[int(log(m2,18))]+m2
                                if solution<minmove:
                                    minmove=solution
                                qtmvalue=htm=l
                                numstr=decodevalue(solution)
                                for i in range(1,len(numstr),2):
                                    if numstr[i]=="1":
                                        qtmvalue+=1
                                if qtmvalue<qtm:
                                    qtm=qtmvalue
                                print("{:<8}{:<18}{:<6}{:<24}{:<14f}1     {:<36}{}\n".format(solveid,f"{htm} = {step} + {htm-step-int(log(m2,18))} + {int(log(m2,18))}",qtmvalue,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution,numstr),end="")
                                ep4rf01=ep4r1[f0]
                                nc1,ne11,ne21,ne31=cr1[f0][nc1],ep4rf01[ne11],ep4rf01[ne21],ep4rf01[ne31]
                                key2=((nc1*11880+ne11)*11880+ne21)*11880+ne31
                                if key2 in dict2:
                                    m2=dict2[key2]
                                    l=int(log(m1,18))+int(log(m2,18))
                                    if l<=htm:
                                        solution=(m1-1)*eighteen[int(log(m2,18))]+m2
                                        if solution<minmove:
                                            minmove=solution
                                        qtmvalue=htm=l
                                        numstr=decodevalue(solution)
                                        for i in range(1,len(numstr),2):
                                            if numstr[i]=="1":
                                                qtmvalue+=1
                                        if qtmvalue<qtm:
                                            qtm=qtmvalue
                                        print("{:<8}{:<18}{:<6}{:<24}{:<14f}2     {:<36}{}\n".format(solveid,f"{htm} = {step} + {htm-step-int(log(m2,18))} + {int(log(m2,18))}",qtmvalue,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution,numstr),end="")
    print("finish thread {}    min htm {}  qtm {}  {}/{}    time {:f}s    {}\n".format(solveid,htm,qtm,solutionnum,totalnum,time.time()-tstart,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())),end="")
    return htm,qtm,minmove,solutionnum,time.time()-tstart

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
t1=time.time()
cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1=getdicts()
tinit=time.time()-t1
print("initialize time",tinit,"s")
phase1maxstep=5#6
dict1step=7#8
dict2step=8#9
stepshouldbelow=phase1maxstep+dict1step+dict2step+1
print("{} + {} + {}".format(phase1maxstep,dict1step,dict2step))
print("\ndict1\n{:<8}{:<16}{:<16}{:<16}\n".format("step","cubes left","dict length","time/s"),end="")
tdict0=time.time()
dict1=getdict1(dict1step)
tdict1=time.time()
print("\ndict2\n{:<8}{:<16}{:<16}{:<16}\n".format("step","cubes left","dict length","time/s"),end="")
dict2=getdict2(dict2step)
tdict2=time.time()
print(f"dicts time {tdict2-tdict0}s = {tdict1-tdict0}s + {tdict2-tdict1}s")

htms,qtms,verifiednum,times,miss=[],[],[],[],0
n=6
cubenumber=10

starttime=time.time()
for i in range(cubenumber):
    print("\n\ncube",i+1)
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print("search depth",phase1maxstep,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
    htm,qtm,minmove=stepshouldbelow,stepshouldbelow*2,eighteen[stepshouldbelow]
    
    randomstrings=randomcube()
    l=len(randomstrings[0])//2
    print("random with",l,"moves\n")
    print("{:<8}{:<18}{:<6}{:<24}{:<14}{:<6}{:<36}".format("thread","htm","qtm","in dict1/total","time/s","type","solution"))
    solutions=[eighteen[stepshouldbelow]]*n
    t=0
    for base in range(n):
        htm,qtm,minmove,solutionnum,t1=solve(*getcubewithbase(randomstrings[base//3],base%3,l),base,htm,qtm,minmove)
        solutions[base]=minmove
        verifiednum.append(solutionnum)
        t+=t1
    times.append(t)
    print("\nfinish solve cube",i+1)
    print("completed phase one number",verifiednum[-n:],sum(verifiednum[-n:]))
    
    if htm>=stepshouldbelow:
        miss+=1
        print("no solution below",htm,"steps for this cube")
        print("miss rate",miss,"/",i+1)
    else:
        print("{:<8}{:<8}{}".format("thread","htm","solution"))
        for j in range(n):
            print("{:<8}{:<8}{:<36}{}".format(j,int(log(solutions[j],18)),solutions[j],decodevalue(solutions[j])))
        htms.append(htm)
        qtms.append(qtm)
        print("\nmin htm",htm,", qtm",qtm,"solution",minmove,decodevalue(minmove),rotatenumbertostring(decodevalue(minmove)))
        if i<100:
            print("current htm results:",htms)
        print("average htm",sum(htms)/len(htms),"\naverage qtm",sum(qtms)/len(qtms))
    print("time:",t,"s ","average time",sum(times)/(i+1),time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print("estimated time for rest",cubenumber-i-1,"cubes:",(time.time()-starttime)*(cubenumber-i-1)/(i+1),"s")
endtime=time.time()

print("\n\ntwo phase algorithm version 20")
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("initialize time",tinit,"s")
print(f"dicts time {tdict2-tdict0}s = {tdict1-tdict0}s + {tdict2-tdict1}s")
print(f"total time {endtime-starttime}s, actual time {sum(times)}s, average time {sum(times)/cubenumber}s")
print("average phase 1 completed number per thread",sum(verifiednum)/len(verifiednum),"max",max(verifiednum),"min",min(verifiednum))
print("search depth",phase1maxstep,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
if cubenumber<=100:
    print("htm",htms,"\nqtm",qtms)
print(cubenumber,"cubes")
if len(htms)>0:
    print("\nhtm average",sum(htms)/len(htms),"range",min(htms),"-",max(htms),"\nhtm     number")
    for i in range(min(htms),max(htms)+1):
        print("{:<8}{:<8}{}".format(i,htms.count(i),"-"*int(100*htms.count(i)/cubenumber)))
    print("\nqtm average",sum(qtms)/len(qtms),"range",min(qtms),"-",max(qtms),"\nqtm     number")
    for i in range(min(qtms),max(qtms)+1):
        print("{:<8}{:<8}{}".format(i,qtms.count(i),"-"*int(100*qtms.count(i)/cubenumber)))
if miss!=0:
    print("miss rate",miss,"/",cubenumber)
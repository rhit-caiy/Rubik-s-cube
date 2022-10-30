import random,time,sys,threading
from math import log
cc=[0,1,2,3,4,5,6,7]
ccd=[0,0,0,0,5,5,5,5]
ce=[0,1,2,3,4,5,6,7,8,9,10,11]
ced=[0,0,0,0,1,1,3,3,5,5,5,5]
cmed=[1,1,3,3]

facecorner=[[0,2,3,1],[0,6,4,2],[2,4,5,3],[3,5,7,1],[1,7,6,0],[4,6,7,5]]
faceedge=[[0,1,2,3],[1,4,9,5],[2,5,10,6],[3,6,11,7],[0,7,8,4],[10,9,8,11]]
adj=[[4,3,2,1],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[1,2,3,4]]
antithesis=[5,3,4,1,2,0]
positionsimplify=[0,1,2,1,2,0]
eighteen=[18**i for i in range(30)]
t=time.time()

def getdict1(dict1step):
    global dict1
    predictstate=[(cc,ccd,ce,ced,1,-1,-1)]
    newpredictstate=[]
    key=(cpsimplify[str([positionsimplify[ccd[cc[i]]] for i in range(7)])]*177147+epsimplify[str([positionsimplify[ced[ce[i]]] for i in range(11)])])*495+mepsimplify[str(sorted([ce.index(i) for i in range(4,8)]))]
    dict1[key]=0
    t0=time.time()
    for step in range(1,dict1step+1):
        t1=time.time()
        for cube in predictstate:
            oc0,ocd0,oe0,oed0,oldstep,f1,f2=cube
            for f in range(6):
                if step==1 or f1!=f and not (step>2 and f==f2 and (f==0 and f1==5 or 
                                                                   f==5 and f1==0 or 
                                                                   f==1 and f1==3 or 
                                                                   f==3 and f1==1 or 
                                                                   f==2 and f1==4 or 
                                                                   f==4 and f1==2)):
                    re=faceedge[f]
                    rc=facecorner[f]
                    adjf=adj[f]
                    newstep=oldstep*18+3*f+2
                    oc,ocd,oe,oed=oc0,ocd0,oe0,oed0
                    for t in range(1,4):
                        ne=oe.copy()
                        ned=oed.copy()
                        nc=oc.copy()
                        ncd=ocd.copy()
                        for n in range(4):
                            ne[re[n]]=oe[re[n-3]]
                            nc[rc[n]]=oc[rc[n-3]]
                            en=oe[re[n]]
                            if oed[en]!=f:
                                ned[en]=adjf[adjf.index(oed[en])-3]
                            cn=oc[rc[n]]
                            if ocd[cn]!=f:
                                ncd[cn]=adjf[adjf.index(ocd[cn])-3]
                        oc,ocd,oe,oed=nc,ncd,ne,ned
                        key=(cpsimplify[str([positionsimplify[ncd[nc[i]]] for i in range(7)])]*177147+epsimplify[str([positionsimplify[ned[ne[i]]] for i in range(11)])])*495+mepsimplify[str(sorted([ne.index(i) for i in range(4,8)]))]
                        if key not in dict1:
                            dict1[key]=newstep
                            if step!=dict1step:
                                newpredictstate.append((nc,ncd,ne,ned,newstep,f,f1))
                        newstep-=1
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,step,len(newpredictstate),len(dict1),time.time()-t1),end="")
        predictstate=newpredictstate
        newpredictstate=[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,"total",len(newpredictstate),len(dict1),time.time()-t0),end="")

#corner, edge position simplify
cpsimplify={}
epsimplify={}
cnum=0
enum=0
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                for m in range(3):
                    for n in range(3):
                        for o in range(3):
                            cpsimplify[str([i,j,k,l,m,n,o])]=cnum
                            cnum+=1
                            for p in range(3):
                                for q in range(3):
                                    for r in range(3):
                                        for s in range(3):
                                            epsimplify[str([i,j,k,l,m,n,o,p,q,r,s])]=enum
                                            enum+=1
print("length of cpsimplify",len(cpsimplify))
print("length of epsimplify",len(epsimplify))

#middle edge position
mepsimplify={}
num=0
for i in range(12):
    for j in range(i+1,12):
        for k in range(j+1,12):
            for l in range(k+1,12):
                mepsimplify[str([i,j,k,l])]=num
                num+=1
print("length of mepsimplify",len(mepsimplify))

phase2rotations=[0,1,2,4,7,10,13,15,16,17]
def getdict2(dict2step):
    global dict2
    predictstate=[(cc,ce,cmed,0,-1,-1)]
    newpredictstate=[]
    key=((cornersimplify[str(cc)]*40320+udesimplify[str(ce[0:4]+ce[8:12])])*24+mesimplify[str(ce[4:8])])*6+medsimplify[str(cmed)]
    dict2[key]=1
    t0=time.time()
    for step in range(1,dict2step+1):
        t1=time.time()
        for cube in predictstate:
            oc,oe,omed,oldstep,f1,f2=cube
            for r in phase2rotations:
                f=r//3
                t=r%3+1
                if step==1 or f1!=f and not (step>2 and f==f2 and (f==0 and f1==5 or 
                                                                   f==5 and f1==0 or 
                                                                   f==1 and f1==3 or 
                                                                   f==3 and f1==1 or 
                                                                   f==2 and f1==4 or 
                                                                   f==4 and f1==2)):
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
                                nmed[en]=antithesis[omed[en]]
                    key=((cornersimplify[str(nc)]*40320+udesimplify[str(ne[0:4]+ne[8:12])])*24+mesimplify[str(ne[4:8])])*6+medsimplify[str(nmed)]
                    if key not in dict2:
                        newstep=oldstep+(3*f+3-t)*eighteen[step-1]
                        dict2[key]=newstep+eighteen[step]
                        if step!=dict2step:
                            newpredictstate.append((nc,ne,nmed,newstep,f,f1))
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,step,len(newpredictstate),len(dict2),time.time()-t1),end="")
        predictstate=newpredictstate
        newpredictstate=[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,"total",len(newpredictstate),len(dict2),time.time()-t0),end="")
    
    
#corner
cornersimplify={}
num=0
for i in range(8):
    for j in range(8):
        for k in range(8):
            for l in range(8):
                for m in range(8):
                    for n in range(8):
                        for o in range(8):
                            for p in range(8):
                                if sorted([i,j,k,l,m,n,o,p])==[0,1,2,3,4,5,6,7]:
                                    cornersimplify[str([i,j,k,l,m,n,o,p])]=num
                                    num+=1
print("length of cornersimplify",len(cornersimplify))

#up down edge
udesimplify={}
ude=[0,1,2,3,8,9,10,11]
num=0
for i in ude:
    for j in ude:
        for k in ude:
            for l in ude:
                for m in ude:
                    for n in ude:
                        for o in ude:
                            for p in ude:
                                if sorted([i,j,k,l,m,n,o,p])==ude:
                                    udesimplify[str([i,j,k,l,m,n,o,p])]=num
                                    num+=1
print("length of udesimplify",len(cornersimplify))

#middle edge position
mesimplify={}
num=0
for i in range(4,8):
    for j in range(4,8):
        for k in range(4,8):
            for l in range(4,8):
                if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                    mesimplify[str([i,j,k,l])]=num
                    num+=1
print("length of mesimplify",len(mesimplify))

#middle edge direction
medsimplify={'[1, 1, 3, 3]':0,'[1, 3, 1, 3]':1,'[1, 3, 3, 1]':2,'[3, 1, 1, 3]':3,'[3, 1, 3, 1]':4,'[3, 3, 1, 1]':5}
print("length of medsimplify",len(medsimplify))

print(time.time()-t,"s")

def solve(c,cd,e,ed,threadid):
    global threadsolutions,minstep,minmove,verifiednum
    tstart=time.time()
    cubes=[(c,cd,e,ed,1,0,-1,-1)]#initial move representation,step number,previous face,previous face 2 steps ago
    solutionnum=0
    totalnum=1
    minstr=eighteen[stepshouldbelow]
    
    while cubes:
        oc0,ocd0,oe0,oed0,previousstep,step,f1,f2=cubes.pop()
        step+=1
        for f in range(6):
            if step==1 or not (f==f1 or (f1==5 and f==0 or f1==4 and f==2 or f1==3 and f==1) or (step>2 and f==f2 and (f==0 and f1==5 or f==1 and f1==3 or f==2 and f1==4))):
                re=faceedge[f]
                rc=facecorner[f]
                adjf=adj[f]
                m1_1=previousstep*18+3*f
                totalnum+=3
                oc,ocd,oe,oed=oc0,ocd0,oe0,oed0
                for t in range(3):
                    # if step>=4 and (m1_1[-1]==m1_1[-3]==m1_1[-5]==m1_1[-7]=="2" and m1_1[-8]+m1_1[-6]+m1_1[-4]+m1_1[-2] in ["0513","1324","2405"]):
                    #     continue
                    ne=oe.copy()
                    ned=oed.copy()
                    nc=oc.copy()
                    ncd=ocd.copy()
                    for n in range(4):
                        ne[re[n]]=oe[re[n-3]]
                        nc[rc[n]]=oc[rc[n-3]]
                        en=oe[re[n]]
                        if oed[en]!=f:
                            ned[en]=adjf[adjf.index(oed[en])-3]
                        cn=oc[rc[n]]
                        if ocd[cn]!=f:
                            ncd[cn]=adjf[adjf.index(ocd[cn])-3]
                    oc,ocd,oe,oed=nc,ncd,ne,ned
                    if step<phase1maxstep:
                        cubes.append((nc,ncd,ne,ned,m1_1,step,f,f1))
                    key=(cpsimplify[str([positionsimplify[ncd[nc[i]]] for i in range(7)])]*177147+epsimplify[str([positionsimplify[ned[ne[i]]] for i in range(11)])])*495+mepsimplify[str(sorted([ne.index(i) for i in range(4,8)]))]
                    if key in dict1:
                        solutionnum+=1
                        m1_2=dict1[key]
                        if m1_2!=1:
                            nc1,ncd1,ne1,ned1=oc1,ocd1,oe1,oed1=nc,ncd,ne,ned
                            m1=m1_1
                            f0=f
                            while m1_2>=18:
                                ft=m1_2%18
                                m1=18*m1+ft
                                m1_2//=18
                                f0=ft//3
                                t0=ft%3+1
                                re1=faceedge[f0]
                                rc1=facecorner[f0]
                                adjf1=adj[f0]
                                ne1=oe1.copy()
                                ned1=oed1.copy()
                                nc1=oc1.copy()
                                ncd1=ocd1.copy()
                                for n in range(4):
                                    ne1[re1[n]]=oe1[re1[n+t0-4]]
                                    nc1[rc1[n]]=oc1[rc1[n+t0-4]]
                                    en=oe1[re1[n]]
                                    if oed1[en]!=f0:
                                        ned1[en]=adjf1[adjf1.index(oed1[en])+t0-4]
                                    cn=oc1[rc1[n]]
                                    if ocd1[cn]!=f0:
                                        ncd1[cn]=adjf1[adjf1.index(ocd1[cn])+t0-4]
                                oc1,ocd1,oe1,oed1=nc1,ncd1,ne1,ned1
                            
                            key=((cornersimplify[str(nc1)]*40320+udesimplify[str(ne1[0:4]+ne1[8:12])])*24+mesimplify[str(ne1[4:8])])*6+medsimplify[str(ned1[4:8])]
                            if key in dict2:
                                m2=dict2[key]
                                solution=(m1-1)*eighteen[int(log(m2,18))]+m2
                                if solution<minmove:
                                    minmove=minstr=solution
                                    minstep=int(log(solution,18))
                                    p1=int(log(m1,18))
                                    p1_1=int(log(m1_1,18))
                                    print("{:<8}{:<24}{:<20}{:<16f}1     {} {}\n".format(threadid,f"{minstep} = {p1_1} + {p1-p1_1} + {minstep-p1}",str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution,decodevalue(solution)),end="")
                                    
                                if int(log(solution,18))<=minstep:
                                    re1=faceedge[f0]
                                    rc1=facecorner[f0]
                                    adjf1=adj[f0]
                                    ne1=oe1.copy()
                                    ned1=oed1.copy()
                                    nc1=oc1.copy()
                                    ncd1=ocd1.copy()
                                    for n in range(4):
                                        ne1[re1[n]]=oe1[re1[n-2]]
                                        nc1[rc1[n]]=oc1[rc1[n-2]]
                                        en=oe1[re1[n]]
                                        if oed1[en]!=f0:
                                            ned1[en]=adjf1[adjf1.index(oed1[en])-2]
                                        cn=oc1[rc1[n]]
                                        if ocd1[cn]!=f0:
                                            ncd1[cn]=adjf1[adjf1.index(ocd1[cn])-2]
                                            
                                    key=((cornersimplify[str(nc1)]*40320+udesimplify[str(ne1[0:4]+ne1[8:12])])*24+mesimplify[str(ne1[4:8])])*6+medsimplify[str(ned1[4:8])]
                                    if key in dict2:
                                        m2=dict2[key]
                                        solution=(m1-3)*eighteen[int(log(m2,18))]+m2
                                        if solution<minmove:
                                            minmove=minstr=solution
                                            minstep=int(log(solution,18))
                                            p1=int(log(m1,18))
                                            p1_1=int(log(m1_1,18))
                                            print("{:<8}{:<24}{:<20}{:<16f}2     {} {}\n".format(threadid,f"{minstep} = {p1_1} + {p1-p1_1} + {minstep-p1}",str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution,decodevalue(solution)),end="")
                    m1_1+=1
    threadsolutions[threadid]=minstr
    verifiednum.append(solutionnum)
    print("finish thread {}    thread min {}    {}/{}    time {:f}s\n".format(threadid,int(log(minstr,18)),solutionnum,totalnum,time.time()-tstart),end="")

def randomcube():
    a=random.randrange(512,1024)
    randomstring=""
    for i in range(a):
        r=str(random.randrange(0,6))+str(random.randrange(1,4))
        randomstring+=r
    return randomstring

changebasetable=[[1,5,2,0,4,3],[2,1,5,3,0,4],[0,1,2,3,4,5]]
def getcubewithbase(randomstring,base):
    l=int(len(randomstring)/2)
    cubepack=(cc,ccd,ce,ced)
    #s=""
    for i in range(l):
        f=changebasetable[base][int(randomstring[2*i])]
        t=int(randomstring[2*i+1])
        cubepack=rotatecube(f,t,*cubepack)
        #s+=str(f)+str(t)
    return cubepack
    
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
    return nc,ncd,ne,ned

def decodevalue(n):
    s=""
    while n>=18:
        ft=n%18
        n//=18
        s=str(ft//3)+str(ft%3+1)+s
    return s
    
allrotation=["U","U2","U'","L","L2","L'","F","F2","F'","R","R2","R'","B","B2","B'","D","D2","D'"]
def rotatenumbertostring(s):
    r=""
    for i in range(int(len(s)/2)):
        r+=allrotation[3*int(s[2*i])+int(s[2*i+1])-1]
    return r

def rotatestringtonumber(s):
    r=""
    for c in s:
        if c=="2":
            r=r[:-1]+"2"
        elif c=="'" or c=="3":
            r=r[:-1]+"3"
        elif c in allrotation:
            i=allrotation.index(c)
            r+=str(i//3)+"1"
    return r

def reverserotation(s):
    r=""
    for i in range(int(len(s)/2)):
        r=s[2*i]+str(4-int(s[2*i+1]))+r
    return r

def printdictsize(d):
    a=sys.getsizeof(d)
    b=0
    for i in d.keys():
        b+=sys.getsizeof(i)
    for i in d.values():
        b+=sys.getsizeof(i)
    print("dict",a,"B    values and keys",b,"B    total",(a+b)/1000000000,"GB    ",(a+b)/1000000,"MB")

dict1={}
dict2={}
dict1step=8#8
dict2step=9#9
dict1thread=threading.Thread(target=getdict1,args=(dict1step,))
dict2thread=threading.Thread(target=getdict2,args=(dict2step,))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("{:<8}{:<8}{:<16}{:<16}{:<16}\n".format("dict","step","cubes left","dict length","time/s"),end="")
tdictstart=time.time()
dict1thread.start()
dict2thread.start()
dict2thread.join()
dict1thread.join()
tdictend=time.time()
print("time",tdictend-tdictstart,"s")

print("dict1 size",len(dict1))
printdictsize(dict1)
print("dict2 size",len(dict2))
printdictsize(dict2)

htm=[]
qtm=[]
verifiednum=[]
starttime=time.time()
phase1maxstep=5#6
stepshouldbelow=phase1maxstep+dict1step+dict2step+1
miss=0
threadn=6

cubenumber=100
for i in range(cubenumber):
    t1=time.time()
    print("\n\ncube",i+1)
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    minstep=stepshouldbelow
    minmove=eighteen[stepshouldbelow]
    
    randomstring=randomcube()
    # randomstring=rotatestringtonumber("R L U2 F U' D F2 R2 B2 L U2 F' B' U R2 D F2 U R2 U")
    # randomstring=rotatestringtonumber(strings[i])
    # print("random string",randomstring)
    
    print("random with",int(len(randomstring)/2),"move")
    print("search depth",phase1maxstep,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
    
    unsolvedcubes=[]
    for base in range(3):
        unsolvedcubes.append(getcubewithbase(randomstring,base))
    reverserandomstring=reverserotation(randomstring)
    for base in range(3):
        unsolvedcubes.append(getcubewithbase(randomstring,base))
    threadsolutions=[0]*threadn
    
    #solve(*unsolvedcubes[0],0)
    
    cubethread0=threading.Thread(target=solve,args=(*unsolvedcubes[0],0))
    cubethread1=threading.Thread(target=solve,args=(*unsolvedcubes[1],1))
    cubethread2=threading.Thread(target=solve,args=(*unsolvedcubes[2],2))
    cubethread3=threading.Thread(target=solve,args=(*unsolvedcubes[3],3))
    cubethread4=threading.Thread(target=solve,args=(*unsolvedcubes[4],4))
    cubethread5=threading.Thread(target=solve,args=(*unsolvedcubes[5],5))
    threads=[cubethread0,cubethread1,cubethread2,cubethread3,cubethread4,cubethread5]
    print("start",threadn,"threads")
    print("{:<8}{:<24}{:<20}{:<16}{:<6}{:<40}".format("thread","solution formation","in dict1/total","time/s","type","solution"))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    print("\nfinish all threads of cube",i+1)
    print("completed phase one number",verifiednum[-threadn:])
    
    if minstep>=stepshouldbelow:
        miss+=1
        print("no solution below",minstep,"steps for this cube")
        print("miss rate",miss,"/",i+1)
        #print(randomstring)
    else:
        bestthread=0
        print("{:<8}{:<8}{}".format("thread","min","solution"))
        for j in range(threadn):
            print("{:<8}{:<8}{}    {}".format(j,int(log(threadsolutions[j],18)),threadsolutions[j],decodevalue(threadsolutions[j])))
            if minmove==threadsolutions[j]:
                bestthread=j
            elif minmove>threadsolutions[j]:
                minmove=threadsolutions[j]
                minstep=int(log(threadsolutions[j],18))
                bestthread=j
        
        bestrotation=decodevalue(minmove)
        
        htm.append(minstep)
        qtmvalue=minstep
        for j in range(minstep):
            if bestrotation[2*j+1]=="2":
                qtmvalue+=1
        qtm.append(qtmvalue)
        print("\nbest solution in thread",bestthread)
        print("min htm",minstep,", qtm",qtmvalue,"solution",minmove,bestrotation,rotatenumbertostring(bestrotation))
        print("current htm results:",htm)
        print("average htm",sum(htm)/len(htm))
        print("average qtm",sum(qtm)/len(qtm))
    t2=time.time()
    print("time:",t2-t1,"s ","average time",(t2-starttime)/(i+1),time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print("estimated time for rest",cubenumber-i-1,"cubes :",(t2-starttime)*(cubenumber-i-1)/(i+1),"s")
endtime=time.time()

print("\n\ntwo phase algorithm 10")
print("average phase 1 completed number",sum(verifiednum)/len(verifiednum),"max",max(verifiednum),"min",min(verifiednum))
print("search depth",phase1maxstep,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("dict time",tdictend-tdictstart,"s")
print("total time",endtime-starttime,"s, average time",(endtime-starttime)/cubenumber,"s")
print("htm",htm)
print("qtm",qtm)
print("htm average",sum(htm)/len(htm),"range",min(htm),"-",max(htm))
print("qtm average",sum(qtm)/len(qtm),"range",min(qtm),"-",max(qtm))
print("\nmove  number")
for i in range(min(htm),max(htm)+1):
    print(i,"  ",htm.count(i))
if miss!=0:
    print("there are",miss,"of",cubenumber,"cubes has no solution under this search depth")

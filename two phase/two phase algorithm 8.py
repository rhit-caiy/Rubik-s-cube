import random,time,threading,sys
corner=[i for i in range(8)]
cornerd=[0,0,0,0,5,5,5,5]
edge=[i for i in range(12)]
edged=[0,0,0,0,1,1,3,3,5,5,5,5]
cc=corner.copy()
ccd=cornerd.copy()
ce=edge.copy()
ced=edged.copy()
cmed=[1,1,3,3]

facecorner=[[0,2,3,1],[0,6,4,2],[2,4,5,3],[3,5,7,1],[1,7,6,0],[4,6,7,5]]
faceedge=[[0,1,2,3],[1,4,9,5],[2,5,10,6],[3,6,11,7],[0,7,8,4],[10,9,8,11]]
adj=[[4,3,2,1],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[1,2,3,4]]

phase2rotations=["01","02","03","12","22","32","42","51","52","53"]
antithesis=[5,3,4,1,2,0]

t=time.time()

def getdict1(dict1step):
    global dict1
    predictstate=[(cc,ccd,ce,ced,0)]
    newpredictstate=[]
    key=getkey1(cc,ccd,ce,ced)
    dict1[key]=0
    t0=time.time()
    for step in range(1,dict1step+1):
        t1=time.time()
        for cube in predictstate:
            oc,ocd,oe,oed,oldstep=cube
            for f in range(6):
                f1=oldstep%18//3
                f2=oldstep//18%18//3
                if step>2 and (f==f1 or (f==f2 and (f==0 and f1==5 or 
                                                    f==5 and f1==0 or 
                                                    f==1 and f1==3 or 
                                                    f==3 and f1==1 or 
                                                    f==2 and f1==4 or 
                                                    f==4 and f1==2))):
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
                    key=getkey1(nc,ncd,ne,ned)
                    if key not in dict1:
                        if step==1:
                            newstep=f
                        else:
                            newstep=oldstep*18+3*f+3-t
                        dict1[key]=newstep
                        if step!=dict1step:
                            newpredictstate.append((nc,ncd,ne,ned,newstep))
        
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

positionsimplify=[0,1,2,1,2,0]
def getkey1(c,cd,e,ed):
    k1=cpsimplify[str([positionsimplify[cd[c[i]]] for i in range(7)])]
    k2=epsimplify[str([positionsimplify[ed[e[i]]] for i in range(11)])]
    k3=mepsimplify[str(sorted([e.index(i) for i in range(4,8)]))]
    return (k1*177147+k2)*495+k3
    
#phase2rotations=["01","02","03","12","22","32","42","51","52","53"]
phase2rotations=[0,1,2,4,7,10,13,15,16,17]
def getdict2(dict2step):
    global dict2
    predictstate=[(cc,ce,cmed,1)]
    newpredictstate=[]
    key=getkey2(cc,ce,cmed)
    dict2[key]=1
    t0=time.time()
    for step in range(1,dict2step+1):
        t1=time.time()
        for cube in predictstate:
            oc,oe,omed,oldstep=cube
            for r in phase2rotations:
                f=r//3
                t=r%3+1
                f1=oldstep%18//3
                f2=oldstep//18%18//3
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
                    key=getkey2(nc,ne,nmed)
                    if key not in dict2:
                        newstep=oldstep*18+3*f+3-t
                        dict2[key]=newstep
                        if step!=dict2step:
                            newpredictstate.append((nc,ne,nmed,newstep))
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

def getkey2(c,e,med):
    k1=cornersimplify[str(c)]
    k2=udesimplify[str(e[0:4]+e[8:12])]
    k3=mesimplify[str(e[4:8])]
    k4=medsimplify[str(med)]
    return ((k1*40320+k2)*24+k3)*6+k4


def decodephase1value(n):
    if n<18:
        return str(n)
    else:
        a=n%18
        return str(a//3)+str(a%3+1)+decodephase1value(n//18)
    
def decodephase2value(n):
    if n==1:
        return ""
    else:
        a=n%18
        return str(a//3)+str(a%3+1)+decodephase2value(n//18)


def phase1(c,cd,e,ed,threadid):
    global threadsolutions,minstep,verifiednum
    tstart=time.time()
    cubes=[[c,cd,e,ed,"",0]]
    solutionnum=0
    totalnum=1
    minstr="x"*2*stepshouldbelow
    
    #check first
    key=getkey1(c,cd,e,ed)
    step=0
    if key in dict1:
        solutionnum+=1
        m1_2=decodephase1value(dict1[key])
        if m1_2=="":
            solution=phase2([c,cd,e,ed],m1_2)
            if solution!=False and steplen(solution)<minstep:
                minstr=solution
                minstep=steplen(solution)
                fourparts=fourpartmove(m1_2,solution)
                print("{:<8}{:<24}{:<20}{:<16f}{}\n".format(threadid,fourparts,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution),end="")
        else:
            phase2cube=[c,cd,e,ed]
            for i in range(int(len(m1_2)/2)):
                phase2cube=rotatecube(int(m1_2[2*i]),int(m1_2[2*i+1]),*phase2cube)
            solution=phase2(rotatecube(int(m1_2[-1]),1,*phase2cube),m1_2+"1")
            if solution!=False and steplen(solution)<minstep:
                minstep=steplen(solution)
                minstr=solution
                fourparts=fourpartmove(m1_2+"1",solution)
                print("{:<8}{:<24}{:<20}{:<16f}{}\n".format(threadid,fourparts,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution),end="")
            solution=phase2(rotatecube(int(m1_2[-1]),3,*phase2cube),m1_2+"3")
            if solution!=False and steplen(solution)<minstep:
                minstep=steplen(solution)
                minstr=solution
                fourparts=fourpartmove(m1_2+"3",solution)
                print("{:<8}{:<24}{:<20}{:<16f}{}\n".format(threadid,fourparts,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution),end="")
                
    while cubes:
        cubepack=cubes.pop()
        previousstep=cubepack[4]
        step=cubepack[5]+1
        for f in range(6):
            if step!=1 and (str(f)==previousstep[-2] or (previousstep[-2]+str(f) in ["50","42","31"]) or (step>2 and str(f)==previousstep[-4] and previousstep[-4]+previousstep[-2] in ["05","13","24"])):
                continue
            for t in range(1,4):
                m1_1=previousstep+str(f)+str(t)
                # if step>=4 and (m1_1[-1]==m1_1[-3]==m1_1[-5]==m1_1[-7]=="2" and m1_1[-8]+m1_1[-6]+m1_1[-4]+m1_1[-2] in ["0513","1324","2405"]):
                #     continue
                totalnum+=1
                newcubepack=rotatecube(f,t,*cubepack[:4])
                nc,ncd,ne,ned=newcubepack
                if step<phase1maxstep:
                    newcubepack+=[m1_1,step]
                    cubes.append(newcubepack)
                else:
                    key=getkey1(*newcubepack)
                    if key in dict1:
                        solutionnum+=1
                        m1_2=decodephase1value(dict1[key])
                        phase2cube=[nc,ncd,ne,ned]
                        if m1_2=="":
                            solution=phase2(phase2cube,m1_1)
                            if solution!=False and steplen(solution)<minstep:
                                minstep=steplen(solution)
                                minstr=solution
                                fourparts=fourpartmove(m1_1,solution)
                                print("{:<8}{:<24}{:<20}{:<16f}{}\n".format(threadid,fourparts,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution),end="")
                        else:
                            m1_2+="1"
                            for i in range(int(len(m1_2)/2)):
                                phase2cube=rotatecube(int(m1_2[2*i]),int(m1_2[2*i+1]),*phase2cube)
                            solution=phase2(phase2cube,m1_1+m1_2)
                            if solution!=False and steplen(solution)<minstep:
                                minstep=steplen(solution)
                                minstr=solution
                                fourparts=fourpartmove(m1_1+m1_2,solution)
                                print("{:<8}{:<24}{:<20}{:<16f}{}\n".format(threadid,fourparts,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution),end="")
                            solution=phase2(rotatecube(int(m1_2[-2]),2,*phase2cube),m1_1+m1_2[:-1]+"3")
                            if solution!=False and steplen(solution)<minstep:
                                minstep=steplen(solution)
                                minstr=solution
                                fourparts=fourpartmove(m1_1+m1_2,solution)
                                print("{:<8}{:<24}{:<20}{:<16f}{}\n".format(threadid,fourparts,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution),end="")
                
    threadsolutions[threadid]=minstr
    verifiednum.append(solutionnum)
    print("finish thread {}    thread min {}    {}/{}    time {:f}s\n".format(threadid,steplen(minstr),solutionnum,totalnum,time.time()-tstart),end="")
    return

def phase2(cubepack,s):
    c,cd,e,ed=cubepack
    phase1len=steplen(s)
    #check first
    if getkey2(c,e,ed[4:8]) in dict2:
        return s+decodephase2value(dict2[getkey2(c,e,ed[4:8])])
    elif phase1len+dict2step+1>=minstep:
        return False
    maxstep=min(minstep-phase1len-dict2step-1,phase2maxstep)
    cubes=[[c,cd,e,ed,s]]
    newcubes=[]
    for step in range(1,maxstep+1):
        if phase1len+step+dict2step>=minstep:
            return False
        for cube in cubes:
            previousstep=cube[4]
            for r in phase2rotations:
                f,t=str(r//3),str(r%3+1)
                if len(previousstep)==0 or f!=previousstep[-2] and not (step>1 and previousstep[-2]+f in ["50","42","31"]) and not (step>2 and f==previousstep[-4] and previousstep[-4]+previousstep[-2] in ["05","13","24"]):
                    newcorner,newcornerd,newedge,newedged=rotatecube(int(f),int(t),*cube[:4])
                    key=getkey2(newcorner,newedge,newedged[4:8])
                    if key in dict2:
                        return previousstep+f+t+decodephase2value(dict2[key])
                    newcubes.append([newcorner,newcornerd,newedge,newedged,previousstep+f+t])
        cubes=newcubes
        newcubes=[]
    return False

def fourpartmove(phase1,whole):
    p1=steplen(phase1)
    p2=steplen(whole)-p1
    p11=0
    p12=0
    p21=0
    p22=p2
    if p1>phase1maxstep:
        p11=phase1maxstep
        p12=p1-p11
    else:
        p12=p1
    if p22>dict1step:
        p21=p22-dict2step
        p22=dict2step
    return f"{steplen(whole)} = {p11} + {p12} + {p21} + {p22}"
    

def steplen(s):
    return int(len(s)/2)

def initialcube():
    return [cc,ccd,ce,ced]

def randomcube():
    a=random.randrange(512,1024)
    randomstring=""
    for i in range(a):
        r=str(random.randrange(0,6))+str(random.randrange(1,4))
        randomstring+=r
    return randomstring

changebasetable=[[1,5,2,0,4,3],[2,1,5,3,0,4],[0,1,2,3,4,5]]
def getcubewithbase(randomstring,base):
    l=steplen(randomstring)
    cubepack=initialcube()
    s=""
    for i in range(l):
        f=changebasetable[base][int(randomstring[2*i])]
        t=int(randomstring[2*i+1])
        cubepack=rotatecube(f,t,*cubepack)
        s+=str(f)+str(t)
    return [cubepack,s]
    
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

allrotation=["U","U2","U'","L","L2","L'","F","F2","F'","R","R2","R'","B","B2","B'","D","D2","D'"]
def rotatenumbertostring(s):
    r=""
    for i in range(steplen(s)):
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
    for i in range(steplen(s)):
        r=s[2*i]+str(4-int(s[2*i+1]))+r
    return r

dict1={}
dict2={}
dict1step=8
dict2step=9
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
def printdictsize(d):
    a=sys.getsizeof(d)
    b=0
    for i in d.keys():
        b+=sys.getsizeof(i)
    for i in d.values():
        b+=sys.getsizeof(i)
    print("dict",a,"B    values and keys",b,"B    total",(a+b)/1000000000,"GB    ",(a+b)/1000000,"MB")

print("dict1 size",len(dict1))
printdictsize(dict1)
print("dict2 size",len(dict2))
printdictsize(dict2)

htm=[]
qtm=[]
verifiednum=[]
starttime=time.time()
phase1maxstep=5#6
phase2maxstep=6#6
stepshouldbelow=phase1maxstep+dict1step+phase2maxstep+dict2step
miss=0
threadn=6
strings=["R L U2 F U' D F2 R2 B2 L U2 F' B' U R2 D F2 U R2 U","F U' F2 D' B U R' F' L D' R' U' L U B' D2 R' F U2 D2"]
# cubenumber=len(strings)
cubenumber=100
for i in range(cubenumber):
    t1=time.time()
    print("\n\ncube",i+1)
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    minstep=stepshouldbelow
    
    randomstring=randomcube()
    
    # randomstring=rotatestringtonumber(strings[i])
    
    #print("random string",randomstring)
    print("random with",steplen(randomstring),"move")
    print("search depth",phase1maxstep,"+",dict1step,"+",phase2maxstep,"+",dict2step,"=",stepshouldbelow)
    
    unsolvedcubes=[]
    #randomstrings=[]
    for base in range(3):
        basereturn=getcubewithbase(randomstring,base)
        unsolvedcubes.append(basereturn[0])
        #randomstrings.append(basereturn[1])
        
    reverserandomstring=reverserotation(randomstring)
    for base in range(3):
        basereturn=getcubewithbase(reverserandomstring,base)
        unsolvedcubes.append(basereturn[0])
        #randomstrings.append(reverserotation(basereturn[1]))
    threadsolutions=["x"*2*stepshouldbelow]*threadn
    
    # phase1(*unsolvedcubes[0],0)
    
    cubethread0=threading.Thread(target=phase1,args=(*unsolvedcubes[0],0))
    cubethread1=threading.Thread(target=phase1,args=(*unsolvedcubes[1],1))
    cubethread2=threading.Thread(target=phase1,args=(*unsolvedcubes[2],2))
    cubethread3=threading.Thread(target=phase1,args=(*unsolvedcubes[3],3))
    cubethread4=threading.Thread(target=phase1,args=(*unsolvedcubes[4],4))
    cubethread5=threading.Thread(target=phase1,args=(*unsolvedcubes[5],5))
    threads=[cubethread0,cubethread1,cubethread2,cubethread3,cubethread4,cubethread5]
    print("start",threadn,"threads")
    print("{:<8}{:<24}{:<20}{:<16}{}".format("thread","solution formation","in dict1/total","time/s","solution"))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    print("\nfinish all threads of cube",i+1)
    print("completed phase one number",verifiednum[-threadn:])
    print(minstep,stepshouldbelow)
    if minstep>=stepshouldbelow:
        miss+=1
        print("no solution below",minstep,"steps for this cube")
        #print(randomstring)
    else:
        # for j in range(3,6):
        #     if threadsolutions[j][0]!="x":
        #         threadsolutions[j]=reverserotation(threadsolutions[j])
        bestthread=0
        print("{:<8}{:<8}{}".format("thread","min","solution"))
        for j in range(threadn):
            print("{:<8}{:<8}{}".format(j,steplen(threadsolutions[j]),threadsolutions[j]))
            if steplen(threadsolutions[j])==minstep:
                bestthread=j
            elif steplen(threadsolutions[j])<minstep:
                minstep=steplen(threadsolutions[j])
                bestthread=j
        htm.append(minstep)
        qtmvalue=minstep
        for j in range(minstep):
            if threadsolutions[bestthread][2*j+1]=="2":
                qtmvalue+=1
        qtm.append(qtmvalue)
        t2=time.time()
        print("\nbest solution in thread",bestthread)
        #print("random string number format",randomstrings[bestthread])
        #print("random string rotate notation",rotatenumbertostring(randomstrings[bestthread]))
        print("min htm",minstep,", qtm",qtmvalue,"solution",threadsolutions[bestthread],rotatenumbertostring(threadsolutions[bestthread]))
        print("current htm results:",htm)
        print("average htm",sum(htm)/len(htm))
        print("average qtm",sum(qtm)/len(qtm))
        print("time:",t2-t1,"s ","average time",(t2-starttime)/(i+1),time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        print("estimated time left for rest",cubenumber-i-1,"cubes :",(t2-starttime)*(cubenumber-i-1)/(i+1),"s")
endtime=time.time()

print("\n\naverage phase 1 completed number",sum(verifiednum)/len(verifiednum),"max",max(verifiednum),"min",min(verifiednum))
print("search depth",phase1maxstep,"+",dict1step,"+",phase2maxstep,"+",dict2step,"=",stepshouldbelow)
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

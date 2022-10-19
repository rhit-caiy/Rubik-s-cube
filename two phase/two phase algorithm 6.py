import random,time
import threading
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

def getdict1(dict1step):
    global dict1
    predictstate=[[cc,ccd,ce,ced,""]]
    newpredictstate=[]
    key=str([ccd[cc[i]] for i in range(7)]+[ced[ce[i]] for i in range(11)]+sorted([ce.index(i) for i in range(4,8)]))
    dict1[key]=""
    t0=time.time()
    for step in range(1,dict1step+1):
        t1=time.time()
        for cube in predictstate:
            oc,ocd,oe,oed,oldstep=cube
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
                    key=str([ncd[nc[i]] for i in range(7)]+[ned[ne[i]] for i in range(11)]+sorted([ne.index(i) for i in range(4,8)]))
                    if key not in dict1:
                        if step==1:
                            newstep=str(f)
                        else:
                            newstep=str(f)+str(4-t)+oldstep
                        dict1[key]=newstep
                        if step!=dict1step:
                            newpredictstate.append([nc,ncd,ne,ned,newstep])
        
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,step,len(newpredictstate),len(dict1),time.time()-t1),end="")
        predictstate=newpredictstate.copy()
        newpredictstate.clear()
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,"total",len(newpredictstate),len(dict1),time.time()-t0),end="")

def getdict2(dict2step):
    global dict2
    predictstate=[[cc,ce,cmed,""]]
    newpredictstate=[]
    dict2[str(cc+ce+cmed)]=""
    t0=time.time()
    for step in range(1,dict2step+1):
        t1=time.time()
        for cube in predictstate:
            oc,oe,omed,oldstep=cube
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
                                nmed[en]=antithesis[omed[en]]
                    key=str(nc+ne+nmed)
                    if key not in dict2:
                        newstep=j[0]+str(4-int(j[1]))+oldstep
                        dict2[key]=newstep
                        if step!=dict2step:
                            newpredictstate.append([nc,ne,nmed,newstep])
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,step,len(newpredictstate),len(dict2),time.time()-t1),end="")
        predictstate=newpredictstate.copy()
        newpredictstate.clear()
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,"total",len(newpredictstate),len(dict1),time.time()-t0),end="")
    


def phase1(c,cd,e,ed,threadid):
    global threadsolutions,minstep,verifiednum
    tstart=time.time()
    cubes=[[c,cd,e,ed,""]]
    newcubes=[]
    solutionnum=0
    minstr="6"*2*stepshouldbelow
    
    #check first
    key=str([cd[c[i]] for i in range(7)]+[ed[e[i]] for i in range(11)]+sorted([e.index(i) for i in range(4,8)]))
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
                        nc,ncd,ne,ned=newcubepack
                        newstep=previousstep+str(f)+str(t)
                        key=str([ncd[nc[i]] for i in range(7)]+[ned[ne[i]] for i in range(11)]+sorted([ne.index(i) for i in range(4,8)]))
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
                            if solutionnum>=phase1solutionlimit:
                                threadsolutions[threadid]=minstr
                                verifiednum.append(solutionnum)
                                return
                        elif step!=phase1maxstep:
                            newcubepack.append(newstep)
                            newcubes.append(newcubepack)
        cubes=newcubes.copy()
        newcubes.clear()
        print("{}-{} cubes in list {} thread min {} time {:f}s\n".format(threadid,step,len(cubes),steplen(minstr),time.time()-tloop),end="")
    threadsolutions[threadid]=minstr
    verifiednum.append(solutionnum)
    print("finish thread {}, thread min {} verified complete phase one number {} time {:f}s\n".format(threadid,steplen(minstr),solutionnum,time.time()-tstart),end="")
    return

def phase2(cubepack,s):
    c,cd,e,ed=cubepack
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
                    newcorner,newcornerd,newedge,newedged=newcubepack
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

def randomcube():
    a=random.randrange(64,128)
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
    #print(rotatenumbertostring(s))
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

allrotation=[["U","U2","U'"],["L","L2","L'"],["F","F2","F'"],["R","R2","R'"],["B","B2","B'"],["D","D2","D'"]]
def rotatenumbertostring(s):
    r=""
    for i in range(steplen(s)):
        r+=allrotation[int(s[2*i])][int(s[2*i+1])-1]
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
print("{:<8}{:<8}{:<16}{:<16}{:<16}\n".format("dict","step","cubes left","dict length","time"),end="")
tdict=time.time()
dict1thread.start()
dict2thread.start()
dict2thread.join()
dict1thread.join()

print("time",time.time()-tdict,"s")
print("finish dicts",len(dict1),len(dict2))

phase1solutionlimit=100000000
cubenumber=100
htm=[]
qtm=[]
verifiednum=[]
starttime=time.time()
phase1maxstep=6#6
phase2maxstep=6#6
stepshouldbelow=phase1maxstep+dict1step+phase2maxstep+dict2step
miss=0
threadn=6
for i in range(cubenumber):
    t1=time.time()
    print("\n\ncube",i+1)
    minstep=stepshouldbelow
    randomstring=randomcube()
    print("random string",randomstring)
    reverserandomstring=reverserotation(randomstring)
    unsolvedcubes=[]
    randomstrings=[]
    for base in range(3):
        basereturn=getcubewithbase(randomstring,base)
        unsolvedcubes.append(basereturn[0])
        randomstrings.append(basereturn[1])
    for base in range(3):
        basereturn=getcubewithbase(reverserandomstring,base)
        unsolvedcubes.append(basereturn[0])
        randomstrings.append(reverserotation(basereturn[1]))
    threadsolutions=["6"*2*stepshouldbelow]*threadn
    
    cubethread0=threading.Thread(target=phase1,args=(*unsolvedcubes[0],0))
    cubethread1=threading.Thread(target=phase1,args=(*unsolvedcubes[1],1))
    cubethread2=threading.Thread(target=phase1,args=(*unsolvedcubes[2],2))
    cubethread3=threading.Thread(target=phase1,args=(*unsolvedcubes[3],3))
    cubethread4=threading.Thread(target=phase1,args=(*unsolvedcubes[4],4))
    cubethread5=threading.Thread(target=phase1,args=(*unsolvedcubes[5],5))
    threads=[cubethread0,cubethread1,cubethread2,cubethread3,cubethread4,cubethread5]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    print("\nfinish all threads of cube",i+1)
    print("completed phase 1 number",verifiednum[-3:])
    if minstep==stepshouldbelow:
        miss+=1
        print("no solution below",minstep,"steps for cube",randomstring)
    else:
        for j in range(3,6):
            if threadsolutions[j][0]!="6":
                threadsolutions[j]=reverserotation(threadsolutions[j])
        bestthread=0
        for j in range(threadn):
            print("thread",j,"length",steplen(threadsolutions[j]),"solution",threadsolutions[j])
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
        print("random string number format",randomstrings[bestthread])
        print("random string rotate notation",rotatenumbertostring(randomstrings[bestthread]))
        print("min htm",minstep,", qtm",qtmvalue,"solution",threadsolutions[bestthread],rotatenumbertostring(threadsolutions[bestthread]))
        print("current htm results:",htm,"average htm",sum(htm)/len(htm),"average qtm",sum(qtm)/len(qtm))
        print("time:",t2-t1,"s ",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        print("estimated time left:",(t2-starttime)*(cubenumber-i-1)/(i+1),"s")
endtime=time.time()
print()
#print("completed phase 1 number",verifiednum)
print("average phase 1 completed number",sum(verifiednum)/len(verifiednum),"max",max(verifiednum),"required max phase 1 solution limit",phase1solutionlimit)
print("search depth",phase1maxstep,"+",dict1step,"+",phase2maxstep,"+",dict2step,"=",stepshouldbelow)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("total time",endtime-starttime,"s, average time",(endtime-starttime)/cubenumber,"s")
print(htm,"htm average",sum(htm)/len(htm),"range",min(htm),"-",max(htm))
print(qtm,"qtm average",sum(qtm)/len(qtm),"range",min(qtm),"-",max(qtm))
if miss!=0:
    print("no solution for",miss,"/",cubenumber)
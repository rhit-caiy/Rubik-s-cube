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
medchange=[0,3,4,1,2]

def getdict1(dict1step):
    global dict1
    predictstate=[[cc,ccd,ce,ced,""]]
    newpredictstate=[]
    key=getkey(cc,ccd,ce,ced)
    dict1[key]=""
    print("phase 1 dict")
    print("{:<8}{:<8}{:<16}{:<16}{:<16}".format("dict","step","cubes left","dict 1 length","time"))
    t0=time.time()
    for step in range(1,dict1step+1):
        t1=time.time()
        for cube in predictstate:
            oc=cube[0]
            ocd=cube[1]
            oe=cube[2]
            oed=cube[3]
            oldstep=cube[4]
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
                    key=getkey(nc,ncd,ne,ned)
                    if key not in dict1:
                        if step==1:
                            newstep=str(f)
                        else:
                            newstep=str(f)+str(4-t)+oldstep
                        dict1[key]=newstep
                        if step!=dict1step:
                            newpredictstate.append([nc,ncd,ne,ned,newstep])
        
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}".format(1,step,len(newpredictstate),len(dict1),time.time()-t1))
        predictstate=newpredictstate.copy()
        newpredictstate.clear()
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}".format(1,"total",len(newpredictstate),len(dict1),time.time()-t0))
positionsimplify=[0,1,2,1,2,0]
def getkey(c,cd,e,ed):
    cpd=[positionsimplify[cd[c[i]]] for i in range(7)]
    epd=[positionsimplify[ed[e[i]]] for i in range(11)]
    cepd=cpd+epd#18 0-2
    k1=0
    t=1
    for i in cepd:
        k1+=i*t
        t*=3
    mep=sorted([e.index(i) for i in range(4,8)])
    k2=str(mep[0])+str(mep[1]-mep[0]-1)+str(mep[2]-mep[1]-1)+str(mep[3]-mep[2]-1)
    key=str(k1)+k2
    return key

def getdict2(dict2step):
    global dict2
    predictstate=[[cc,ce,cmed,""]]
    newpredictstate=[]
    dict2[str(cc+ce+cmed)]=""
    print("phase 2 dict")
    print("{:<8}{:<8}{:<16}{:<16}{:<16}".format("dict","step","cubes left","dict 2 length","time"))
    t0=time.time()
    for step in range(1,dict2step+1):
        t1=time.time()
        for cube in predictstate:
            oc=cube[0]
            oe=cube[1]
            omed=cube[2]
            oldstep=cube[3]
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
                                nmed[en]=medchange[omed[en]]
                    key=str(nc+ne+nmed)
                    if key not in dict2:
                        newstep=j[0]+str(4-int(j[1]))+oldstep
                        dict2[key]=newstep
                        if step!=dict2step:
                            newpredictstate.append([nc,ne,nmed,newstep])
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}".format(2,step,len(newpredictstate),len(dict2),time.time()-t1))
        predictstate=newpredictstate.copy()
        newpredictstate.clear()
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}".format(2,"total",len(newpredictstate),len(dict1),time.time()-t0))
    


def phase1(c,cd,e,ed,threadid):
    global facesolutions,minstep,verifiednum
    cubes=[[c,cd,e,ed,""]]
    newcubes=[]
    solutionnum=0
    minstr="6"*2*minstep
    
    #check first
    key=getkey(c,cd,e,ed)
    if key in dict1:
        solutionnum+=1
        furtherstep=dict1[key]
        if furtherstep=="":
            solution=phase2([c,cd,e,ed],"")
            if solution and steplen(solution)<minstep:
                minstr=solution
                minstep=steplen(solution)
                print(threadid,minstep,solution)
        else:
            phase2cube=[c,cd,e,ed]
            for i in range(int(len(furtherstep)/2)):
                phase2cube=rotatecube(int(furtherstep[2*i]),int(furtherstep[2*i+1]),*phase2cube)
            solution=phase2(rotatecube(int(furtherstep[-1]),1,*phase2cube),furtherstep+"1")
            if solution and steplen(solution)<minstep:
                minstep=steplen(solution)
                minstr=solution
                print(threadid,minstep,solution)
            solution=phase2(rotatecube(int(furtherstep[-1]),3,*phase2cube),furtherstep+"3")
            if solution and steplen(solution)<minstep:
                minstep=steplen(solution)
                minstr=solution
                print(threadid,minstep,solution)
            
    for step in range(1,phase1maxstep+1):
        for cubepack in cubes:
            previousstep=cubepack[4]
            for f in range(6):
                if step==1 or str(f)!=previousstep[-2] and not (step>2 and str(f)==previousstep[-4] and previousstep[-4]+previousstep[-2] in ["05","50","13","31","24","42"]):
                    for t in range(1,4):
                        newcubepack=rotatecube(f,t,*cubepack[:4])
                        nc=newcubepack[0]
                        ncd=newcubepack[1]
                        ne=newcubepack[2]
                        ned=newcubepack[3]
                        newstep=previousstep+str(f)+str(t)
                        key=getkey(nc,ncd,ne,ned)
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
                                print(threadid,minstep,step,"/",phase1maxstep,"verified complete number",solutionnum,solution)
                            solution=phase2(rotatecube(int(furtherstep[-1]),2,*phase2cube),newstep+furtherstep[:-1]+"3")
                            if solution and steplen(solution)<minstep:
                                minstep=steplen(solution)
                                minstr=solution
                                print(threadid,minstep,step,"/",phase1maxstep,"verified complete number",solutionnum,solution)
                            if solutionnum>=phase1solutionlimit:
                                facesolutions[threadid]=minstr
                                verifiednum.append(solutionnum)
                                return
                        elif step!=phase1maxstep:
                            newcubepack.append(newstep)
                            newcubes.append(newcubepack)
        cubes=newcubes.copy()
        newcubes.clear()
        print("thread",threadid,"step",step,"size",len(cubes))
    facesolutions[threadid]=minstr
    verifiednum.append(solutionnum)
    return

def phase2(cubepack,s):
    c=cubepack[0]
    cd=cubepack[1]
    e=cubepack[2]
    ed=cubepack[3]
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
                    newcorner=newcubepack[0]
                    newcornerd=newcubepack[1]
                    newedge=newcubepack[2]
                    newedged=newcubepack[3]
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
    for i in range(l):
        f=changebasetable[base][int(randomstring[2*i])]
        t=int(randomstring[2*i+1])
        cubepack=rotatecube(f,t,*cubepack)
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
    return [nc,ncd,ne,ned]

dict1={}
dict2={}
dict1step=8
dict2step=9
dict1thread=threading.Thread(target=getdict1,args=(dict1step,))
dict2thread=threading.Thread(target=getdict2,args=(dict2step,))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
tdict=time.time()
dict1thread.start()
dict2thread.start()
dict2thread.join()
dict1thread.join()

print("time",time.time()-tdict,"s")
print("finish dicts",len(dict1),len(dict2))

phase1solutionlimit=1000000
cubenumber=100
allcubestep=[]
verifiednum=[]
starttime=time.time()
phase1maxstep=6#6
phase2maxstep=6#6 or even lower
stepshouldbelow=phase1maxstep+dict1step+phase2maxstep+dict2step
for i in range(cubenumber):
    t1=time.time()
    print("\ncube",i+1)
    minstep=stepshouldbelow
    randomstring=randomcube()
    print("random string",randomstring)
    unsolvedcubes=[]
    for base in range(3):
        unsolvedcubes.append(getcubewithbase(randomstring,base))
    facesolutions=["6"*2*stepshouldbelow]*3
    
    cubethread0=threading.Thread(target=phase1,args=(*unsolvedcubes[0],0))
    cubethread1=threading.Thread(target=phase1,args=(*unsolvedcubes[1],1))
    cubethread2=threading.Thread(target=phase1,args=(*unsolvedcubes[2],2))
    threads=[cubethread0,cubethread1,cubethread2]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    print("finish all threads of cube",i+1)
    print("each thread verified number",verifiednum[-3:])
    minstr=""
    for j in range(3):
        print("thread",j,"length",steplen(facesolutions[j]),"solution",facesolutions[j])
        if steplen(facesolutions[j])==minstep:
            minstr=facesolutions[j]
    allcubestep.append(minstep)
    print("min step length",minstep,"solution",minstr)
    t2=time.time()
    print("current results:",allcubestep,"average",sum(allcubestep)/len(allcubestep))
    print("time:",t2-t1,"s",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print("estimated time left:",(t2-starttime)*(cubenumber-i-1)/(i+1),"s")
endtime=time.time()
print()
print("verified number",verifiednum)
print("average verified number",sum(verifiednum)/len(verifiednum),"required max phase 1 solution limit",phase1solutionlimit)
print("search depth",phase1maxstep,"+",dict1step,"+",phase2maxstep,"+",dict2step,"    step should below",stepshouldbelow)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),"total time",endtime-starttime,"s, average time",(endtime-starttime)/cubenumber,"s")
print(allcubestep,"average",sum(allcubestep)/len(allcubestep),"range",min(allcubestep),"-",max(allcubestep))

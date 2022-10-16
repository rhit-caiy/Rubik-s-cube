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
    key=str([cornerd[corner[i]] for i in range(7)]+[edged[edge[i]] for i in range(11)]+sorted([edge[i] for i in range(4,8)]))
    dict1[key]=""
    print("phase 1 dict")
    print("{:<8}{:<8}{:<16}{:<16}{:<16}".format("dict","step","cubes left","dict 1 length","time"))
    t0=time.time()
    cube=rotatecube(1,1,cc,ccd,ce,ced)
    predictstate=[cube+["1"]]
    nc=cube[0]
    ncd=cube[1]
    ne=cube[2]
    ned=cube[3]
    key=str([ncd[nc[i]] for i in range(7)]+[ned[ne[i]] for i in range(11)]+sorted([ne.index(i) for i in range(4,8)]))
    dict1[key]="1"
    newpredictstate=[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}".format(1,1,len(predictstate),len(dict1),0))
    for step in range(2,dict1step+1):
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
                    key=str([ncd[nc[i]] for i in range(7)]+[ned[ne[i]] for i in range(11)]+sorted([ne.index(i) for i in range(4,8)]))
                    if key not in dict1:
                        newstep=str(f)+str(4-t)+oldstep
                        dict1[key]=newstep
                        if step!=dict1step:
                            newpredictstate.append([nc,ncd,ne,ned,newstep])
        
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}".format(1,step,len(newpredictstate),len(dict1),time.time()-t1))
        predictstate=newpredictstate.copy()
        newpredictstate.clear()
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}".format(1,"total",len(newpredictstate),len(dict1),time.time()-t0))
    
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
    keys=getkeys(c,cd,e,ed)
    for i in range(4):
        if keys[i] in dict1:
            solutionnum+=1
            furtherstep=getstringwithdirection(dict1[keys[i]],i)
            print(threadid,i,dict1[keys[i]],furtherstep)
            if furtherstep=="":
                #phase 2
                solution=phase2([c,cd,e,ed],"")
                if solution and steplen(solution)<minstep:
                    minstr=solution
                    minstep=steplen(solution)
                    print(threadid,minstep)
            else:
                solution1=phase2([c,cd,e,ed],furtherstep+"1")
                solution2=phase2([c,cd,e,ed],furtherstep+"3")
                if len(solution1)<=len(solution2) and solution1 and steplen(solution1)<minstep:
                    minstr=solution1
                    minstep=steplen(solution1)
                    print(threadid,minstep)
                elif solution2 and steplen(solution2)<minstep:
                    minstr=solution2
                    minstep=steplen(solution2)
                    print(threadid,minstep)
    
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
                        keys=getkeys(nc,ncd,ne,ned)
                        isin=False
                        for i in range(4):
                            if keys[i] in dict1:
                                isin=True
                                solutionnum+=1
                                furtherstep=getstringwithdirection(dict1[keys[i]],i)
                                phase2cube=newcubepack
                                for i in range(int(len(furtherstep[:-1])/2)):
                                    phase2cube=rotatecube(int(furtherstep[2*i]),int(furtherstep[2*i+1]),*phase2cube)
                                solution1=phase2(rotatecube(int(furtherstep[-1]),1,*phase2cube),newstep+furtherstep+"1")
                                if solution1 and steplen(solution1)<minstep:
                                    minstep=steplen(solution1)
                                    minstr=solution1
                                    print(threadid,minstep,step,"/",phase1maxstep,"solution number",solutionnum)
                                solution2=phase2(rotatecube(int(furtherstep[-1]),3,*phase2cube),newstep+furtherstep+"3")
                                if solution2 and steplen(solution2)<minstep:
                                    minstep=steplen(solution2)
                                    minstr=solution2
                                    print(threadid,minstep,step,"/",phase1maxstep,"solution number",solutionnum)
                                if solutionnum>=phase1solutionlimit:
                                    facesolutions[threadid]=minstr
                                    verifiednum.append(solutionnum)
                                    return
                        if not isin and step!=phase1maxstep:
                            newcubepack.append(newstep)
                            newcubes.append(newcubepack)
        cubes=newcubes.copy()
        newcubes.clear()
    facesolutions[threadid]=minstr
    verifiednum.append(solutionnum)
    return

def getkeys(c,cd,e,ed):
    keys=[]
    for j in range(4):
        key=str([cd[c[i]] for i in range(7)]+[ed[e[i]] for i in range(11)]+sorted([e[i] for i in range(4,8)]))
        keys.append(key)
        cube=[c,cd,e,ed]
        cube=rotatecube(0,1,*cube)
        cube=rotatecube(5,3,*cube)
        c=cube[0]
        cd=cube[1]
        e=cube[2]
        ed=cube[3]
        ne=e.copy()
        ned=ed.copy()
        for i in range(4):
            ne[i+4]=e[(i+1)%4+4]
            ned[e[i+4]]=(ed[e[i+4]]+2)%4+1
        e=ne
        ed=ned
    return keys

directionchange=[[0,1,2,3,4,5],[0,2,3,4,1,5],[0,3,4,1,2,5],[0,4,1,2,3,5]]
#input odd digits, usuall last is 1 due to dict1
def getstringwithdirection(string,t):
    l=steplen(string)
    s=""
    d=directionchange[t]
    for i in range(l):
        s+=str(d[int(string[2*i])])+string[2*i+1]
    s+=str(d[int(string[-1])])
    return s

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
    maxstep=min(minstep-steplen(s)-dict2step-1,phase2maxstep)
    cubes=[[c,cd,e,ed,s]]
    newcubes=[]
    for step in range(1,maxstep+1):
        if steplen(s)+step+dict2step>=minstep:
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

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
tdict=time.time()
dict1step=7
dict2step=8
dict1thread=threading.Thread(target=getdict1,args=(dict1step,))#kwargs={"dict1step":dict1step})
dict2thread=threading.Thread(target=getdict2,args=(dict2step,))#kwargs={"dict2step":dict2step})

dict1thread.start()
dict2thread.start()
dict2thread.join()
dict1thread.join()
    
print("finish dicts",len(dict1),len(dict2))
print("time",time.time()-tdict)

phase1solutionlimit=100000000
cubenumber=100
allcubestep=[]
verifiednum=[]
starttime=time.time()
phase1maxstep=4#6
phase2maxstep=4#6 or even lower
stepshouldbelow=25#22
miss=0
missedstring=[]
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
    if minstep==stepshouldbelow:
        miss+=1
        missedstring.append(randomstring)
        print("don't have solution step <",stepshouldbelow)
    else:
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
if miss!=0:
    print("cube that don't have solution below",stepshouldbelow,":",miss,"/",cubenumber)
    print(missedstring)

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

dict1={}
dict2={}

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

def getdict1(dict1step):
    global dict1
    predictstate=[[cc,ccd,ce,ced,""]]
    newpredictstate=[]
    key=str([ccd[cc[i]] for i in range(7)]+[ced[ce[i]] for i in range(11)]+sorted([ce[i] for i in range(4,8)]))
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
                    key=str([ncd[nc[i]] for i in range(7)]+[ned[ne[i]] for i in range(11)]+sorted([ne.index(i) for i in range(4,8)]))
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
                if step==1 or oldstep[0]!=j[0] and not (step>2 and j[0]==oldstep[0] and oldstep[0]+oldstep[2] in ["05","50","13","31","24","42"]):
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
    
tdict=time.time()
dict1step=7
dict2step=9
dict1thread=threading.Thread(target=getdict1,args=(dict1step,))#kwargs={"dict1step":dict1step})
dict2thread=threading.Thread(target=getdict2,args=(dict2step,))#kwargs={"dict2step":dict2step})

dict2thread.start()
dict1thread.start()

dict1thread.join()
dict2thread.join()
    
print("finish dicts",len(dict1),len(dict2))
print("time",time.time()-tdict)


def phase1(c,cd,e,ed,phase1solutionnum,threadid):
    global facesolutions,minstep
    #print("start thread",threadid)
    cubes=[[c,cd,e,ed,""]]
    newcubes=[]
    maxstep=6
    solutionnum=0
    minstr="6"*64
    
    #check first
    key=str([cd[c[i]] for i in range(7)]+[ed[e[i]] for i in range(11)]+sorted([e.index(i) for i in range(4,8)]))
    if key in dict1:
        solutionnum+=1
        furtherstep=dict1[key]
        if furtherstep=="":
            #phase 2
            solution=phase2([c,cd,e,ed],"")
            if solution!="6":
                minstr=solution
                minstep=steplen(solution)
        else:
            solution1=phase2([c,cd,e,ed],furtherstep+"1")
            solution2=phase2([c,cd,e,ed],furtherstep+"3")
            if solution1=="6" and solution2=="6":
                pass
            elif len(solution1)<=len(solution2) and solution1!="6":
                minstr=solution1
                minstep=steplen(solution1)
            elif solution2!="6":
                minstr=solution2
                minstep=steplen(solution2)
        if solutionnum>=phase1solutionnum:
            facesolutions[threadid]=minstr
            #print("finish thread",threadid,"verified phase 1 number",solutionnum,"its min solution len",steplen(minstr),",",minstr)
            return
    
    for step in range(1,maxstep+1):
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
                        key=str([ncd[nc[i]] for i in range(7)]+[ned[ne[i]] for i in range(11)]+sorted([ne.index(i) for i in range(4,8)]))
                        if key in dict1:
                            furtherstep=dict1[key]
                            phase2cube=newcubepack
                            for i in range(int(len(furtherstep[:-1])/2)):
                                phase2cube=rotatecube(int(furtherstep[2*i]),int(furtherstep[2*i+1]),*phase2cube)
                            #print(threadid)
                            solution1=phase2(rotatecube(int(furtherstep[-1]),1,*phase2cube),newstep+furtherstep+"1")
                            if solution1!="6" and steplen(solution1)<minstep:
                                minstep=steplen(solution1)
                                minstr=solution1
                                print(threadid,minstep)
                            solution2=phase2(rotatecube(int(furtherstep[-1]),3,*phase2cube),newstep+furtherstep+"3")
                            if solution2!="6" and steplen(solution2)<minstep:
                                minstep=steplen(solution2)
                                minstr=solution2
                                print(threadid,minstep)
                            solutionnum+=1
                            if solutionnum>=phase1solutionnum:
                                facesolutions[threadid]=minstr
                                #print("finish thread",threadid,"verified number",solutionnum,"solution",minstr)
                                return
                        elif step!=maxstep:
                            newcubepack.append(newstep)
                            newcubes.append(newcubepack)
        cubes=newcubes.copy()
        newcubes.clear()
    facesolutions[threadid]=minstr
    #print("finish thread",threadid,"verified number",solutionnum,"solution",minstr)
    return

def phase2(cubepack,s):
    c=cubepack[0]
    cd=cubepack[1]
    e=cubepack[2]
    ed=cubepack[3]
    #check first
    if str(c+e+ed[4:8]) in dict2:
        return s+dict2[str(c+e+ed[4:8])]
    elif steplen(s)+dict2step>20:
        return "6"#unable to find in 20 steps
    #if can't find solution within maxstep, directly return
    maxstep=min(minstep-steplen(s)-dict2step-1,7)
    if maxstep<1:
        return "6"
    cubes=[[c,cd,e,ed,s]]
    newcubes=[]
    for step in range(1,maxstep+1):
        if step>minstep-steplen(s)-dict2step-1:
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
                    elif step!=maxstep:
                        newcubes.append([newcorner,newcornerd,newedge,newedged,previousstep+r])
        cubes=newcubes.copy()
        newcubes.clear()
    return "6"

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
    l=int(len(randomstring)/2)
    cubepack=initialcube()
    newrandomstring=""
    for i in range(l):
        f=str(changebasetable[base][int(randomstring[2*i])])
        t=randomstring[2*i+1]
        newrandomstring+=f+t
        cubepack=rotatecube(int(f),int(t),*cubepack)
    return [cubepack,newrandomstring]
    
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

phase1solutionnum=10
cubenumber=1
allcubestep=[]
starttime=time.time()
for i in range(cubenumber):
    t1=time.time()
    print("\ncube",i+1)
    minstep=30
    randomstring=randomcube()
    print("randomstring",randomstring)
    unsolvedcubes=[]
    randomstrings=[]
    for base in range(3):
        getcubewithbasereturn=getcubewithbase(randomstring,base)
        unsolvedcubes.append(getcubewithbasereturn[0])
        randomstrings.append(getcubewithbasereturn[1])
    facesolutions=["","",""]
    cubethread0=threading.Thread(target=phase1,args=(*unsolvedcubes[0],phase1solutionnum,0))
    cubethread1=threading.Thread(target=phase1,args=(*unsolvedcubes[1],phase1solutionnum,1))
    cubethread2=threading.Thread(target=phase1,args=(*unsolvedcubes[2],phase1solutionnum,2))
    threads=[cubethread0,cubethread1,cubethread2]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("finish all threads of cube",i+1)
    print("min step",minstep)
    for j in range(3):
        print("thread",j,"length",steplen(facesolutions[j]),"solution",facesolutions[j])
    allcubestep.append(minstep)
    t2=time.time()
    print("current results:",allcubestep,"average",sum(allcubestep)/len(allcubestep))
    print("time:",t2-t1,"s")
    print("estimated time left:",(t2-starttime)*(cubenumber-i-1)/(i+1),"s")
endtime=time.time()
print("dict depth used",dict1step,"+",dict2step)
print("total time",endtime-starttime,"s, average time",(endtime-starttime)/cubenumber,"s")
print(allcubestep,"average",sum(allcubestep)/cubenumber,"max",max(allcubestep),"min",min(allcubestep))

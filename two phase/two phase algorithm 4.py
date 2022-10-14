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
    key=str([cornerd[corner[i]] for i in range(7)]+[edged[edge[i]] for i in range(11)]+sorted([edge[i] for i in range(4,8)]))
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
    
tdict=time.time()
dict1step=7
dict2step=9
dict1thread=threading.Thread(target=getdict1,args=(dict1step,))#kwargs={"dict1step":dict1step})
dict2thread=threading.Thread(target=getdict2,args=(dict2step,))#kwargs={"dict2step":dict2step})

dict2thread.start()
dict1thread.start()

dict1thread.join()
dict2thread.join()
    
print("finish",len(dict1),len(dict2))
print("time",time.time()-tdict)


def phase1(c,cd,e,ed,phase1solutionnum):
    cubes=[[c,cd,e,ed,""]]
    newcubes=[]
    maxstep=6
    phase1return=[]#
    #check first
    key=str([cornerd[corner[i]] for i in range(7)]+[edged[edge[i]] for i in range(11)]+sorted([edge.index(i) for i in range(4,8)]))
    if key in dict1:
        furtherstep=dict1[key]
        if furtherstep=="":
            #phase 2
            phase1return.append(furtherstep)
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
                            phase1return.append(newstep+furtherstep)
                            #phase 2
                            if len(phase1return)>=phase1solutionnum:
                                return phase1return
                        elif step!=maxstep:
                            newcubepack.append(newstep)
                            newcubes.append(newcubepack)
        cubes=newcubes.copy()
        newcubes.clear()
    return phase1return

def phase2(cubepack,s,stepleft):
    c=cubepack[0]
    cd=cubepack[1]
    e=cubepack[2]
    ed=cubepack[3]
    newcubes=[]
    #if can't find solution within maxstep, directly return
    maxstep=stepleft-dict2step-1
    #check first
    if str(c+e+ed[4:8]) in dict2:
        return s+dict2[str(c+e+ed[4:8])]
    if maxstep<1:
        return "0"*100
    cubes=[[c,cd,e,ed,s]]
    for step in range(1,maxstep+1):
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
    return "0"*100

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
        if n+t-4>3 or n+t-4<-4:
            print(n,t,n+t-4)
        ne[re[n]]=oe[re[n+t-4]]
        nc[rc[n]]=oc[rc[n+t-4]]
        en=oe[re[n]]
        if oed[en]!=f:
            ned[en]=adjf[adjf.index(oed[en])+t-4]
        cn=oc[rc[n]]
        if ocd[cn]!=f:
            ncd[cn]=adjf[adjf.index(ocd[cn])+t-4]
    return [nc,ncd,ne,ned]

phase1solutionnum=100
cubenumber=10
for i in range(cubenumber):
    print("\ncube",i+1)
    randomstring=randomcube()
    unsolvedcubes=[]
    randomstrings=[]
    for base in range(3):
        getcubewithbasereturn=getcubewithbase(randomstring,base)
        unsolvedcubes.append(getcubewithbasereturn[0])
        randomstring.append(getcubewithbasereturn[1])
        print("random string",base,getcubewithbasereturn[1])
    '''
    3 threads
    '''
    
import random,time
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

def rotate(a):
    global edge,edged,corner,cornerd
    #edge
    t=int(a[1])
    f=int(a[0])
    cubepack=rotatecube(f,t,corner,cornerd,edge,edged)
    corner=cubepack[0]
    cornerd=cubepack[1]
    edge=cubepack[2]
    edged=cubepack[3]

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


def randomcube():
    a=random.randrange(64,128)
    randomstring=""
    for i in range(a):
        r=str(random.randrange(0,6))+str(random.randrange(1,4))
        randomstring+=r
    return randomstring
    
def do(s):
    for i in range(int(len(s)/2)):
        rotate(s[2*i:2*i+2])

dict1={}
predictstate=[[cc,ccd,ce,ced,""]]
newpredictstate=[]
#key=cornerpositiondirection+edgepositiondirection+middleedgeposition
key=str([cornerd[corner[i]] for i in range(7)]+[edged[edge[i]] for i in range(11)]+sorted([edge[i] for i in range(4,8)]))
dict1[key]=""
#7: 173.5s, 6: 14.3s
dict1step=7
print("phase 1 dict")
print("{:<8}{:<16}{:<16}{:<16}".format("step","cubes left","dict 1 length","time"))
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
                    newstep=str(f)+str(4-t)+oldstep
                    dict1[key]=newstep
                    if step!=dict1step:
                        newpredictstate.append([nc,ncd,ne,ned,newstep])
    
    print("{:<8}{:<16}{:<16}{:<16f}".format(step,len(newpredictstate),len(dict1),time.time()-t1))
    predictstate=newpredictstate.copy()
    newpredictstate.clear()
print("dict 1 total time",time.time()-t0,"s")


def phase1(corner,cornerd,edge,edged):
    cubes=[[corner,cornerd,edge,edged,""]]
    newcubes=[]
    maxstep=6
    phase1return=[]
    #check first
    key=str([cornerd[corner[i]] for i in range(7)]+[edged[edge[i]] for i in range(11)]+sorted([edge.index(i) for i in range(4,8)]))
    if key in dict1:
        furtherstep=dict1[key]
        phase1return.append(furtherstep)
    for step in range(1,maxstep+1):
        for cubepack in cubes:
            previousstep=cubepack[4]#formed by <face,degree>... string
            for f in range(6):
                if step==1 or str(f)!=previousstep[-2] and not (step>2 and str(f)==previousstep[-4] and previousstep[-4]+previousstep[-2] in ["05","50","13","31","24","42"]):
                    for t in range(1,4):
                        newcubepack=rotatecube(f,t,*cubepack[:4])
                        nc=newcubepack[0]
                        ncd=newcubepack[1]
                        ne=newcubepack[2]
                        ned=newcubepack[3]
                        #use dictionary to mock edge position
                        newstep=previousstep+str(f)+str(t)
                        key=str([ncd[nc[i]] for i in range(7)]+[ned[ne[i]] for i in range(11)]+sorted([ne.index(i) for i in range(4,8)]))
                        if key in dict1:
                            furtherstep=dict1[key]
                            phase1return.append(newstep+furtherstep)
                            if len(phase1return)>=phase1solutionnum:
                                return phase1return
                        elif step!=maxstep:
                            newcubepack.append(newstep)
                            newcubes.append(newcubepack)
        cubes=newcubes.copy()
        newcubes.clear()
    return phase1return


phase2rotations=["01","02","03","12","22","32","42","51","52","53"]
medchange=[0,3,4,1,2]

dict2={}
predictstate=[[cc,ce,cmed,""]]
newpredictstate=[]
dict2[str(cc+ce+cmed)]=""
#9: 192s; 8: 41.8s
dict2step=9
print("phase 2 dict")
print("{:<8}{:<16}{:<16}{:<16}".format("step","cubes left","dict 1 length","time"))
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
                    #rotate top or bottom
                    for k in range(4):
                        ne[fe[k]]=oe[fe[(k+t)-4]]
                        nc[fc[k]]=oc[fc[(k+t)-4]]
                else:
                    #side rotate
                    #corner and edge
                    for k in range(4):
                        ne[fe[k]]=oe[fe[k-2]]
                        nc[fc[k]]=oc[fc[k-2]]
                    #middle edge
                    for e in [fe[1],fe[3]]:
                        en=oe[e]-4
                        if omed[en]!=f:
                            nmed[en]=medchange[omed[en]]#1 to 3, 3 to 1, 2 to 4, 4 to 2
                key=str(nc+ne+nmed)
                if key not in dict2:
                    newstep=j[0]+str(4-int(j[1]))+oldstep
                    dict2[key]=newstep
                    if step!=dict2step:
                        newpredictstate.append([nc,ne,nmed,newstep])
    print("{:<8}{:<16}{:<16}{:<16f}".format(step,len(newpredictstate),len(dict2),time.time()-t1))
    predictstate=newpredictstate.copy()
    newpredictstate.clear()
print("dict2 time",time.time()-t0,"s")

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
            previousstep=cube[4]#formed by <face,degree>... string
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

def initialize():
    global corner,cornerd,edge,edged
    corner=[i for i in range(8)]
    cornerd=[0,0,0,0,5,5,5,5]
    edge=[i for i in range(12)]
    edged=[0,0,0,0,1,1,3,3,5,5,5,5]

changebasetable=[[5,1,4,3,2,0],[3,0,2,5,4,1],[4,1,0,3,5,2],[1,5,2,0,4,3],[2,1,5,3,0,4],[0,1,2,3,4,5]]
def rotatewithbase(randomstring,base):
    l=int(len(randomstring)/2)
    initialize()
    newrandomstring=""
    for i in range(l):
        newrandomstring+=str(changebasetable[base][int(randomstring[2*i])])+randomstring[2*i+1]
    do(newrandomstring)
    
phase1solutionnum=100000
n=100
print("phase 1 max predict step",dict1step)
print("phase 2 max predict step",dict2step)
print("number of phase 1 solution",phase1solutionnum,"total cube",n)
print("3 colors as base")
allcubestep=[]
starttime=time.time()
phasetime=[0,0]
for i in range(n):
    print("\ncube",i+1)
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    randomstring=randomcube()
    print("random string:",randomstring)
    t1=time.time()
    #max expected step number
    currentminstep=30
    minstring=""
    for f in range(3):
        tp0=time.time()
        rotatewithbase(randomstring,5-f)
        p1solutions=phase1(corner,cornerd,edge,edged)
        tp1=time.time()
        print(f,"/ 3, len",len(p1solutions),end=", ")
        for j in range(len(p1solutions)):
            s=p1solutions[j]
            p1length=int(len(s)/2)
            cubepack=[corner,cornerd,edge,edged]
            #phase 1
            for l in range(p1length):
                cubepack=rotatecube(int(s[2*l]),int(s[2*l+1]),*cubepack)
            stepleft=currentminstep-p1length
            solution1=phase2(cubepack,s,stepleft)
            #reduce one of the first step in phase 2 by another cube
            cubepack2=cubepack
            s2=s
            solution2=solution1
            if p1length>0:
                cubepack2=rotatecube(int(s[-2]),2,*cubepack)
                s2=s2[:-1]+"1"
                solution2=phase2(cubepack,s2,stepleft)
                
            #phase 2
            stepsum1=int(len(solution1)/2)
            stepsum2=int(len(solution2)/2)
            stepsum=min(stepsum1,stepsum2)
            if stepsum<currentminstep:
                currentminstep=stepsum
                if stepsum1>=stepsum2:
                    minstring=solution1
                else:
                    minstring=solution2
                print(stepsum,end=" ")
        tp2=time.time()
        phasetime[0]+=tp1-tp0
        phasetime[1]+=tp2-tp1
        print()
    t2=time.time()
    print("minimum step",currentminstep)
    print(t2-t1,"s","two phase time sum",phasetime)
    allcubestep.append(currentminstep)
    print("finish",i+1,"cubes, current results:",allcubestep,"average",sum(allcubestep)/len(allcubestep))
    #print("finish",i+1,"cubes, average",sum(allcubestep)/len(allcubestep))
    print("estimated time:",(t2-starttime)*(n-i-1)/(i+1),"s")
    print("min solution",minstring)
endtime=time.time()
print("total time",endtime-starttime,"s, average time",(endtime-starttime)/n,"s")
print("two phase time",phasetime[0]/n,"s +",phasetime[1]/n,"s")
print(allcubestep,"average",sum(allcubestep)/n,"max",max(allcubestep),"min",min(allcubestep))

import random,time

corner=[i for i in range(8)]#0,1,2,3,4,5,6,7,lub,rub,luf,ruf,ldf,rdf,ldb,rdb
cornerd=[0,0,0,0,5,5,5,5]#white or yellow face direction
edge=[i for i in range(12)]#0,1,2,3,4,5,6,7,8,9,10,11,ub,ul,uf,ur,lb,lf,rf,rb,db,dl,df,dr
edged=[0,0,0,0,1,2,3,4,5,5,5,5]#white or yellow, then right color on equator edge
center=[0,1,2,3,4,5]#center

facecorner=[[0,2,3,1],[0,6,4,2],[2,4,5,3],[3,5,7,1],[1,7,6,0],[4,6,7,5]]
faceedge=[[0,1,2,3],[1,4,9,5],[2,5,10,6],[3,6,11,7],[0,7,8,4],[10,9,8,11]]
adj=[[4,3,2,1],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[1,2,3,4]]#adjacent face of each

def rotate(a):
    global edge,edged,corner,cornerd
    #edge
    t=int(a[1])
    a=int(a[0])
    r=faceedge[a]
    ne=edge.copy()
    ned=edged.copy()
    for i in range(4):
        ne[r[i]]=edge[r[(i+t)%4]]
    for i in r:
        i=edge[i]
        if edged[i]!=a:
            ned[i]=adj[a][(adj[a].index(edged[i])+t)%4]
    edge=ne
    edged=ned
    #corner
    r=facecorner[a]
    nc=corner.copy()
    ncd=cornerd.copy()
    for i in range(4):
        nc[r[i]]=corner[r[(i+t)%4]]
    for i in r:
        i=corner[i]
        if cornerd[i]!=a:
            ncd[i]=adj[a][(adj[a].index(cornerd[i])+t)%4]
    corner=nc
    cornerd=ncd
    
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
        
def rotatecube(a,t,corner,cornerd,edge,edged):
    #edge
    r=faceedge[a]
    ne=edge.copy()
    ned=edged.copy()
    for i in range(4):
        ne[r[i]]=edge[r[(i+t)%4]]
    for i in r:
        i=edge[i]
        if edged[i]!=a:
            ned[i]=adj[a][(adj[a].index(edged[i])+t)%4]
    #corner
    r=facecorner[a]
    nc=corner.copy()
    ncd=cornerd.copy()
    for i in range(4):
        nc[r[i]]=corner[r[(i+t)%4]]
    for i in r:
        i=corner[i]
        if cornerd[i]!=a:
            ncd[i]=adj[a][(adj[a].index(cornerd[i])+t)%4]
    return [nc,ncd,ne,ned]

ccd=[0,0,0,0,5,5,5,5]#position from 0 to 7, first 4 can only be 0 to 4, last 4 is 1 to 5


'''

#1-2
correctmiddleedgep=[4,5,6,7]
dict1={}
predictstate=[[ccd,correctmiddleedgep,""]]
newpredictstate=[]
dict1[str(ccd+correctmiddleedgep)]=""
print("phase 1 dict")
t0=time.time()
for c in range(1,10):
    for i in predictstate:
        oldcornerd=i[0]
        oldmedgep=i[1]
        oldstep=i[2]
        for j in range(6):
            #6 face, no repeated rotation
            if (c==1 and j!=0 and j!=5) or (c!=1 and oldstep[0]!=str(j)):
                #3 rotations
                for k in range(1,4):
                    if c==1 and k==2:
                        continue
                    newcornerd=oldcornerd.copy()
                    newmedgep=oldmedgep.copy()
                    for l in range(4):
                        if oldcornerd[facecorner[j][(l+k)%4]]!=j:
                            newcornerd[facecorner[j][l]]=adj[j][(adj[j].index(oldcornerd[facecorner[j][(l+k)%4]])+k)%4]
                        else:
                            newcornerd[facecorner[j][l]]=j
                        if newmedgep[l] in faceedge[j]:
                            newmedgep[l]=faceedge[j][(faceedge[j].index(oldmedgep[l])+k)%4]
                    newmedgep.sort()
                    if str(newcornerd+newmedgep) not in dict1:
                        newstep=str(j)+str(4-k)+oldstep
                        dict1[str(newcornerd+newmedgep)]=newstep
                        newpredictstate.append([newcornerd.copy(),newmedgep.copy(),newstep])
    print(c,"cube left",len(newpredictstate),"dict length",len(dict1))
    predictstate=newpredictstate.copy()
    newpredictstate.clear()
print("dict1 time",time.time()-t0,"s")
def phase1(corner,cornerd,edge,edged):
    cubes=[[corner,cornerd,edge,edged,""]]#element in: [corner,cornerd,edge,edged,steps represented by 0 to 5]
    newcubes=[]
    phase1solution=[]
    maxstep=7
    #check first
    key=[edge.index(j) for j in range(4,8)]
    key.sort()
    key=str([cornerd[j] for j in corner]+key)
    furtherstep=dict1[key]
    #do the further rotations, simple way to turn edge
    oe=edge
    oed=edged
    ne=edge.copy()
    ned=edged.copy()
    for j in range(int(len(furtherstep)/2)):
        a=int(furtherstep[2*j])#turning face
        t=int(furtherstep[2*j+1])#turning time
        r=faceedge[a]
        for k in range(4):
            ne[r[k]]=oe[r[(k+t)%4]]
        for k in r:
            k=oe[k]
            if oed[k]!=a:
                ned[k]=adj[a][(adj[a].index(oed[k])+t)%4]
        oe=ne.copy()
        oed=ned.copy()
    finish=True
    for j in [0,1,2,3,8,9,10,11]:
        if ned[j]!=0 and ned[j]!=5:
            finish=False
            break
    if finish:
        phase1solution.append(furtherstep)
        
    for step in range(1,maxstep+1):
        for cubepack in cubes:
            cubecorner=cubepack[0]
            cubecornerd=cubepack[1]
            cubeedge=cubepack[2]
            cubeedged=cubepack[3]
            previousstep=cubepack[4]#formed by <face,degree>... string
            for i in range(6):
                if step==1 or str(i)!=previousstep[-2] and not (step>2 and str(i)==previousstep[-4] and previousstep[-4]+previousstep[-2] in ["05","50","13","31","24","42"]):
                    for t in range(1,4):
                        #rotate cube, return [nc,ncd,ne,ned]
                        newcubepack=rotatecube(i,t,cubecorner,cubecornerd,cubeedge,cubeedged)
                        newcorner=newcubepack[0]
                        newcornerd=newcubepack[1]
                        oe=newcubepack[2]
                        oed=newcubepack[3]
                        ne=oe.copy()
                        ned=oed.copy()
                        #use dictionary to mock edge position
                        newstep=previousstep+str(i)+str(t)
                        key=[ne.index(j) for j in range(4,8)]
                        key.sort()
                        key=str([newcornerd[j] for j in newcorner]+key)
                        furtherstep=dict1[key]
                        #do the further rotations, simple way to turn edge
                        for j in range(int(len(furtherstep)/2)):
                            a=int(furtherstep[2*j])#turning face
                            t=int(furtherstep[2*j+1])#turning time
                            r=faceedge[a]
                            for k in range(4):
                                ne[r[k]]=oe[r[(k+t)%4]]
                            for k in r:
                                k=oe[k]
                                if oed[k]!=a:
                                    ned[k]=adj[a][(adj[a].index(oed[k])+t)%4]
                            oe=ne.copy()
                            oed=ned.copy()
                        finish=(i!=0 and i!=5)
                        for j in [0,1,2,3,8,9,10,11]:
                            if ned[j]!=0 and ned[j]!=5:
                                finish=False
                                break
                        if finish:
                            if ned[4] in [1,3] and ned[6] in [1,3] and ned[5] in [2,4] and ned[7] in [2,4]:
                                phase1solution.append(newstep+furtherstep)
                                if len(phase1solution)>=phase1solutionnum:
                                    return phase1solution
                        elif step!=maxstep:
                            newcubepack.append(newstep)
                            newcubes.append(newcubepack)
        cubes=newcubes.copy()
        newcubes.clear()
    return phase1solution



'''
#1-1
dict1={}
predictstate=[[ccd,""]]
newpredictstate=[]
dict1[str(ccd)]=""
print("phase 1 dict")
for c in range(1,7):
    for i in predictstate:
        oldcornerd=i[0]
        oldstep=i[1]
        for j in range(6):
            if (c==1 and j!=0 and j!=5) or (c!=1 and oldstep[0]!=str(j)):
                for k in range(1,4):
                    if c==1 and k==2:
                        continue
                    newcornerd=oldcornerd.copy()
                    for l in range(4):
                        if oldcornerd[facecorner[j][(l+k)%4]]!=j:
                            newcornerd[facecorner[j][l]]=adj[j][(adj[j].index(oldcornerd[facecorner[j][(l+k)%4]])+k)%4]
                        else:
                            newcornerd[facecorner[j][l]]=j
                    if str(newcornerd) not in dict1:
                        newstep=str(j)+str(4-k)+oldstep
                        dict1[str(newcornerd)]=newstep
                        newpredictstate.append([newcornerd.copy(),newstep])
            
    print(c,"cube left",len(newpredictstate),"dict length",len(dict1))
    predictstate=newpredictstate.copy()
    newpredictstate.clear()

def phase1(corner,cornerd,edge,edged):
    cubes=[[corner,cornerd,edge,edged,""]]#element in: [corner,cornerd,edge,edged,steps represented by 0 to 5]
    newcubes=[]
    phase1solution=[]
    maxstep=7
    
    #check first
    furtherstep=dict1[str([cornerd[j] for j in corner])]
    oe=edge
    oed=edged
    ne=oe.copy()
    ned=oed.copy()
    for j in range(int(len(furtherstep)/2)):
        a=int(furtherstep[2*j])#turning face
        t=int(furtherstep[2*j+1])#turning time
        r=faceedge[a]
        for k in range(4):
           ne[r[k]]=oe[r[(k+t)%4]]
        for k in r:
            k=oe[k]
            if oed[k]!=a:
                ned[k]=adj[a][(adj[a].index(oed[k])+t)%4]
        oe=ne.copy()
        oed=ned.copy()
    finish=True
    for j in [0,1,2,3,8,9,10,11]:
        if ned[j]!=0 and ned[j]!=5:
            finish=False
            break
    if finish:
        phase1solution.append(furtherstep)
        print(len(phase1solution),end=" ")
    for step in range(1,maxstep+1):
        for cubepack in cubes:
            cubecorner=cubepack[0]
            cubecornerd=cubepack[1]
            cubeedge=cubepack[2]
            cubeedged=cubepack[3]
            previousstep=cubepack[4]#formed by <face,degree>... string
            for i in range(6):
                if step==1 or str(i)!=previousstep[-2] and not (step>2 and str(i)==previousstep[-4] and previousstep[-4]+previousstep[-2] in ["05","50","13","31","24","42"]):
                    for t in range(1,4):
                        #rotate cube, return [nc,ncd,ne,ned]
                        newcubepack=rotatecube(i,t,cubecorner,cubecornerd,cubeedge,cubeedged)
                        newcorner=newcubepack[0]
                        newcornerd=newcubepack[1]
                        #use dictionary to mock edge position
                        newstep=previousstep+str(i)+str(t)
                        furtherstep=dict1[str([newcornerd[j] for j in newcorner])]
                        #do the further rotations
                        oe=newcubepack[2]
                        oed=newcubepack[3]
                        ne=oe.copy()
                        ned=oed.copy()
                        #simple way to turn edge
                        for j in range(int(len(furtherstep)/2)):
                            a=int(furtherstep[2*j])#turning face
                            t=int(furtherstep[2*j+1])#turning time
                            r=faceedge[a]
                            for k in range(4):
                               ne[r[k]]=oe[r[(k+t)%4]]
                            for k in r:
                                k=oe[k]
                                if oed[k]!=a:
                                    ned[k]=adj[a][(adj[a].index(oed[k])+t)%4]
                            oe=ne.copy()
                            oed=ned.copy()
                        
                        finish=True
                        for j in [0,1,2,3,8,9,10,11]:
                            if ned[j]!=0 and ned[j]!=5:
                                finish=False
                                break
                        if finish:
                            if ned[4] in [1,3] and ned[6] in [1,3] and ned[5] in [2,4] and ned[7] in [2,4]:
                                phase1solution.append(newstep+furtherstep)
                                print(len(phase1solution),end=" ")
                                if len(phase1solution)>=phase1solutionnum:
                                    return phase1solution
                        
                        if step!=maxstep:
                            newcubepack.append(newstep)
                            newcubes.append(newcubepack)
        cubes=newcubes.copy()
        newcubes.clear()
    return phase1solution





#correct corner, correct edge, correct middle edge direction
cc=[0,1,2,3,4,5,6,7]
ce=[0,1,2,3,4,5,6,7,8,9,10,11]
ced=[0,0,0,0,1,2,3,4,5,5,5,5]
cmed=[1,2,3,4]

phase2rotations=["01","02","03","12","22","32","42","51","52","53"]

dict2={}
predictstate=[[cc,ce,cmed,""]]
newpredictstate=[]
dict2[str(cc+ce+cmed)]=""
#usually 8+-1
phase2maxstep=9
print("phase 2 dict")
t0=time.time()
for c in range(1,phase2maxstep+1):
    t1=time.time()
    for i in predictstate:
        #old
        oc=i[0]
        oe=i[1]
        omed=i[2]
        oldstep=i[3]
        for j in phase2rotations:
            f=int(j[0])
            t=int(j[1])
            if c==1 or oldstep[0]!=j[0] and not (c>2 and str(f)==oldstep[0] and oldstep[0]+oldstep[2] in ["05","50","13","31","24","42"]):
                #rotate
                nc=oc.copy()
                ne=oe.copy()
                nmed=omed.copy()
                fe=faceedge[f]
                fc=facecorner[f]
                if f==0 or f==5:
                    #rotate top or bottom
                    for k in range(4):
                        ne[fe[k]]=oe[fe[(k+t)%4]]
                        nc[fc[k]]=oc[fc[(k+t)%4]]
                else:
                    #rotate side
                    #corner and edge
                    for k in range(4):
                        ne[fe[k]]=oe[fe[(k+2)%4]]
                        nc[fc[k]]=oc[fc[(k+2)%4]]
                    #middle edge
                    for e in [fe[1],fe[3]]:
                        if omed[oe[e]-4]!=f:
                            nmed[oe[e]-4]=(omed[oe[e]-4]+1)%4+1
                key=str(nc+ne+nmed)
                if key not in dict2:
                    newstep=j[0]+str(4-int(j[1]))+oldstep
                    dict2[key]=newstep
                    if c!=phase2maxstep:
                        newpredictstate.append([nc.copy(),ne.copy(),nmed.copy(),newstep])
    print(c,"cube left",len(newpredictstate),"dict length",len(dict2),time.time()-t1)
    predictstate=newpredictstate.copy()
    newpredictstate.clear()
print("dict2 time",time.time()-t0,"s")

def phase2(cubepack):
    c=cubepack[0]
    cd=cubepack[1]
    e=cubepack[2]
    ed=cubepack[3]
    cubes=[[c,cd,e,ed,""]]#element in: [corner,cornerd,edge,edged,steps represented by 0 to 5]
    newcubes=[]
    maxstep=16#sum to 16 with dict2 max step
    if str(c+e+ed[4:8]) in dict2:
        return dict2[str(c+e+ed[4:8])]
    for step in range(1,maxstep+1):
        for cube in cubes:
            cubecorner=cube[0]
            cubecornerd=cube[1]
            cubeedge=cube[2]
            cubeedged=cube[3]
            previousstep=cube[4]#formed by <face,degree>... string
            for r in phase2rotations:
                f=r[0]
                t=r[1]
                if step==1 or f!=previousstep[-2] and not (step>2 and f==previousstep[-4] and previousstep[-4]+previousstep[-2] in ["05","50","13","31","24","42"]):
                    newcubepack=rotatecube(int(f),int(t),cubecorner,cubecornerd,cubeedge,cubeedged)
                    newcorner=newcubepack[0]
                    newcornerd=newcubepack[1]
                    newedge=newcubepack[2]
                    newedged=newcubepack[3]
                    key=str(newcorner+newedge+newedged[4:8])
                    if key in dict2:
                        return previousstep+r+dict2[key]
                    if step!=maxstep:
                        newcubes.append([newcorner.copy(),newcornerd.copy(),newedge.copy(),newedged.copy(),previousstep+r])
        cubes=newcubes.copy()
        newcubes.clear()

def initialize():
    global corner,cornerd,edge,edged,center
    corner=[i for i in range(8)]
    cornerd=[0,0,0,0,5,5,5,5]
    edge=[i for i in range(12)]
    edged=[0,0,0,0,1,2,3,4,5,5,5,5]

changebasetable=[[5,1,4,3,2,0],[3,0,2,5,4,1],[4,1,0,3,5,2],[1,5,2,0,4,3],[2,1,5,3,0,4],[0,1,2,3,4,5]]
def rotatewithbase(randomstring,base):
    l=int(len(randomstring)/2)
    initialize()
    newrandomstring=""
    for i in range(l):
        newrandomstring+=str(changebasetable[base][int(randomstring[2*i])])+randomstring[2*i+1]
    do(newrandomstring)

phase1solutionnum=10
n=1
print("1-1 phase 1 predict 2187 situations of corner block position")
#print("1-2 phase 1 predict middle edge and corner position")
print("phase 2 max predict step",phase2maxstep)
print("number of phase 1 solution",phase1solutionnum,"total cube",n)
allcubestep=[]
starttime=time.time()
for i in range(n):
    print("\ncube",i+1)
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    initialize()
    randomstring=randomcube()
    print("random string:",randomstring)
    t1=time.time()
    onecubestep=[]
    for f in range(6):
        print("cube",i+1,"face",f)
        rotatewithbase(randomstring,f)
        print("phase 1")
        p1solutions=phase1(corner,cornerd,edge,edged)
        p1solutions.sort(key=len)
        print([int(len(j)/2) for j in p1solutions])
        print("phase 2")
        for j in range(len(p1solutions)):
            s=p1solutions[j]
            print(i+1,"-",f,"-",j+1,end="    ")
            p1length=int(len(s)/2)
            cubepack=[corner.copy(),cornerd.copy(),edge.copy(),edged.copy()]
            for l in range(p1length):
                cubepack=rotatecube(int(s[2*l]),int(s[2*l+1]),cubepack[0],cubepack[1],cubepack[2],cubepack[3])
            
            p2solution=phase2(cubepack)
            p2length=int(len(p2solution)/2)
            for l in range(p2length):
                cubepack=rotatecube(int(p2solution[2*l]),int(p2solution[2*l+1]),cubepack[0],cubepack[1],cubepack[2],cubepack[3])
            stepsum=p1length+p2length
            print(p1length,"+",p2length,"=",stepsum)
            onecubestep.append(stepsum)
    t2=time.time()
    print(t2-t1,"s",onecubestep,"size",len(onecubestep),"minimum step",min(onecubestep))
    allcubestep.append(min(onecubestep))
    print("finish",i+1,"cubes, current results:",allcubestep,"average",sum(allcubestep)/len(allcubestep))
endtime=time.time()
print("total time",endtime-starttime,"s, average time",(endtime-starttime)/n,"s")
print(allcubestep,"average number",sum(allcubestep)/n)

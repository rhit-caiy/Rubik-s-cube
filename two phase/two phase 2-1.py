import random,time

corner=[i for i in range(8)]#0,1,2,3,4,5,6,7,lub,rub,luf,ruf,ldf,rdf,ldb,rdb
cornerd=[0,0,0,0,5,5,5,5]#white or yellow face direction
edge=[i for i in range(12)]#0,1,2,3,4,5,6,7,8,9,10,11,ub,ul,uf,ur,lb,lf,rf,rb,db,dl,df,dr
edged=[0,0,0,0,1,2,3,4,5,5,5,5]#white or yellow, then right color on equator edge
center=[0,1,2,3,4,5]#center

facecorner=[[0,2,3,1],[0,6,4,2],[2,4,5,3],[3,5,7,1],[1,7,6,0],[4,6,7,5]]
faceedge=[[0,1,2,3],[1,4,9,5],[2,5,10,6],[3,6,11,7],[0,7,8,4],[10,9,8,11]]
adj=[[4,3,2,1],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[1,2,3,4]]#adjacent face of each
# cornerposition=[[[0,0],[1,0],[4,2]],[[0,2],[4,0],[3,2]],[[0,6],[2,0],[1,2]],[[0,8],[3,0],[2,2]],
#                 [[5,0],[1,8],[2,6]],[[5,2],[2,8],[3,6]],[[5,6],[4,8],[1,6]],[[5,8],[3,8],[4,6]]]#corner face map to position
# edgeposition=[[[0,1],[4,1]],[[0,3],[1,1]],[[0,7],[2,1]],[[0,5],[3,1]],
#               [[1,3],[4,5]],[[2,3],[1,5]],[[3,3],[2,5]],[[4,3],[3,5]],
#               [[5,7],[4,7]],[[5,3],[1,7]],[[5,1],[2,7]],[[5,5],[3,7]]]#edge face map to position

# centeredge=[[0,2,10,8],[4,5,6,7],[1,3,11,9]]#middle rotation block
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
        r=random.choice(phase2rotations)
        randomstring+=r
    #print("random string",randomstring)
    do(randomstring)
    
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

#correct corner, correct edge, correct middle edge direction
cc=[0,1,2,3,4,5,6,7]
ce=[0,1,2,3,4,5,6,7,8,9,10,11]
cmed=[1,2,3,4]

phase2rotations=["01","02","03","12","22","32","42","51","52","53"]

dict2={}
predictstate=[[cc,ce,cmed,""]]
newpredictstate=[]
dict2[str(cc+ce+cmed)]=""
#usually 8+-1
maxstep=9
for c in range(1,maxstep+1):
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
            if c==1 or oldstep[0]!=j[0] and not (c>2 and str(f)==oldstep[-4] and oldstep[-4]+oldstep[-2] in ["05","50","13","31","24","42"]):
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
                    if c!=maxstep:
                        newpredictstate.append([nc.copy(),ne.copy(),nmed.copy(),newstep])
            
    print(c,"cube left",len(newpredictstate),"dict length",len(dict2),time.time()-t1)
    predictstate=newpredictstate.copy()
    newpredictstate.clear()

def phase2(corner,cornerd,edge,edged):
    cubes=[[corner,cornerd,edge,edged,""]]#element in: [corner,cornerd,edge,edged,steps represented by 0 to 5]
    newcubes=[]
    maxstep=16
    if str(corner+edge+edged[4:8]) in dict2:
        #print("find in step 0")
        return dict2[str(corner+edge+edged[4:8])]
    for step in range(1,maxstep+1):
        for cubepack in cubes:
            cubecorner=cubepack[0]
            cubecornerd=cubepack[1]
            cubeedge=cubepack[2]
            cubeedged=cubepack[3]
            previousstep=cubepack[4]#formed by <face,degree>... string
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
                        #print("find in step",step)
                        return previousstep+r+dict2[key]
                    newcubes.append([newcorner.copy(),newcornerd.copy(),newedge.copy(),newedged.copy(),previousstep+r])
        #print(step,len(newcubes))
        cubes=newcubes.copy()
        newcubes.clear()
        
print("phase 2",maxstep,"+ ?")
n=1000
t1=time.time()
allsteps=[]
print("number",n)
for i in range(n):
    randomcube()
    solutionstring=phase2(corner,cornerd,edge,edged)
    stepnum=int(len(solutionstring)/2)
    allsteps.append(stepnum)
    print(i+1,stepnum,sum(allsteps)/(i+1))
t2=time.time()
print("time used",t2-t1,"average",(t2-t1)/n)
print(sum(allsteps)/n)
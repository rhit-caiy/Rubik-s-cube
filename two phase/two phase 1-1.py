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
# color=["#FFFF00","#0000FF","#FF0000","#00FF00","#FF8000","#FFFFFF"]
# rotates=["U","L","F","R","B","D","M","E","S","x","y","z"]
# allrotation=[["U","U2","U'"],["L","L2","L'"],["F","F2","F'"],["R","R2","R'"],["B","B2","B'"],["D","D2","D'"]]
def rotate(a):
    global edge,edged,corner,cornerd
    #edge
    r=faceedge[a]
    ne=edge.copy()
    ned=edged.copy()
    for i in range(4):
        ne[r[i]]=edge[r[(i+1)%4]]
    for i in r:
        i=edge[i]
        if edged[i]!=a:
            ned[i]=adj[a][(adj[a].index(edged[i])+1)%4]
    edge=ne
    edged=ned
    #corner
    r=facecorner[a]
    nc=corner.copy()
    ncd=cornerd.copy()
    for i in range(4):
        nc[r[i]]=corner[r[(i+1)%4]]
    for i in r:
        i=corner[i]
        if cornerd[i]!=a:
            ncd[i]=adj[a][(adj[a].index(cornerd[i])+1)%4]
    corner=nc
    cornerd=ncd

def randomcube():
    a=random.randrange(64,128)
    randomstring=""
    for i in range(a):
        r=random.randrange(0,6)
        randomstring+=str(r)
    #print("random string",randomstring)
    do(randomstring)

def do(s):
    for i in s:
        rotate(int(i))

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

def checkphase1(cubepack):
    cornerd=cubepack[1]
    edge=cubepack[2]
    edged=cubepack[3]
    #middle edge position
    for i in range(4,8):
        if edge[i] not in [4,5,6,7]:
            return False
    #cornerd
    for i in range(8):
        if cornerd[i]!=0 and cornerd[i]!=5:
            return False
    #edged
    for i in range(4):
        if edged[i]!=0 and edged[i]!=5 or edged[i+8]!=0 and edged[i+8]!=5:
            return False
    return True

correctcornerd=[0,0,0,0,5,5,5,5]#position from 0 to 7, first 4 can only be 0 to 4, last 4 is 1 to 5
dict1={}
predictstate=[[correctcornerd,""]]
newpredictstate=[]
dict1[str(correctcornerd)]=""
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
    maxsolution=10
    '''
    if checkphase1([corner,cornerd,edge,edged]):
        #print("already satisfy phase 1")
        return ""
    '''
    maxstep=7
    #print("max detect",maxstep+6,"steps")
    #print(0,len(cubes))
    for step in range(1,maxstep+1):
        #time1=time.time()
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
                        # print(newstep,newcorner,newcornerd,[newcornerd[j] for j in newcorner],furtherstep)
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
                            #print("find solution at step",step,"solution",newstep)
                            #return newstep+furtherstep
                            phase1solution.append(newstep+furtherstep)
                            if len(phase1solution)>=maxsolution:
                                return phase1solution
                        
                        if step!=maxstep:
                            newcubepack.append(newstep)
                            newcubes.append(newcubepack)
        cubes=newcubes.copy()
        newcubes.clear()
        #print(step,len(cubes),time.time()-time1)
    #print("not found in",step,"steps")
    return phase1solution

# #do("0123451234")
# randomcube()
# print("corner =",corner)
# print("cornerd =",cornerd)
# print("edge =",edge)
# print("edged =",edged)
# solutionstring=phase1(corner,cornerd,edge,edged)
# stepnum=int(len(solutionstring)/2)
# for i in range(stepnum):
#     for j in range(int(solutionstring[2*i+1])):
#         do(solutionstring[2*i])
# print("solutionstring",solutionstring,"length",int(len(solutionstring)/2))
# print("corner =",corner)
# print("cornerd =",cornerd)
# print("edge =",edge)
# print("edged =",edged)

print("126720*2187")
n=10
t1=time.time()
allsteps=[]
print("max detect phase 1 in 13 steps")
print("number",n)
for i in range(n):
    print(i+1)
    randomcube()
    solutionstrings=phase1(corner,cornerd,edge,edged)
    #print(solutionstrings)
    onecubesolutionstep=[]
    for solutionstring in solutionstrings:
        l=int(len(solutionstring)/2)
        onecubesolutionstep.append(l)
    minstepnum=min(onecubesolutionstep)
    allsteps.append(minstepnum)
    print(onecubesolutionstep,minstepnum,sum(allsteps)/(i+1))
t2=time.time()
print("time used",round(t2-t1,3),"s, average time",round((t2-t1)/n,3),"s")
print("average step",sum(allsteps)/n)
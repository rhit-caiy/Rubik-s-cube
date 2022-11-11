import time,sys,threading
from itertools import permutations,product
from math import log

cblock=[0,1,2,3,4,5,6]
cblockd=[0,0,0,5,5,5,5]
faceblock=[[1,3,4,2],[2,4,6,0],[3,5,6,4]]
adj=[[0,3,5,1],[0,4,5,2],[1,2,3,4]]
facetimecorner=[[(1,3,4,2),(3,4,2,1),(4,2,1,3),(2,1,3,4)],[(2,4,6,0),(4,6,0,2),(6,0,2,4),(0,2,4,6)],[(3,5,6,4),(5,6,4,3),(6,4,3,5),(4,3,5,6)]]
facetimedirection=[[[0,1,2,3,4,5],[3,0,2,5,4,1],[5,3,2,1,4,0],[1,5,2,0,4,3]],[[0,1,2,3,4,5],[4,1,0,3,5,2],[5,1,4,3,2,0],[2,1,5,3,0,4]],[[0,1,2,3,4,5],[0,2,3,4,1,5],[0,3,4,1,2,5],[0,4,1,2,3,5]]]
cornerdirection=[(0,3,4),(0,1,2),(0,2,3),(5,1,2),(5,2,3),(5,4,1),(5,3,4)]

cdict={}
n=0
for i in permutations(range(7)):
    cdict[i]=n
    n+=1
print(len(cdict))
cpddict={}
n=0
for i in product(*cornerdirection):
    cpddict[i]=n
    n+=1
print(len(cpddict))

def rotatecubeaddress(f,t,c,cd):
    c1,c2,c3,c4=faceblock[f]
    nc1,nc2,nc3,nc4=facetimecorner[f][t]
    cn1,cn2,cn3,cn4=c[c1],c[c2],c[c3],c[c4]=c[nc1],c[nc2],c[nc3],c[nc4]
    ftd=facetimedirection[f][t]
    cd[cn1],cd[cn2],cd[cn3],cd[cn4]=ftd[cd[cn1]],ftd[cd[cn2]],ftd[cd[cn3]],ftd[cd[cn4]]

def gethtm():
    global htm
    cubelist=[[cblock,cblockd,1,-1]]
    newcubelist=[]
    key=cdict[tuple(cblock)]*2187+cpddict[tuple(cblockd)]
    htm[key]=1
    tstart=time.time()
    for step in range(1,17):
        t1=time.time()
        for cube in cubelist:
            c,cd,oldstep,f1=cube
            for f in range(3):
                if f==f1:
                    continue
                for t in range(1,4):
                    nc=c.copy()
                    ncd=cd.copy()
                    rotatecubeaddress(f,t,nc,ncd)
                    key=cdict[tuple(nc)]*2187+cpddict[tuple([ncd[i] for i in nc])]
                    newstep=oldstep*9+f*3+t-1
                    if key not in htm:
                        htm[key]=newstep
                        newcubelist.append([nc,ncd,newstep,f])
        print("{:<10}{:<20}{:<20}{:f}".format(step,len(htm),"",time.time()-t1))
        if newcubelist==[]:
            break
        cubelist=newcubelist
        newcubelist=[]
    print("htm",time.time()-tstart)

def getqtm():
    global qtm
    cubelist=[[cblock,cblockd,1]]
    newcubelist=[]
    key=cdict[tuple(cblock)]*2187+cpddict[tuple(cblockd)]
    qtm[key]=1
    tstart=time.time()
    for step in range(1,17):
        t1=time.time()
        for cube in cubelist:
            c,cd,oldstep=cube
            for f in range(3):
                for t in (1,3):
                    nc=c.copy()
                    ncd=cd.copy()
                    rotatecubeaddress(f,t,nc,ncd)
                    key=cdict[tuple(nc)]*2187+cpddict[tuple([ncd[i] for i in nc])]
                    newstep=oldstep*9+f*3+t-1
                    if key not in qtm:
                        qtm[key]=newstep
                        newcubelist.append([nc,ncd,newstep])
        print("{:<10}{:<20}{:<20}{:f}".format(step,"",len(qtm),time.time()-t1))
        if newcubelist==[]:
            break
        cubelist=newcubelist
        newcubelist=[]
    print("qtm",time.time()-tstart)
    
print("{:<10}{:<20}{:<20}{}".format("step","htm","qtm","time"))
print("{:<10}{:<20}{:<20}{:f}".format(0,1,1,0))
htm={}
qtm={}
dict1thread=threading.Thread(target=gethtm)
dict2thread=threading.Thread(target=getqtm)
tdictstart=time.time()
dict1thread.start()
dict2thread.start()
dict2thread.join()
dict1thread.join()
tdictend=time.time()
print("{:<10}{:<20}{:<20}{:f}".format("total",len(htm),len(qtm),tdictend-tdictstart))

def printdictsize(d):
    a=sys.getsizeof(d)
    b=0
    for i in d.keys():
        b+=sys.getsizeof(i)
    for i in d.values():
        b+=sys.getsizeof(i)
    print([name for name in globals() if globals()[name] is d][0],len(d),"dict space",a,"B    values and keys space",b,"B    total",(a+b)/1000000000,"GB    ",(a+b)/1000000,"MB")
printdictsize(cdict)
printdictsize(cpddict)
printdictsize(htm)
printdictsize(qtm)
s=0
for i in htm.values():
    s+=log(i,18)
print("average htm",s/len(htm))
s=0
for i in qtm.values():
    s+=log(i,18)
print("average qtm",s/len(qtm))

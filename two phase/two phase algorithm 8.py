import random,time,sys,threading
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

antithesis=[5,3,4,1,2,0]

t=time.time()

def getdict1(dict1step):
    global dict1
    predictstate=[[cc,ccd,ce,ced,0]]
    newpredictstate=[]
    key=getkey1(cc,ccd,ce,ced)
    dict1[key]=0
    t0=time.time()
    for step in range(1,dict1step+1):
        t1=time.time()
        for cube in predictstate:
            oc,ocd,oe,oed,oldstep=cube
            for f in range(6):
                f1=oldstep%18//3
                f2=oldstep//18%18//3
                if step>2 and (f==f1 or (f==f2 and (f==0 and f1==5 or 
                                                    f==5 and f1==0 or 
                                                    f==1 and f1==3 or 
                                                    f==3 and f1==1 or 
                                                    f==2 and f1==4 or 
                                                    f==4 and f1==2))):
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
                    key=getkey1(nc,ncd,ne,ned)
                    if key not in dict1:
                        if step==1:
                            newstep=f
                        else:
                            newstep=oldstep*18+6*f+3-t
                        dict1[key]=newstep
                        if step!=dict1step:
                            newpredictstate.append([nc,ncd,ne,ned,newstep])
        
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,step,len(newpredictstate),len(dict1),time.time()-t1),end="")
        predictstate=newpredictstate
        newpredictstate=[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,"total",len(newpredictstate),len(dict1),time.time()-t0),end="")

#corner, edge position simplify
cpsimplify={}
epsimplify={}
cnum=0
enum=0
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                for m in range(3):
                    for n in range(3):
                        for o in range(3):
                            cpsimplify[str([i,j,k,l,m,n,o])]=cnum
                            cnum+=1
                            for p in range(3):
                                for q in range(3):
                                    for r in range(3):
                                        for s in range(3):
                                            epsimplify[str([i,j,k,l,m,n,o,p,q,r,s])]=enum
                                            enum+=1
print("length of cpsimplify",len(cpsimplify))
print("length of epsimplify",len(epsimplify))

#middle edge position
mepsimplify={}
num=0
for i in range(12):
    for j in range(i+1,12):
        for k in range(j+1,12):
            for l in range(k+1,12):
                mepsimplify[str([i,j,k,l])]=num
                num+=1
print("length of mepsimplify",len(mepsimplify))

positionsimplify=[0,1,2,1,2,0]
def getkey1(c,cd,e,ed):
    k1=cpsimplify[str([positionsimplify[cd[c[i]]] for i in range(7)])]
    k2=epsimplify[str([positionsimplify[ed[e[i]]] for i in range(11)])]
    k3=mepsimplify[str(sorted([e.index(i) for i in range(4,8)]))]
    return ((k1*177147+k2)*495)+k3
    
phase2rotations=["01","02","03","12","22","32","42","51","52","53"]
phase2rotations=[i-1 for i in [1,2,3,5,8,11,14,16,17,18]]
def getdict2(dict2step):
    global dict2
    predictstate=[[cc,ce,cmed,1]]
    newpredictstate=[]
    key=getkey2(cc,ce,cmed)
    dict2[key]=1
    t0=time.time()
    for step in range(1,dict2step+1):
        t1=time.time()
        for cube in predictstate:
            oc,oe,omed,oldstep=cube
            for r in phase2rotations:
                # r=phase2rotations[j]
                f=r//3
                t=r%3
                f1=oldstep%18//3
                f2=oldstep//18%18//3
                if step==1 or f1!=f and not (step>2 and f==f2 and (f==0 and f1==5 or 
                                                                        f==5 and f1==0 or 
                                                                        f==1 and f1==3 or 
                                                                        f==3 and f1==1 or 
                                                                        f==2 and f1==4 or 
                                                                        f==4 and f1==2)):
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
                    key=getkey2(nc,ne,nmed)
                    if key not in dict2:
                        newstep=oldstep*18+6*f+3-t
                        dict2[key]=newstep
                        if step!=dict2step:
                            newpredictstate.append([nc,ne,nmed,newstep])
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,step,len(newpredictstate),len(dict2),time.time()-t1),end="")
        predictstate=newpredictstate
        newpredictstate=[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,"total",len(newpredictstate),len(dict1),time.time()-t0),end="")
    
#corner
cornersimplify={}
num=0
for i in range(8):
    for j in range(8):
        for k in range(8):
            for l in range(8):
                for m in range(8):
                    for n in range(8):
                        for o in range(8):
                            for p in range(8):
                                if sorted([i,j,k,l,m,n,o,p])==[0,1,2,3,4,5,6,7]:
                                    cornersimplify[str([i,j,k,l,m,n,o,p])]=num
                                    num+=1
print("length of cornersimplify",len(cornersimplify))

#up down edge
udesimplify={}
ude=[0,1,2,3,8,9,10,11]
num=0
for i in ude:
    for j in ude:
        for k in ude:
            for l in ude:
                for m in ude:
                    for n in ude:
                        for o in ude:
                            for p in ude:
                                if sorted([i,j,k,l,m,n,o,p])==ude:
                                    udesimplify[str([i,j,k,l,m,n,o,p])]=num
                                    num+=1
print("length of udesimplify",len(cornersimplify))

#middle edge position
mesimplify={}
num=0
for i in range(4,8):
    for j in range(4,8):
        for k in range(4,8):
            for l in range(4,8):
                if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                    mesimplify[str([i,j,k,l])]=num
                    num+=1
print("length of mesimplify",len(mesimplify))

#middle edge direction
medsimplify={'[1, 1, 3, 3]':0,'[1, 3, 1, 3]':1,'[1, 3, 3, 1]':2,'[3, 1, 1, 3]':3,'[3, 1, 3, 1]':4,'[3, 3, 1, 1]':5}
print("length of medsimplify",len(medsimplify))

print(time.time()-t,"s")

def getkey2(c,e,med):
    k1=cornersimplify[str(c)]
    k2=udesimplify[str(e[0:4]+e[8:12])]
    k3=mesimplify[str(e[4:8])]
    k4=medsimplify[str(med)]
    return ((k1*40320+k2)*24+k3)*6+k4

dict1={}
dict2={}
dict1step=5
dict2step=6
dict1thread=threading.Thread(target=getdict1,args=(dict1step,))
dict2thread=threading.Thread(target=getdict2,args=(dict2step,))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("{:<8}{:<8}{:<16}{:<16}{:<16}\n".format("dict","step","cubes left","dict length","time/s"),end="")
tdictstart=time.time()
dict1thread.start()
dict1thread.join()
dict2thread.start()
dict2thread.join()
tdictend=time.time()
print("time",tdictend-tdictstart,"s")
def printdictsize(d):
    a=sys.getsizeof(d)
    b=0
    for i in d.keys():
        b+=sys.getsizeof(i)
    for i in d.values():
        b+=sys.getsizeof(i)
    print("dict",a,"B    values and keys",b,"B    total",(a+b)/1000000000,"GB    ",(a+b)/1000000,"MB")
print("dict1 size",len(dict1))
printdictsize(dict1)
print("dict2 size",len(dict2))
printdictsize(dict2)
print("other dicts")
printdictsize(cpsimplify)
printdictsize(epsimplify)
printdictsize(mepsimplify)
printdictsize(cornersimplify)
printdictsize(udesimplify)
printdictsize(mesimplify)
printdictsize(medsimplify)
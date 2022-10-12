import time
corner=[i for i in range(8)]
cornerd=[0,0,0,0,5,5,5,5]
edge=[i for i in range(12)]
edged=[0,0,0,0,1,1,3,3,5,5,5,5]#middle edge direction changes from 1234 to 1133 for convinience, where 1234 is better for CFOP
cc=corner.copy()
ccd=cornerd.copy()
ce=edge.copy()
ced=edged.copy()

facecorner=[[0,2,3,1],[0,6,4,2],[2,4,5,3],[3,5,7,1],[1,7,6,0],[4,6,7,5]]
faceedge=[[0,1,2,3],[1,4,9,5],[2,5,10,6],[3,6,11,7],[0,7,8,4],[10,9,8,11]]
adj=[[4,3,2,1],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[1,2,3,4]]

dict1={}
#corner position direction, doesn't care which block it is, just focus on direction
k1=[cornerd[corner.index(i)] for i in range(7)]
#edge position direction similar to above
k2=[edged[edge.index(i)] for i in range(11)]
#middle edge position, doesn't care which middle edge so use sort, rests are up down edges
k3=[edge.index(i) for i in range(4,8)]
k3.sort()
#use 7 and 11 here because of cube's property on edge and corner. Don't care about last 

dict1={}
predictstate=[[cc,ccd,ce,ced,""]]#cube=[corner,cornerd,edge,edged,steptosolve]
newpredictstate=[]
#key=cornerpositiondirection+edgepositiondirection+middleedgeposition
key=str(k1+k2+k3)[1:-1].replace(", ","")
dict1[key]=""
t0=time.time()
dict1step=7
print("phase 1 dict")
for c in range(1,dict1step+1):
    t1=time.time()
    for cube in predictstate:
        oc=cube[0]
        ocd=cube[1]
        oe=cube[2]
        oed=cube[3]
        oldstep=cube[4]
        for f in range(6):
            if c>2 and (str(f)==oldstep[0] or (str(f)==oldstep[2] and oldstep[0]+oldstep[2] in ["05","50","13","31","24","42"])):
                continue
            re=faceedge[f]
            rc=facecorner[f]
            for t in range(1,4):
                ne=oe.copy()
                ned=oed.copy()
                nc=oc.copy()
                ncd=ocd.copy()
                for n in range(4):
                    ne[re[n]]=oe[re[(n+t)%4]]
                    nc[rc[n]]=oc[rc[(n+t)%4]]
                    en=oe[re[n]]
                    if oed[en]!=f:
                        ned[en]=adj[f][(adj[f].index(oed[en])+t)%4]
                    cn=oc[rc[n]]
                    if ocd[cn]!=f:
                        ncd[cn]=adj[f][(adj[f].index(ocd[cn])+t)%4]
                
                k1=[ncd[nc.index(i)] for i in range(7)]
                k2=[ned[ne.index(i)] for i in range(11)]
                k3=[ne.index(i) for i in range(4,8)]
                k3.sort()
                key=str(k1+k2+k3)[1:-1].replace(", ","")
                if key not in dict1:
                    newstep=str(f)+str(4-t)+oldstep
                    dict1[key]=newstep
                    if c!=dict1step:
                        newpredictstate.append([nc,ncd,ne,ned,newstep])
        
    print(c,"cube left",len(newpredictstate),"dict length",len(dict1),time.time()-t1)
    predictstate=newpredictstate.copy()
    newpredictstate.clear()
print("dict 1 time",time.time()-t0,"size",len(dict1))
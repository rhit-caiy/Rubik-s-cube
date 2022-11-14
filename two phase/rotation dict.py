import random,time,sys,threading
from math import log
from itertools import permutations,product,combinations
cc=[0,1,2,3,4,5,6,7]
cco=[0,0,0,0,5,5,5,5]
ce=[0,1,2,3,4,5,6,7,8,9,10,11]
ceo=[0,0,0,0,1,1,3,3,5,5,5,5]

facetimecorner=[[(2,3,1,0),(3,1,0,2),(1,0,2,3)],[(6,4,2,0),(4,2,0,6),(2,0,6,4)],[(4,5,3,2),(5,3,2,4),(3,2,4,5)],[(5,7,1,3),(7,1,3,5),(1,3,5,7)],[(7,6,0,1),(6,0,1,7),(0,1,7,6)],[(6,7,5,4),(7,5,4,6),(5,4,6,7)]]
facetimeedge=[[(1,2,3,0),(2,3,0,1),(3,0,1,2)],[(4,9,5,1),(9,5,1,4),(5,1,4,9)],[(5,10,6,2),(10,6,2,5),(6,2,5,10)],[(6,11,7,3),(11,7,3,6),(7,3,6,11)],[(7,8,4,0),(8,4,0,7),(4,0,7,8)],[(9,8,11,10),(8,11,10,9),(11,10,9,8)]]
facecorner=[(0,2,3,1),(0,6,4,2),(2,4,5,3),(3,5,7,1),(1,7,6,0),(4,6,7,5)]
faceedge=[(0,1,2,3),(1,4,9,5),(2,5,10,6),(3,6,11,7),(0,7,8,4),(10,9,8,11)]
facetimedirection=[[[0,4,1,2,3,5],[0,3,4,1,2,5],[0,2,3,4,1,5]],[[2,1,5,3,0,4],[5,1,4,3,2,0],[4,1,0,3,5,2]],[[3,0,2,5,4,1],[5,3,2,1,4,0],[1,5,2,0,4,3]],[[4,1,0,3,5,2],[5,1,4,3,2,0],[2,1,5,3,0,4]],[[1,5,2,0,4,3],[5,3,2,1,4,0],[3,0,2,5,4,1]],[[0,2,3,4,1,5],[0,3,4,1,2,5],[0,4,1,2,3,5]]]
cornerdirection=[(0,4,1),(0,3,4),(0,1,2),(0,2,3),(5,2,1),(5,3,2),(5,1,4),(5,4,3)]
edgedirection=[(0,4),(0,1),(0,2),(0,3),(1,4),(1,2),(3,2),(3,4),(5,4),(5,1),(5,2),(5,3)]

cdict={}
rcdict={}
codict={}
rcodict={}
ep4dict={}
rep4dict={}
eodict={}
reodict={}

def rotatecubeaddress(f,t,c,cd,e,ed):
    c1,c2,c3,c4=facecorner[f]
    nc1,nc2,nc3,nc4=facetimecorner[f][t]
    cn1,cn2,cn3,cn4=c[c1],c[c2],c[c3],c[c4]=c[nc1],c[nc2],c[nc3],c[nc4]
    
    e1,e2,e3,e4=faceedge[f]
    ne1,ne2,ne3,ne4=facetimeedge[f][t]
    en1,en2,en3,en4=e[e1],e[e2],e[e3],e[e4]=e[ne1],e[ne2],e[ne3],e[ne4]
    
    ftd=facetimedirection[f][t]
    cd[cn1],cd[cn2],cd[cn3],cd[cn4]=ftd[cd[cn1]],ftd[cd[cn2]],ftd[cd[cn3]],ftd[cd[cn4]]
    ed[en1],ed[en2],ed[en3],ed[en4]=ftd[ed[en1]],ftd[ed[en2]],ftd[ed[en3]],ftd[ed[en4]]

#cdict, (0,1,2,3,4,5,6,7),(0,1,2,3,4,5,7,6) 40320 8!
n=0
for i in permutations(range(8)):
    cdict[i]=n
    rcdict[n]=i
    n+=1
print(len(cdict))

#codict, (0,0,0,0,5,5,5,5),(0,0,0,0,5,5,4,4) 2187 3**7
n=0
for i in product(range(3),repeat=8):
    if sum(i)%3==0:
        a=()
        for j in range(8):
            a+=(cornerdirection[j][i[j]],)
        codict[a]=n
        rcodict[n]=a
        n+=1
print(len(codict))

#eodict, (0,0,0,0,1,1,3,3,5,5,5,5),(0,0,0,0,1,1,3,3,5,5,2,3) 2048 2**11
n=0
for i in product(range(2),repeat=12):
    if sum(i)%2==0:
        a=()
        for j in range(12):
            a+=(edgedirection[j][i[j]],)
        eodict[a]=n
        reodict[n]=a
        n+=1
print(len(eodict))

#ep4dict,up edge,middle edge,bottom edge, (0,1,2,3),(0,1,2,11),(0,1,3,2) 11880 P(12,4)
n=0
for i in combinations(range(12),r=4):
    for j in permutations(i):
        ep4dict[j]=n
        rep4dict[n]=j
        n+=1
print(len(ep4dict))

cr=[[{} for j in range(3)] for i in range(6)]
cor=[[{} for j in range(3)] for i in range(6)]
eor=[[{} for j in range(3)] for i in range(6)]
ep4r=[[{} for j in range(3)] for i in range(6)]

for f in range(6):
    c1,c2,c3,c4=facecorner[f]
    e1,e2,e3,e4=faceedge[f]
    for t in range(3):
        print(f,t)
        nc1,nc2,nc3,nc4=facetimecorner[f][t]
        ne1,ne2,ne3,ne4=facetimeedge[f][t]
        ftd=facetimedirection[f][t]
        for dc in cdict.keys():
            c=list(dc)
            c[c1],c[c2],c[c3],c[c4]=c[nc1],c[nc2],c[nc3],c[nc4]
            cr[f][t][cdict[dc]]=cdict[tuple(c)]
        for dco in codict.keys():
            co=list(dco)
            co[c1],co[c2],co[c3],co[c4]=ftd[co[nc1]],ftd[co[nc2]],ftd[co[nc3]],ftd[co[nc4]]
            cor[f][t][codict[dco]]=codict[tuple(co)]
        for deo in eodict.keys():
            eo=list(deo)
            eo[e1],eo[e2],eo[e3],eo[e4]=ftd[eo[ne1]],ftd[eo[ne2]],ftd[eo[ne3]],ftd[eo[ne4]]
            eor[f][t][eodict[deo]]=eodict[tuple(eo)]
        for dep in ep4dict.keys():
            ep=list(dep)
            for i in range(4):
                if ep[i] in faceedge[f]:
                    ep[i]=faceedge[f][facetimeedge[f][t].index(ep[i])]
            ep4r[f][t][ep4dict[dep]]=ep4dict[tuple(ep)]


print(len(cr[0][0]))
print(rcdict[cr[0][0][cdict[tuple(cc)]]])
print(len(cor[0][0]))
print(rcodict[cor[1][0][codict[(0,0,0,0,2,2,1,3)]]])
print(len(eor[0][0]))
print(reodict[eor[1][0][eodict[(0,0,0,0,1,1,3,3,5,5,5,5)]]])
print(len(ep4r[0][0]))
print(rep4dict[ep4r[1][2][ep4dict[(0,1,2,3)]]])

'''
t=time.time()
for i in range(1000000):
    rcdict[cr[0][0][cdict[tuple(cc)]]]
print(time.time()-t)

t=time.time()
c=cc
for i in range(1000000):
    c1,c2,c3,c4=facecorner[0]
    nc1,nc2,nc3,nc4=facetimecorner[0][0]
    c[c1],c[c2],c[c3],c[c4]=c[nc1],c[nc2],c[nc3],c[nc4]
print(time.time()-t)
'''

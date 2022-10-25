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

phase2rotations=["01","02","03","12","22","32","42","51","52","53"]
medchange=[0,3,4,1,2]

def getdict1(dict1step):
    global dict1
    predictstate=[[cc,ccd,ce,ced,""]]
    newpredictstate=[]
    key=getkey(cc,ccd,ce,ced)
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
                    key=getkey(nc,ncd,ne,ned)
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

positionsimplify=[0,1,2,1,2,0]
def getkey(c,cd,e,ed):
    cpd=[positionsimplify[cd[c[i]]] for i in range(7)]
    epd=[positionsimplify[ed[e[i]]] for i in range(11)]
    cepd=cpd+epd#18 0-2
    k1=0
    t=1
    for i in cepd:
        k1+=i*t
        t*=3
    mep=sorted([e.index(i) for i in range(4,8)])
    k2=str(mep[0])+str(mep[1]-mep[0]-1)+str(mep[2]-mep[1]-1)+str(mep[3]-mep[2]-1)
    key=str(k1)+k2
    return key
# rotatetable=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
# def encodevalue(v):
#     s=""
#     for i in range(int(len(v)/2)):
#         f=int(v[2*i])
#         t=int(v[2*i+1])-1
#         s+=rotatetable[3*f+t]
#     s+=v[-1]
#     return s
# def decodevalue(s):
#     if s=="":
#         return ""
#     v=""
#     for i in range(len(s)-1):
#         a=rotatetable.index(s[i])
#         v+=str(a//3)+str(a%3+1)
#     v+=s[-1]
#     return v
        
# print(getkey(cc,ccd,ce,ced))
# print(encodevalue("1122334101531"))
# print(decodevalue(encodevalue("1122334101531")))
dict1={}
getdict1(7)
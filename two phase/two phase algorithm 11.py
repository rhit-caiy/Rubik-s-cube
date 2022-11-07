import random,time,sys,threading
from math import log
from itertools import permutations,product,combinations
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
cc=[0,1,2,3,4,5,6,7]
ccd=[0,0,0,0,5,5,5,5]
ce=[0,1,2,3,4,5,6,7,8,9,10,11]
ced=[0,0,0,0,1,1,3,3,5,5,5,5]
cmed=[1,1,3,3]

facetimecorner=[[(0,2,3,1),(2,3,1,0),(3,1,0,2),(1,0,2,3)],[(0,6,4,2),(6,4,2,0),(4,2,0,6),(2,0,6,4)],[(2,4,5,3),(4,5,3,2),(5,3,2,4),(3,2,4,5)],[(3,5,7,1),(5,7,1,3),(7,1,3,5),(1,3,5,7)],[(1,7,6,0),(7,6,0,1),(6,0,1,7),(0,1,7,6)],[(4,6,7,5),(6,7,5,4),(7,5,4,6),(5,4,6,7)]]
facetimeedge=[[(0,1,2,3),(1,2,3,0),(2,3,0,1),(3,0,1,2)],[(1,4,9,5),(4,9,5,1),(9,5,1,4),(5,1,4,9)],[(2,5,10,6),(5,10,6,2),(10,6,2,5),(6,2,5,10)],[(3,6,11,7),(6,11,7,3),(11,7,3,6),(7,3,6,11)],[(0,7,8,4),(7,8,4,0),(8,4,0,7),(4,0,7,8)],[(10,9,8,11),(9,8,11,10),(8,11,10,9),(11,10,9,8)]]
facecorner=[i[0] for i in facetimecorner]
faceedge=[i[0] for i in facetimeedge]
adj=[(4,3,2,1),(0,2,5,4),(0,3,5,1),(0,4,5,2),(0,1,5,3),(1,2,3,4)]
facetimedirection=[[[0,1,2,3,4,5],[0,4,1,2,3,5],[0,3,4,1,2,5],[0,2,3,4,1,5]],[[0,1,2,3,4,5],[2,1,5,3,0,4],[5,1,4,3,2,0],[4,1,0,3,5,2]],[[0,1,2,3,4,5],[3,0,2,5,4,1],[5,3,2,1,4,0],[1,5,2,0,4,3]],[[0,1,2,3,4,5],[4,1,0,3,5,2],[5,1,4,3,2,0],[2,1,5,3,0,4]],[[0,1,2,3,4,5],[1,5,2,0,4,3],[5,3,2,1,4,0],[3,0,2,5,4,1]],[[0,1,2,3,4,5],[0,2,3,4,1,5],[0,3,4,1,2,5],[0,4,1,2,3,5]]]

positionsimplify=[0,1,2,1,2,0]
phase2rotations=[0,1,2,4,7,10,13,15,16,17]
eighteen=[18**i for i in range(28)]

def printdictsize(d):
    a=sys.getsizeof(d)
    b=0
    for i in d.keys():
        b+=sys.getsizeof(i)
    for i in d.values():
        b+=sys.getsizeof(i)
    print([name for name in globals() if globals()[name] is d][0],len(d),"dict space",a,"B    values and keys space",b,"B    total",(a+b)/1000000000,"GB    ",(a+b)/1000000,"MB")

#dict11 177147
#dict12 1082565
#dict21 241920
#dict22 967680
t1=time.time()
dict11,dict12,dict21,dict22={},{},{},{}
n1=n2=n3=n4=0
for i in product(range(3),repeat=11):
    dict11[i]=n1
    n1+=1
t2=time.time()
j2=[i for i in combinations(range(12),r=4)]
for i in product(range(3),repeat=7):
    for j in j2:
        dict12[i+j]=n2
        n2+=1
t3=time.time()
j3=((1,1,3,3),(1,3,1,3),(1,3,3,1),(3,1,1,3),(3,1,3,1),(3,3,1,1))
for i in permutations(range(8)):
    for j in j3:
        dict21[i+j]=n3
        n3+=1
t4=time.time()
j4=[i for i in permutations(range(4,8))]
for i in permutations((0,1,2,3,8,9,10,11)):
    i1=i[:4]
    i2=i[4:]
    for j in j4:
        dict22[i1+j+i2]=n4
        n4+=1
t5=time.time()
print(t5-t4,t4-t3,t3-t2,t2-t1)
print(t5-t1,"s")

printdictsize(dict11)
printdictsize(dict12)
printdictsize(dict21)
printdictsize(dict22)

dict121={}#sort middle edge position
for i in j2:
    for j in permutations(i):
        dict121[j]=i

def getdict1(dict1step):
    global dict1
    predictstate=[(cc,ccd,ce,ced,1,-1,-1)]
    newpredictstate=[]
    key1=dict11[tuple([positionsimplify[ced[i]] for i in ce[:11]])]*1082565+dict12[tuple([positionsimplify[ccd[i]] for i in cc[:7]])+dict121[tuple([ce.index(i) for i in range(4,8)])]]
    dict1[key1]=1
    t0=time.time()
    for step in range(1,dict1step+1):
        t1=time.time()
        for cube in predictstate:
            oc,ocd,oe,oed,oldstep,f1,f2=cube
            for f in range(6):
                if step==1 or f1!=f and not ((f1==5 and f==0 or f1==4 and f==2 or f1==3 and f==1) or (step>2 and f==f2 and (f==0 and f1==5 or f==1 and f1==3 or f==2 and f1==4))):
                    newstep=oldstep*18+3*f+2
                    for t in range(1,4):
                        nc=oc.copy()
                        ncd=ocd.copy()
                        ne=oe.copy()
                        ned=oed.copy()
                        rotatecubeaddress(f,t,nc,ncd,ne,ned)
                        key1=dict11[tuple([positionsimplify[ned[i]] for i in ne[:11]])]*1082565+dict12[tuple([positionsimplify[ncd[i]] for i in nc[:7]])+dict121[tuple([ne.index(i) for i in range(4,8)])]]
                        if key1 not in dict1:
                            dict1[key1]=newstep
                            if step!=dict1step:
                                newpredictstate.append((nc,ncd,ne,ned,newstep,f,f1))
                        newstep-=1
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,step,len(newpredictstate),len(dict1),time.time()-t1),end="")
        predictstate=newpredictstate
        newpredictstate=[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,"total","",len(dict1),time.time()-t0),end="")

def getdict2(dict2step):
    global dict2
    predictstate=[(cc,ce,cmed,0,-1,-1)]
    newpredictstate=[]
    key2=dict21[tuple(cc+cmed)]*967680+dict22[tuple(ce)]
    dict2[key2]=1
    t0=time.time()
    for step in range(1,dict2step+1):
        t1=time.time()
        for cube in predictstate:
            oc,oe,omed,oldstep,f1,f2=cube
            for r in phase2rotations:
                f,t=r//3,r%3+1
                if step==1 or f1!=f and not ((f1==5 and f==0 or f1==4 and f==2 or f1==3 and f==1) or (step>2 and f==f2 and (f==0 and f1==5 or f==1 and f1==3 or f==2 and f1==4))):
                    nc=oc.copy()
                    ne=oe.copy()
                    nmed=omed.copy()
                    c1,c2,c3,c4=facecorner[f]
                    nc1,nc2,nc3,nc4=facetimecorner[f][t]
                    nc[c1],nc[c2],nc[c3],nc[c4]=nc[nc1],nc[nc2],nc[nc3],nc[nc4]
                    e1,e2,e3,e4=faceedge[f]
                    ne1,ne2,ne3,ne4=facetimeedge[f][t]
                    ne[e1],ne[e2],ne[e3],ne[e4]=ne[ne1],ne[ne2],ne[ne3],ne[ne4]
                    if f==0 or f==5:
                        pass
                    else:
                        en2,en4=ne[e2]-4,ne[e4]-4
                        ftd=facetimedirection[f][t]
                        nmed[en2],nmed[en4]=ftd[nmed[en2]],ftd[nmed[en4]]
                    
                    key2=dict21[tuple(nc+nmed)]*967680+dict22[tuple(ne)]
                    if key2 not in dict2:
                        newstep=oldstep+(3*f+3-t)*eighteen[step-1]
                        dict2[key2]=newstep+eighteen[step]
                        if step!=dict2step:
                            newpredictstate.append((nc,ne,nmed,newstep,f,f1))
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,step,len(newpredictstate),len(dict2),time.time()-t1),end="")
        predictstate=newpredictstate
        newpredictstate=[]
    print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,"total","",len(dict2),time.time()-t0),end="")

def solve(c,cd,e,ed,threadid):
    global threadsolutions,htm,qtm,minmove,verifiednum
    tstart=time.time()
    cubes=[(c,cd,e,ed,1,0,-1,-1)]
    solutionnum=0
    totalnum=1
    minstr=eighteen[stepshouldbelow]
    #phase 1
    while cubes:
        oc,ocd,oe,oed,previousstep,step,f1,f2=cubes.pop()
        step+=1
        for f in range(6):
            if step==1 or f!=f1 and not ((f1==5 and f==0 or f1==4 and f==2 or f1==3 and f==1) or (step>2 and f==f2 and (f==0 and f1==5 or f==1 and f1==3 or f==2 and f1==4))):
                m1_1=previousstep*18+3*f
                totalnum+=3
                for t in range(1,4):
                    nc=oc.copy()
                    ncd=ocd.copy()
                    ne=oe.copy()
                    ned=oed.copy()
                    rotatecubeaddress(f,t,nc,ncd,ne,ned)
                    if step<phase1maxstep:
                        cubes.append((nc,ncd,ne,ned,m1_1,step,f,f1))
                    key1=dict11[tuple([positionsimplify[ned[i]] for i in ne[:11]])]*1082565+dict12[tuple([positionsimplify[ncd[i]] for i in nc[:7]])+dict121[tuple([ne.index(i) for i in range(4,8)])]]
                    if key1 in dict1:
                        solutionnum+=1
                        m1_2=dict1[key1]
                        if m1_2!=1:
                            nc1=nc.copy()
                            ncd1=ncd.copy()
                            ne1=ne.copy()
                            ned1=ned.copy()
                            m1=m1_1
                            f0=f
                            while m1_2>=18:
                                ft=m1_2%18
                                m1=18*m1+ft
                                m1_2//=18
                                f0,t0=ft//3,ft%3+1
                                rotatecubeaddress(f0,t0,nc1,ncd1,ne1,ned1)
                            #phase 2
                            key2=dict21[tuple(nc1+ned1[4:8])]*967680+dict22[tuple(ne1)]
                            if key2 in dict2:
                                m2=dict2[key2]
                                solution=(m1-1)*eighteen[int(log(m2,18))]+m2
                                if solution<minmove:
                                    minmove=minstr=solution
                                    htm=int(log(solution,18))
                                    p2=int(log(m2,18))
                                    qtmvalue=htm
                                    numstr=decodevalue(solution)
                                    for i in range(int(len(numstr)/2)):
                                        if numstr[2*i+1]=="2":
                                            qtmvalue+=1
                                    if qtmvalue<qtm:
                                        qtm=qtmvalue
                                    print("{:<8}{:<18}{:<6}{:<24}{:<14f}1     {:<36}{}\n".format(threadid,f"{htm} = {step} + {htm-step-p2} + {p2}",qtmvalue,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution,numstr),end="")
                            if int(log(m1,18))+dict2step<=htm or key2 in dict2 and int(log(solution,18))-1<=htm:
                                rotatecubeaddress(f0,2,nc1,ncd1,ne1,ned1) 
                                key2=dict21[tuple(nc1+ned1[4:8])]*967680+dict22[tuple(ne1)]
                                if key2 in dict2:
                                    m2=dict2[key2]
                                    solution=(m1-3)*eighteen[int(log(m2,18))]+m2
                                    if solution<minmove:
                                        minmove=minstr=solution
                                        htm=int(log(solution,18))
                                        p2=int(log(m2,18))
                                        qtmvalue=htm
                                        numstr=decodevalue(solution)
                                        for i in range(int(len(numstr)/2)):
                                            if numstr[2*i+1]=="2":
                                                qtmvalue+=1
                                        if qtmvalue<qtm:
                                            qtm=qtmvalue
                                        print("{:<8}{:<18}{:<6}{:<24}{:<14f}2     {:<36}{}\n".format(threadid,f"{htm} = {step} + {htm-step-p2} + {p2}",qtmvalue,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution,numstr),end="")
                    m1_1+=1
    threadsolutions[threadid]=minstr
    verifiednum.append(solutionnum)
    print("finish thread {}    thread min htm {}    {}/{}    time {:f}s\n".format(threadid,int(log(minstr,18)),solutionnum,totalnum,time.time()-tstart),end="")

def randomcube():
    a=random.randrange(512,1024)
    randomstring=""
    for i in range(a):
        r=str(random.randrange(0,6))+str(random.randrange(1,4))
        randomstring+=r
    return randomstring

changebasetable=[[1,5,2,0,4,3],[2,1,5,3,0,4],[0,1,2,3,4,5]]
def getcubewithbase(randomstring,base):
    l=int(len(randomstring)/2)
    cubepack=(cc.copy(),ccd.copy(),ce.copy(),ced.copy())
    for i in range(l):
        f,t=changebasetable[base][int(randomstring[2*i])],int(randomstring[2*i+1])
        rotatecubeaddress(f,t,*cubepack)
    return cubepack

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

def decodevalue(n):
    s=""
    while n>=18:
        ft=n%18
        n//=18
        s=str(ft//3)+str(ft%3+1)+s
    return s
    
allrotation=["U","U2","U'","L","L2","L'","F","F2","F'","R","R2","R'","B","B2","B'","D","D2","D'"]
def rotatenumbertostring(s):
    r=""
    for i in range(int(len(s)/2)):
        r+=allrotation[3*int(s[2*i])+int(s[2*i+1])-1]
    return r

def rotatestringtonumber(s):
    r=""
    for c in s:
        if c=="2":
            r=r[:-1]+"2"
        elif c=="'" or c=="3":
            r=r[:-1]+"3"
        elif c in allrotation:
            i=allrotation.index(c)
            r+=str(i//3)+"1"
    return r

def reverserotation(s):
    r=""
    for i in range(int(len(s)/2)):
        r=s[2*i]+str(4-int(s[2*i+1]))+r
    return r

dict1={}
dict2={}
dict1step=7#8
dict2step=8#9
dict1thread=threading.Thread(target=getdict1,args=(dict1step,))
dict2thread=threading.Thread(target=getdict2,args=(dict2step,))
print("{:<8}{:<8}{:<16}{:<16}{:<16}\n".format("dict","step","cubes left","dict length","time/s"),end="")
tdictstart=time.time()
dict1thread.start()
dict2thread.start()
dict2thread.join()
dict1thread.join()
tdictend=time.time()
print("time",tdictend-tdictstart,"s")

printdictsize(dict1)
printdictsize(dict2)

htms=[]
qtms=[]
verifiednum=[]
starttime=time.time()
phase1maxstep=5#6
stepshouldbelow=phase1maxstep+dict1step+dict2step+1
miss=0
threadn=6
cubenumber=10
for i in range(cubenumber):
    t1=time.time()
    print("\n\ncube",i+1)
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    htm=stepshouldbelow
    qtm=htm*2
    minmove=eighteen[stepshouldbelow]
    
    randomstring=randomcube()
    #randomstring=rotatestringtonumber("R L U2 F U' D F2 R2 B2 L U2 F' B' U R2 D F2 U R2 U")
    print("random with",int(len(randomstring)/2),"moves")
    #print(randomstring)
    print("search depth",phase1maxstep,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
    
    unsolvedcubes=[]
    for base in range(3):
        unsolvedcubes.append(getcubewithbase(randomstring,base))
    reverserandomstring=reverserotation(randomstring)
    for base in range(3):
        unsolvedcubes.append(getcubewithbase(reverserandomstring,base))
    threadsolutions=[eighteen[stepshouldbelow]]*threadn
    
    print("start",threadn,"threads")
    print("{:<8}{:<18}{:<6}{:<24}{:<14}{:<6}{:<36}".format("thread","htm","qtm","in dict1/total","time/s","type","solution"))
    
    threads=[threading.Thread(target=solve,args=(*unsolvedcubes[t],t)) for t in range(threadn)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    '''
    #solve(*unsolvedcubes[0],0)
    for j in range(6):
        solve(*unsolvedcubes[j],j)
    '''
    print("\nfinish all threads of cube",i+1)
    print("completed phase one number",verifiednum[-threadn:])
    
    if htm>=stepshouldbelow:
        miss+=1
        print("no solution below",htm,"steps for this cube")
        print("miss rate",miss,"/",i+1)
    else:
        bestthread=0
        print("{:<8}{:<8}{}".format("thread","htm","solution"))
        for j in range(threadn):
            print("{:<8}{:<8}{:<36}{}".format(j,int(log(threadsolutions[j],18)),threadsolutions[j],decodevalue(threadsolutions[j])))
            if minmove==threadsolutions[j]:
                bestthread=j
            elif minmove>threadsolutions[j]:
                minmove=threadsolutions[j]
                htm=int(log(threadsolutions[j],18))
                bestthread=j
        
        bestrotation=decodevalue(minmove)
        htms.append(htm)
        qtms.append(qtm)
        print("\nbest solution in thread",bestthread)
        print("min htm",htm,", qtm",qtm,"solution",minmove,bestrotation,rotatenumbertostring(bestrotation))
        print("current htm results:",htms)
        print("average htm",sum(htms)/len(htms))
        print("average qtm",sum(qtms)/len(qtms))
    t2=time.time()
    print("time:",t2-t1,"s ","average time",(t2-starttime)/(i+1),time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print("estimated time for rest",cubenumber-i-1,"cubes:",(t2-starttime)*(cubenumber-i-1)/(i+1),"s")
endtime=time.time()

print("\n\ntwo phase algorithm version 11")
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("dict time",tdictend-tdictstart,"s")
print("total time",endtime-starttime,"s, average time",(endtime-starttime)/cubenumber,"s")
print("average phase 1 completed number",sum(verifiednum)/len(verifiednum),"max",max(verifiednum),"min",min(verifiednum))
print("search depth",phase1maxstep,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
print("htm",htms)
print("qtm",qtms)
if len(htms)>0:
    print("htm average",sum(htms)/len(htms),"range",min(htms),"-",max(htms))
    print("qtm average",sum(qtms)/len(qtms),"range",min(qtms),"-",max(qtms))
    print("\nmove  number")
    for i in range(min(htms),max(htms)+1):
        print(i,"  ",htms.count(i))
if miss!=0:
    print("there are",miss,"of",cubenumber,"cubes has no solution under this search depth")

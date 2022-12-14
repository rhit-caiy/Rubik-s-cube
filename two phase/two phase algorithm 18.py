import time
from random import randint
from math import log
from itertools import permutations,product,combinations
from multiprocessing import Process,Pool,Manager,Lock#,Value,Array
eighteen=[18**i for i in range(28)]

def getdicts():
    cc=(0,1,2,3,4,5,6,7)
    cco=(0,0,0,0,3,3,3,3)
    ce=(0,1,2,3,4,5,6,7,8,9,10,11)
    ceo=(0,0,0,0,1,1,4,4,3,3,3,3)
    facetimecorner=[[(2,3,1,0),(3,1,0,2),(1,0,2,3)],[(6,4,2,0),(4,2,0,6),(2,0,6,4)],[(4,5,3,2),(5,3,2,4),(3,2,4,5)],[(6,7,5,4),(7,5,4,6),(5,4,6,7)],[(5,7,1,3),(7,1,3,5),(1,3,5,7)],[(7,6,0,1),(6,0,1,7),(0,1,7,6)]]
    facetimeedge=[[(1,2,3,0),(2,3,0,1),(3,0,1,2)],[(4,9,5,1),(9,5,1,4),(5,1,4,9)],[(5,10,6,2),(10,6,2,5),(6,2,5,10)],[(9,8,11,10),(8,11,10,9),(11,10,9,8)],[(6,11,7,3),(11,7,3,6),(7,3,6,11)],[(7,8,4,0),(8,4,0,7),(4,0,7,8)]]
    facecorner=[(0,2,3,1),(0,6,4,2),(2,4,5,3),(4,6,7,5),(3,5,7,1),(1,7,6,0)]
    faceedge=[(0,1,2,3),(1,4,9,5),(2,5,10,6),(10,9,8,11),(3,6,11,7),(0,7,8,4)]
    facetimedirection=[[[0,5,1,3,2,4],[0,4,5,3,1,2],[0,2,4,3,5,1]],[[2,1,3,5,4,0],[3,1,5,0,4,2],[5,1,0,2,4,3]],[[4,0,2,1,3,5],[3,4,2,0,1,5],[1,3,2,4,0,5]],[[0,2,4,3,5,1],[0,4,5,3,1,2],[0,5,1,3,2,4]],[[5,1,0,2,4,3],[3,1,5,0,4,2],[2,1,3,5,4,0]],[[1,3,2,4,0,5],[3,4,2,0,1,5],[4,0,2,1,3,5]]]
    cornerdirection=[(0,5,1),(0,4,5),(0,1,2),(0,2,4),(3,2,1),(3,4,2),(3,1,5),(3,5,4)]
    edgedirection=[(0,5),(0,1),(0,2),(0,4),(1,5),(1,2),(4,2),(4,5),(3,5),(3,1),(3,2),(3,4)]
    cdict,codict,ep4dict,eodict={},{},{},{}
    #cdict, (0,1,2,3,4,5,6,7),(0,1,2,3,4,5,7,6) 40320 8!
    n=0
    for i in permutations(range(8)):
        cdict[i]=n
        n+=1
    #codict, (0,0,0,0,5,5,5,5),(0,0,0,0,5,5,4,4) 2187 3**7
    n=0
    for i in product(range(3),repeat=8):
        if sum(i)%3==0:
            codict[tuple([cornerdirection[j][i[j]] for j in range(8)])]=n
            n+=1
    #ep4dict,up edge,middle edge,bottom edge, (0,1,2,3),(0,1,2,11),(0,1,3,2) 11880 P(12,4)
    n=0
    for i in combinations(range(12),r=4):
        for j in permutations(i):
            ep4dict[j]=n
            n+=1
    #eodict, (0,0,0,0,1,1,3,3,5,5,5,5),(0,0,0,0,1,1,3,3,5,5,2,3) 2048 2**11
    n=0
    for i in product(range(2),repeat=12):
        if sum(i)%2==0:
            eodict[tuple([edgedirection[j][i[j]] for j in range(12)])]=n
            n+=1
    cr,cor,ep4r,eor=[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)],[[{},{},{}] for i in range(6)]
    for f in range(6):
        c1,c2,c3,c4=facecorner[f]
        e1,e2,e3,e4=fe=faceedge[f]
        sfe=set(fe)
        for t in range(3):
            nc1,nc2,nc3,nc4=facetimecorner[f][t]
            ne1,ne2,ne3,ne4=fte=facetimeedge[f][t]
            ftd=facetimedirection[f][t]
            
            d=cr[f][t]
            for dc in cdict:
                c=list(dc)
                c[c1],c[c2],c[c3],c[c4]=c[nc1],c[nc2],c[nc3],c[nc4]
                d[cdict[dc]]=cdict[tuple(c)]
            d=cor[f][t]
            for dco in codict:
                co=list(dco)
                co[c1],co[c2],co[c3],co[c4]=ftd[co[nc1]],ftd[co[nc2]],ftd[co[nc3]],ftd[co[nc4]]
                d[codict[dco]]=codict[tuple(co)]
            d=ep4r[f][t]
            for dep in ep4dict:
                ep=list(dep)
                for i in [0,1,2,3]:
                    if ep[i] in sfe:
                        ep[i]=fe[fte.index(ep[i])]
                d[ep4dict[dep]]=ep4dict[tuple(ep)]
            d=eor[f][t]
            for deo in eodict:
                eo=list(deo)
                eo[e1],eo[e2],eo[e3],eo[e4]=ftd[eo[ne1]],ftd[eo[ne2]],ftd[eo[ne3]],ftd[eo[ne4]]
                d[eodict[deo]]=eodict[tuple(eo)]
    ccn,ccon,cen1,cen2,cen3,ceon=cdict[cc],codict[cco],ep4dict[ce[0:4]],ep4dict[ce[4:8]],ep4dict[ce[8:12]],eodict[ceo]
    cr0,cor0,eor0,ep4r0,cr1,ep4r1=[i[0] for i in cr],[i[0] for i in cor],[i[0] for i in eor],[i[0] for i in ep4r],[i[1] for i in cr],[i[1] for i in ep4r]
    return cdict,codict,ep4dict,eodict,cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1

t1=time.time()
cdict,codict,ep4dict,eodict,cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1=getdicts()
tinit=time.time()-t1
print("initial time",tinit,"s")

dict1step=7#8
dict2step=8#9
phase1maxstep=5#6
stepshouldbelow=phase1maxstep+dict1step+dict2step+1

def decodevalue(n):
    s=""
    while n>=18:
        ft=n%18
        n//=18
        s=str(ft//3)+str(ft%3)+s
    return s

def solve(c,co,eo,e1,e2,e3,solveid,htm,qtm,minmove,dict1,dict2):#,cdict,codict,ep4dict,eodict,cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1):
    #print(id(dict1),id(dict2),len(dict1),len(dict2))
    tstart=time.time()
    cubes=[(c,co,eo,e1,e2,e3,1,0,-1)]
    solutionnum=0
    totalnum=1
    #phase 1
    while cubes:
        oc,oco,oeo,oe1,oe2,oe3,previousstep,step,f1=cubes.pop()
        step+=1
        for f in [0,1,2,3,4,5]:
            if f!=f1 and f1-f!=3:
                m1_1=previousstep*18+3*f
                totalnum+=3
                crf0,corf0,eorf0,ep4rf0=cr0[f],cor0[f],eor0[f],ep4r0[f]
                nc,nco,neo,ne1,ne2,ne3=oc,oco,oeo,oe1,oe2,oe3
                for t in [0,0,0]:
                    nc,nco,neo,ne1,ne2,ne3=crf0[nc],corf0[nco],eorf0[neo],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                    if step<phase1maxstep:
                        cubes.append((nc,nco,neo,ne1,ne2,ne3,m1_1,step,f))
                    key1=(nco*2048+neo)*495+ne2//24
                    if key1 in dict1:
                        solutionnum+=1
                        m1_2=dict1[key1]
                        if m1_2!=1:
                            nc1,ne11,ne21,ne31=nc,ne1,ne2,ne3
                            m1=m1_1
                            f0=f
                            while m1_2>=18:
                                f0,t0=(m1_2//3)%6,m1_2%3
                                m1=18*m1+m1_2%18
                                m1_2//=18
                                ep4rf0t0=ep4r[f0][t0]
                                nc1,ne11,ne21,ne31=cr[f0][t0][nc1],ep4rf0t0[ne11],ep4rf0t0[ne21],ep4rf0t0[ne31]
                            #phase 2
                            key2=((nc1*11880+ne11)*11880+ne21)*11880+ne31
                            if key2 in dict2:
                                m2=dict2[key2]
                                solution=(m1-1)*eighteen[int(log(m2,18))]+m2
                                if solution<minmove.value:
                                    minmove.value=solution
                                    qtmvalue=htm.value=int(log(solution,18))
                                    p2=int(log(m2,18))
                                    numstr=decodevalue(solution)
                                    for i in range(int(len(numstr)/2)):
                                        if numstr[2*i+1]=="1":
                                            qtmvalue+=1
                                    if qtmvalue<qtm.value:
                                        qtm.value=qtmvalue
                                    print("{:<8}{:<18}{:<6}{:<24}{:<14f}1     {:<36}{}\n".format(solveid,f"{htm.value} = {step} + {htm.value-step-p2} + {p2}",qtmvalue,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution,numstr),end="")
                                if solution<eighteen[htm.value+1]:
                                    ep4rf01=ep4r1[f0]
                                    nc1,ne11,ne21,ne31=cr1[f0][nc1],ep4rf01[ne11],ep4rf01[ne21],ep4rf01[ne31]
                                    key2=((nc1*11880+ne11)*11880+ne21)*11880+ne31
                                    if key2 in dict2:
                                        m2=dict2[key2]
                                        solution=(m1-3)*eighteen[int(log(m2,18))]+m2
                                        if solution<minmove.value:
                                            minmove.value=solution
                                            qtmvalue=htm.value=int(log(solution,18))
                                            p2=int(log(m2,18))
                                            numstr=decodevalue(solution)
                                            for i in range(int(len(numstr)/2)):
                                                if numstr[2*i+1]=="1":
                                                    qtmvalue+=1
                                            if qtmvalue<qtm.value:
                                                qtm.value=qtmvalue
                                            print("{:<8}{:<18}{:<6}{:<24}{:<14f}2     {:<36}{}\n".format(solveid,f"{htm.value} = {step} + {htm.value-step-p2} + {p2}",qtmvalue,str(solutionnum)+"/"+str(totalnum),time.time()-tstart,solution,numstr),end="")
                    m1_1+=1
    print("finish thread {}    current min htm {}    {}/{}    time {:f}s\n".format(solveid,int(log(minmove.value,18)),solutionnum,totalnum,time.time()-tstart),end="")
    #return htm,qtm,minmove,solutionnum

if __name__=="__main__":
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    
    def getdict1(dict1step):
        dict1={}
        predictstate=[(ccon,ceon,cen2,1,-1)]
        newpredictstate=[]
        dict1[(ccon*2048+ceon)*495+cen2//24]=1
        t0=time.time()
        for step in range(1,dict1step+1):
            t1=time.time()
            for cube in predictstate:
                oco,oeo,oe2,oldstep,f1=cube
                for f in [0,1,2,3,4,5]:
                    if f1!=f and f1-f!=3:
                        newstep=oldstep*18+3*f+2
                        nco,neo,ne2=oco,oeo,oe2
                        corf0,eorf0,ep4rf0=cor0[f],eor0[f],ep4r0[f]
                        for t in [0,0,0]:
                            nco,neo,ne2=corf0[nco],eorf0[neo],ep4rf0[ne2]
                            key1=(nco*2048+neo)*495+ne2//24
                            if key1 not in dict1:
                                dict1[key1]=newstep
                                if step!=dict1step:
                                    newpredictstate.append((nco,neo,ne2,newstep,f))
                            newstep-=1
            print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,step,len(newpredictstate),len(dict1),time.time()-t1),end="")
            predictstate,newpredictstate=newpredictstate,[]
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(1,"total","",len(dict1),time.time()-t0),end="")
        return dict1

    def getdict2(dict2step):
        dict2={}
        predictstate=[(ccn,cen1,cen2,cen3,0,-1)]
        newpredictstate=[]
        dict2[((ccn*11880+cen1)*11880+cen2)*11880+cen3]=1
        t0=time.time()
        for step in range(1,dict2step+1):
            t1=time.time()
            for cube in predictstate:
                oc,oe1,oe2,oe3,oldstep,f1=cube
                for f in [0,3]:
                    if f1!=f and (f1!=3 or f!=3):
                        crf0,ep4rf0=cr0[f],ep4r0[f]
                        nc,ne1,ne2,ne3=oc,oe1,oe2,oe3
                        for t in [2,1,0]:
                            nc,ne1,ne2,ne3=crf0[nc],ep4rf0[ne1],ep4rf0[ne2],ep4rf0[ne3]
                            key2=((nc*11880+ne1)*11880+ne2)*11880+ne3
                            if key2 not in dict2:
                                newstep=oldstep+(3*f+t)*eighteen[step-1]
                                dict2[key2]=newstep+eighteen[step]
                                if step!=dict2step:
                                    newpredictstate.append((nc,ne1,ne2,ne3,newstep,f))
                for f in [1,2,4,5]:
                    if f1!=f and f1-f!=3:
                        ep4rf1=ep4r1[f]
                        nc,ne1,ne2,ne3=cr1[f][oc],ep4rf1[oe1],ep4rf1[oe2],ep4rf1[oe3]
                        key2=((nc*11880+ne1)*11880+ne2)*11880+ne3
                        if key2 not in dict2:
                            newstep=oldstep+(3*f+1)*eighteen[step-1]
                            dict2[key2]=newstep+eighteen[step]
                            if step!=dict2step:
                                newpredictstate.append((nc,ne1,ne2,ne3,newstep,f))
            print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,step,len(newpredictstate),len(dict2),time.time()-t1),end="")
            predictstate,newpredictstate=newpredictstate,[]
        print("{:<8}{:<8}{:<16}{:<16}{:<16f}\n".format(2,"total","",len(dict2),time.time()-t0),end="")
        return dict2

    def randomcube():
        a=randint(512,1024)
        randomstring=""
        reverserandomstring=""
        for i in range(a):
            f=randint(0,5)
            t=randint(0,2)
            randomstring+=str(f)+str(t)
            reverserandomstring=str(f)+str(2-t)+reverserandomstring
        return randomstring,reverserandomstring

    def getcubewithbase(randomstring,base):
        direction=[[0,1,2,3,4,5],[1,2,0,4,5,3],[2,0,1,5,3,4]][base]
        l=int(len(randomstring)/2)
        c,co,eo,e1,e2,e3=ccn,ccon,ceon,cen1,cen2,cen3
        for i in range(l):
            f,t=direction[int(randomstring[2*i])],int(randomstring[2*i+1])
            ep4rft=ep4r[f][t]
            c,co,eo,e1,e2,e3=cr[f][t][c],cor[f][t][co],eor[f][t][eo],ep4rft[e1],ep4rft[e2],ep4rft[e3]
        return c,co,eo,e1,e2,e3
        '''
    def decodevalue(n):
        s=""
        while n>=18:
            ft=n%18
            n//=18
            s=str(ft//3)+str(ft%3)+s
        return s
        '''
    def rotatenumbertostring(s):
        allrotation=["U","U2","U'","L","L2","L'","F","F2","F'","D","D2","D'","R","R2","R'","B","B2","B'"]
        r=""
        for i in range(int(len(s)/2)):
            r+=allrotation[3*int(s[2*i])+int(s[2*i+1])]
        return r
    '''
    def rotatestringtonumber(s):
        allrotation=["U","U2","U'","L","L2","L'","F","F2","F'","D","D2","D'","R","R2","R'","B","B2","B'"]
        r=""
        for c in s:
            if c=="2":
                r=r[:-1]+"1"
            elif c=="'" or c=="3":
                r=r[:-1]+"2"
            elif c in allrotation:
                i=allrotation.index(c)
                r+=str(i//3)+"0"
        return r

    def printdictsize(d):
        t=time.time()
        a=getsizeof(d)
        b=0
        for i in d:
            b+=getsizeof(i)
        for i in d.values():
            b+=getsizeof(i)
        print([name for name in globals() if globals()[name] is d][0],len(d),"dict space",a,"B    values and keys space",b,"B    total",(a+b)/2**30,"GB ",(a+b)/2**20,"MB ",time.time()-t,"s")
    '''
    
    manager=Manager()
    print("{} + {}\n{:<8}{:<8}{:<16}{:<16}{:<16}\n".format(dict1step,dict2step,"dict","step","cubes left","dict length","time/s"),end="")
    tdict0=time.time()
    dict1=manager.dict(getdict1(dict1step))
    tdict1=time.time()
    dict2=manager.dict(getdict2(dict2step))
    tdict2=time.time()
    print(f"dicts time {tdict2-tdict0}s = {tdict1-tdict0}s + {tdict2-tdict1}s")
    #printdictsize(dict1)
    #printdictsize(dict2)
    
    htms,qtms=[],[]
    #verifiednum=[]
    times=[]
    
    miss=0
    threadn=6
    cubenumber=2

    starttime=time.time()
    for i in range(cubenumber):
        print("\n\ncube",i+1)
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        print("search depth",phase1maxstep,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
        # htm=stepshouldbelow
        # qtm=htm*2
        # minmove=eighteen[stepshouldbelow]
        htm=manager.Value("i",stepshouldbelow)
        qtm=manager.Value("i",stepshouldbelow*2)
        minmove=manager.Value("i",eighteen[stepshouldbelow])
        
        randomstring,reverserandomstring=randomcube()
        print("random with",int(len(randomstring)/2),"moves")
        unsolvedcubes=[]
        for base in range(3):
            unsolvedcubes.append(getcubewithbase(randomstring,base))
        for base in range(3):
            unsolvedcubes.append(getcubewithbase(reverserandomstring,base))
        threadsolutions=[eighteen[stepshouldbelow]]*threadn
        print("{:<8}{:<18}{:<6}{:<24}{:<14}{:<6}{:<36}".format("thread","htm","qtm","in dict1/total","time/s","type","solution"))
        '''
        t1=time.time()
        processes=[Process(target=solve,args=(*unsolvedcubes[p],p,htm,qtm,minmove,dict1,dict2,cdict,codict,ep4dict,eodict,cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1)) for p in range(threadn)]
        print("start")
        [p.start() for p in processes]
        print("start all")
        [p.join() for p in processes]
        print("end")
        '''
        po=Pool(threadn)
        t1=time.time()
        for p in range(threadn):
            po.apply_async(solve,args=(*unsolvedcubes[p],p,htm,qtm,minmove,dict1,dict2))#,cdict,codict,ep4dict,eodict,cr,cor,ep4r,eor,ccn,ccon,cen1,cen2,cen3,ceon,cr0,cor0,eor0,ep4r0,cr1,ep4r1))
        po.close()
        po.join()
        
        '''
        for j in range(threadn):
            htm,qtm,minmove,solutionnum=solve(*unsolvedcubes[j],j,htm,qtm,minmove)
            threadsolutions[j]=minmove
            verifiednum.append(solutionnum)
            '''
        t2=time.time()
        times.append(t2-t1)
        print("\nfinish all threads of cube",i+1)
        #print("completed phase one number",verifiednum[-threadn:],sum(verifiednum[-threadn:]))
        
        if htm.value>=stepshouldbelow:
            miss+=1
            print("no solution below",htm.value,"steps for this cube")
            print("miss rate",miss,"/",i+1)
        else:
            print("{:<8}{:<8}{}".format("thread","htm","solution"))
            for j in range(threadn):
                print("{:<8}{:<8}{:<36}{}".format(j,int(log(threadsolutions[j],18)),threadsolutions[j],decodevalue(threadsolutions[j])))
            
            htms.append(htm.value)
            qtms.append(qtm.value)
            print("\nmin htm",htm.value,", qtm",qtm.value,"solution",minmove.value,decodevalue(minmove.value),rotatenumbertostring(decodevalue(minmove.value)))
            if i<100:
                print("current htm results:",htms)
            print("average htm",sum(htms)/len(htms))
            print("average qtm",sum(qtms)/len(qtms))
        print("time:",t2-t1,"s ","average time",sum(times)/(i+1),time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        print("estimated time for rest",cubenumber-i-1,"cubes:",(t2-starttime)*(cubenumber-i-1)/(i+1),"s")
    endtime=time.time()

    print("\n\ntwo phase algorithm version 18")
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print("initial time",tinit,"s")
    print(f"dicts time {tdict2-tdict0}s = {tdict1-tdict0}s + {tdict2-tdict1}s")
    print(f"total time {endtime-starttime}s, actual time {sum(times)}s, average time {sum(times)/cubenumber}s")
    #print("average phase 1 completed number per thread",sum(verifiednum)/len(verifiednum),"max",max(verifiednum),"min",min(verifiednum))
    print("search depth",phase1maxstep,"+",dict1step,"+",dict2step,"=",stepshouldbelow-1)
    if cubenumber<=100:
        print("htm",htms)
        print("qtm",qtms)
    print(cubenumber,"cubes")
    if len(htms)>0:
        print("htm average",sum(htms)/len(htms),"range",min(htms),"-",max(htms))
        print("qtm average",sum(qtms)/len(qtms),"range",min(qtms),"-",max(qtms))
        print("\nhtm     number")
        for i in range(min(htms),max(htms)+1):
            print("{:<8}{:<8}{}".format(i,htms.count(i),"-"*int(100*htms.count(i)/cubenumber)))
        print("\nqtm     number")
        for i in range(min(qtms),max(qtms)+1):
            print("{:<8}{:<8}{}".format(i,qtms.count(i),"-"*int(100*qtms.count(i)/cubenumber)))
    if miss!=0:
        print("there are",miss,"of",cubenumber,"cubes has no solution under this search depth")

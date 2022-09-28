rotates=["U","L","F","R","B","D","M","E","S","x","y","z"]
adj=[[4,3,2,1],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[1,2,3,4]]
center=[0,1,2,3,4,5]
def flatten(s):
    s=s.replace("2","-")
    s=s.replace("'","--")
    s2=""
    for i in range(len(s)):
        if s[i]=="-":
            s2=s2+s2[-1]
        else:
            s2=s2+s[i]
    
    return s2
def replacemiddle(s):
    s=s.replace("M","RLLLxxx")
    s=s.replace("E","UDDDyyy")
    s=s.replace("S","BFFFz")
    return s
def decode(s):
    global center
    s2=""
    newcenter=center.copy()
    for i in s:
        n=rotates.index(i)
        if n<6:
            s2+=str(center[n])
        elif n>=9:
            #RUF
            rotatecube=[3,0,2]
            n-=9
            for j in range(4):
                newcenter[adj[rotatecube[n]][(j+1)%4]]=center[adj[rotatecube[n]][j]]
            center=newcenter.copy()
    return s2

#0,5  1,3  2,4
def group(s):
    anti=[[0,5],[1,3],[2,4]]
    g=[]
    m=0
    n=0
    for i in s:
        i=int(i)
        if i in anti[0]:
            n=0
        elif i in anti[1]:
            n=1
        elif i in anti[2]:
            n=2
        m=anti[n].index(i)
        if g==[]:
            g=[[n,0,0]]
        if g[-1][0]!=n:
            g.append([n,0,0])
        g[-1][m+1]+=1
    for i in g:
        i[1]%=4
        i[2]%=4
    g=[i for i in g if not (i[1]==0 and i[2]==0)]
    return g

def stm(g):
    global compressedstep
    anti=[[0,5],[1,3],[2,4]]
    allrotation=[["U","U2","U'"],["L","L2","L'"],["F","F2","F'"],["R","R2","R'"],["B","B2","B'"],["D","D2","D'"]]
    middlerotation=[["Ey","E2y2","E'y'"],["M'x'","M2x2","Mx"],["S'z","S2z2","Sz'"]]
    s=""
    totalstm=0
    for i in g:
        a=i[1]
        b=i[2]
        if a==4-b:
            s+=middlerotation[i[0]][a-1]
            totalstm+=1
        elif a==0:
            s+=allrotation[anti[i[0]][1]][b-1]
            totalstm+=1
        elif b==0:
            s+=allrotation[anti[i[0]][0]][a-1]
            totalstm+=1
        else:
            s+=allrotation[anti[i[0]][0]][a-1]+allrotation[anti[i[0]][1]][b-1]
            totalstm+=2
    #print("total stm step",totalstm)
    compressedstep=totalstm
    return s
'''
rotationstring="BRSSFUMDMBMRMBBBRDEFMEDUFRMRSSFFBSBUERBBMSSEEMELMELMLFMRULMEEERSBFMSDLBRMEFBUFFDURESUFBDBMUBUDMFBLx2yyF2RD2FR'DyyyyyyyyyyyUR'F'RURU'R'FyyyyyyyyyyyyyyyyyRUR'yyyyyyyyyyyyyyyyRUR'yyyyyyyyyyyyyyyyyRUR'yyyyyU'F'U2FUF'U'FyyUF'U'FU2F'UFyU'UF'U'FU2F'UFyyyyyyyyyyyyyyyyR'FRUR'U'F'URyyyyRUR'U'R'FR2U'R'U'RUR'F'yyy"
print("original:",rotationstring)
d=flatten(rotationstring)
print("flattened:",d)
d=replacemiddle(d)
print("eliminate middle rotation:",d)
d=decode(d)
print("decoded numeric:",d)
g=group(d)
print("group antithesis:",g)
#different step method and decode method
s=stm(g)
print("stm rotation:",s)
'''
def compress(s):
    return stm(group(decode(replacemiddle(flatten(s)))))
compressedstep=0
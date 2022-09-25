import random,time
cube=[[i+1]*9 for i in range(6)]

color=["","#FFFF00","#0000FF","#FF0000","#00FF00","#FF8000","#FFFFFF"]
rotates=["U","L","F","R","B","D","M","E","S","x","y","z"]
adj=[[4,3,2,1],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[1,2,3,4]]
edge=[[[2,1,0],[2,1,0],[2,1,0],[2,1,0]],
      [[0,3,6],[0,3,6],[0,3,6],[8,5,2]],
      [[6,7,8],[0,3,6],[2,1,0],[8,5,2]],
      [[8,5,2],[0,3,6],[8,5,2],[8,5,2]],
      [[2,1,0],[0,3,6],[6,7,8],[8,5,2]],
      [[6,7,8],[6,7,8],[6,7,8],[6,7,8]]]
middle=[[[1,4,7],[1,4,7],[1,4,7],[7,4,1]],
        [[3,4,5],[3,4,5],[3,4,5],[3,4,5]],
        [[3,4,5],[1,4,7],[5,4,3],[7,4,1]]]
totalstep=0

def rotate(a,b):
    rotateface(a,b)
    rotateedge(a,b)
    
def rotateface(a,b):
    global cube
    cube1=copy()
    c=[6,3,0,7,4,1,8,5,2]
    if b==1:
        for i in range(9):
            cube1[a][i]=cube[a][c[i]]
    else:
        for i in range(9):
            cube1[a][c[i]]=cube[a][i]
    cube=cube1

def rotateedge(a,b):
    global cube
    newcube=copy()
    l=edge[a]
    if b==1:
        for i in range(4):
            for j in range(3):
                newcube[adj[a][i]][l[i][j]]=cube[adj[a][(i-1)%4]][l[(i-1)%4][j]]
    else:
        for i in range(4):
            for j in range(3):
                newcube[adj[a][(i-1)%4]][l[(i-1)%4][j]]=cube[adj[a][i]][l[i][j]]
    cube=newcube
    
def rotatemiddle(a,b):
    global cube
    newcube=copy()#ldf
    l=middle[a]
    facenum=0
    if a==0:
        facenum=1
    elif a==1:
        facenum=5
    else:
        facenum=2
    if b==1:
        for i in range(4):
            for j in range(3):
                newcube[adj[facenum][i]][l[i][j]]=cube[adj[facenum][(i-1)%4]][l[(i-1)%4][j]]
    else:
        for i in range(4):
            for j in range(3):
                newcube[adj[facenum][(i-1)%4]][l[(i-1)%4][j]]=cube[adj[facenum][i]][l[i][j]]
    cube=newcube

def rotatecube(a,b):
    if a==0:
        rotate(1,1-b)
        rotate(3,b)
        rotatemiddle(0,1-b)
    if a==1:
        rotate(0,b)
        rotate(5,1-b)
        rotatemiddle(1,1-b)
    if a==2:
        rotate(2,b)
        rotate(4,1-b)
        rotatemiddle(2,b)
    
def copy():
    cube1=[[0 for i in range(9)] for j in range(6)]
    for i in range(6):
        for j in range(9):
            cube1[i][j]=cube[i][j]
    return cube1

def randomcube():
    global cube
    cube=[[i+1]*9 for i in range(6)]
    a=random.randrange(21,51)
    b=random.randrange(0,10)
    for i in range(a):
        r=random.randrange(0,12)
        rotate(r%6,1-r//6)
    for i in range(b):
        r=random.randrange(0,6)
        rotatecube(r%3,1-r//3)

def do(s):
    global totalstep
    l=len(s)
    i=0
    while i<l:
        a=rotates.index(s[i])
        if 0<=a<=5:
            rotate(a,1)
            totalstep+=1
        elif 6<=a<=8:
            rotatemiddle(a-6,1)
            totalstep+=1
        elif 9<=a<=11:
            rotatecube(a-9,1)
        i+=1
        if i<l:
            if s[i]=="'":
                i+=1
                if 0<=a<=5:
                    rotate(a,1)
                    rotate(a,1)
                elif 6<=a<=8:
                    rotatemiddle(a-6,1)
                    rotatemiddle(a-6,1)
                elif 9<=a<=11:
                    rotatecube(a-9,1)
                    rotatecube(a-9,1)
            elif s[i]=='2':
                i+=1
                if 0<=a<=5:
                    rotate(a,1)
                elif 6<=a<=8:
                    rotatemiddle(a-6,1)
                elif 9<=a<=11:
                    rotatecube(a-9,1)

def solve():
    global totalstep
    totalstep=0
    step1()
    step2()
    step3()
    step4()
    step5()
    step6()
    step7()
    step8()
    step9()
    
def step1():
    if cube[5][4]!=6:
        if cube[0][4]==6:
            do("x2")
        elif cube[1][4]==6:
            do("z'")
        elif cube[2][4]==6:
            do("x'")
        elif cube[3][4]==6:
            do("z")
        elif cube[4][4]==6:
            do("x")
            
def step2():
    n=0
    for i in range(4):
        if cube[0][2*i+1]==6:
            n+=1
    tt=time.time()
    while n<4:
        if cube[2][3]==6:
            while cube[0][3]==6:
                do("U")
            do("L'")
        if cube[2][5]==6:
            while cube[0][5]==6:
                do("U")
            do("R")
        if cube[5][1]==6:
            while cube[0][7]==6:
                do("U")
            do("F2")
        if cube[2][1]==6:
            do("FU'R")
        if cube[2][7]==6:
            while cube[0][5]==6:
                do("U")
            do("F'RF")
        do("y")
        n=0
        tt1=time.time()
        if tt1-tt>2:
            print("error",cube)
            break
        for i in range(4):
            if cube[0][2*i+1]==6:
                n+=1
    
def step3():
    '''
    while cube[2][4]!=3:
        do("y")'''
    for i in range(4):
        for j in range(4):
            if cube[2][1]==cube[2][4] and cube[0][7]==6:
                do("F2")
                break
            do("U")
        do("y")
def step4():
    for i in range(4):
        for j in range(4):
            for k in range(6):
                do("RUR'U'")
                if cube[5][2]==6 and cube[2][8]==cube[2][7]:
                    break
            do("U")
            if cube[5][2]!=6 or cube[2][8]!=cube[2][7]:
                color=cube[2][4]
                for k in range(3):
                    do("y")
                    if cube[2][8]==color and cube[5][2]==6 or cube[5][2]==color and cube[3][6]==6 or cube[3][6]==color and cube[2][8]==6:
                        do("RUR'")
                do("y")
                for k in range(6):
                    do("RUR'U'")
                    if cube[5][2]==6 and cube[2][8]==cube[2][7]:
                        break
        do("y")
def step5():
    for i in range(16):
        for j in range(4):
            if cube[2][1]==cube[2][4]:
                if cube[0][7]==cube[1][4]:
                    do("F'L'FUFU'F'L")
                elif cube[0][7]==cube[3][4]:
                    do("FRF'U'F'UFR'")
            do("U")
        do("y")
    for i in range(4):
        if cube[2][5]==cube[3][4] and cube[3][3]==cube[2][4]:
            do("RU'R'Uy'R'U2RU2R'UR")
        else:
            do("y")
    for i in range(16):
        if cube[1][5]!=cube[1][4] or cube[2][3]!=cube[2][4]:
            do("F'L'FUFU'F'L")
            for j in range(4):
                for k in range(4):
                    if cube[2][1]==cube[2][4]:
                        if cube[0][7]==cube[1][4]:
                            do("F'L'FUFU'F'L")
                        elif cube[0][7]==cube[3][4]:
                            do("FRF'U'F'UFR'")
                    do("U")
                do("y")
        do("y")
    
def step6():
    n=0
    for i in range(4):
        if cube[0][2*i+1]==1:
            n+=1
    while n<4:
        if n==0:
            do("FRUR'U'F'y2FURU'R'F'")
        else:
            if cube[0][1]==1 and cube[0][7]==1:
                do("U")
            if cube[0][3]==1 and cube[0][5]==1:
                do("FRUR'U'F'")
            else:
                while cube[0][1]!=1 or cube[0][3]!=1:
                    do("U")
                do("FURU'R'F'")
        for i in range(4):
            if cube[0][2*i+1]==1:
                n+=1
def step7():
    n=0
    for i in [0,2,6,8]:
        if cube[0][i]==1:
            n+=1
    while n<4:
        if n==0:
            while (cube[2][0]!=1 or cube[2][2]!=1):
                do("U")
            if cube[4][2]==1:
                do("FRUR'U'RUR'U'RUR'U'F'")
            else:
                do("URU2R2U'R2U'R2U2R")
        elif n==1:
            while cube[0][6]!=1:
                do("U")
            if cube[2][2]==1:
                do("RUR'URU2R'")
            else:
                do("U'L'U'LU'L'U2L")
        else:
            while cube[2][0]!=1:
                do("U")
            do("RUR'URU2R'")
        n=0
        for i in [0,2,6,8]:
            if cube[0][i]==1:
                n+=1
    
def step8():
    n=0
    for i in range(1,5):
        if cube[i][0]==cube[i][2]:
            n+=1
    while n<4:
        if n==0:
            do("R'UL'U2RU'R'U2LR")
        elif n==1:
            while cube[2][0]!=cube[2][2]:
                do("U")
            do("R'UL'U2RU'R'U2LR")
        n=0
        for i in range(1,5):
            if cube[i][0]==cube[i][2]:
                n+=1
def step9():
    while cube[2][4]!=3:
        do("y")
    while cube[2][0]!=cube[2][4]:
        do("U")
    n=0
    for i in range(1,5):
        if cube[i][1]==cube[i][4]:
            n+=1
    if n==0:
        if cube[2][1]==cube[1][4]:
            do("UM2UM2UM'U2M2U2M'U2")
        elif cube[2][1]==cube[3][4]:
            do("M2UM2UM'U2M2U2M'U2")
        else:
            do("M2UM2U2M2UM2")
    elif n==1:
        while cube[4][1]!=cube[4][0]:
            do("U")
        if cube[2][1]==cube[1][2]:
            do("RRURUR'U'R'U'R'UR'")
        else:
            do("L'L'U'L'U'LULULU'L")
    while cube[2][1]!=cube[2][4]:
        do("U")

start=time.time()
timerandom=0
timesolve=0
totalsteps=0
number=10000
for cubes in range(number):
    if cubes%1000==0 and cubes!=0:
        print(cubes,timerandom,timesolve,totalsteps/cubes)
    t1=time.time()
    randomcube()
    t2=time.time()
    solve()
    t3=time.time()
    timerandom+=t2-t1
    timesolve+=t3-t2
    totalsteps+=totalstep
end=time.time()
print("total",number)
print("average steps:",totalsteps/number)
print("total time",end-start)
print("time per solve:",(end-start)/number)
print("total random",timerandom,"solve",timesolve)
print("average random",timerandom/number,"solve",timesolve/number)
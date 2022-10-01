from tkinter import Tk,Canvas
import random,time
window=Tk()
canvas=Canvas(window,bg="#808080",width=1300,height=650)
window.title("2x2x2 cube")

block=[0,1,2,3,4,5,6]
blockd=[0,0,0,5,5,5,5]
#only front right down rotation,fix upper back left block
faceblock=[[1,2,4,3],[2,0,6,4],[3,4,6,5]]
rotates=["F","R","D"]
allrotation=[["F","F2","F'"],["R","R2","R'"],["D","D2","D'"]]
blockposition=[[[0,1],[4,0],[3,1]],[[0,2],[2,0],[1,1]],[[0,3],[3,0],[2,1]],
                [[5,0],[1,3],[2,2]],[[5,1],[2,3],[3,2]],[[5,2],[4,3],[1,2]],[[5,3],[3,3],[4,2]]]
cube=[[i]*4 for i in range(6)]
adj=[[0,3,5,1],[0,4,5,2],[1,2,3,4]]#adjacent face of front, right, down
facerotate=[2,3,5]

color=["#FFFF00","#0000FF","#FF0000","#00FF00","#FF8000","#FFFFFF"]

def start():
    draw()
    display()
def draw():
    canvas.create_rectangle(50,500,150,550,fill="#C0C0C0")
    canvas.create_text(100,525,text="reset")
    canvas.create_rectangle(200,500,300,550,fill="#C0C0C0")
    canvas.create_text(250,525,text="random")
    canvas.create_rectangle(50,560,150,610,fill="#C0C0C0")
    canvas.create_text(100,585,text="solve")
    canvas.create_rectangle(200,560,300,610,fill="#C0C0C0")
    canvas.create_text(250,585,text="random and solve")
    #canvas.create_rectangle(900,500,1000,550,fill="#C0C0C0")
    #canvas.create_text(950,525,text="input")
    for i in range(3):
        canvas.create_rectangle(100*i+110,650,100*i+190,690,fill="#C0C0C0")
        canvas.create_text(100*i+140,670,text=rotates[i])
        
def click(coordinate):
    global cube,block,blockd
    x=coordinate.x
    y=coordinate.y
    if 650<y<690:
        a=(x-100)//100
        if 0<=a<=2:
            rotate(a)
    elif 50<x<150 and 500<y<550:
        cube=[[i]*4 for i in range(6)]
        block=[0,1,2,3,4,5,6]
        blockd=[0,0,0,5,5,5,5]
    elif 200<x<300 and 500<y<550:
        randomcube()
        print("random")
        print("cube =",cube)
        print("block =",block)
        print("blockd =",blockd)
    elif 50<x<150 and 560<y<610:
        print("solve")
        print("cube =",cube)
        print("block =",block)
        print("blockd =",blockd)
        solve()
    elif 200<x<300 and 560<y<610:
        randomcube()
        print("random and solve")
        print("cube =",cube)
        print("block =",block)
        print("blockd =",blockd)
        solve()
        '''
    elif 900<x<1000 and 500<y<550:
        i=input("input:")'''
    display()
    
def display():
    updatecube()
    canvas.delete("all")
    draw()
    for i in range(6):
        x=0
        y=0
        if i==0:
            x=500
            y=0
        elif i==5:
            x=500
            y=400
        else:
            x=i*200+100
            y=200
        for j in range(2):
            for k in range(2):
                canvas.create_rectangle(x+60*k,y+60*j+20,x+60*k+60,y+60*j+80,fill=color[cube[i][2*j+k]])
    canvas.update()
    
def updatecube():
    global cube
    #corner
    for i in range(7):
        b=block[i]
        if blockd[b]==blockposition[i][0][0]:
            cube[blockposition[i][0][0]][blockposition[i][0][1]]=blockposition[block[i]][0][0]
            cube[blockposition[i][1][0]][blockposition[i][1][1]]=blockposition[block[i]][1][0]
            cube[blockposition[i][2][0]][blockposition[i][2][1]]=blockposition[block[i]][2][0]
        elif blockd[b]==blockposition[i][1][0]:
            cube[blockposition[i][0][0]][blockposition[i][0][1]]=blockposition[block[i]][2][0]
            cube[blockposition[i][1][0]][blockposition[i][1][1]]=blockposition[block[i]][0][0]
            cube[blockposition[i][2][0]][blockposition[i][2][1]]=blockposition[block[i]][1][0]
        else:
            cube[blockposition[i][0][0]][blockposition[i][0][1]]=blockposition[block[i]][1][0]
            cube[blockposition[i][1][0]][blockposition[i][1][1]]=blockposition[block[i]][2][0]
            cube[blockposition[i][2][0]][blockposition[i][2][1]]=blockposition[block[i]][0][0]

def randomcube():
    a=random.randrange(50,60)
    randomstring=""
    for i in range(a):
        r=random.randrange(0,3)
        rotate(r)
        randomstring+=rotates[r]
    print("mix up steps:",randomstring)
    display()
    
def rotate(a):
    #input: 0,1,2
    global block,blockd
    r=faceblock[a]
    nb=block.copy()
    nbd=blockd.copy()
    f=facerotate[a]
    for i in range(4):
        nb[r[i]]=block[r[(i-1)%4]]
    for i in r:
        i=block[i]
        if blockd[i]!=f:
            nbd[i]=adj[a][(adj[a].index(blockd[i])+1)%4]
    block=nb
    blockd=nbd
    
def do(s):
    #input:[face,degree] #htm<=qtm
    global htm,qtm
    print(s)
    for i in s:
        htm+=1
        qtm+=abs(i[1]-1)
        for j in range(i[1]+1):
            rotate(i[0])
        display()
        time.sleep(0.5)
    print("htm",htm,"qtm",qtm)
    
correctblock=[0,1,2,3,4,5,6]
correctblockd=[0,0,0,5,5,5,5]
htm=0
qtm=0
#almost solved
almost=[[correctblock,correctblockd]]
almostsolution=[[]]

almoststep=0
#1 step to solve

for n in range(len(almost)):
    if len(almostsolution[n])==almoststep:
        for i in range(3):#3 or 2 face able to rotate
            corner=almost[n][0].copy()
            cornerd=almost[n][1].copy()
            newcorner=corner.copy()
            newcornerd=cornerd.copy()
            reversesolution=almostsolution[n].copy()
            #if i!=reversesolution[1][0]:#for 2 or more steps
            for j in range(3):#3 degree for 1 face
                for k in range(4):
                    newcorner[faceblock[i][k]]=corner[faceblock[i][(k-j-1)%4]]
                for k in faceblock[i]:
                    if cornerd[corner[k]]!=facerotate[i]:
                        newcornerd[corner[k]]=adj[i][(adj[i].index(cornerd[k])+j+1)%4]
                solution=[[i,2-j]]+reversesolution
                
                almost.append([newcorner.copy(),newcornerd.copy()])
                almostsolution.append(solution.copy())
print(len(almost))
almoststep=1

for n in range(len(almost)):
    if len(almostsolution[n])==almoststep:
        for i in range(3):#3 or 2 face able to rotate
            reversesolution=almostsolution[n].copy()
            if i==reversesolution[-1][0]:#for 2 or more steps
                continue
            corner=almost[n][0].copy()
            cornerd=almost[n][1].copy()
            newcorner=corner.copy()
            newcornerd=cornerd.copy()
            for j in range(3):#3 degree for 1 face
                for k in range(4):
                    newcorner[faceblock[i][k]]=corner[faceblock[i][(k-j-1)%4]]
                for k in faceblock[i]:
                    if cornerd[corner[k]]!=facerotate[i]:
                        newcornerd[corner[k]]=adj[i][(adj[i].index(cornerd[k])+j+1)%4]
                solution=[[i,2-j]]+reversesolution
                
                almost.append([newcorner.copy(),newcornerd.copy()])
                almostsolution.append(solution.copy())
print(len(almost))
'''
almoststep=2
for n in range(len(almost)):
    if len(almostsolution[n])==almoststep:
        for i in range(3):#3 or 2 face able to rotate
            reversesolution=almostsolution[n].copy()
            if i==reversesolution[-1][0]:#for 2 or more steps
                continue
            corner=almost[n][0].copy()
            cornerd=almost[n][1].copy()
            newcorner=corner.copy()
            newcornerd=cornerd.copy()
            for j in range(3):#3 degree for 1 face
                for k in range(4):
                    newcorner[faceblock[i][k]]=corner[faceblock[i][(k-j-1)%4]]
                for k in faceblock[i]:
                    if cornerd[corner[k]]!=facerotate[i]:
                        newcornerd[corner[k]]=adj[i][(adj[i].index(cornerd[k])+j+1)%4]
                solution=[[i,2-j]]+reversesolution
                
                almost.append([newcorner.copy(),newcornerd.copy()])
                almostsolution.append(solution.copy())
print(len(almost))
'''
#[block,blockd,stepsofar]
def solve():
    global htm,qtm
    htm=0
    qtm=0
    if block==correctblock and blockd==correctblockd:
        print("already solved")
        return
    queue=[]
    newqueue=[]
    queue.append([block.copy(),blockd.copy(),[]])
    for c in range(1,12):
        print(c,"queue size",len(queue))
        for cube in queue:
            corner=cube[0]
            cornerd=cube[1]
            step=cube[2]
            #3 face to rotate
            for i in range(3):
                if len(step)==0 or step[-1][0]!=i:
                    newcorner=corner.copy()
                    newcornerd=cornerd.copy()
                    for j in range(3):
                        #directly rotate that face 90 degree
                        for k in range(4):
                            newcorner[faceblock[i][k]]=corner[faceblock[i][(k-j-1)%4]]
                        for k in faceblock[i]:
                            if cornerd[corner[k]]!=facerotate[i]:
                                newcornerd[corner[k]]=adj[i][(adj[i].index(cornerd[corner[k]])+j+1)%4]
                        newstep=step.copy()+[[i,j]]
                        if newcorner==correctblock and newcornerd==correctblockd:
                            do(newstep)
                            return
                        elif [newcorner,newcornerd] in almost:
                            do(newstep+almostsolution[almost.index([newcorner,newcornerd])])
                            return
                        
                        
                        newqueue.append([newcorner.copy(),newcornerd.copy(),newstep.copy()])

        queue=newqueue.copy()
        newqueue=[]
            
canvas.bind("<Button-1>",click)
start()
canvas.pack()
window.mainloop()

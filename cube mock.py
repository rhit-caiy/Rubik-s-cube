# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:15:26 2022

@author: caiy
"""
#ulfrbd mesxyz
from tkinter import Tk,Canvas
import random,time
cube=[[i+1]*9 for i in range(6)]
'''
cube=[[1, 1, 1, 1, 1, 1, 1, 1, 1], 
      [2, 2, 2, 2, 2, 2, 2, 2, 2], 
      [3, 3, 3, 3, 3, 3, 3, 3, 3], 
      [4, 4, 4, 4, 4, 4, 4, 4, 4], 
      [5, 5, 5, 5, 5, 5, 5, 5, 5], 
      [6, 6, 6, 6, 6, 6, 6, 6, 6]]
'''
cube=[[0, 0, 1, 4, 0, 4, 5, 0, 4], [1, 3, 4, 2, 1, 1, 3, 1, 1], [3, 3, 5, 2, 2, 0, 2, 2, 2], [1, 0, 2, 2, 3, 1, 0, 3, 0], [0, 1, 4, 4, 4, 3, 4, 4, 2], [5, 5, 3, 5, 5, 5, 5, 5, 3]]
for i in range(6):
    for j in range(9):
        cube[i][j]+=1
#print(cube)
window=Tk()
canvas=Canvas(window,bg="#808080",width=1440,height=810)
window.title("cube")

color=["","#FFFF00","#0000FF","#FF0000","#00FF00","#FF8000","#FFFFFF"]
rotates=["U","L","F","R","B","D","M","E","S","x","y","z"]
adj=[[4,3,2,1],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[1,2,3,4]]#clockwise
edge=[[[2,1,0],[2,1,0],[2,1,0],[2,1,0]],
      [[0,3,6],[0,3,6],[0,3,6],[8,5,2]],
      [[6,7,8],[0,3,6],[2,1,0],[8,5,2]],
      [[8,5,2],[0,3,6],[8,5,2],[8,5,2]],
      [[2,1,0],[0,3,6],[6,7,8],[8,5,2]],
      [[6,7,8],[6,7,8],[6,7,8],[6,7,8]]]#corresponding to adj, position index of 4 face adjacent part clockwise
middle=[[[1,4,7],[1,4,7],[1,4,7],[7,4,1]],
        [[3,4,5],[3,4,5],[3,4,5],[3,4,5]],
        [[3,4,5],[1,4,7],[5,4,3],[7,4,1]]]

def draw():
    canvas.create_rectangle(50,500,150,550,fill="#C0C0C0")
    canvas.create_text(100,525,text="reset")
    canvas.create_rectangle(200,500,300,550,fill="#C0C0C0")
    canvas.create_text(250,525,text="random")
    canvas.create_rectangle(50,560,150,610,fill="#C0C0C0")
    canvas.create_text(100,585,text="solve")
    canvas.create_rectangle(200,560,300,610,fill="#C0C0C0")
    canvas.create_text(250,585,text="random and solve")
    for i in range(12):
        canvas.create_rectangle(100*i+110,650,100*i+190,690,fill="#C0C0C0")
        canvas.create_text(100*i+140,670,text=rotates[i])
    for i in range(12):
        canvas.create_rectangle(100*i+110,700,100*i+190,740,fill="#C0C0C0")
        canvas.create_text(100*i+140,720,text=rotates[i]+"'")
def start():
    draw()
    display()

def click(coordinate):
    global cube
    x=coordinate.x
    y=coordinate.y
    if 650<y<690:
        a=(x-100)//100
        if 0<=a<=5:
            print("clockwise rotate surface",a)
            rotate(a,1)
        elif 6<=a<=8:
            rotatemiddle(a-6,1)
        elif 9<=a<=11:
            rotatecube(a-9,1)
    elif 700<y<740:
        a=(x-100)//100
        if 0<=a<=5:
            print("counter-clockwise rotate surface",a)
            rotate(a,0)
        elif 6<=a<=8:
            rotatemiddle(a-6,0)
        elif 9<=a<=11:
            rotatecube(a-9,1)
    elif 50<x<150 and 500<y<550:
        cube=[[i+1]*9 for i in range(6)]
    elif 200<x<300 and 500<y<550:
        randomcube()
        print("random cube",cube)
    elif 50<x<150 and 560<y<610:
        print("solve",cube)
        solve()
    elif 200<x<300 and 560<y<610:
        randomcube()
        print("random and solve",cube)
        solve()
    display()

def rotate(a,b):
    #time.sleep(1)
    rotateface(a,b)
    rotateedge(a,b)
    display()
    
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
    a=random.randrange(30,51)
    b=random.randrange(0,10)
    for i in range(a):
        r=random.randrange(0,12)
        rotate(r%6,1-r//6)
    for i in range(b):
        r=random.randrange(0,6)
        rotatecube(r%3,1-r//3)
        
    
def keypress(key):
    k=key.keysym
    if k=='u':
        rotate(0,1)
    elif k=='l':
        rotate(1,1)
    elif k=='f':
        rotate(2,1)
    elif k=='r':
        rotate(3,1)
    elif k=='b':
        rotate(4,1)
    elif k=='d':
        rotate(5,1)
    elif k=='x':
        rotatecube(0,1)
    elif k=='y':
        rotatecube(1,1)
    elif k=='z':
        rotatecube(2,1)
    display()
        
    
canvas.bind("<Button-1>",click)
canvas.bind_all("<KeyPress>",keypress)

def display():
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
        for j in range(3):
            for k in range(3):
                canvas.create_rectangle(x+60*k,y+60*j+20,x+60*k+60,y+60*j+80,fill=color[cube[i][3*j+k]])
    canvas.update()
    time.sleep(0.01)

#no R'2 notation kind, allow R' and R2
totalstep=0
def do(s):
    global totalstep
    #display()
    l=len(s)
    rotates=["U","L","F","R","B","D","M","E","S","x","y","z"]
    i=0
    #print(s)
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
            
#layer by layer, 9 steps
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
    print("total step:",totalstep)
    print("solved:",cube==[[i+1]*9 for i in range(6)])
    
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

start()
canvas.pack()
window.mainloop()
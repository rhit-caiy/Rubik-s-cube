# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:18:58 2022

@author: caiy
"""
correctedge=[8,9,10,11]
correctedged=[5,5,5,5]
faceedge=[[0,1,2,3],[1,4,9,5],[2,5,10,6],[3,6,11,7],[0,7,8,4],[10,9,8,11]]
adj=[[4,3,2,1],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[1,2,3,4]]#adjacent face of each

almostrightedge=[]
almostrightedged=[]
almostrightsolution=[]

#one step to cross
for i in range(1,6):
    r=faceedge[i]
    newedge=correctedge.copy()
    newedged=correctedged.copy()
    for j in range(3):
        for l in range(4):
            if newedge[l] in r:
                newedge[l]=r[(r.index(newedge[l])-1)%4]
                if newedged[l]!=i:
                    newedged[l]=adj[i][(adj[i].index(newedged[l])+1)%4]
        solution=[[i,2-j]]
        almostrightedge.append(newedge.copy())
        almostrightedged.append(newedged.copy())
        almostrightsolution.append(solution)
'''
print(almostrightedge)
print(almostrightedged)
print(almostrightsolution)
'''

print(len(almostrightedge))
print(len(almostrightedged))
print(len(almostrightsolution))
#two steps to cross
for n in range(len(almostrightedge)):
    for i in range(6):
        r=faceedge[i]
        newedge=almostrightedge[n].copy()
        newedged=almostrightedged[n].copy()
        reversesolution=almostrightsolution[n].copy()
        if i!=reversesolution[0][0]:
            for j in range(3):
                for l in range(4):
                    if newedge[l] in r:
                        newedge[l]=r[(r.index(newedge[l])-1)%4]
                        if newedged[l]!=i:
                            newedged[l]=adj[i][(adj[i].index(newedged[l])+1)%4]
                solution=[[i,2-j]]+reversesolution.copy()
                almostrightedge.append(newedge.copy())
                almostrightedged.append(newedged.copy())
                almostrightsolution.append(solution.copy())

print(len(almostrightedge))
print(len(almostrightedged))
print(len(almostrightsolution))
print(almostrightsolution)
#three step
for n in range(len(almostrightedge)):
    if len(almostrightsolution[n])==2:
        for i in range(6):
            newedge=almostrightedge[n].copy()
            newedged=almostrightedged[n].copy()
            reversesolution=almostrightsolution[n].copy()
            if i!=reversesolution[1][0]:
                for j in range(3):
                    for l in range(4):
                        if newedge[l] in faceedge[i]:
                            newedge[l]=faceedge[i][(faceedge[i].index(newedge[l])-1)%4]
                            if newedged[l]!=i:
                                newedged[l]=adj[i][(adj[i].index(newedged[l])+1)%4]
                    solution=[[i,2-j]]+reversesolution
                    almostrightedge.append(newedge.copy())
                    almostrightedged.append(newedged.copy())
                    almostrightsolution.append(solution.copy())
                    
print(len(almostrightedge))
print(len(almostrightedged))
print(len(almostrightsolution))
#four step
for n in range(len(almostrightedge)):
    if len(almostrightsolution[n])==3:
        for i in range(6):
            newedge=almostrightedge[n].copy()
            newedged=almostrightedged[n].copy()
            reversesolution=almostrightsolution[n].copy()
            if i!=reversesolution[2][0]:
                for j in range(3):
                    for l in range(4):
                        if newedge[l] in faceedge[i]:
                            newedge[l]=faceedge[i][(faceedge[i].index(newedge[l])-1)%4]
                            if newedged[l]!=i:
                                newedged[l]=adj[i][(adj[i].index(newedged[l])+1)%4]
                    solution=[[i,2-j]]+reversesolution
                    almostrightedge.append(newedge.copy())
                    almostrightedged.append(newedged.copy())
                    almostrightsolution.append(solution.copy())
                    
print(len(almostrightedge))
print(len(almostrightedged))
print(len(almostrightsolution))
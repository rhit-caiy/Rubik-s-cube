# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:51:36 2022

@author: caiy
"""
import time
def random():
    cube=''
    
s=input("rotation, random for random:")
if s=="random":
    random()
else:
    l=len(s)
    i=0
    while i<l:
        print(s[i])
        i+=1
        if i<l:
            if s[i]=="'":
                print("reverse'")
                i+=1
                if i<l and s[i].isdigit():
                    print(s[i],"number")
                    i+=1
            elif s[i].isdigit():
                print(s[i],"number")
                i+=1
        time.sleep(1)
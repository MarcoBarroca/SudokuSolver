#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:32:21 2019

@author: magbarroca
"""

def find_next(b):
    for i in range (len(b)):
        for j in range(len(b[0])):
            if b[i][j]==0:
                return (i,j)
            
    return None

def isValid(b, num, pos):
    
    """box Check"""
    
    x = pos[1] // 3
    y = pos[0] // 3
    
    for i in range(y*3,y*3+3):
        for j in range (x*3,x*3+3):
            if b[i][j]==num and (i,j)  != pos:
                return False
    
    """Row check"""
    
    for i in range(0,len(b)):
        if b[pos[0]][i]==num and pos[1] != i:  
            return False
    
    """Collumn Check"""
    
    for i in range(0,len(b)):
        if b[i][pos[1]] ==num and pos[1]!=i:  
            return False
                              
    return True

def solve(b):
    empty=find_next(b)
    if empty:
        row,col=empty
    else:
        return True
    
    for i in range(1,10):
        if isValid(b, i, (row,col)):
            b[row][col]=i
            
            if solve(b):
                return True
            
            b[row][col]=0
            
    return False
    
def print_b(b):
    for i in range(len(b)):
        
        """separate Blocks"""
            
        if i % 3==0 and i!=0:
            print("------------")
            
        """Separate collums in trios"""
            
        for j in range(len(b[0])):
            if j % 3 == 0:
                print("|", end="")          
                
                """Jump a line after 9 collumns"""
            if j==8:
                print(b[i][j],end="\n")     
                
                """Print the numbers as strings"""
            else:
                print(str(b[i][j]) + "",end="")
        
    
board=[
   [7,8,0,4,0,0,1,2,0],
   [6,0,0,0,7,5,0,0,9],
   [0,0,0,6,0,1,0,7,8],
   [0,0,7,0,4,0,2,6,0],
   [0,0,1,0,5,0,9,3,0],
   [9,0,4,0,6,0,0,0,5],
   [0,7,0,3,0,0,0,1,2],
   [1,2,0,0,0,7,4,0,0],
   [0,4,9,2,0,6,0,0,7]
    ]
   
solve(board)
print_b(board)          
        

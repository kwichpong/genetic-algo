# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 02:58:04 2016

@author: Wiiill
"""
import random

def Sequencing():
    if chromosome:
        for x in chromosome:
            aim = sqco[x-1]
            #print aim
            req = aim[1:4]
            #print req
            isSkip = False
            for y in req:
                if((y not in seq) and (y != 0)):
                    #print "Skip",x,y,ans
                    isSkip = True
                    break
                #print chromosome
            if(isSkip is False):        
                seq.append(x)
                chromosome.remove(x)
                #print "addAns",x
                Sequencing()
                
def ReadSqco():
    count=0
   # f = open('sqco.csv', 'r')
    f = open('sqcoMo.csv', 'r')
    next(f)
    for line in f:
        sqco.append(map(int,map(str.rstrip,line.split(","))))
        count+=1
    return count
   # print sqco
    
def VerticalReadInput():
    f=open('input.csv','r')
    for line in f:
        chromosome.append(int(line))
  
    
def HorizontalReadInput():
    f=open('input_tt.csv','r')
    for line in f:
        return map(int,line.split(','))
    
def GenerateInput():
    gen = random.sample(range(1,size+1),size)
    return gen

        
def IsCanStart(toCheck):
    status=True
    for x in toCheck:
        if(x==0):
            continue
        else:
            if(x not in jobDone):
                status=False
    return status

def IsUsing():
    return True
def TestGit():
    print "asdasd"
'''
def readresource():
    f=open('resource.csv','r')
    for line in f:
        resource.append(int(line))
    for x in range(0,len(resource)):
        print "Resource",x+1,"=",resource[x]
'''

#size=32
sqco=[]
chromosome=[]
seq=[]
resource=[]
fitness=0
size=ReadSqco()
#VerticalReadInput()
#chromosome=GenerateInput()
chromosome=[8, 10, 3, 5, 6, 1, 9, 11, 4, 2, 7]
#chromosome=HorizontalReadInput()
print "start: ",chromosome
Sequencing()  
print "finish: ",seq

print sqco
jobq=seq
jobDoing=[]
jobDone=[]
machineStatus=[0,0,0,0,0,0,0,0]
time=0
timeout=0
while 1:
    if(len(jobDone)==size or timeout==1):
        break
    else:
        for x in jobq:
            detemine = sqco[x-1]
            name=detemine[0]
            precedence=detemine[1:][:3]
            duration=detemine[4]
            resource=detemine[5:]
            print name
            print precedence
            print duration
            print resource
            if(IsCanStart(precedence)):
                
                jobDoing.append(x)
                
                print str(name)+" is Starting"
                
            else:
                print "Can't Start"
           # print detemine
            timeout+=1
            
        
#readresource()
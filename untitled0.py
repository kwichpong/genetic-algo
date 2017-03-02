# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 02:58:04 2016

@author: Wiiill
"""
import random
import xlrd
import collections
from operator import itemgetter

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
                

def Sequencing_test(chromosome):
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
                Sequencing(chromosome)
    else:
        return seq
                
def ReadSqco():
    count=0
   # f = open('sqco.csv', 'r')
    f = open('sqcoMo.csv', 'r')
    next(f)
    for line in f:
        mappedLine = line.split(",")
        for x in range(0,4):
#            print "before "+mappedLine[x]
            if(mappedLine[x]!="-"):
                mappedLine[x]=AlphabetToNumber(mappedLine[x])
            else:
                mappedLine[x]=str(0)
#            print "after "+mappedLine[x]
#            print
        sqco.append(map(int,map(str.rstrip,mappedLine)))
#        sqco.append(map(int,map(str.rstrip,line.split(","))))
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

def NumberToAlphabet(number):
    if number==0:
        return "_"
    else:
        return chr(64+number)

def ConvertListToAlphabet(numlist):
    alphabetList=[]
    for x in range(0,len(numlist)):
        alphabetList.append(NumberToAlphabet(numlist[x]))
    return alphabetList
    
def ConvertListToNumber(alphalist):
    numlist=[]
    for x in range(0,len(alphalist)):
        numlist.append(AlphabetToNumber(alphalist[x]))
    return numlist
    

def AlphabetToNumber(alphabet):
    return str(ord(alphabet.lower())-96)
        
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

'''
def readresource():
    f=open('resource.csv','r')
    for line in f:
        resource.append(int(line))
    for x in range(0,len(resource)):
        print "Resource",x+1,"=",resource[x]
'''

def ReadExcel():
    workbook = xlrd.open_workbook("sqcoMo.xlsx")
    sheet = workbook.sheet_by_index(0)
    
    for rowx in range(sheet.nrows):
        cols = sheet.row_values(rowx)
        print(cols)

def checkTaskCanStart(task,taskdone):
    req=[]
    for x in sqco:
        if x[0]==task:
            for y in range(1,4):
                if x[y] == 0:
                    continue
                else:
                    req.append(x[y])
    #print req
    if(set(req)<=set(taskdone)):
        return True
    else:
        return False
        
def checkMachine(NoMac):
    return machine[NoMac]

def usesamemachine(tasktodo):
    isSame=False
    uselist = []
    for x in tasktodo:
        machinelistTask = sqco[x-1][5:]
        machineduration=[]
        machineorder=[]
        count=0
        for y in machinelistTask:
            if count%2==0:
                machineduration.append(y)
            else:
                machineorder.append(y)
            count+=1
#        print machineduration,machineorder
        for y in range(0,len(machineduration)):
            if(machineduration[y]!=0):
                uselist.append(y+1)
        #print "uselist",uselist 
        if(len(uselist)!=len(set(uselist))):
            isSame = True
    return isSame

def checktime(tasktodo):
    durationlist=[]
    for x in tasktodo:
        durationlist.append(sqco[x-1][4])
    if len(tasktodo) == 1:
        return sqco[tasktodo[0]-1][4]
    if (not usesamemachine(tasktodo)):
    #    print "tasktodo",tasktodo
        return max(durationlist)

    else:
        time=0
        for order in range(1,9):
            allInThisOrder=[]
            indexing=[]
            machineDurationList=[]
            for eachtask in tasktodo:
                machinelistTask = sqco[eachtask-1][5:]
                machineduration=[]
                machineorder=[]
                count=0
                for y in machinelistTask:
                    if count%2==0:
                        machineduration.append(y)
                    else:
                        machineorder.append(y)
                    count+=1
                machineDurationList.append(machineduration)
                machineUseInThisOrder = [i for i, x in enumerate(machineorder) if x == order]
                allInThisOrder.extend(machineUseInThisOrder)
                indexing.append(machineUseInThisOrder)
#                print "No. Machine that use in order",order,"of Task No.",eachtask,"is", machineUseInThisOrder

            if allInThisOrder:
#                print "allInThisOrder",allInThisOrder,(indexing)
                
                timeinthisorder=0
                if len(allInThisOrder)==len(set(allInThisOrder)):
#                    print "didn't dup"
                    xxduration = []
                    for x in range(0,len(allInThisOrder)):
               #         print sqco[tasktodo[x]-1][5+2*allInThisOrder[x]]              
                        xxduration.append(sqco[tasktodo[x]-1][5+2*allInThisOrder[x]])
#                    for machineNo in allInThisOrder:
#                        print sqco[eachtask-1][5+2*machineNo]
#                        xxduration.append(sqco[eachtask-1][5+2*machineNo])
#                    if xxduration:
#                    print "xxduration",xxduration
              #      print
                    timeinthisorder=max(xxduration)
                    time+=timeinthisorder
                   
                else:
                    duplist=[item for item, xxx in collections.Counter(allInThisOrder).items() if xxx > 1]
#                    print "duplicate",duplist
                    for dup in duplist:
                        for eachtask in tasktodo:
                            timeinthisorder=sqco[eachtask-1][5+2*dup]
                            time += timeinthisorder
#                print "timeinthisorder",timeinthisorder
#        print "time to return",time
        return time
#        for eachtask in tasktodo:
#                machinelistTask = sqco[eachtask-1][5:]
#                machineduration=[]
#                machineorder=[]
#                count=0
#                for y in machinelistTask:
#                    if count%2==0:
#                        machineduration.append(y)
#                    else:
#                        machineorder.append(y)
#                    count+=1
#                for order in range(1,9):
#                    machineUseInThisOrder = [i for i, x in enumerate(machineorder) if x == order] 
#                    print "No. Machine that use in order",order,"of Task No.",eachtask,"is", machineUseInThisOrder 
        
        return 0
    return 0
    
def findTotalFitnessPop(totalRandom):
    ans=0
    for x in range(0,len(totalRandom)):
        ans+=(1.0/totalRandom[x][1])
   # print "Ans",ans
    
    return ans

def UniformCrossOver(father,mother):
    son=[]
    crossovermask=[random.randint(0, 1) for i in range(size)]
    for x in range(0,len(crossovermask)):
        if(crossovermask[x]==1):
            son.append(father[x])
        else:
            son.append(mother[x])
    return son,crossovermask

def CrossOver(father,mother):
    son1=[]
    son2=[]
    crossOverPoint=random.randint(1,9)
    print "CrossOver Point",crossOverPoint
    son1=father[:crossOverPoint]
    print "Son1Head: ",ConvertListToAlphabet(son1)
    son1tail=list(set(mother)-set(son1))
    son1.extend(son1tail)
    
    son2=mother[:crossOverPoint]
    print "Son2Head: ",ConvertListToAlphabet(son2)
    son2tail=list(set(father)-set(son2))
    son2.extend(son2tail)
    
    print "Son1:",ConvertListToAlphabet(son1)
    print "Son2:",ConvertListToAlphabet(son2)
    return son1,son2

def TimecalNoPrint(seq):
    test_taskdone=[]
   # print "Input of time cal",ConvertListToAlphabet(seq)
 #   taskdoing=[]
    totaltime=0
    aim_len=len(seq)
    ##Split Task to do
    test_seq=seq
    while(True):
        if(len(test_taskdone)==aim_len):
            break
        tasktodo=[]
        aim=0
        for x in range(0,len(test_seq)):
            if checkTaskCanStart(test_seq[x],test_taskdone):
                tasktodo.append(test_seq[x])
                aim=x
            else:
                for y in range(0,aim+1):
                    test_seq.pop(0)
                break   

        #ChecktimeHere
        
        roundtime=checktime(tasktodo)
        totaltime+=roundtime
     #   print
        
      #  print "taskToDo",ConvertListToAlphabet(tasktodo),"Time to do:",roundtime,"Total time:",totaltime
        test_taskdone.extend(tasktodo)
      #  print "TaskDone",ConvertListToAlphabet(test_taskdone)
       # print "Remaining Task",ConvertListToAlphabet(test_seq)


#        raw_input()
    return test_taskdone,totaltime




def Timecal(seq):
    test_taskdone=[]
   # print "Input of time cal",ConvertListToAlphabet(seq)
 #   taskdoing=[]
    totaltime=0
    aim_len=len(seq)
    ##Split Task to do
    test_seq=seq
    while(True):
        tasktodo=[]
        aim=0
        for x in range(0,len(test_seq)):
            if checkTaskCanStart(test_seq[x],test_taskdone):
                tasktodo.append(test_seq[x])
                aim=x
            else:
                for y in range(0,aim+1):
                    test_seq.pop(0)
                break   

        #ChecktimeHere
        print "tasktodo",ConvertListToAlphabet(tasktodo)
        roundtime=checktime(tasktodo)
        totaltime+=roundtime
        print "Time to do:",roundtime,"Total time:",totaltime
        test_taskdone.extend(tasktodo)
        #print "TaskDone",ConvertListToAlphabet(test_taskdone)
       # print "Remaining Task",ConvertListToAlphabet(test_seq)

        if(len(test_taskdone)==aim_len):
            break
#        raw_input()
    return test_taskdone,totaltime

  #  taskSize=len(seq)
 #   print "TaskSize",taskSize
   # print seq
 #   print
    #print sqco

#    while(len(taskdone)<11):
#        print x
#        taskdone.append("a")
    
#    if len(taskdone)
    
    
    
    #xxxxxxxxxxxxxxxxx Oldxxxxxxxxxxxxxxxxxx#
#    while(len(seq)>0):
##        if(len(taskdone)==taskSize):
##            break
#        tasktodo=[]
#        for x in seq:
#            if checkTaskCanStart(x,taskdone):
#                tasktodo.append(x)
#            seq = list(set(seq) - set(tasktodo))
#        #print "taskNotDoYet",seq
#       
#        #ChecktimeHere
#        roundtime=checktime(tasktodo)
#        print "taskToDo",ConvertListToAlphabet(tasktodo),"Time to do:",roundtime
#        raw_input()
#        totaltime+=roundtime
#        
#        ##end check time
#        taskdone.extend(tasktodo)
#        print "taskDone",ConvertListToAlphabet(taskdone)
#        print "timeCumulative",totaltime
#        raw_input()
#    
#    return taskdone,totaltime
##        
        #xxxxxxxxxxxxxxxxx Oldxxxxxxxxxxxxxxxxxx#
    
    
    
#        index=0
#        timeMac=[]
#        orderMac=[]
#        for machine in machinelistTask:
#            
#            totaltime=0
#            if(index%2==0):
#                print "Time\t",machine
#                timeMac.append(machine)
#            else:
#                print "Order\t",machine
#                orderMac.append(machine)
#            print timeMac,orderMac
#            index+=1
#        for x in range(0,8):
#            print orderMac.index(x)
#        print machinelistTask,durationTask
#size=32
#sqco=[]
#chromosome=[]
#seq=[]
#resource=[]
#fitness=0
#size=ReadSqco()
#machine=[True,True,True,True,True,True,True,True]

#VerticalReadInput()
#chromosome=GenerateInput()

#inputChromosome=['H', 'J', 'C', 'E', 'F', 'A', 'I', 'K', 'D', 'B', 'G']
inputChromosome=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
print
print "init chromosome",inputChromosome
print

totalRandom=[]

randomTime=input("Input Popsize: ")
pc=input("Cross Over Probability(%): ")
pc=pc/100.0
pm=input("Mutation Probability(%): ")
pm=pm/100.0
maximumGen=input("Maximum Generation: ")

initChromosome=[]

for asdf in range(0,randomTime):
    sqco=[]
    chromosome=[]
    seq=[]
    resource=[]
    taskdone=[]
    totaltime=0
    size=ReadSqco()
    machine=[True,True,True,True,True,True,True,True]
    inputChromosome=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    random.shuffle(inputChromosome)
    for x in range(0,len(inputChromosome)):
        chromosome.append(int(AlphabetToNumber(inputChromosome[x])))
    #chromosome=HorizontalReadInput()
  #  print "start: ",inputChromosome
    Sequencing()  
    #print "finish: ", ConvertListToAlphabet(seq)
    print "==============""Chromosome",asdf+1,"====================="
    print "Start: ",inputChromosome
    print "Initial Chromosome",ConvertListToAlphabet(seq)
    initChromosome.append([seq,asdf+1])
  #  taskdone,totaltime=TimecalNoPrint(seq)
    #totalRandom.append([taskdone,totaltime])
   # totalRandom.append([taskdone,totaltime,asdf+1])
  #  print "Finish:",ConvertListToAlphabet(taskdone)
  #  print "Total time",totaltime
   # print
#print totalRandom

raw_input("Press Enter to find Parent Chrmosome")
random.shuffle(initChromosome)
parentChromosome=[]
for x in range(0,len(initChromosome),2):
    print "===============Parent No.:",(x/2)+1,"==============="
    print "NO:",initChromosome[x][1],ConvertListToAlphabet(initChromosome[x][0])
    print "NO:",initChromosome[x+1][1],ConvertListToAlphabet(initChromosome[x+1][0])
    parentChromosome.append([initChromosome[x],initChromosome[x+1]])
newGenCrossOver=[]
raw_input("Press Enter to show crossover process")
for x in range(0,len(parentChromosome)):
    print "===============Parent No.:",x+1,"==============="
    crossOverProb=random.random()
    print "Cross Over probability",crossOverProb
    if(crossOverProb<=pc):
        crossovermask=[random.randint(0, 1) for i in range(size)]
        son1=[0]*len(crossovermask)
        son2=[0]*len(crossovermask)
    
        print "Cross Over Mask:",crossovermask
        print "Father","From NO.:",parentChromosome[x][0][1],":",ConvertListToAlphabet(parentChromosome[x][0][0])
        print "Mother","From NO.:",parentChromosome[x][1][1],":",ConvertListToAlphabet(parentChromosome[x][1][0])
        print "Fill Mask Logic 1"
        fatherFilled=[]
        motherFilled=[]
        for find1 in range(0,len(crossovermask)):
            if(crossovermask[find1]==1):
                son1[find1]=parentChromosome[x][0][0][find1]
                fatherFilled.append(son1[find1])
            else:
                son2[find1]=parentChromosome[x][1][0][find1]
                motherFilled.append(son2[find1])
    
    #    print "fatherFilled",ConvertListToAlphabet(fatherFilled)
    #    print "motherFilled",ConvertListToAlphabet(motherFilled)
        print "Son1",ConvertListToAlphabet(son1)
        print "Son2",ConvertListToAlphabet(son2)    
   
        print "Fill Mask Logic 0"
        son1TobeFilled = [xx for xx in parentChromosome[x][1][0] if xx not in fatherFilled]
        
        son2TobeFilled = [xx for xx in parentChromosome[x][0][0] if xx not in motherFilled]
        print "son1TobeFilled",ConvertListToAlphabet(son1TobeFilled)
        print "son2TobeFilled",ConvertListToAlphabet(son2TobeFilled)
        for find0 in range(0,len(crossovermask)):
            if(crossovermask[find0]==0):
                for tobefilled in son1TobeFilled:
                    if(checkTaskCanStart(tobefilled,son1[:find0])):
                        son1[find0]=tobefilled
                        son1TobeFilled.remove(tobefilled)
                        break
            else:
                for tobefilled in son2TobeFilled:
                    if(checkTaskCanStart(tobefilled,son2[:find0])):
                        son2[find0]=tobefilled
                        son2TobeFilled.remove(tobefilled)
                        break
        newGenCrossOver.append(son1)
        print "Son1",ConvertListToAlphabet(son1)
        newGenCrossOver.append(son2)
        print "Son2",ConvertListToAlphabet(son2)
    else:
        print "No Need To CrossOver"
        print "Son1",ConvertListToAlphabet(parentChromosome[x][0][0])
        newGenCrossOver.append(son1)
        print "Son2",ConvertListToAlphabet(parentChromosome[x][1][0])
        newGenCrossOver.append(son2)
newGenMutation=[]
raw_input("Press Enter to show mutation process")
for newgen in newGenCrossOver:
    print "==========================================="
    print "Chromosome: ",ConvertListToAlphabet(newgen)
    mutationProb=random.random()
    print "Mutation probability",mutationProb
    if(mutationProb<=pm):
        print "Do Mutation"
        muIndex1=random.randint(0,size-1)
        muIndex2=muIndex1
        while(muIndex2==muIndex1):
           muIndex2=random.randint(0,size-1)
        print "Mutation Index:",muIndex1+1,">>",NumberToAlphabet(newgen[muIndex1])
        print "Mutation Index:",muIndex2+1,">>",NumberToAlphabet(newgen[muIndex2])
        if(checkTaskCanStart(newgen[muIndex1],newgen[:muIndex2]) and checkTaskCanStart(newgen[muIndex2],newgen[:muIndex1])):
            print "Can Swap"
            tmpnewgen=newgen
            tmpnewgen[muIndex2], tmpnewgen[muIndex1] = tmpnewgen[muIndex1], tmpnewgen[muIndex2]
            newGenMutation.append(tmpnewgen)
        else:
            print "Can't Swap"
            newGenMutation.append(newgen)
    else:
        print "Didn't Mutation"
        newGenMutation.append(newgen)
        
totalGeneration=[]
print "===========Summary========="
print "New Generation Chromosome"
tdone=[]
for x in range(0,len(newGenMutation)):
    print ConvertListToAlphabet(newGenMutation[x])
    
    chromosome=[]
    seq=[]
    for y in range(0,len(newGenMutation[x])):
        chromosome.append(newGenMutation[x][y])
    #chromosome=HorizontalReadInput()
  #  print "start: ",inputChromosome
    Sequencing()  
    
    tdone,totaltime=Timecal(seq)
    totalGeneration.append([tdone,totaltime,len(totalGeneration)+1])
    print "TotalTime: ",totaltime
    print "==============================="
print "Parent Chromosome"
for x in range(0,len(initChromosome)):
    print ConvertListToAlphabet(initChromosome[x][0])
    tdone,totaltime=Timecal(initChromosome[x][0])
    totalGeneration.append([tdone,totaltime,len(totalGeneration)+1])
    print "TotalTime: ",totaltime
    print "==============================="

nextgen=[]

totalGeneration=sorted(totalGeneration, key=itemgetter(1))
print "=============ELETIS==============="
eletis=[totalGeneration[0][2],totalGeneration[0][0],totalGeneration[0][1]]
print eletis[0],ConvertListToAlphabet(eletis[1]),eletis[2]
nextgen.append(eletis)
    
raw_input("Press Enter to find Probability Roulette Wheel Method")
print"========================================================"
print "Roulette Wheel Method"
print "No.|  \t\t\tChromosome\t\t\t      | Fitness |    Probability    |          Range"

#print totalRandom
TotalFitnessPop=findTotalFitnessPop(totalGeneration)
popcumu=0
for x in totalGeneration:
    temp=[]
    temp.append(popcumu)
    pop=(1.0/x[1])/TotalFitnessPop
    popcumu+=pop
    temp.append(popcumu)
    x.append(pop)
    x.append(temp)
    print x[2]," | ",ConvertListToAlphabet(x[0]),"|  ",x[1],"   |  ",x[3]," |",x[4]
    print

raw_input("Press Enter to choose another for next generation")
print "==========================================="
print "Random Prob:","====>","No.: Chromosome"
for x in range(randomTime-1):
    rannum=random.random()
    for y in totalGeneration:
        if(rannum>=y[4][0] and rannum<=y[4][1]):
            print rannum,"===>",y[2],"  : ",ConvertListToAlphabet(y[0])
            nextgen.append([y[2],y[0],y[1]])
print "==========================================="
print "NextGeneration Chromosome"

nextgen=sorted(nextgen, key=itemgetter(2))
initChromosome=[]
for x in nextgen:
    print x[0],ConvertListToAlphabet(x[1]),x[2]
    
    initChromosome.append([x[1],x[0]])
    
    
   
    


#===============V.19022017===================================

#raw_input("Press Enter to find Probability Roulette Wheel Method")
#print"========================================================"
#print "Roulette Wheel Method"
#print "No.|  \t\t\tChromosome\t\t\t      | Fitness |    Probability    |          Range"
#totalRandom=sorted(totalRandom, key=itemgetter(1))
##print totalRandom
#TotalFitnessPop=findTotalFitnessPop(totalRandom)
##print TotalFitnessPop
#popcumu=0
#for x in totalRandom:
#    temp=[]
#    temp.append(popcumu)
#    pop=(1.0/x[1])/TotalFitnessPop
#    popcumu+=pop
#    temp.append(popcumu)
#    x.append(pop)
#    x.append(temp)
#    print x[2]," | ",ConvertListToAlphabet(x[0]),"|  ",x[1],"   |  ",x[3]," |",x[4]
#    print
#fathermotherOrder=[]
#
#
##cando=False
##while(not cando):
##    doingTime=input("How many best fitness's Chromosome to Do next(2 to numbers of init chromosome, Even number): ")
##    if(doingTime<=randomTime and doingTime%2==0 and doingTime!=0):
##        cando=True
#raw_input("Press Enter to find Father | Mother Chromosome")
#print "==========================================="
#print "Choose Father | Mother"
#print "Random Prob:","====>","No.: Chromosome"
#for x in range(randomTime):
#    rannum=random.random()
#    for y in totalRandom:
#        if(rannum>=y[4][0] and rannum<=y[4][1]):
#            print rannum,"===>",y[2],"  : ",ConvertListToAlphabet(y[0])
#            fathermotherOrder.append(y[0])
##print fathermotherOrder
##print
#sons=[]
#crossOverProbthreshold=0.8
#raw_input("Press Enter to show crossover process")
#crossOverChoice=input("Which type of Crossover: (1)Uniform Crossover (2)Single Point Crossover")
#if(crossOverChoice==1):
#    #xxxxxxUniform CrossOverxxxxxxxxxx
#    for x in range(0,randomTime,2):
#       
#        
#      #  print "Pair:",(x/2)+1," | CrossOverMask: ",crossOvermask
#       
#        print "Father==>",ConvertListToAlphabet(fathermotherOrder[x])
#        print "Mother==>",ConvertListToAlphabet(fathermotherOrder[x+1])
#        sonU1,crossovermask=UniformCrossOver(fathermotherOrder[x],fathermotherOrder[x+1])
#        print "Son1: ",ConvertListToAlphabet(sonU1),"Cross Over mask: ",crossovermask
#        sonU2,crossovermask=UniformCrossOver(fathermotherOrder[x+1],fathermotherOrder[x])
#        print "Son2: ",ConvertListToAlphabet(sonU2),"Cross Over mask: ",crossovermask
#        sons.append(sonU1)
#        sons.append(sonU2)
#        print
#        
#    #xxxxxxUniform CrossOverxxxxxxxxxx
#elif(crossOverChoice==2):
#    #xxxxxxxxxxx old_crossoverxxxxxxxxxxxxxxxxxx
#    print "xxxx CrossOverProbthreshold =",crossOverProbthreshold,"xxxxxxxxxxx\n"
#    for x in range(0,randomTime,2):
#        crossOverProb=random.random()
#    
#        print "Pair:",(x/2)+1," | CrossOverProbability: ",crossOverProb
#       
#        print "Father==>",ConvertListToAlphabet(fathermotherOrder[x])
#        print "Mother==>",ConvertListToAlphabet(fathermotherOrder[x+1])
#        if(crossOverProb<=crossOverProbthreshold): ##DO CrossOver
#            #print "CrossOver"
#            son1,son2=CrossOver(fathermotherOrder[x],fathermotherOrder[x+1])
#            sons.append(son1)
#            sons.append(son2)
#        else:
#            print "Did't CrossOver"
#            print "Son1: ",ConvertListToAlphabet(fathermotherOrder[x])
#            print "Son2: ",ConvertListToAlphabet(fathermotherOrder[x+1])
#            sons.append(fathermotherOrder[x])
#            sons.append(fathermotherOrder[x+1])
#        print
#        
#    #xxxxxxxxxxx old_crossoverxxxxxxxxxxxxxxxxxx
#        
#raw_input("Press Enter to show mutation process")
#print "==========Mutation Process============"
#mutationProbthreshold=input("Input You mutation Prob Threshold: ")
#print "xxxx Mutation Prob Threshold =", mutationProbthreshold, "xxxx"
#
#def CanSwap(source,target):
#    print source,target
#
#def mutation(checkChromosome):
#   # print "mutationMethod",checkChromosome
#    for x in range(0,len(checkChromosome)):
#        gene=checkChromosome[x]
#        if(gene[2]==True): #Mutation
#            print "Mu it at",NumberToAlphabet(gene[0])," | Index: ",x
#
#for x in range(0,randomTime):
#
#    checkMutation=[]
#    for gene in sons[x]:
#        #temp=[NumberToAlphabet(gene)]
#        temp=[gene]
#        mutationProb=random.random()
#        #mutationProb=round(random.uniform(0.11, 1.0), 3)
#        temp.append(mutationProb)
#        if mutationProb<mutationProbthreshold:
#            temp.append(True)
#        else:
#            temp.append(False)
#        checkMutation.append(temp)
#    print "Son",x+1,":","['GENE' | 'Mutation Probability' | 'Need Mutation?']"
#    print checkMutation
#    #mutation(checkMutation)
#
#
#raw_input("Press Enter to show New Generation Chromosome")
#newSpring=[]
#print "\nxxxxxx Offspring Chromosome xxxxxxxxx"
#for x in range(0,len(sons)):
#    if(len(set(sons[x]))!=len(sons[x])):        
#        print "Son No:",x+1,ConvertListToAlphabet(sons[x]),"Duplicate gene Can't calculate Time"
#    else:
#        son,sonTime=TimecalNoPrint(sons[x])
#        print "Son No:",x+1,ConvertListToAlphabet(son),"Time: ",sonTime
#        newSpring.append([x+1,son,sonTime])
#   # print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#print
#print
#print "xxxxxxxxxxxxxxxxxxxxxxxSUMMARYxxxxxxxxxxxxxxxxxxxxxxxxx"
#
#newSpring=sorted(newSpring, key=itemgetter(1),reverse=False)
#
#for x in range(0,len(newSpring)):
#    print "Son No.:",newSpring[x][0],ConvertListToAlphabet(newSpring[x][1]),"Time: ",newSpring[x][2]
#
#print "xxxxxxxxxxxxxxxxxxx Parent Chromosome xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#for x in range(0,len(totalRandom)):
#    print "Parent No.:",totalRandom[x][2],ConvertListToAlphabet(totalRandom[x][0]),"Time: ",totalRandom[x][1]
#

#===============V.19022017===================================



#crossOverProb=input("Input Crossover Probability: ")
#print crossOverProb


#print totalRandom
#print "Shuffle",inputChromosome

#print sqco
#jobq=seq
#jobDoing=[]
#jobDone=[]
#machineStatus=[0,0,0,0,0,0,0,0]
#time=0
#timeout=0
#while 1:
#    if(len(jobDone)==size or timeout==1):
#        break
#    else:
#        for x in jobq:
#            detemine = sqco[x-1]
#            name=detemine[0]
#            precedence=detemine[1:][:3]
#            duration=detemine[4]
#            resource=detemine[5:]
#            print name
#            print precedence
#            print duration
#            print resource
#            if(IsCanStart(precedence)):
#                
#                jobDoing.append(x)
#                
#                print str(name)+" is Starting"
#                
#            else:
#                print "Can't Start"
#           # print detemine
#            timeout+=1
#            
#        
#readresource()
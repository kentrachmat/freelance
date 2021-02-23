import copy
import random 

def check(TT):
    # respect lunch break
    for anyday in TT :
        if (anyday[1] != 0) and (anyday[2] != 0) and (anyday[3] != 0) :
            print("Attention: no lunch break on day ", anyday)
            return False
    
    # no lesson on Monday morning
    if (TT[0][0] != 0) or (TT[0][1] != 0):
        print("Attention: lesson on Monday morning")
        return False

    # each course exactly 3 slots in the week
    # we have to go through the entire week and find out how many slots
    # does each lecturer have
    slots={ 0:0, 1:0, 2:0, 3:0, 4:0 }
    day=0
    while day<=4:
        hour=0
        while hour<=4:
            currentProf=TT[day][hour]
            slots[currentProf]=slots[currentProf]+1
            hour=hour+1
        day=day+1
    # now inside slots I have how many slots does each prof have
    for x in slots:
        if x>0 and slots[x]!=3:
            print("Attention! Lecturer ",x," has ",slots[x]," slots")
            return False
    
    # maximum 1 slot every day for each course
    for d in TT :
        perday = []
        for e in d :
            if e in perday and e != 0 :
                print("max 1 slot every day for each course")
                return False
            perday.append(e)

    # C never lesson on two consecutive days
    for k in range(0,4) :
        if 1 in TT[k] and 1 in TT[k+1] :
            print("C lessons on two consecutive days")
            return False
    
    # F and L can never meet, i.e. their lessons cannot be consecutive
    for m in TT :
        for c in range(0,4) :
            if (m[c] == 2 and m[c+1] == 3) or (m[c] == 3 and m[c+1] == 2) :
                print("F and L met")
                return False
    return True
#print(check([[0, 0, 1, 0, 4], [0, 2, 0, 0, 3], [1, 2, 0, 4, 3], [0, 0, 0, 3, 4], [1, 2, 0, 0, 0]]))


def checkPartial(day,slot,TT) :
# write here a modified check procedure, which checks things up to day-1 and for day it checks only up to slot
# obvisouly some checks cannot be done while others need to be adjusted
    
    # partial : respect lunch break
    if len(TT[0]) > 3 :
        for x in range(0, day) :
            if (TT[x][1] != 0) and (TT[x][2] != 0) and (TT[x][3] != 0) :
                print("Attention: no lunch break on")
                return False
    if len(TT[day]) > 3 :
        if (TT[day][1] != 0) and (TT[day][2] != 0) and (TT[day][3] != 0) :
            print("Attention: no lunch break on")
            return False
        
    # partial : no lesson on Monday morning
    if len(TT[0]) == 1 :
        if (TT[0][0] != 0) :
            print("Attention: lesson on Monday morning")
            return False
    if len(TT[0]) > 1 :
        if (TT[0][0] != 0) or (TT[0][1] != 0):
            print("Attention: lesson on Monday morning")
            return False
    
    # partial : maximum 1 slot every day for each course
    for e in range(0, day) :
        perday = []
        for x in range(0,5) :
            if TT[e][x] in perday and TT[e][x]!= 0 :
                print("max 1 slot every day for each course")
                return False
            perday.append(TT[e][day])
    
    if slot > 0 :
        perday = []
        for e in range(0, slot + 1) :
            if TT[day][e] in perday and TT[day][e] != 0 :
                print("max 1 slot every day for each course")
                return False
            perday.append(TT[day][e])
    
    # partial : C never lesson on two consecutive days
    if day != 0 :
        for aday in range(0, day) :
            if (1 in TT[aday] ) and (1 in TT[aday + 1]) :
                print("C shouldn't lessons on two consecutive days, but he does")
                return False
    
    # partial : F and L can never meet, i.e. their lessons cannot be consecutive
    for x in range(0, day) :
        for y in range(0, 4) :
            if (TT[x][y] == 2 and TT[x][y + 1] == 3) or (TT[x][y] == 3 and TT[x][y + 1] == 2) :
                print("F and L shoudn't meet, but they do")
                return False
    if slot > 0 :
        for y in range(0, slot) :
            if (TT[day][y] == 2 and TT[day][y + 1] == 3) or (TT[day][y] == 3 and TT[day][y + 1] == 2) :
                print("F and L shoudn't meet, but they do")
                return False
                
    return True

#print(checkPartial(0,0,[ [0],[],[],[],[] ])) 
#print(checkPartial(0,3,[ [0,0,4,1],[],[],[],[] ])) 
#print(checkPartial(1,1,[ [0,0,3,2,1] , [2,4],[],[],[] ])) 
#print(checkPartial(1,1,[ [0,0,3,1,2] , [2,4],[],[],[] ])) 
#print(checkPartial(1,4,[ [0,0,3,1,2] , [2,4,0,0,1],[],[],[] ])) 
#print(checkPartial(1, 4, [[0, 0, 1, 0, 4], [0, 2, 0, 0, 3], [1, 2, 0, 4, 3], [0, 0, 0, 3, 4], [1, 2, 0, 0, 0]]))

def insertBT(BT, depth, day, slot, TT):
    # this function inserts [depth,day,slot,TT] into the data structure BT in its right place, 
    # keeping BT sorted from largest depth to smallest. 
    # In case you must insert an element with the same depth as an existing one, it doesn't matter whether inserting it before or after

    # how do you make it? Well, copy my insertBB function and modify it to adapt it to the current situation.
    # that's how 95% of modern programs are written....
    i=0
    print("Insert [",depth,day,slot,TT, "] into",BT, end=" ") 
    while i<len(BT):
        if BT[i][0]<depth:
            BT.insert(i,[depth,day,slot,TT])
            print(" and getting", BT,"\n")
            return
        i=i+1
    BT.append([depth,day,slot,TT])
    print("and getting ", BT,"\n")

# we set up the first branch, i.e. the ROOT, with depth 0, current filled day -1, current filled slot 4 
# (setting -1 and 4 will help you branching correctly into branches with current day 0 and current slot 0)

BT=[[0, -1, 4, [[], [], [], [], []]]]
prof=[0, 1, 2, 3, 4]
# now we loop and write the core of the algorithm
while True:
# we take the first element out from the list and store it in a variable. Do not forget that the element is made up of 
# [depth,day,slot,TT]
# please write the code here
    first = BT.pop()
# we check whether the element we just took out is a leaf, i.e. depth is 25
# In this case, we check its validity and if it is a valid complete solution we print the result. 
# If it is not valid, we have already popped it out and we just go back with the while loop

# please write the code here
    if first[0] == 25:
        the_table = first[3]
        valid = check(the_table)
        if valid :
            print(the_table)
            
    # else when the first element of BT is not a leaf, we have to branch 
    # building all the branches and inserting them in the data structure BT (if they are valid)
    # pay attention when building TT that if slot is equal to 4, you will have to insert a new day

    # NOTE: if for any reason you need to copy a list, beware that a=b is not a duplication of the list but only of the pointer
    # to copy a list duplicating it, use  a=copy.deepcopy(b)  In this way a and b will be two different objects using two different spaces in the memory

    # please write the code here
    depth = copy.deepcopy(first[0]) + 1
    day = copy.deepcopy(first[1])
    slot = copy.deepcopy(first[2]) + 1
    if slot > 4 :
        day = copy.deepcopy(first[1]) + 1
        slot = 0
    for x in range(4, -1, -1) :
        TT = copy.deepcopy(first[3])
        TT[day].append(x)
        valid_partial = checkPartial(day, slot, TT)
        if valid_partial :
            insertBT(BT, depth, day, slot, TT)

def insertBTrandom(BT, depth, day, slot, TT):
    # this function inserts [depth,day,slot,TT] into the data structure BT in its right place, 
    # keeping BT sorted from largest depth to smallest. 
    # In case you must insert an element with the same depth as an existing one, it inserts it randomly
    i=0
    print("Insert [",depth,day,slot,TT, "] into",BT, end=" ") 
    while i<len(BT):
        if BT[i][0]<depth:
            BT.insert(i,[depth,day,slot,TT])
            print(" and getting", BT,"\n")
            return
        i=i+1
    for c in range(len(BT)):
        if BT[c][0] == depth:
            BT.insert(random.randint(0, len(BT)),[depth,day,slot,TT])
            break
    BT.append([depth,day,slot,TT])
    print("and getting ", BT,"\n")

def insertBTColetti(BT, depth, day, slot, TT):
    # this function inserts [depth,day,slot,TT] into the data structure BT in its right place, 
    # keeping BT sorted from largest depth to smallest. 
    # In case you must insert an element with the same depth as an existing one, 
    # if it is a slot with C at the end it is inserted first, otherwise randomly 

    # if you were not able to do the previous procedure, then if it is not C
    # insert it after all the ones with the same depth
    i=0
    print("Insert [",depth,day,slot,TT, "] into",BT, end=" ") 
    while i<len(BT):
        if BT[i][0]<depth:
            BT.insert(i,[depth,day,slot,TT])
            print(" and getting", BT,"\n")
            return
        i=i+1
    for c in range(len(BT)):
        if BT[c][0] == depth:
            if 1 in BT[len(BT)-1][3]:
                BT.insert(len(BT)-2,[depth,day,slot,TT])     
            else:
                BT.insert(random.randint(0, len(BT)),[depth,day,slot,TT])
            break
    BT.append([depth,day,slot,TT])
    print("and getting ", BT,"\n")
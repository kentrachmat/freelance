def check(TT):
    # no lesson on Monday morning, i.e. slots first and second must be 0;
    if TT[0][0] != 0:
        print("Attention: lesson on Monday morning")
        return False
    if TT[0][1] != 0:
        print("Attention: lesson on Monday morning")
        return False
    
    # no lesson on Friday afternoon, i.e. slots third, fourth and fifth must be 0
    if TT[4][2] != 0:
        print("Attention: lesson on Friday afternoon")
        return False
    if TT[4][3] != 0:
        print("Attention: lesson on Friday afternoon")
        return False
    if TT[4][4] != 0:
        print("Attention: lesson on Friday afternoon")
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
            if m[c] == 2 and m[c+1] == 3 :
                print("F and L met")
                return False
            if m[c] == 3 and m[c+1] == 2 :
                print("F and L met")
                return False

    return True


def nextOne(TT,j,i):
    # this function increments by 1 the timetable at day j and hour i, for profs which go from 0 to 4
    if i>4:
        nextOne(TT,j+1,0)
    else:        
        if TT[j][i]<4:
            TT[j][i]+=1
        else:
            TT[j][i]=0
            nextOne(TT,j,i+1)
def nextAttempt(TT):
    nextOne(TT,0,0)
    

TT=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# write here your code



from random import randint

# part 1

def find_TT(TT) :
    """ 
        Will try a table until it finds a right one... takes a while, as expected 

        Returns : 
            TT (list) : a right TimeTable
    """
    result = False
    while result != True :
        result = check(TT)
        nextAttempt(TT)
        print(TT, False)
    print(True)
    return TT

#find_TT(TT)


# part 2
TT2 = [[0,0,0,4,0],[0,0,0,0,0],[0,0,4,0,0],[0,0,0,0,0],[0,4,0,0,0]]

def nextOne_v2(TT,j,i):
    # this function increments by 1 the timetable at day j and hour i, for profs which go from 0 to 4
        if i>4:
            nextOne_v2(TT,j+1,0)
        else:
            if TT[j][i]<3 :
                TT[j][i]+=1
            elif TT[j][i] == 4 :
                nextOne_v2(TT,j,i+1)
            else:
                TT[j][i]=0
                nextOne_v2(TT,j,i+1)

def nextAttempt_v2(TT2) :
    nextOne_v2(TT2,0,0)

def find_TT_v2(TT2) :
    """ 
        Will try a table until it finds a right one... takes a while, as expected 

        Returns : 
            TT (list) : a right TimeTable
    """
    result = False
    while result != True :
        result = check(TT2)
        nextAttempt_v2(TT2)
        print(TT2, False)
    print(True)
    return TT2

#find_TT_v2(TT2)


# part 3




from random import randint


def fill_TT(TT) :
    for day in TT :
        for i in range(0,5) :
            alea = randint(0,4)
            day[i] = alea
    table = TT
    return table

#print(fill_TT(TT))

def fizzy_right(TT) :
    count = 1
    tab = fill_TT(TT)
    res = check(tab)
    while res == False :
        tab = fill_TT(TT)
        res = check(tab)
        print(tab)
        count += 1
    return count, tab


#print(fizzy_right(TT))
        
        
# part 4

def optimized(TT) :
    """
        Will give a timetable with maximum 3 courses of each a week


        Returns :
            TT (list) : a Timetable

    """
    

    for i in range(1,5) :
        for y in range(0,3) :
            TT[randint(0,4)][randint(0,4)] = i
    return TT
print(optimized(TT))

def opti_right(TT) :
    """
        will find a right optimized Timetable

        Returns :
            TT2 (list) : a right Timetable
            count (int) : the number of attempt in order to get a right Timetable
    """
    count = 1
    
    while True:
        tab = optimized(TT)
        TT=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        print(tab)
        res = check(tab)
        count += 1
        if res == True :
            return tab, count


print(opti_right(TT))
# SORT THE ITEMS

import copy

N=["water","blanket","food","binocular"]
S=[3,6,4,3]
U=[5,7,8,4]

def bubbleSort(U,S,N):
# your code here. You do not need to use bubbleSort, you can use any other sorting algorithm you want
    U, S, N = zip(*sorted(zip(U, S, N), reverse = True))
    return list(U), list(S), list(N)

N = ['food', 'blanket', 'water', 'binocular']
S = [4, 6, 3, 3]
U = [8, 7, 5, 4]


def calcUtil(U,Status):
    # this function calculates the utility scalar-multiplying the utility list with the bool list 
    # (this means U[0]*Status[0]+U[1]*Status[1]+...+U[N]*Status[N])
    # PAY ATTENTION that Status is shorter (it contains the items decided so far and not the other items), 
    # you will have to skip the rest of U
    
    # write your code here
    utility = 0
    for x in range(len(Status)) :
        if Status[x] == True :
            utility += U[x]
    return utility
#print(calcUtil(U,[True,False,True])) 

    
    
def calcMaxUtil(U,Status):
    # this function calculates the maximum utility exactly as the previous function but once Status is over you have to...

    # write your code here
    maxUtility = sum(U)
    for x in range(len(Status)) :
        if Status[x] == False :
            maxUtility -= U[x]
    return maxUtility
#print(calcMaxUtil(U,[False]))


def insertBB(BB,maxutility,utility,size,Status):
    # this function inserts [maxutility,utility,size,Status] into the data structure BB in its right place, 
    # keeping BB sorted from largest maxutility to smallest
    i=0
    print("Insert [",maxutility,utility,size,Status, "] into",BB, end=" ") 
    while i<len(BB):
        if BB[i][0]<maxutility: # let's see whether we find a space for our maxutility
            BB.insert(i,[maxutility,utility,size,Status])
            print(" and getting", BB,"\n")
            return # I return just to interrupt the procedure, there is nothing to return here
        i=i+1
    # if we arrive here we have not yet inserted it, so it goes at the end
    BB.append([maxutility,utility,size,Status])
    print("and getting ", BB,"\n")
    
# I have already written this procedure for you to avoid that you spend too much time.
# thre procedure also prints some debugging information
    
    
# here the program starts, let's set up the situation of the example 
# (to apply it to another example you have just to modify these values)
N=["water","blanket","food","binocular", "rope", "Mom", "PS5", "pencil", "tire", "Superman"]
S=[3,6,4,3, 2, 6, 5, 3, 7, 1]
U=[5,7,8,4, 6, 10, 1, 2, 1, 10]
maxSize=20



# we sort the data by utility
# please do it

#print(bubbleSort(U,S,N))

N = ['Mom', 'Superman', 'food', 'blanket', 'rope', 'water', 'binocular', 'pencil', 'tire', 'PS5']
S = [6, 1, 4, 6, 2, 3, 3, 3, 7, 5]
U = [10, 10, 8, 7, 6, 5, 4, 2, 1, 1]


# we set up the first branch, i.e. the ROOT
# please do it, look at the picture for how is the root of the tree
maxutility = sum(U)
utility = 0
size = 0
Status = []
# we put the first branch in the BB list
# easy peasy, you have a function which does it!
#insertBB([], maxutility, utility, size, Status)
BB = [[maxutility, 0, 0, []]]
# now we loop and write the core of the algorithm
while True:
    # we take the first element out from the list and store it in a variable. Do not forget that the element is made up of 
    # [maxutility,utility,size,Status]
    # please write the code here
    first = BB[0]
    # we check whether the element we just took out is a leaf, i.e. Status has exactly length equal to the number of items. 
    # In this case, it is finished and we print the result.
    # it would be nice to print the result in a human-readable form, such as:
    # take food
    # leave blanket
    # take water
    # take binocular
    
    # please write the code here
    if len(first[3]) == len(U) :
        bools = first[3]
        print(first)
        for x in range(len(bools)) :
            if bools[x] :
                print("Take " + N[x])
            else :
                print("Leave "+ N[x])
        break
    
    # else when the first element of BB is not a leaf, we have to branch 
    # building both branches and inserting them in the data structure BB (if they do not exceed the size)

    # branch left, we consider the next item and we DO take it. We have to update utility and size, maxutility remains the same
    # this might have a consequence that we exceed the size and in this case we do NOT insert it in the BB structure

    # NOTE: if for any reason you need to copy a list, beware that a=b is not a duplication of the list but only of the pointer
    # to copy a list duplicating it, use  a=copy.deepcopy(b)  In this way a and b will be two different objects using two different spaces in the memory
    
    # please write the code here
    BB.pop(0)
    Status = first[3]
    if len(Status) > 0 and Status[-1] == False :
        Ot_copy = copy.deepcopy(Status)
        maxutility = calcMaxUtil(U, Ot_copy)
    Status.append(True)
    St_copy = copy.deepcopy(Status)
    Status.pop()
    pot_uti = calcUtil(U, St_copy)
    pot_size = calcUtil(S, St_copy)
    bo = (pot_size <= maxSize)
    if bo :
        insertBB(BB, maxutility, pot_uti, pot_size, St_copy)
    
    
    # branch right, we consider the next item and we DO NOT take it. We have to update maxutility, while utility and size remain the same
    # there is no risk  that the size is exceeded

    # please write the code here
    Status.append(False)
    Ot_copy = copy.deepcopy(Status)
    pot_max = calcMaxUtil(U, Ot_copy)
    insertBB(BB, pot_max, utility, size, Ot_copy)
    if bo :
        utility = pot_uti
        size = pot_size
        
import random
listSize = 20   # arbit listSize
domain = 50     # arbit domain

def init():
    global a
    a = []
    for x in range(listSize):
        a.append(random.randint(0,domain))
    a.sort()        # sorting and ridding dupes
    set(a)
        
def findEvenNum(list):
    res = []
    for x in list:
        if x%2 == 0:
            res.append(x)
    return res

if __name__ == '__main__':
    init()
    print('a: ' + str(a))
    print('Even numbers of a: ' + str(findEvenNum(a)))
    
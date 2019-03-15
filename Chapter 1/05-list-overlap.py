import random
listSize = 20       # arbit listSize
domain = 50         # arbit domain

def init():
    global a, b
    a = []
    b = []
    for x in range(listSize):
        a.append(random.randint(0,domain))
        b.append(random.randint(0,domain))
    a.sort()
    b.sort()
    
def findIntersects(a, b):
    if len(a) == 0 or len(b) == 0:
        return  # Invalid statement
    res = []
    for x in range(len(b)):
        if a[x] in b:
            res.append(a[x])
    set(res)
    return res
    
if __name__ == '__main__':
    init()
    print('a: ' + str(a))
    print('b: ' + str(b))   
    print('Intersects: ' + str(findIntersects(a,b)))
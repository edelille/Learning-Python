import random
listSize = 10  # arbit size of list, as as will

def init():
    global list
    list = [0] * listSize
    for x in range(len(list)):
        list[x] = random.randint(0,100)
    
if __name__ == "__main__":
    init()
    
    DET = int(input('I will print out values of the list which are lower than '
                    'your input int:'))
                    
    for x in range(len(list)):
        a = list[x]
        if(a < DET):
            print('%d This is smaller than your int!' % a)
        else:
            print(a)
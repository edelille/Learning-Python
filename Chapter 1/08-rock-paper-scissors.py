import re
import random

def cleanList(a):
    for x in range(len(a)):
        a[x] = a[x].lower()
    a = set(a)
    return a
    
def userChoice(a):
    res = re.findall(r'(?i)(rock|paper|scissors)', a)
    res = cleanList(res)
    r = True if 'rock' in res else False
    p = True if 'paper' in res else False
    s = True if 'scissors' in res else False
    if p and s or (r and (p or s)): return -1
    elif r: return 1
    elif p: return 2
    elif s: return 3
    else: return 0
        
    return res
    
def botChoice():
    return random.randint(1,3)
    
def rockPaperScissors(a):
    DET = {
        -1: 'more than 1 option',
        0: 'none of the options',
        1: 'Rock',
        2: 'Paper',
        3: 'Scissors',    
    }
    return DET.get(a)

def winDET(a):
    global uChoice, bChoice
    a = userChoice(a)
    b = botChoice()
    uChoice = rockPaperScissors(a)
    bChoice = rockPaperScissors(b)
    if a == 1 and b == 3:
        return 1
    elif a < b:
        return -1
    else:
        return 0
    
if __name__ == '__main__':
    uChoice = ''
    bChoice = ''
    while True:
        inp = input('Rock Paper or Scissors: ')
        if inp == '':
            break
        win = winDET(inp)
        print('You chose: %s\nRobot chose: %s' % (uChoice, bChoice))
        if win == 0:
            print('You tied the robot\n')
        elif win == -1:
            print('You lost to the robot\n')
        else:
            print('You won to the robot!\n')
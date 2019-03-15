import math

def highestPowerof2(n):
    if n < 1:
        return 0  # Invalid Input
    
    res = 1       # Default return
    for x in range(1, 8):
        curr = 1 << x
        
        if curr > n:
            break
        res = curr
    return res

def highestPowerof2log(n):
    # Uses log to find highest power of 2 of n
    if n < 1:
        return 0  # Invalid Input
        
    p = int(math.log(n,2))
    return int(pow(2,p))

def JosephusDET(n):
    # Express n as 2^a + l
    # W(n) = 2l + 1
    l = n - highestPowerof2log(n)
    Winner = 2*l + 1
    return Winner  # W(n)
    
while True:
	inp = input('Enter the number of soldiers: ')
	if inp == '':
		break
	numSoldiers = int(inp)
	print('The winner is: %d' % JosephusDET(numSoldiers))
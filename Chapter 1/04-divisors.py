def findDivisors(list, n):
    for x in range(n, 0, -1):
        if n%x == 0:
            list.append(x)

if __name__ == '__main__':
    n = int(input('Enter a number to find all divisors of: '))
    listOfDivisors = []
    findDivisors(listOfDivisors, n)
    for x in listOfDivisors:
        print(x)
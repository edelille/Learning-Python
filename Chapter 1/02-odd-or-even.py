def oddOrEven(n):
    if n%2 == 1:
        return 'Odd!'
    else:
        return 'Even!'

if __name__ == '__main__':
    print('This program will print out whether the integer is odd or even, Go ahead:')
    while True:
        inp = input('')
        if inp == '':
            break
        print(oddOrEven(int(inp)))
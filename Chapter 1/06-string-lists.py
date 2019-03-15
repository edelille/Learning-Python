def isPalindrome(a):
    n = len(a) - 1
    for m in range(0, n):
        if a[m] != a[n]:
            return False
        n -= 1
    return True
    
if __name__ == '__main__':
    while True:
        inp = input("Enter suspect Palindrome: ")
        if inp == '':
            break
        
        if isPalindrome(inp):
            print('This is a Palindrome!')
        else:
            print('Nope, this is not.')
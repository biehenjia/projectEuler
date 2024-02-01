

def isPalindrome(num):
    lnum = str(num)
    return lnum == lnum[::-1]

maxval = 0
for i in range(902):
    for j in range(902):
        if isPalindrome((1000-i)*(1000-j)): 
            print((1000-j)*(1000-i))
            maxval = max(maxval,(1000-j)*(1000-i))
            break
print(maxval)
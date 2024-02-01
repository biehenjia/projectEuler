res = 0
prev1,prev2=1,2

while prev2 < 4 * 10**6:
    placeholder = prev1 + prev2
    prev1 = prev2
    if not prev2 %2: 
        res += prev2
    prev2 = placeholder

print(res)
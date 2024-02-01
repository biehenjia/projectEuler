number = 600851475143
prime = 2
for i in range(2,number):
    if number == 1: break
    while not number%i:
        number //= i
        prime = max(prime,i)
        print(i)
print(prime)

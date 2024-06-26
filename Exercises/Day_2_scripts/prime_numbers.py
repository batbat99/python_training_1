def is_prime(n: int):
    if n > 1:
        for i in range(2,n//2+1):
            if n % i == 0:
                return False
        return True
    else:
        return
    
x = int(input("Please enter a number: "))

counter = 0

for i in range(2,x+1):
    if is_prime(i):
        counter += 1

print(counter)
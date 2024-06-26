def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def list_factorial(l):
    return [factorial(f) for f in l]
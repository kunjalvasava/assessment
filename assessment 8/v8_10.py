def is_armstrong(n):
    temp = n
    total = 0
    digits=len(str(n))
    while temp > 0:
        d=temp %10
        total+=d**digits
        temp //= 10
    return total == n
print(is_armstrong(153))    
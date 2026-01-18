a=int(input("Enter first nnumber : "))
b=int(input("Enter second nnumber : "))
c=int(input("Enter third nnumber : "))
if a == b == c :
    print("Equilateral")
elif a == b != c or b == c != a or a == c != b:
    print("isoscales")
elif a != b != c:
    print("scalene")    
else:
    print("Not a type of triangle")        
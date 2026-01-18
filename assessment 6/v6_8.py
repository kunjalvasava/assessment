try:
    a=int(input("Enter first number :"))
    b=int(input("Enter second number :"))
    print(a/b)
except (ValueError , ZeroDivisionError) as e:
    print("Error:",e)    
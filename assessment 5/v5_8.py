unit=int(input("Enter units consumed :"))
if unit <= 100:
    bill=unit*2
elif unit <= 200:
    bill=unit*3
else :
    bill=unit*5    
print("Bill :",bill)
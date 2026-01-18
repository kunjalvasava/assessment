try:
    a=int(input("Enter number :"))
    b=int(input("Enter number :"))
    print(a/b)
except Exception as e: 
    with open("error.log","a") as f:         
        f.write(str(e) + "\n")
    print("Error logged to file")
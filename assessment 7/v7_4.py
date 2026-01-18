with open("sentances.txt","w") as f:
    for i in range(5):
        s=input("Enter sentance :") 
        f.write(s + "\n")

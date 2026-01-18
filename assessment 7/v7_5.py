items=["Apple","Banana","Mango"]
with open("data.txt","a") as f:
    for item in items:
        f.write(item + "\n")

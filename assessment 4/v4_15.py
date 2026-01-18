#Create a nested list and access a specific inner element
list=["10","20",["20.5","20.10"],"20","30"]
a="20"
count=0
for i in list:
    if i==a:
        count=count+1
print("number",a,"count in list : ",count,"times..")

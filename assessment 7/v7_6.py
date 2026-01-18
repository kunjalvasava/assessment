word=input("Enter word to find :")
with open("data.txt","r") as f:
     for line in f:
          if word in line:
               print(line)
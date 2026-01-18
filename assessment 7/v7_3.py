word = input("Enter word to search : ")
with open("data.txt","r") as f:
    content = f.read()
    count = content.count(word)

    print("Word count :",count)


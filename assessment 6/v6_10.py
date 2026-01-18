email=input("Enter email :")
if "@" not in email or "." not in email :
    raise Exception("Invalid email format")
else:
    print("Valid email")
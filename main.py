#myUser = {"name": "Mira", "age": 28}
#print(f"Your name is {myUser['name']} and your age is {myUser['age']}")

myUser = {"name":"Andy", "age":128}
myUser["age"] = 129

print("Contact Card") 
name = input("Input your name >").strip()
dob = input("Input your date of birt >").strip()
telephone = input("Input your telephone number >").strip()
email = input("Input your email address >").strip()
address = input("Input your address > ").strip()
myUser = {"name":name, "dob":dob, "telephone":telephone, "email": email, "address": address}
print(f"Hi {myUser['name']}.Our dictionary says that you were born on {myUser['dob']}, we can call you on {myUser['telephone']}, email {myUser['email']}, or write to {myUser['address']}.")
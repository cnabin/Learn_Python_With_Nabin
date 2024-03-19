age=int(input("Enter your age:"))
# print("Entered age is : " +age)

if age>=18 and age<50:
    print("You can drink")
elif age>50:
    print(f"You can't drink, You are too old because your age is greater than {age}")  #formatted String : f "{ }"
else:
    print(f"You are under age because your age is less than {age}")
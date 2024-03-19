# Exam program Requirements
# Ask the user for his/her exam percentage
# If the percentage is 90 to 100 print Outstanding.
# If the percentage is 80 to 90 print Excellent.
# If the percentage is 70 to 80 print Very good.
# If the percentage is 60 to 70 print good.
# If the percentage is 50 to 60 print better.
# If the percentage is 40 to 50 print passed.
# If the percentage is below 40 print failed.

percentage=int(input("Enter Your Exam Percentage: "))

if percentage>=90 and percentage<=100:
    print("Outstanding")

elif percentage>=80 and percentage<90:
    print("Excellent")

elif percentage>=70 and percentage<80:
    print("Very good")

elif percentage>=60 and percentage<70:
    print("good")

elif percentage>=50 and percentage<60:
    print("better")

elif percentage>=40 and percentage<50:
    print("passed")

else:
    print("failed")
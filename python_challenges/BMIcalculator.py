height=int(input("Enter your height in cm: "))
weight=int(input("Enter your weight in kg: "))

BMI = weight/(height/100)**2
print(f"Your BMI is : {BMI}")

if BMI <= 18.5:
    print("You are under weight")
elif BMI <= 24.9:
    print("you are in shape")
elif BMI <= 29.9:
    print("You are over weight")
else:
    print("You are obese")
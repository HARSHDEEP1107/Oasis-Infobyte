print("Calculation of BMI of an Individual\n")
weight=float(input("Enter Your Weight:"))
height=float(input("Enter Your Height:"))
height_in_metres=height/100
bmi=weight/(height_in_metres**2)
print("Your BMI is:",bmi)
if bmi<18.5:
    print("You're underweight")
elif 18.5<=bmi<25:
    print("You're a normal Weight")
elif 25<=bmi<30:
    print("You're overweight")
else:
    print("You are obese")            

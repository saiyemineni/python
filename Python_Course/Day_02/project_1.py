# Create a BMI calculator
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

BMI = weight /(height**2)


print(f"Your BMI for weight: {weight} and height: {height} is {BMI}")
print(BMI)
print(int(BMI))
print(round(BMI))
print(round(BMI,2))
print(type(BMI))


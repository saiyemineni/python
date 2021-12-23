weight = float(input("Weight: "))
height = float(input("Height: "))

if height > 3 :
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
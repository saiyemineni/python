fruits = ['Apple','Peach','Pears']
for fruit in fruits:
    print(fruit)
    print(fruit+" Pie")

#Averge height of the students

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
count = 0
sum = 0
for height in student_heights:
    sum += height
    count+=1
Average = sum/count
Average = round(Average)
print(f"The average height of students in the class is {Average}")
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
student_grades = {}
for student in student_scores:
    marks = student_scores[student]
    if marks >= 91 and  marks <= 100:
        student_grades[student] = "Outstanding"
    elif marks >= 81 and  marks <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif marks >= 71 and  marks <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)
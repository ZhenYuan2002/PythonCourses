student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}


#My take
for student in student_scores:
  if student_scores[student] > 90:
    student_scores[student] = 'Outstanding'
  elif student_scores[student] >= 81 and student_scores[student] <= 90:
    student_scores[student] = 'Exceeds Expectations'
  elif student_scores[student] >= 71 and student_scores[student] <= 80:
    student_scores[student] = 'Acceptable'
  else:
    student_scores[student] = 'Fail'
    print(student_scores)

#Course answer
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)


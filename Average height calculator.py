#My answer
studentheights = input("Enter student heights separated by space:\n")
student_heights = studentheights.split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

totalheight = sum(student_heights)
averageheight = int(totalheight / len(student_heights))
print('Total height = ' + str(sum(student_heights)))
print('Number of students = ' + str(len(student_heights)))
print('Average height = ' + str(averageheight))


#Course Answer
studentheights = input("Enter student heights separated by space:\n")
student_heights = studentheights.split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")

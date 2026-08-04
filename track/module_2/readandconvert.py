# Read and convert the student details
student_name = input()
student_age = input()
course_rating = input()
student_age = int(student_age)
course_rating = float(course_rating)
# Display the values
print(f"Student: {student_name}")
print(f"Age: {student_age}")
print(f"Rating: {course_rating}")
# Display type 
print(type(student_name))
print(type(student_age))
print(type(course_rating))
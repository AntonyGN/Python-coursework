#elif_statement
#grading statement

maths = int(input("Enter score in Maths "))
english = int(input("Enter score in English "))
kiswahili = int(input("Enter score in Kiswahili "))
chemistry = int(input("Enter the score in Chemistry "))
physics = int(input("Enter the score in Physics "))

total = maths + english + kiswahili + chemistry + physics
score = total/5

if score >=70 and score <=100:
  grade = "A"
elif score >=60 and score <=69:
  grade = "B"
elif score >=50 and score <=59:
  grade = "C"
elif score >=40 and score <=49:
  grade = "D"
elif score >=0 and score <=39:
  grade = "Fail"

print(grade)

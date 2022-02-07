#if else statement
salary = int(input("Enter the salary "))
year = int(input("Enter the years of service "))

if year>10:
  bonus = salary*0.1 
elif year>=6 and year <=10:
  bonus = salary*0.08
else :
  bonus = salary*0.05
print(bonus)


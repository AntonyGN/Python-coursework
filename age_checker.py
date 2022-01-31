#logical operator
citizen=(input("Are you a kenyan citizen: yes or no ")).lower()
age=int(input("what is your age: "))
if(citizen=="yes" and age>=18):
  print("You can vote")
else:
  print("You can't vote")
#Assighnment_1

#Question_1
#a
print(10*(90+2)-5)
#b
print(10*90+2-5)
#c
print(10*90+(2-5))
#d
print(10.0*(90+2)-5)
#e
print(120/(20+40)-(6-2)/4)
#f
print(5.0/2)
#g
print(5/2)
#h
print(5.0/2.0)
#i
print(5/2.0)
#j
print(678%3*(8-(9/4)))


#Question_2
#ID
user_id = input("Eter your ID: ")
print("Your ID is:", "0" + user_id) 
#Name
user_name = input("Enter you name: ")
user_name = user_name.upper()
print("your name is:", user_name)
#Date of Birth
user_dob = input("Enter your birth of date: ")
for i in range(len(user_dob)):
  if user_dob[i] == "-":
    user_dob = user_dob[0:i] + "/" + user_dob[i+1:]
print("your date of birth is: ",user_dob)
#Adress
user_address = input("Enter your adress: ")
user_address = user_address.lower().strip()
print("Your adress is:", user_address)


#Question_3
number = input("Enter a number: ")
count = 0
for i in range(len(number)):
  count += 1
print(number, "has", count, "digits")


#Question_4
grade = eval(input("Enter your grade: "))
letter_grade = ""
if (grade >= 90):
  if (grade >= 97):
    letter_grade = "A+"
  elif (grade >= 93):
    letter_grade = "A"
  else: letter_grade = "A-"
elif (grade >= 80):
  if (grade >= 87):
     letter_grade = "B+"
  elif (grade >= 83):
     letter_grade = "B"
  else: letter_grade = "B-"
elif (grade >= 70):
  if (grade >= 77):
     letter_grade = "C+"
  elif (grade >= 73):
     letter_grade = "C"
  else: letter_grade = "C-"
elif (grade >= 60):
  if (grade >= 67):
     letter_grade = "D+"
  elif (grade >= 63):
     letter_grade= 'D'
  else: letter_grade = "D-"
else: letter_grade = "F"
print("your letter grade is: ", letter_grade)


#Question_5
number = int(input("Enter a number: "))
for i in range(1, number):
 print("*"*i)
for j in range(number, 0, -1):
  print("*"*j)
  

#Question_6
num_1 = eval(input("Enter your first number: "))
num_2 = eval(input("Enter your second number: "))
while num_1 > num_2 :
  print("second number must be larger than the first number")
  num_1 = eval(input("Enter your first number: "))
  num_2 = eval(input("Enter your second number: "))
for i in range(num_1, num_2+1):
  if i%2 == 0:
    print(i)
####end####
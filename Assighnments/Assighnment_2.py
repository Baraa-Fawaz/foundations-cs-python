#Assighnment_2
#Question_1
def reversWord(s, i):
  str = ""
  if i == 0:
    return str
  else:
    for j in range(len(s) - 1, -1, -1):
      str += s[j]
    return str * i


string = input("Enter a word to be reversed: ")
integer = eval(input("Enter a number: "))
print("the revers of", string, integer, "times is",
      reversWord(string, integer))


#Question_2
def arangeUpperAndLower(s):
  upper = ""
  lower = ""
  for i in s:
    if i == i.upper():
      upper += i
    if i == i.lower():
      lower += i
  return upper + lower


string = input("Enter a word: ")
print("The arangment of", string, "is", arangeUpperAndLower(string))


#Question_3
def checkreordering(s1, s2):
  return sorted(s1) == sorted(s2)


string_1 = input("Enter the first word: ")
string_2 = input("Enter the second word: ")
print(checkreordering(string_1, string_2))


#Question_4
def findMaxValue(lst):
  max_value = lst[0]
  for i in range(1, len(lst)):
    if lst[i] > max_value:
      max_value = lst[i]
  return max_value


list = input("Enter elements of a list separated by space: ")
list_1 = list.split()
list_1 = [int(x) for x in list_1]
print("The highest value is", findMaxValue(list_1))


#Question_4_2
def findLowestValue(lst):
  Lowest_value = lst[0]
  for i in range(1, len(lst)):
    if lst[i] < Lowest_value:
      Lowest_value = lst[i]
  return Lowest_value


list = input("Enter elements of a list separated by space: ")
list_1 = list.split()
list_1 = [int(x) for x in list_1]
print("The Lowest value is", findLowestValue(list_1))


#Question_5
def calcSum(num):
  if num == 0:
    return 0
  else:
    return (num % 10) + (calcSum(num // 10))


number = eval(input(("Enter a number: ")))
print("the sum of digits of", number, "is equal to", calcSum(number))


#Question_6
def removeDuplicate(str):
  if len(str) < 2:
    return str
  elif str[0] == str[1]:
    return removeDuplicate(str[1:])
  else:
    return str[0] + removeDuplicate(str[1:])


string = input("Enter a word to remove is duplicate values: ")
print(removeDuplicate(string))


#Question_7
def reversNumber(n):
  if n < 10:
    return n
  else:
    return int(str(n % 10) + str(reversNumber(n // 10)))


number = eval(input("Enter a number: "))
print(reversNumber(number))
####end####

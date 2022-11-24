import random

def generatingNumbers(min,max):
  number1 = random.randint(min,max)
  number2 = random.randint(min,max)
 
  return number1, number2


def result(list):
 return list[0] + list[1]


num1 = int(input("Enter the min number"))
num2 = int(input("Enter the max number"))
nums = generatingNumbers(num1,num2)


finalResult = result(nums)
answer = ""

while(answer != finalResult):
  answer = int(input("What is " + str(nums[0]) + " + " + str(nums[1]) + " ?"))

print("You guessed it correctly")
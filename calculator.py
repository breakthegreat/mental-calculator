import random
import time


def generatingNumbers(min, max):
    number1 = random.randint(min, max)
    number2 = random.randint(min, max)

    return number1, number2


def resultAdd(list):
    return list[0] + list[1]


def resultSub(list):
    return list[0] - list[1]


def resultDiv(list):
    return list[0] / list[1]


def resultMulti(list):
    return list[0] * list[1]


num1 = int(input("Enter the min number"))
num2 = int(input("Enter the max number"))
nums = generatingNumbers(num1, num2)


finalResult = resultAdd(nums)
initial = time.time()
answer = ""

while (answer != finalResult):

    answer = int(
        input("What is " + str(nums[0]) + " + " + str(nums[1]) + " ?"))
seconds = time.time()
finalSecond = str(seconds - initial)
finalSecond = finalSecond[0:4]  # get only up to 2 decimals
print("You guessed it correctly! it took you " + finalSecond + " seconds")

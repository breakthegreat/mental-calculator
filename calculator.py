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


num1 = int(input("Enter the min number: "))
num2 = int(input("Enter the max number: "))

while (True):
    choosing = True
    add = False
    sub = False
    div = False
    multi = False
    while (choosing):
        nums = generatingNumbers(num1, num2)
        operation = input(
            "What type of operation do you want to perfom? (ADD/SUB/MULTI/DIV) or type quit to exit ")
        if (operation.lower() == "add"):
            finalResult = resultAdd(nums)
            choosing = False
            add = True
        elif (operation.lower() == "sub"):
            finalResult = resultSub(nums)
            choosing = False
            sub = True
        elif (operation.lower() == "multi"):
            finalResult = resultMulti(nums)
            choosing = False
            multi = True
        elif (operation.lower() == "div"):
            finalResult = resultDiv(nums)  # FIX THIS FLOAT NUMBER !!!
            choosing = False
            div = True
        elif (operation.lower() == "quit"):
            quit()
        else:
            print("Incorrect input please retype ")

    initial = time.time()
    answer = ""

    while (answer != finalResult):
        if (add):
            answer = int(
                input("What is " + str(nums[0]) + " + " + str(nums[1]) + " ? "))
        elif (sub):
            answer = int(
                input("What is " + str(nums[0]) + " - " + str(nums[1]) + " ? "))
        elif (div):
            answer = int(
                input("What is " + str(nums[0]) + " / " + str(nums[1]) + " ? "))
        elif (multi):
            answer = int(
                input("What is " + str(nums[0]) + " * " + str(nums[1]) + " ? "))

        # TODO ADD MORE INPUT ACCORDING TO EACH OPERATION CHOSED
    seconds = time.time()
    finalSecond = str(seconds - initial)
    finalSecond = finalSecond[0:4]  # get only up to 2 decimals
    print("You guessed it correctly! it took you " + finalSecond + " seconds")

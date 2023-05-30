#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 != 0:
            print("Fizz ", end="")
        elif number % 5 == 0 and number % 3 != 0:
            if number == 100:
                print("Buzz", end=" ")
            else:
                print("Buzz ", end="")
        elif number % 3 != 0 or number % 5 != 0:
            print(number, end=" ")
        else:
            print("FizzBuzz ", end="")

"""
File: hailstone.py
Name: Justin Kao
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Use while loop to keep doing Hailstone sequence.
        If the number entered is a Even number, divided by 2.
        If the number entered is a Odd number, make 3n+1.
        Use another variable(num_old) to store the previous number when printing out.
    """
    print("This program computes Hailstone sequences!")
    num = int(input("Enter a number: "))
    print("----------------------------------")
    count = 0
    while True:
        if num == 1:
            break
        if num % 2 == 1:   # Odd number
            num_old = num  # Previous number
            num = int(num*3+1)
            print(str(num_old) + " is odd, so I make 3n+1: " + str(num))
        else:              # Even number
            num_old = num  # Previous number
            num = int(num / 2)
            print(str(num_old) + " is even, so I take half: " + str(num))
        count += 1
    print("I took " + str(count) + " steps to reach 1.")
###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()

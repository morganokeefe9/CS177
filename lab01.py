
# CS 177 Lab Introduction
# This is my first Python program – labintro.py
# Morgan O'Keefe


def main():

    print("This program prompts the user for their name")

    print(" and their height in feet and inches.")

    print(" After that, it displays (who is here today) song, ")

    print(" calculates and displays the height in centimeters ")

    print()

   

    # Prompt the user for name and age

    name = input("Please enter your name: ")

    feet = eval(input("Enter your height (the feet part) "))

    inches = eval(input("Enter your height (the inches part) "))


    print()

   

    # Display the song

    print(name, "is here today")

    print(name, "is here today")

    print(name, "is here today")

    print("we're so happy that", name, "is here today")

    print()

   

    # Calculate and display the height in centimeters

    height =  (feet * 30.48) + (inches * 2.54)

    print("Your height in centimeters is ", height)


main()

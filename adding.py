#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Apr 2022
# This program adds all the integers between one and a number


def main():
    # This function adds numbers

    # This is to keep track of how many times you go through the loop
    loop_counter = 0

    # This is used to calculate the output
    answer = 0

    # input
    string = input("Please enter a positive integer: ")

    # process & output
    print("")
    try:
        number = int(string)
        if number < 0:
            print("{} is not positive :c".format(number))
        else:
            while loop_counter < number:
                loop_counter = loop_counter + 1
                answer = answer + loop_counter
            print(
                "The sum of all integer between 0 to {0} is {1}.".format(number, answer)
            )
    except Exception:
        print("{} is not an integer.".format(string))

    print("\nDone.")


if __name__ == "__main__":
    main()

import sys

def Number_checker():

    answer = None
    while answer is None or answer < 1 or answer > 10:
        try:
            # prompt for user input
            answer = int(input("Enter a number between 1 and 10\n"))

        except ValueError:
            # Checking for non-integer input
            print("Please enter a valid integer", flush=True)
            sys.stdout.flush()
            continue

         # Verifying right range of user input
        if answer < 1 or answer > 10:
            print("please enter a number between 1 and 10")
            sys.stdout.flush()
            answer = None
            continue


    print("Final answer is " + str(answer))


if __name__ == "__main__":
    Number_checker()

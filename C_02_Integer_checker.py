def integer_checker(question):
    error = f"Please enter a whole number between 1 and 200\n"
    while True:
        try:
            # ask the user for a width
            response = input(question)

            # check the number is more than 0
            if response == "xxx":
                return response

            else:

                if 1 <= int(response) <= 200:
                    return response

                else:
                    print(error)

        except ValueError:

            print(error)


# Main routine goes here
while True:

    integer = integer_checker("Integer: ")

    if integer == "xxx":

        break

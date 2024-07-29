def integer_checker(question):
    error = f"Please enter a whole number between 1 and 200\n"
    while True:

        # ask the user for a integer
        response = input(question)

        # xxx break code
        if response == "xxx":
            return response

        try:

            response = int(response)
            # see if number between 1 and 200
            if 1 <= response <= 200:
                return response

            else:
                print(error)

        except ValueError:

            print(error)


def find_unity(number):

    error = "This number has no factors apart from 1"
    if number == 1:
        return error


# Main routine goes here

while True:

    integer = integer_checker("Integer: ")

    if integer == "xxx":

        break

    answer = find_unity(integer)
    print(answer)

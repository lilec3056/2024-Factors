# Functions go here.
# Generates heading (eg: ----- Heading -----).
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions.

def instructions():
    statement_generator("Instructions", "-")

    print('''
- Enter an integer between 1 and 200.
- Type "xxx" to exit.

''')


# Checks for an integer and break code.
def integer_checker(question):
    error = f"Please enter a whole number between 1 and 200.\n"
    while True:

        # ask the user for an integer
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
        # if the number entered is not a number or xxx it'll output an error.
        except ValueError:

            print(error)


# Finds all the factors and outputs them.
# Also tells us if the number is a prime, unity, or perfect square.
def factor_finder(needs_factoring):
    # Makes list for all the factors.
    all_factors = []

    for item in range(1, 201):
        # Multiplies by every number from 1 to 201 (you can't enter 201).
        num_left = needs_factoring % item
        # If number fits evenly it will add it to the list
        if num_left == 0:
            all_factors.append(item)
    # Finds out if the number is unity.
    if len(all_factors) == 1:
        print()
        print("1 is UNITY (has only one factor, itself).")
        print()
    # Finds out if the number is a prime number.
    elif len(all_factors) == 2:
        print(f'''
{all_factors}
{needs_factoring} a prime number''')
        print()
    # Finds out if the number is a perfect square and outputs it.
    elif all_factors.__contains__(needs_factoring ** 0.5):
        print()
        print(f"The factors of {needs_factoring} are as follows:")
        all_factors.sort()
        print(all_factors)
        print(f"The square root of {needs_factoring} is {int(needs_factoring ** 0.5)}.")
        print(f"This means {needs_factoring} is a perfect square.")
        print()
    # If the number is nothing special this outputs its factors.
    else:
        print()
        print(f"The factors of {needs_factoring} are as follows:")
        all_factors.sort()
        print(all_factors)
        print()


# Main routine goes here.
statement_generator("Cameron's Fabulous Factor Finder", "-")

# Display instructions if requested.

print()

want_instructions = input("Press <enter> to read the instructions or any key to continue (then press <enter>). ")

if want_instructions == "":
    instructions()
# Loops the code, exit code = xxx.
while True:
    # Gets the integer from the user and double checks that it's an integer between 1-200
    # just in case they can't read or don't read the instructions.
    to_factor = integer_checker("Number you want factorized: ")
    # Exit code.
    if to_factor == "xxx":
        break
    # Runs the factor finder code.
    factor_finder(to_factor)

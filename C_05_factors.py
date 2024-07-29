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
        print("1 is unity (has only one factor, itself.)")
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
        print(f"The Square root of {needs_factoring} is {int(needs_factoring ** 0.5)}.")
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

factor_finder(int(input("Number needed to be factorized: ")))

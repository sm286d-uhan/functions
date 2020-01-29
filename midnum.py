def midnum(alpha):
    """
    Checks to see if a number is a valid alpha number
    for the class of 2022.

    Arguments:
        alpha: Alpha number to test

    Output:
        Does not return a value.
        Prints a message if the alpha number input is valid
        for the class of 2022.
    """
    # Check if the alpha number without the leading 22 is a multiple of 6
    if (alpha - 220000) % 6 == 0:
        print(f"The alpha number {alpha} is a valid midshipman alpha number.")

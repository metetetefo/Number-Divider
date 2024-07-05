                    #NUMBER DIVIDER

# ANSI escape codes for colored text
RESET = "\033[0m"  # Reset colors
BOLD = "\033[1m"  # Bold text
UNDERLINE = "\033[4m"  # Underlined text
RED = "\033[91m"  # Red
GREEN = "\033[92m"  # Green
YELLOW = "\033[93m"  # Yellow
BLUE = "\033[94m"  # Blue
MAGENTA = "\033[95m"  # Magenta
CYAN = "\033[96m"  # Cyan
WHITE = "\033[97m"  # White

def format_number(number):
    """ Return the number as int if it's an integer, otherwise float. """
    if number.is_integer():  # If number is an integer
        return int(number)  # Return as int
    return number  # Otherwise return as float

def precise_round(number):
    """ Perform precise rounding based on the number's decimal precision. """
    if number == 0:  # If the number is zero
        return 0  # Return 0

    abs_number = abs(number)  # Get the absolute value of the number

    # Determine the length of the decimal part
    decimal_part = f"{abs_number:.10f}".split('.')[1]  # Convert number to decimal format and get decimal part
    length = len(decimal_part)  # Get the length of the decimal part

    if length == 0:
        return number  # If there's no decimal part, return the original number

    # Perform rounding based on the most significant decimal place
    rounded = round(number, length - 1)  # Round based on the most significant decimal place

    # If rounding results in zero
    if rounded == 0:
        # If the number is extremely small, avoid returning zero
        if abs(number) < 1e-10:
            return 1e-10
        return 0
    
    return rounded

def division_operation():
    try:
        number = float(input(f"{GREEN}Enter the number to be divided: {RESET}"))  # Get the number to be divided from the user
        divisor = float(input(f"{GREEN}Enter the divisor: {RESET}"))  # Get the divisor from the user

        if divisor == 0:  # If the divisor is zero
            print(f"{RED}Divisor cannot be zero.{RESET}")  # Print warning message
        else:
            estimate = number // divisor  # Calculate the estimated result (integer division)
            actual_result = number / divisor  # Calculate the actual result (decimal division)
            rounded_result = precise_round(actual_result)  # Round the actual result precisely

            # Check the results
            if estimate == actual_result == rounded_result:  # If estimated result, actual result, and rounded result are the same
                print(f"""
{BLUE}The estimated result, actual result, and rounded result are the same:{RESET}
If the number: {format_number(number)} 
is divided by: {format_number(divisor)}
the estimated result is {format_number(estimate)}.
The actual result is {format_number(actual_result)} and the rounded result is also {format_number(rounded_result)}.
                """)
            else:
                print(f"""
{YELLOW}If the number: {format_number(number)} 
is divided by: {format_number(divisor)}
the estimated result is {format_number(estimate)}.
The actual result is {format_number(actual_result)}, and if rounded, it becomes {format_number(rounded_result)}.{RESET}
                """)

    except ValueError:  # If the user does not enter a valid number
        print(f"{RED}Please enter a valid number.{RESET}")  # Print error message

while True:  # Infinite loop
    division_operation()  # Perform the division operation
    
    while True:  # Loop until a valid response is obtained
        continue_response = input(f"{GREEN}Do you want to perform another operation? (Y/N): {RESET}").strip().lower()  # Ask the user if they want to continue
        # .strip() method removes any leading and trailing whitespace
        # .lower() method converts all characters to lowercase
        if continue_response in ('y', 'n'):  # If the response is 'y' or 'n'
            break  # Exit the loop if a valid response is received
        else:
            print(f"{RED}Invalid response. Please enter 'Y' or 'N'.{RESET}")  # Print invalid response warning

    if continue_response != 'y':  # If the user does not enter 'y' (yes)
        break  # Exit the loop

print(f"{BLUE}Program terminated.{RESET}")  # Print message when the program ends
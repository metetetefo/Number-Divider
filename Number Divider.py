RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

def format_number(number):
    """Return the number as int if it's an integer, otherwise float."""
    if number.is_integer():
        return int(number)
    return number

def precise_round(number):
    """
    Round based on the input's decimal precision:
    - If the number has D decimal digits in its minimal decimal form, round to (D-1) decimals.
    - Preserve the sign for extremely small values that would collapse to 0 by returning ±1e-10.
    """
    if number == 0:
        return 0

    s = ("%f" % abs(number)).rstrip("0").rstrip(".")
    if "." in s:
        decimals = len(s.split(".")[1])
    else:
        decimals = 0

    if decimals == 0:
        return number

    rounded = round(number, max(0, decimals - 1))

    if rounded == 0:
        return 1e-10 if number > 0 else -1e-10

    return rounded

def division_operation():
    try:
        number = float(input(f"{GREEN}Enter the number to be divided: {RESET}"))
        divisor = float(input(f"{GREEN}Enter the divisor: {RESET}"))

        if divisor == 0:
            print(f"{RED}Divisor cannot be zero.{RESET}")
        else:
            estimate = number // divisor
            actual_result = number / divisor
            rounded_result = precise_round(actual_result)

            if estimate == actual_result == rounded_result:
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

    except ValueError:
        print(f"{RED}Please enter a valid number.{RESET}")

while True:
    division_operation()
    
    while True:
        continue_response = input(f"{GREEN}Do you want to perform another operation? (Y/N): {RESET}").strip().lower()
        if continue_response in ('y', 'n'):
            break
        else:
            print(f"{RED}Invalid response. Please enter 'Y' or 'N'.{RESET}")

    if continue_response != 'y':
        break

print(f"{BLUE}Program terminated.{RESET}")

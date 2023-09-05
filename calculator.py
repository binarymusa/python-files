# improved calculator
 
class Colors: # change the color of your output text:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

# function to check validity of an operator
def calculator(num_01, operator, num_02):
    if operator == "+":
        return num_01 + num_02
    elif operator == "-":
        return num_01 - num_02
    elif operator == "*":
        return num_01 * num_02
    elif operator == "/":
        return num_01 / num_02
    else:
        return "invalid operator!"
        
def main():
    while True:
        try:

            get_float_input = lambda message: float(input(message)) # prompts user for input
            values = lambda num_1, oper, num_2: calculator(num_1, oper, num_2)

            num_1 = get_float_input("Enter value 1: ")
            oper = input("Enter valid operator: ")
            num_2 = get_float_input("Enter value 2: ")

            output = values(num_1, oper, num_2)


            if isinstance(output, float): # checks if output = float
                print(Colors.MAGENTA + f"Result: {output:.2f} " + Colors.RESET)
           
        # checks for division error(i.e 2/0) and value error(i.e v/2)
        except ZeroDivisionError as e:
                print(Colors.RED + f':) {e}: cannot divide by zero' + Colors.RESET)
                
        except ValueError as e:
                print(Colors.RED + f':) {e}: enter values only' + Colors.RESET)


        print('execution complete')

        user = input('revisit the calculation, (yes/no): ').lower()
        if user != 'yes':
            break

    print('exiting program......')

if __name__ == "__main__":
    main()
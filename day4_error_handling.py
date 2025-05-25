user_input = input("Please enter to fivide by 100: ") 

try: 
    number = int (input(user_input))
    result = 100 / number
    print(f"100 divide by {number} is {result}")
except ValueError: 
    print("That isn't a number. Please input a valid number")
except ZeroDivisionError:
    print("You can't divide by zero")
except Exception as e: 
    print("Something went worng")
    

finally: 
    print("Program finished running")
    
user_input = input("Enter a number to divide 100 by: ")

try: 
    number = int(user_input)
    result = 100/number 
    print(f"100 divided by {number} is {result}")
    
except ValueError: 
    print("That wasn't a number. Please input a number")
except ZeroDivisionError: 
    print("You can't divide by zero")
except Exception as e:
    
    print("Something went wrong: {e}")
finally: 
    
    print("Program finished running")
    
    
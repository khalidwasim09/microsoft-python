first_number = input("Please enter a number: ")
second_number = input("Please enter a number: ")
try: 
    number1 = int(first_number)
    number2 = int(second_number)
    result = number1 / number2 
    print (f"Dividing {first_number} by {second_number} gives {result}")
    
except ValueError: 
    print("You must enter numbers only")
except ZeroDivisionError: 
    print("You can't divide by zero")
    
except Exception as e: 
    print("Something went wrong")
    
finally: 
    print("Thanks for using the divider app") 
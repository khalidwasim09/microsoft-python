name = input("Enter your name: ")
age = int(input("Enter your age: "))

years_untill_30 = 30 - age

if years_untill_30 > 0: 
    print(f"Hi {name}, you will be 30 in {years_untill_30} years")
elif years_untill_30 == 0: 
    print(f"Hi {name}, you are exactly 30. Welcome to the prime")
else: 
    print(f"Hi {name}, you have been 30 for {-years_untill_30} years")
    
    
    
#task 

user_city = input("Enter your city: ").lower()
if user_city == "toronto": 
    
    print("You live in the 6ix")

else: 
    print(f"Cool! I have heard about {user_city}")
    
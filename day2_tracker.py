# name = "Khalid"
# age = 22
# height_cm = 178.5
# is_tired = True

# print(type(name))
# print(type(age))
# print(type(height_cm))
# print(type(is_tired))

# city = "Toronto"
# mood = "productive"


# print (f"{name} is in {city} and feels {mood}")

# print ("{} is in {} and feels {}".format(name, city, mood))
# print(name + "is in" + city + " and feels" + mood)
#Function 

from datetime import datetime

def log_mood(name, city, mood, energy_level):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    message = f"{timestamp} {name} in {city} is feeling {mood} with energy {energy_level}/10.\n"
    
    with open("mood_log.txt", "a") as file:
        file.write(message)
    
    print("✅ Entry logged.")

# Manual test (optional)
entry = log_mood("Khalid", "Toronto", "tired", 6)
print(entry)

# Real input
name = input("What's your name? ")
city = input("Where are you? ")
mood = input("How are you feeling today? ")
energy = int(input("Energy level (0–10)? "))

log_mood(name, city, mood, energy)

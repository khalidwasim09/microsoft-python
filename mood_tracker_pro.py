from datetime import datetime
name = input("Enter your name: ")
city = input("What city are you from: " )
mood = input("How are you feeling today: ")
energy_level = input("Enter your energy level (0-10): ")

try: 
    energy_input = int(energy_level) 
    
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]") 
    message = f"{timestamp} {name} in {city} is feeling {mood} with {energy_level}"
    with open("mood_log.txt", "a") as file: 
        file.write(message)
except ValueError: 
    print("Energy must be a number between 0 and 10")
finally: 
    print("Thanks for your mood") 
    
    
try:
    with open("mood_log.txt", "r") as file:
        lines = file.readlines()
    energy_scores = []

    for line in lines: 
        cleaned = line.strip()
        print(cleaned) 
        
        try:
            # Step 12: Extract the energy number
            after_energy = cleaned.split("energy ")[1]  # Get "6/10."
            energy = int(after_energy.split("/")[0])    # Get just the 6
            energy_scores.append(energy)

        except:
            # Step 13: If the line was broken, skip it
            print("⚠️ Skipping broken entry")

    # Step 14: After loop, calculate average
    print(f"\n📝 Total entries: {len(lines)}")

    if energy_scores:
        avg = sum(energy_scores) / len(energy_scores)
        print(f"📊 Average energy level: {avg:.2f}/10")
    else:
        print("No valid energy scores found.")

except FileNotFoundError:
    print("No mood log found yet — start by entering your first mood!")
    
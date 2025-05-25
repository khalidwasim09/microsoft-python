# day3_log_analysis.py

energy_list = []

# Step 1: Read all mood logs
with open("mood_log.txt", "r") as file:
    lines = file.readlines()

# Step 2: Print total entries
print(f"You have {len(lines)} mood entries logged.\n")

# Step 3: Loop through each line
for line in lines:
    print(line.strip())  # Print the entry

    try:
        # Step 4: Extract energy number
        after_energy = line.split("energy ")[1]   # Get the "6/10." part
        score = int(after_energy.split("/")[0])   # Get just the 6
        energy_list.append(score)                 # Save to list
    except:
        print("⚠️ Couldn't read energy score from this line.")

# Step 5: Show average if any scores were found
if energy_list:
    avg = sum(energy_list) / len(energy_list)
    print(f"\nAverage energy level: {avg:.2f}/10")
else:
    print("\nNo energy data found.")

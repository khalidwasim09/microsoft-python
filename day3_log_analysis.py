with open("mood_log.txt", "r") as file: 
    lines = file.readlines()
print(f"You have {len(lines)} mood entries logged.")

for line in lines: 
    print(line.strip())
    
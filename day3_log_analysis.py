energy_list = [] 

with open ("mood_log.txt","r") as file: 
    lines = file.readlines()
    
print (f"You have {len(lines)} mood entries logged.\n") 

for line in lines: 
    print(line.strip())
    
    try: 
        after_energy = line.split("energy")[1]
        score =int(after_energy.split("/")[0])
        energy_list.append(score)
    except:
        print("Couldn't read energy score from this line.")
        
if energy_list: 
    avg = sum(energy_list) / len(energy_list)
    print(f"\nAverage energy level: {avg:.2f}/10")
else: 
    print("\nNo energy data found")
    
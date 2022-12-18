f= open(r"C:\Users\Adam\PycharmProjects\Advent_of_code_2022\Day 3\input.txt")
rucksacks =[]
for line in f:
    rucksacks.append(line.strip())
total_priority = 0
for rucksack in rucksacks:
    compartment1 = rucksack[:len(rucksack) // 2]
    compartment2 = rucksack[len(rucksack) // 2:]
    set1 = set(compartment1)
    set2 = set(compartment2)
    common_items = set1.intersection(set2)
    for item in common_items:
      if item.islower():
        total_priority += ord(item) - ord('a') + 1
      else:
        total_priority += ord(item) - ord('A') + 27
print(total_priority)

f = open(r"C:\Users\Adam\PycharmProjects\Advent_of_code_2022\Day1\input_day1.txt",'r')
reindeers_calories =[]
calories_sum = 0
b_calories_sum = 0
top3_sum = 0

for line in f:
    if line.strip() != "":
        calories_sum += int(line)
    else:
        reindeers_calories.append(calories_sum)
        if(calories_sum>b_calories_sum):
            b_calories_sum = calories_sum
            calories_sum = 0
        else:
            calories_sum =0
print(b_calories_sum)
reindeers_calories.sort(reverse=True)
for i in range(3):
    top3_sum += reindeers_calories[i]

print (top3_sum)


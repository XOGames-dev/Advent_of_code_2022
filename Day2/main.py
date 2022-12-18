# rock 1 paper 2 scissors 3
f= open(r"C:\Users\Adam\PycharmProjects\Advent_of_code_2022\Day2\input.txt","r")
opponent_choices =[]
my_choices =[]
my_score =0
my_score2=0

#part one
for line in f:
    opponent_choices.append(line[0])
    my_choices.append(line[2])
    if(line[2]=='X'):
        my_score+=1
    elif(line[2]=='Y'):
        my_score+=2
    else:
        my_score+=3

for i in range(len(my_choices)):
    if (my_choices[i] == 'X' and opponent_choices[i]=='C'):
        my_score += 6
    if (my_choices[i] == 'X' and opponent_choices[i] == 'A'):
        my_score += 3
    if (my_choices[i] == 'Y' and opponent_choices[i]=='A'):
        my_score += 6
    if (my_choices[i] == 'Y' and opponent_choices[i] == 'B'):
        my_score += 3
    if (my_choices[i] == 'Z' and opponent_choices[i] == 'B'):
        my_score += 6
    if (my_choices[i] == 'Z' and opponent_choices[i] == 'C'):
        my_score += 3
print(my_score)
#part 2
for i in range(len(my_choices)):
    if (my_choices[i] == 'X' and opponent_choices[i] == 'A'):
        my_score2 += 3
    if (my_choices[i] == 'X' and opponent_choices[i] == 'B'):
        my_score2 += 1
    if (my_choices[i] == 'X' and opponent_choices[i] == 'C'):
        my_score2 += 2
    if (my_choices[i] == 'Y' and opponent_choices[i] == 'A'):
        my_score2 += 4
    if (my_choices[i] == 'Y' and opponent_choices[i] == 'B'):
        my_score2 += 5
    if (my_choices[i] == 'Y' and opponent_choices[i] == 'C'):
        my_score2 += 6
    if (my_choices[i] == 'Z' and opponent_choices[i] == 'A'):
        my_score2 += 8
    if (my_choices[i] == 'Z' and opponent_choices[i] == 'B'):
        my_score2 += 9
    if (my_choices[i] == 'Z' and opponent_choices[i] == 'C'):
        my_score2 += 7

print(my_score2)



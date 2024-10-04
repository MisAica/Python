numbers = (1, 3, 2, 4, 3, 1, 2, 5, 10)

count_dict = {}

for number in numbers:
    if number in count_dict:
        count_dict[number] +=1
    else:
        count_dict[number] = 1

for number in count_dict:
    if count_dict[number] > 1:
        print(number)
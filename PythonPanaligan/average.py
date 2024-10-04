numbers = (1, 4, 7, 10, 13, 16)

sum_even = 0
count_even = 0

for number in numbers:
    if number % 2 == 0:
        sum_even += number
        count_even += 1

if count_even > 0:
    average_even = sum_even / count_even
    print(average_even)
else:
    print("No even number")


        
list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_m = 0
for i in range(len(list_numbers)):
    maxym = list_numbers[index_m]
    cur = list_numbers[i]
    if cur > maxym:
        index_m = i
list_numbers[index_m], list_numbers[-1] = list_numbers[-1], list_numbers[index_m]

print(list_numbers)

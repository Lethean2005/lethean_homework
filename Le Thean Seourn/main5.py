# EX5.Create function to count of number 5 in array [2,3,5,0,11,5,2]
def count_fives(array):
    count = 0
    for numbers in array:
        if numbers == 5:
            count += 1
    return count

array = [2, 3, 5, 0, 11, 5, 2]
result = count_fives(array)
print(count_fives(array))








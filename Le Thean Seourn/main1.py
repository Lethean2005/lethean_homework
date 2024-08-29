# EX1.Create function to sum numbers in array [1,2,3,4,5,6]
def sum_array(array):
    total = 0
    for numbers in array:
        total += numbers
    return total

numbers = [1, 2, 3, 4, 5, 6]
result = sum_array(numbers)
print(result)  # Output: 21

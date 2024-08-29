# EX2.Create function to sum odd number in array [1,2,3,4,5,6]
def sum_odd_numbers(array):
    total = 0
    for numbers in array:
        if numbers % 2 != 0:
            total += numbers
    return total

numbers = [1,2,3,4,5,6]
result = sum_odd_numbers(numbers)
print(result)  # Output: 9

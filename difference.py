# initialise sum_of_squares
sum_of_squares = 0
# initialise sum = 0 
sum = 0
# initialise i = 0
i = 0

# while i <= 100
while i <= 100:
    # sum_of_squares = sum_of_squares + i * i
    sum_of_squares = sum_of_squares + i ** 2
    # sum = sum + 1
    sum = sum + i
    # i = i + 1
    i = i + 1

# square_of_sum = sum * sum
square_of_sum = sum * sum
# diff = square_of_sum - sum_of_squares
diff = square_of_sum - sum_of_squares

print(diff)

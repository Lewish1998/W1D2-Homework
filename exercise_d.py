# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 6, 99, 7]

# 1. Print out a list of the even integers:
even_int = []
for num in numbers:
    if num % 2 == 0:
        even_int.append(num)

# 2. Print the difference between the largest and smallest value:
difference = max(numbers) - min(numbers)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
for x in range(0, len(numbers)):
    if numbers[x] == numbers[x-1] and numbers[x] == 2 and numbers[x-1] ==2:
        # print(True)
        pass

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

for x in range(0, len(numbers)):
    if numbers[x] == numbers[] and numbers[x] == 2 and numbers[x-1] ==2:
        # print(True)
        pass














# index = 0
# for x in numbers:
#     while x != 6 


# total = sum(numbers)






# x = 0
# for _ in range(0, len(numbers)):
#     if numbers[x] >=6 and numbers[x] <= 7:
#         # numbers.remove[x]
#         print(numbers[x])
#     else:
#         x += 1
# #         print(numbers[x])

# i = 0
# total = 0
# for x in numbers:
#     total += x
    

    # if x == 6:
    #     print(total)
    








# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 


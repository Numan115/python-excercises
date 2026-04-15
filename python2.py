def even_squares(nums):
    return [x**2 for x in nums if x % 2 == 0]

print(even_squares([1,2,3,4,5,6]))

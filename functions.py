# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
def sum_to (num):
  sum = 0
  for i in range(num+1):
    sum+=i
  return sum
print(sum_to(6)) 
print(sum_to(10)) 

#2.Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
### way 1###
def largest(nums):
  return max(nums)

### way2 ###
def largest(list):
    current = 0
    largest_num = 0 
    for num in list:
        if current < num:
            current = num
            largest_num = current
    return largest_num 
 
print(largest([10, 4, 2, 231, 400, 54]) )
print(largest([1, 2, 3, 4, 0]))

#3.Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.
def occurrences(str1, str2):
    return str1.count(str2)

print(occurrences('fleep floop', 'p'))

# 4.Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
def product(*args):
    num = 1
    for arg in args:
        num *= arg
    return num
print(product(-1, 4))
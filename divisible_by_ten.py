#Define the function to accept one
#input parameter called nums
#Initialize a counter to 0
#Loop through every number in nums
#Within the loop, if any of the numbers
#are divisible by 10, increment our counter
#Return the final counter value


#Write your function here
def divisible_by_ten(nums):
  count = 0
  for i in nums:
    if i % 10 == 0:
      count += 1
  return count
#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

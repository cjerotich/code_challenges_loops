#Define the function to accept two lists of numbers, bases and powers
#Create a new list that will contain our answers
#Create a loop that iterates through every base in bases
#Within that loop, create another loop that iterates
#through every power in power
#Within that nested loop, append the result of
#the current base raised to the current power.
#After all iterations of both loops are complete, return the list of answers

#Write your function here
def exponents(bases,powers):
  new_lst=[]
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst
#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

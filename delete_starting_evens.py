#Define our function to accept a single input parameter
#lst which is a list of numbers
#Loop through every number in the list if there
#are still numbers in the list and if we haven’t hit an odd number yet
#Within the loop, if the first number in the list is even,
#then remove the first number of the list
#Once we hit an odd number or we run out of numbers,
#return the modified list

#Write your function here
def delete_starting_evens(lst):
  while len(lst) > 0 and  lst[0] % 2 == 0:
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))

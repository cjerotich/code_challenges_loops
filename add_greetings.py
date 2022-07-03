#Define the function to accept a list of strings
#as a single parameter called names
#Create a new list of strings
#Loop through each name in names
#Within the loop, concatenate 'Hello, ' and
#the current name together and append this new string to the new list of strings
#Afterwards, return the new list of strings

#Write your function here
def add_greetings(names):
  new_lst=[]
  for name in names:
    new_lst.append('Hello, ' + name)
  return new_lst

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

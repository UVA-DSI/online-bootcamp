#Create empty list
userList = []
#Set a true condition
userUnfinished = True
#Check to see if condition still true and prompt user for item
while userUnfinished:
    item = input("What would you like to add to your list? Enter 'q' to finish making list\n")
    #If user doesn't want anything else on list
    if item == 'q':
        userUnfinished = False
        #Otherwise, append item to list
    else: 
            userList.append(item)
print("Here's your list:")
for item in userList:
    print(item)
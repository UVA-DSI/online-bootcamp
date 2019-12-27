#Ask user for x number of inputs and append them to a list
x = 5
user_list = []
for i in range(x):
    print('Please enter a word or phrase:')
    user_list.append(input())
    
#Iterate over list items and print each one
for i in user_list:
    print(i)
#Dictionnary with to do with the priotity as the key
#input question: Here"s what you need to do today in priority order/ Would you like to add or remove anything to the current to do list
#function To add , fucntion to remove(once remove put in a done list, if possible with the date). 
#sort the dic by key. 

from sympy import true
import csv


daily_to_do_list=[]
file = open('my_to_do_list.txt', 'w', newline = '')
    
for i in  daily_to_do_list:
    file.read(i)
    print(i)
    print('File Read Successfully')
options = input('Would you like to ADD or REMOVE an item from your current to do list? Enter Y or N: ')
print(options)
#i need to nest the  add remove ifstatement
while (options == 'Y') or (options =='y') == True:
    if (options == 'Y') or (options =='y'):
        add_remove = input("Press A to ADD an Item or R to remove an Item from the list. ")
        if (add_remove == 'A' )or (add_remove =='a'):
            new_item = input('Please enter the new task: ')
            daily_to_do_list.append(new_item)
            print("Here's the current list: " + str(daily_to_do_list))

        elif (add_remove == 'R' )or (add_remove =='r'):
            daily_to_do_list.remove(input("Please enter what you've completed:  "))
            print("Here's the updated list: " + str(daily_to_do_list))
            
        else:
            print('This is not a valid option. Try Again ')

    elif (options == "N") or (options =='n'):
        print("Here's your current list: " + str(daily_to_do_list))

    else:
        print('This is not a valid option. Try Again ')
    
#Things I need to change :::read in loop to start, adding while loop while a break condition. 
    


for i in  daily_to_do_list:
    file.write(i)
    print(i)
    print('File written Successfully')
file.close()


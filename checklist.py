
checklist = list()
# create
def create(item):
    checklist.append(item)

# read 
def read(index):
    return checklist[index]

# update
def update(index,item):
    checklist[index]=item 

# destroy
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False
    
    else:
        #Catch all
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input
# user_value = user_input("Please Enter a value:")
# print(user_value)

# test
def test():
    create("purple sox")
    create("red cloak")
    create("green hat")
    # print(read(0))
    # print(read(1))

    # update(0,"purple socks")
    # destroy(1)

    # print(read(0))
    # print(read(1))
   
    # Your testing code here
    # ...
    # # Call your new function with the appropriate value
    # select("C")
    # # View the results
    # list_all_items()
    # # Call function with new value
    # select("R")
    # # View results
    # list_all_items()
    # # Continue until all code is run
test()
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    select(selection)
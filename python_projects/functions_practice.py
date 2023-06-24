# A function named hello() that prints a greeting to the user.
# This function should accept no arguments and returns nothing.

def hello():
    print("Hello, people 🤗!")

# A function named pack() that accepts three arguments,
# and returns a single list with the three arguments inside as list elements.


def pack(A1, A2, A3):
    return [A1, A2, A3]

# function called eat_lunch(). This function should accept a list of any length,
# and print out a series of strings that say "First I eat __"
# (the first element of the list), and "Next I eat ___" (for the following elements in the list).
#  If the list is empty, print "My lunchbox is empty!". The function should not return anything.


def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty 😨!")
    else:
        for i in range(len(lunch_list)):
            if i == 0:
                print("First I eat 🥗, {lunch_list[0]}")
                for i in range(1, len(lunch_list)):
                    print("Next I eat🍱, {eat_lunch[i]}")

#Prints Hello people
hello()
#prints pack function of multiple arguements and numbers
print(pack("A1","A2","A3"))
print(pack(1,2,3))
# calling a function with empty arguements
eat_lunch([])
# calling a function with element called salad
eat_lunch(["Salad"])
# calling  a function with listing elements called "Sub Sandwich","Steak","Sushi","Apple Pie","Passion Fruit" 
eat_lunch(["Sub Sandwich","Steak","Sushi","Apple Pie","Passion Fruit"])

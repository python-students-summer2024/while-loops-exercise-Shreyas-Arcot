'''get_starting_number - this function asks the user how many bottles of beer on the wall they want to start singing with,
e.g. "How many bottles of beer on the wall?" The function asks this question as many times as necessary until the user enters
a valid response, which is considered to be any integer 1 or greater. The function then returns the integer equivalent of the
value the user entered. The code for this function can be the same for all three versions of the program, but must be copied
into each file.

sing - this function takes an argument specifying how many bottles of beer to start with, and then outputs the lyrics to the
song, starting from that number of bottles.'''


def get_starting_number():
    starting_bottles = input("How many bottles of beer are on the wall?")
    is_input_numeric = False
    while is_input_numeric == False:
        if starting_bottles.isnumeric():
            if int(starting_bottles) > 0:
                return starting_bottles
                is_input_numeric = True
            else:
                starting_bottles = input("How many bottles of beer are on the wall?")
                continue
        else:
            starting_bottles = input("How many bottles of beer are on the wall?")
            continue


def sing(starting_bottles):
    
    starting_bottles = int(starting_bottles)
    is_bottles_greater_than_1 = True
    while is_bottles_greater_than_1:
        if starting_bottles > 1:
            print (str(starting_bottles) + " bottles of beer on the wall, " + str(starting_bottles) + " bottles of beer.")
            starting_bottles = starting_bottles - 1
            if starting_bottles > 1:
                print("Take one down, pass it around, " + str(starting_bottles) + " bottles of beer on the wall.")
            else:
                print ("Take one down, pass it around, 1 bottle of beer on the wall.")
                print ("1 bottle of beer on the wall, 1 bottle of beer.")
                print ("Take it down, pass it around, no more bottles of beer on the wall!")
                is_bottles_greater_than_1 = False

        elif starting_bottles == 1:
            print ("Take one down, pass it around, 1 bottle of beer on the wall.")
            print ("1 bottle of beer on the wall, 1 bottle of beer.")
            print ("Take it down, pass it around, no more bottles of beer on the wall!")
            is_bottles_greater_than_1 = False
            
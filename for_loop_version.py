'''get_starting_number - this function asks the user how many bottles of beer on the wall they want to start singing with,
e.g. "How many bottles of beer on the wall?" The function asks this question as many times as necessary until the user enters
a valid response, which is considered to be any integer 1 or greater. The function then returns the integer equivalent of the
value the user entered. The code for this function can be the same for all three versions of the program, but must be copied
into each file.

sing - this function takes an argument specifying how many bottles of beer to start with, and then outputs the lyrics to the
song, starting from that number of bottles.'''

def sing(starting_bottles):
    current_bottles = int(starting_bottles)
    
    if current_bottles == 1:
        print ("1 bottle of beer on the wall, 1 bottle of beer.")
        print ("Take it down, pass it around, no more bottles of beer on the wall!")
    else:
        for i in range(current_bottles):
            print (str(current_bottles) + " bottles of beer on the wall, " + str(current_bottles) + " bottles of beer.")
            current_bottles = current_bottles - 1
            if current_bottles > 1:
                print("Take one down, pass it around, " + str(current_bottles) + " bottles of beer on the wall.")
            else:
                print ("Take one down, pass it around, 1 bottle of beer on the wall.")
                print ("1 bottle of beer on the wall, 1 bottle of beer.")
                print ("Take it down, pass it around, no more bottles of beer on the wall!")
                break

def get_starting_number():
    starting_bottles = input("How many bottles of beer are on the wall?")
    while not (starting_bottles.isnumeric() and int(starting_bottles)>0):
        starting_bottles = input("How many bottles of beer are on the wall?")
        continue

    return starting_bottles

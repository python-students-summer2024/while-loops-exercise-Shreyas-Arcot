
def get_starting_number():
    starting_bottles = input("How many bottles of beer are on the wall?")
    while not (starting_bottles.isnumeric() and int(starting_bottles)>0):
        starting_bottles = input("How many bottles of beer are on the wall?")
        continue

    return starting_bottles

def sing(starting_bottles):
    starting_bottles = int(starting_bottles)
    while starting_bottles > 1:
        print (str(starting_bottles) + " bottles of beer on the wall, " + str(starting_bottles) + " bottles of beer.")
        starting_bottles = starting_bottles - 1
        if starting_bottles > 1:
            print("Take one down, pass it around, " + str(starting_bottles) + " bottles of beer on the wall.")
        else:
            print ("Take one down, pass it around, 1 bottle of beer on the wall.")
            print ("1 bottle of beer on the wall, 1 bottle of beer.")
            print ("Take it down, pass it around, no more bottles of beer on the wall!")
            starting_bottles = starting_bottles - 1
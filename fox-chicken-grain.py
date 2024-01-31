# fox chicken grain

# variables

fox = 0
chicken = 0
grain = 0
farmer = 0

items = [fox, chicken, grain, farmer]

solved = False
lost = False

# subprograms
def wrong_move():
    global lost
    if farmer == 1 and fox == 0 and chicken == 0:
        print("The fox at the chicken, Puzzle Lost!")
        lost = True
    
    if farmer == 1 and chicken == 0 and grain == 0:
        print("The chicken ate the grain, Puzzle Lost!")
        lost = True

    if farmer == 0 and fox == 1 and chicken == 1:
        print("The fox at the chicken, Puzzle Lost!")
        lost = True
    
    if farmer == 0 and chicken == 1 and grain == 1:
        print("The chicken ate the grain, Puzzle Lost!")
        lost = True
    

    
def isSolved():
    global solved
    if fox == 1 and chicken == 1 and grain == 1:
        print("You solved the puzzle! Congratulations :)")
        solved = True

def output():
    this_side = []
    other_side = []
    
    if fox == 0:
        this_side.append("Fox")
    else:
        other_side.append("Fox")

    if chicken == 0:
        this_side.append("Chicken")
    else:
        other_side.append("Chicken")

    if grain == 0:
        this_side.append("Grain")
    else:
        other_side.append("Grain")

    if farmer == 0:
        this_side.append("Farmer")
    else:
        other_side.append("Farmer")

    
    print("This side of the river:")
    for y in this_side:
        print(y)
    print("The other side of the river:")
    for z in other_side:
        print(z)

# main program

while solved != True and lost != True:
    choice = input("A fox, chicken and a bag of grain wait by the side of a river.\nWhich item will you take in your rowboat to the other side?\nfox, chicken, grain or farmer?\nChoose: ")
    
    match choice:
        case "farmer":
            if farmer == 0:
                farmer = 1
            else:
                farmer = 0
        case "fox":
            if farmer == 0 and fox == 0:
                farmer = 1
                fox = 1
            else:
                farmer = 0
                fox = 0
        case "chicken":
            if farmer == 0 and chicken == 0 :
                farmer = 1
                chicken = 1
            else:
                farmer = 0
                chicken = 0
        case "grain":
            if farmer == 0 and grain == 0:
                farmer = 1
                grain = 1
            else:
                farmer = 0
                grain = 0

    #calling functions when assigned variables to different values
    output()
    wrong_move()
    isSolved()

# Finally finished
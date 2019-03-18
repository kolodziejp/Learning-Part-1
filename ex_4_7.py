#exercise using the def function

grade = input("Enter number between 0.0 and 1.0")
try:                    # must use a nmber between 1 and 0
    fgrade = float(grade)
except:
    print("ERROR - Please enter a Number between 0.0 and 1.0")
    quit()
def computescore():
    if fgrade > 1:
        print ("ERROR - Number must be between 0.0 and 1.0")
    elif fgrade >= 0.9:
        print ("A")
    elif fgrade >= 0.8:
        print ("B")
    elif fgrade >= 0.7:
        print ("C")
    elif fgrade >= 0.6:
        print ("D")
    elif fgrade < 0.6:
        print ("F")

computescore()

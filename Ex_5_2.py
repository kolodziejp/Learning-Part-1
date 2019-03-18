# Exercise to display largest and smallest numbers from inserted numbers
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        fnum = float(num)
    except:
        print ("Invalid input")
        continue
    #print(num)

    if largest is None:
        largest = fnum
    elif fnum > largest:
        largest = fnum

    if smallest is None:
        smallest = fnum
    elif fnum < smallest:
        smallest = fnum

print("Maximum is", int(largest))
print("Minimum is", int(smallest))

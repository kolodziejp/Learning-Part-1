# Finding the smallest value in a range

small = None
print ("Let us look for the smallest value")

for number in [21, 42, 13, 53, -5, 2, 56, 119, -23, 99, 2, 3, 9, 87]:
    if small is None:
        small = number
    elif number < small:
        small = number
    print (small, number)

print ("The smallest number is", small)

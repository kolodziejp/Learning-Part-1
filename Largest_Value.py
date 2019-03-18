#finding the largest value in a range

largest = -1
print ("Start at", largest)

for number in [21, 42, 13, 2, 119, 99, 2, 3, 9, 87]:
    if number > largest:
        largest = number
    print (largest, number)

print ("The largest number is", largest)

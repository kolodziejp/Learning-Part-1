count = 0
find = "False"

for x in [21, 42, 13, 2, 119, 99, 2, 3, 9, 87]:
    count = count + 1
    if x == 119:
        find = "True"
        print (count, find)
        break
    print (count, find)

print ("Done")

# entered numbers are added, counted and average computed
count = 0
total = 0

while True:
    num = input ("Enter a number: ")
    if num == "done":
            break
    try:
        fnum = float(num)  #convert to floating number
    except:
        print ("Invalid Data!")
        continue        # should only consider valid numbers continue and ignore error

    count = count + 1
    total = total + fnum
    avg = total / count

print (total, count,avg)

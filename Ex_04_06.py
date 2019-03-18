#exercise using the def function
hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    xh = float(hrs)
    xr = float(rate)
except:
    print("Insert Numbers Only!")
    quit()

overtime = xh - 40

xot = float(overtime)

otr = xr * 1.5

def computepay():
    if xh > 40:
        pay = ((xh - xot) * xr) + (xot * otr)
        return pay

    else:
        bpay = xh * xr
        return bpay

print(computepay())

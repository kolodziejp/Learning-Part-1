# Total pay calculator including overtime

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
xh = float(hrs)
xr = float(rate)
overtime = xh - 40
xot = float(overtime)
otr = xr * 1.5
if xh > 40:
    pay = ((xh - xot) * xr) + (xot * otr)
    print(pay)
else:
    bpay = xh * xr
    print ("Salary Due",bpay)

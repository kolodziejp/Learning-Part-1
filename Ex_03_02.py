# Salary calculator - using try and except fuction
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
if xh > 40:
    pay = ((xh - xot) * xr) + (xot * otr)
    print("Salary Due",pay)
else:
    bpay = xh * xr
    print ("Salary Due",bpay)

# overtime pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input('Enter Hourly Rate')
r = float(rate)
if h > 40:
    ot = float(h - 40)
    otp = float (r *1.5)
    print((40 * r) + (ot * otp))
else:
    print(h * r)

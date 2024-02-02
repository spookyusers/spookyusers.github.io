# compute pay function

def computepay(h,r):
    ot = h - 40
    otp = r * 1.5
    p = ((40 * r) + (ot * otp))
    return p

hrs = input("Enter Hours:")
h = float(hrs)
rate = input('Enter Hourly Rate')
r = float(rate)
if h > 40:
    print('Pay',computepay(h, r))
else:
    print('Pay',h * r)
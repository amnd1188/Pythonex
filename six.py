def computepay(h,r):
    if h > 40 :
        x = h * r
        y = (h - 40.0) * (r * 0.5)

        pay = x + y
        return pay

    else :
        pay = h * r
        return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)

p = computepay(h,r)
print("Pay",p)

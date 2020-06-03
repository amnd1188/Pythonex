hours =  input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hours)
r = float(rate)

if h > 40 :
    x = h * r
    y = (h - 40.0) * (r * 0.5)

    p = x + y
else :
    p = h * r

print(p)    

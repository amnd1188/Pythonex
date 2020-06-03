num = 0
tot = 0
while True :
    val = input("Enter a number:")
    if val == 'done':
        break

    try :
        fval = float(val)
    except :
        print("Invalid data")
        continue

    num = num + 1
    tot = tot + fval

#print("Done!")
print(num,tot,tot/num)

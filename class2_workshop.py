price = int(input("Your distance : "))
if price >= 5 and price <= 50:
    print("Your price = 10B")
elif price < 5:
    print("not send")
elif price >= 51 and price <= 100:
    print("Your price = 15B")
elif price >= 101 and price <= 300:
    print("Your price = 25B")
elif price >= 301 and price <= 500:
    print("Your price = 35B")
else:
    print("Your price = 45B")
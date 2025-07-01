cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    profit = sp - cp
    print(f"Profit: Rs. {profit}")
elif cp > sp:
    loss = cp - sp
    print(f"Loss: Rs. {loss}")
else:
    print("No Profit No Loss")

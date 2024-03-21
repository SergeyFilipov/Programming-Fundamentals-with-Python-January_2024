total_price = 0

while True:
    price = input()
    if price == "special" or price == "regular":
        break
    elif float(price) < 0:
        print("Invalid price!")
        continue
    else:
        total_price += float(price)

taxes = total_price * 0.2
price_with_tax = total_price + taxes
if price == "special":
    price_with_tax *= 0.9
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_tax:.2f}$")

total_price = 0
taxes = 0
summ = 0

customer = input()
if "regular" in customer or "special" in customer:
    print("Invalid order!")
else:
    while customer != "special" and customer != "regular":
        price = float(customer)
        if price <= 0:
            print("Invalid price!")
        else:
            summ += price
        customer = input()

    taxes = summ * 0.2

    if customer == "special":
        total_price = (summ + taxes) * 0.9
    elif customer == "regular":
        total_price = summ + taxes

    if total_price == 0:
        print("Invalid order!")
        exit()

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {summ:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")

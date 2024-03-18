year = int(input())
drink = ""
if year <= 14:
    drink = "toddy"
elif year <= 18:
    drink = "coke"
elif year <= 21:
    drink = "beer"
else:
    drink = "whisky"

print(f"drink {drink}")

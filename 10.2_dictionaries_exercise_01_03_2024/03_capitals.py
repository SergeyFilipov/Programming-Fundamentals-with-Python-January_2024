country_names = input().split(", ")
capitals = input().split(", ")

zip_object = dict(zip(country_names, capitals))

for country, capital in zip_object.items():
    print(f"{country} -> {capital}")

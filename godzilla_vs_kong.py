film_budget = float(input())
actors_number = int(input())
clothes_price = float(input())

decor = film_budget * 0.10
clothes_price_total = clothes_price * actors_number

if actors_number > 150:
    clothes_price_total -= clothes_price_total * 0.10

film_price = decor + clothes_price_total

if film_price <= film_budget:
    print('Action!')
    print(f"Wingard starts filming with {film_budget - film_price:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {film_price - film_budget:.2f} leva more.")




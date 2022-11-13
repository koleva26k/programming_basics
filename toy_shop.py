#user input
trip_price = float(input())

puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

#logic
total = puzzle_count * 2.60
total += doll_count * 3
total += bear_count * 4.10
total += minion_count * 8.20
total += truck_count * 2

toys_count = puzzle_count + doll_count + bear_count + minion_count + truck_count

if toys_count >= 50:
    total -= total * 0.25
total -= total * 0.1

#output
if total >= trip_price:
    print(f"Yes! {total - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - total:.2f} lv needed.")

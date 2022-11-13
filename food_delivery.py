chicken_orders = int(input())
fish_orders = int(input())
veg_orders = int(input())
delivery_fee = 2.50

chicken_meal = 10.35
fish_meal = 12.40
veg_meal = 8.15

food_price = (chicken_orders * chicken_meal) + (fish_orders * fish_meal) + (veg_orders * veg_meal)
dessert = food_price * 0.20

full_cost = food_price + dessert + delivery_fee

print(full_cost)

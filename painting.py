naylon = int(input())
paint_lt = int(input())
dilute_lt = int(input())
hours = int(input())

bags = 0.40
naylon_sum = (naylon + 2) * 1.5
paint_sum = (paint_lt + (0.10*paint_lt)) * 14.50
dilute_sum = dilute_lt * 5

total_materials = naylon_sum + paint_sum + dilute_sum + bags
worker_cost = (total_materials * 0.30) * hours

full_cost = total_materials + worker_cost
print(full_cost)




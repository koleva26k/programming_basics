budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = gpu_count * 250
cpu_price = gpu_price * 0.35
all_cpu_price = cpu_price * cpu_count
ram_price = gpu_price * 0.1
all_ram_price = ram_price * ram_count

total = gpu_price + all_cpu_price + all_ram_price

if gpu_count > cpu_count:
    total -= total * 0.15

if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")
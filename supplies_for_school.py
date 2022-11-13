pen_count = int(input())
markers_count = int(input())
detergent_lt = int(input())
discount_percent = int(input())

price_pen = pen_count * 5.80
price_marker = markers_count * 7.20
price_detergent = detergent_lt * 1.20

price_total = price_pen + price_marker + price_detergent
discount = price_total * (discount_percent / 100)
final_sum = price_total - discount
print(final_sum)

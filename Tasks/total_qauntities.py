import itertools

orders = [
    {"Product": "Apple", "Quantity": 5},
    {"Product": "Banana", "Quantity": 2},
    {"Product": "Apple", "Quantity": 3}
]


sorted_list = sorted(orders, key=lambda x: x['Product'])
print(sorted_list)

grouped_orders = itertools.groupby(sorted_list, key=lambda x: x['Product'])
print(grouped_orders)

for product, group in grouped_orders:
    total_quantity = sum(item['Quantity'] for item in group)
    print(f"Product: {product}, Total Quantity: {total_quantity}")

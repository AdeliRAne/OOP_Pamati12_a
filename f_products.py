import json
with open ('f_products.json', 'r', encoding="utf-8") as file:
    products = json.load(file)

total_price = 0
for product in products:
    total_price+=product["price"]
    avarege_price = total_price / len(products)
print(f"Vidējā cena: {avarege_price:.2f} EUR")
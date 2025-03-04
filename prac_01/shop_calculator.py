DISCOUNTED_PRICE_RATE = 0.9
MINIMAL_PRICE_FOR_DISCOUNT = 100

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    item_price = float(input("Price of item: $"))
    total_price += item_price
if total_price > MINIMAL_PRICE_FOR_DISCOUNT:
    total_price = total_price * DISCOUNTED_PRICE_RATE
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
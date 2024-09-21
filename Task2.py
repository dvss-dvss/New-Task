product_name = input("Введіть назву товару: ")
quantity = int(input("Введіть кількість: "))
price = float(input("Введіть ціну за одиницю: "))
days = int(input("Введіть дні продажів "))

total_cost = quantity * price * days

print(f"Продукт: {product_name}, Кількість: {quantity}, Дні продажів: {days}  Вартість: {total_cost}")
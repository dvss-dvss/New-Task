import random

def generate_ticket(last_name, destination, cost_ticket, departure_time, departure_data):
  ticket_number = random.randint(100000, 999999)
  return f"Квиток №{ticket_number}\nПрізвище: {last_name}\nПункт призначення: {destination}\nЧас відправлення: {departure_time}\nДата відправлення: {departure_data}\nЦіна квитка: {cost_ticket}"

last_name = input("Введіть ваше прізвище: ")
destination = input("Введіть пункт призначення: ")
departure_time = input("Введіть час відправлення: ")
departure_data = input("Введіть дату відправлення: ")
cost_ticket = input("Введіть ціну квитка: ")

print(generate_ticket(last_name, destination, cost_ticket, departure_time, departure_data))
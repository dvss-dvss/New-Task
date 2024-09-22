def weather_report(city, temperature, humidity, unltra_fiol, weather_description):
  return f"Погода в місті {city}:\nТемпература: {temperature}°C\nВологість: {humidity}%\nУльтрафіолетове випромінювання: {ultra_fiol}\n{weather_description}"

city = input("Введіть назву міста: ")
temperature = float(input("Введіть температуру: "))
humidity = int(input("Введіть вологість: "))
weather_description = input("Введіть опис погоди: ")
ultra_fiol = input("Введіть силу ултрофіолета: ")

print(weather_report(city, temperature, humidity, ultra_fiol, weather_description))
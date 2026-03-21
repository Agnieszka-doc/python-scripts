import math
# zmienne
n = 2022
x = round(math.pi, 5) #zaokrąglenie do 5 miejsc po przecinku
word = "Python"
polish = "książka"
# zapis do pliku
with open("vars.txt", "w", encoding="utf-8") as f:
 f.write(f"{n}\n")
 f.write(f"{x}\n")
 f.write(f"{word}\n")
 f.write(f"{polish}\n")
# odczyt i wyświetlenie
with open("vars.txt", "r", encoding="utf-8") as f:
 content = f.read()
print(content)
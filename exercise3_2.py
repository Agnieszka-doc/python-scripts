# Rozwiązanie z pętlą for
for x in range(1, 41): #liczby z zakresu 1-40
 if x == 13: 
  continue
 if x % 5 == 0 and x % 7 == 0: # najpierw sprawdza podzielność przez 5 i 7
  print(x, "is divided by 5 and 7")
 elif x % 5 == 0: # podzielność przez 5
  print(x, "is divided by 5")
 elif x % 7 == 0:
  print(x, "is divided by 7") # podzielność przez 7
 else:
  print(x, "is not important") 
# Rozwiązanie z pętlą while
x = 1
while x <= 40:
 if x == 13: #pominięcie 13
  x += 1
  continue
 if x % 5 == 0 and x % 7 == 0:
  print(x, "is divided by 5 and 7")
 elif x % 5 == 0:
  print(x, "is divided by 5")
 elif x % 7 == 0:
  print(x, "is divided by 7")
 else:
  print(x, "is not important")
 x += 1
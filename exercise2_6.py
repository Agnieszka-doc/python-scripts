#EXERCISE 2_6
t = (2, 4) #tworzy krotkę t z dwoma elementami: 2 i 4
print(t[2]) #indeksy zaczynają się od 0, więc nie istnieje t[2], bo krotka ma tylko dwa elementy, wynik: IndexError: tuple index out of range
t.append(6) #append() jest metodą list, ale nie krotki, Wynik: AttributeError: 'tuple' object has no attribute 'append', bo krotki nie mogą się zmieniać po utworzeniu
a, b = t ; print(a, b) #działa poprawnie, jeśli krotka ma dokładnie dwa elementy, wynik: 2 4

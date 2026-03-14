# EXERCISE 2_4
# (a) Kody Unicode dla imienia
name = "Agnieszka"
unicode_codes = [ord(char) for char in name] #tworzenie listy kodów Unicode dla każdego znaku w imieniu
print("Kody Unicode dla imienia: Agnieszka", unicode_codes)
# (b) Tabela pierwiastków
pt = [
    (1, "Hydrogen", "H", 1),
    (2, "Helium", "He", 4),
    (3, "Lithium", "Li", 7),
    (4, "Beryllium", "Be", 9),
    (5, "Boron", "B", 11),
    (6, "Carbon", "C", 12),
    (7, "Nitrogen", "N", 14),
    (8, "Oxygen", "O", 16),
    (9, "Fluorine", "F", 19),
    (10, "Neon", "Ne", 20)
]
# Nagłówek tabeli
print("+---+--------------------+------+----------+")
print("|No.|Name (en)           |Symbol|Weight (u)|")
print("+---+--------------------+------+----------+")
# Wiersze tabeli
for (n, name, symbol, weight) in pt:
    print(f"|{n:>3}|{name:<20}|{symbol:^6}|{weight:>10}|")
# Dolna linia tabeli
print("+---+--------------------+------+----------+")

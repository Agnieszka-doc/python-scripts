# EXERCISE 2_7
# Słownik konwersji liczb rzymskich na arabskie
# Metoda 1, bezpośrednie przypisanie
roman_to_arabic = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}
# Test
print(roman_to_arabic["X"])   # 10
print(roman_to_arabic["CM"])  # 900
# Metoda 2, słownik z dwóch list
romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
roman_to_arabic2 = dict(zip(romans, values))
print(roman_to_arabic2["L"])  # 50
# Metoda 3
roman_to_arabic3 = {r: v for r, v in zip(romans, values)}
print(roman_to_arabic3["XC"])  # 90

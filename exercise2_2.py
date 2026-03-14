# EXERCISE 2_2
x = 5 #przypisanie wartości 5 do zmiennej x 
x == 5 and 3 + 8   # 11 #lewa strona jest równa 5, dlatego zostaje zwrócony wynik dodawania 3+8 czyli 11
x == 4 and 3 + 8   # False #lewa strona nie jest równa 5, dlatego wynik dodawania nie jest zwrócony, otrzymujemy fałsz
3 + 8 and x == 5   # True #lewa strona jest niezerowa, wynik prawda odnosi się do sprawdzenia czy x=5
3 + 8 and x == 4   # False #lewa strona jest niezerowa, więc jest ok, ale x nie jest równy 4 dlatego fałsz 
isinstance(True, int)    # True #sprawdzenie typu obiektu, czy true jest int, jest to prawda
isinstance(True, bool)   # True #sprawdzenie czy True jest bool, jest to prawda
#EXERCISE 2_5
s = """hodowle komorkowe sa wspaniale.
 Ciesze sie ze moge z nimi pracowac.
 Ale bywaja wymagajace""" #przykładowy tekst
# Liczba czarnych znaków
num_black_chars = sum(1 for char in s if not char.isspace()) #liczy każdy znak, który spełnia warunek, czyli jest prawdziwe dla spacji itd, dlatego negacja
print("Liczba czarnych znaków:", num_black_chars)
# Liczba słów
words = s.split()  # dzieli string na listę słów po białych znakach
num_words = len(words)
print("Liczba słów:", num_words)
# Najdłuższe słowo
longest_word = max(words, key=len)
print("Najdłuższe słowo:", longest_word)
# Sortowanie słów
# a) Alfabetycznie
words_sorted_lex = sorted(words)
print("Słowa alfabetycznie:", words_sorted_lex)
# b) Według długości
words_sorted_len = sorted(words, key=len)
print("Słowa według długości:", words_sorted_len)
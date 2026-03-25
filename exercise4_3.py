# (a) generator liczb parzystych
def iter_even():
 n = 0
 while True:
  yield n
  n += 2
even = iter_even() #przykład użycia
for _ in range(5):
 print(next(even))
# (b) generator liczb nieparzystych
def iter_odd():
 n = 1
 while True:
  yield n
  n += 2
odd = iter_odd() #przykład użycia
for _ in range(5):
 print(next(odd))
# (c) generator potęg
def iter_power(k):
 value = 1
 while True:
  yield value
  value *= k
power = iter_power(3) #przykład użycia
for _ in range(5):
 print(next(power))
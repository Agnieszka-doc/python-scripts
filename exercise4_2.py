L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Wersja iteracyjna
def reverse_range(L1, left, right):
 while left < right:
  L1[left], L1[right] = L1[right], L1[left] #zamiana elementów
  left += 1
  right -= 1
reverse_range(L1, 3, 6)
print(L1)
# Wersja rekurencyjna 
def reverse_range_recursive(L2, left, right):
 if left >= right: #warunek stop
  return
 L2[left], L2[right] = L2[right], L2[left]
 reverse_range_recursive(L2, left + 1, right - 1)
reverse_range_recursive(L2, 3, 6)
print(L2)
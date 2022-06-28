def sum_positive_numbers(n):
  if n <= 1:
      return n
  return n + sum_positive_numbers(n-1)
def sum_positive_numbers(n):
  sums = 0
  for v in range(1,n+1):
    sums += v
  return sums
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

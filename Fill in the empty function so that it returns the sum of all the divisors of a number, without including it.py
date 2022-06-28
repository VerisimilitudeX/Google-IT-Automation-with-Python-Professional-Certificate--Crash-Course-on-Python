def sum_divisors(n):
  sum = 0
  divisor = 1
  while divisor < n:
    if n % divisor == 0:
      sum += divisor
    divisor += 1
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

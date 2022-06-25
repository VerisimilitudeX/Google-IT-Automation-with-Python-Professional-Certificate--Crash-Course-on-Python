def lucky_number(name):
  number = len(name) * 9
  string = "Hello " + name + ". Your lucky number is " + str(number)
  return string

print(lucky_number("Kay"))
print(lucky_number("Cameron"))

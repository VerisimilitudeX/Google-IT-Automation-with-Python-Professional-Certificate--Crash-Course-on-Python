def format_address(address_string):
  housenumber = ""
  streetname = ""

  splitaddress = address_string.split()
  housenumber = splitaddress[0]
  streetname = splitaddress[1:(len(splitaddress))]

  formattedstreetname = ""

  lengthofstreetname = len(streetname)

  for part in streetname:
      formattedstreetname += part
      if lengthofstreetname > 1:
        formattedstreetname += " "
      lengthofstreetname -= 1
  lengthofstreetname = 0
  return "house number {} on street named {}".format(housenumber, formattedstreetname)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

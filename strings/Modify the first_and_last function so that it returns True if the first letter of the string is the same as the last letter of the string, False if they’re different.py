def first_and_last(message):
    if message == "":
        return True
    first = message[0]
    last = message[-1]
    if first == last:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

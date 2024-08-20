password = input("Enter Password ")
result = []
if len(password) > 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

upl = False
for i in password:
    if i.isupper():
        upl = True

result.append(upl)
print(result)
print(all(result))
if (all(result)):
    print("Password is strong")
else:
    print("Password is week")

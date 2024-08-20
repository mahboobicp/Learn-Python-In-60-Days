password = "ffsad23456"
result = {}
if len(password) > 8:
    result["Length"] = True
else:
    result["Length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["Digit"] = digit

upl = False
for i in password:
    if i.isupper():
        upl = True

result["Upper Case"] = upl
print(result)
print(all(result.values()))
if (all(result.values())):
    print("Password is strong")
else:
    print("Password is week")

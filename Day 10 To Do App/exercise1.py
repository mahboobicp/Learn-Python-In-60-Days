try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    perct = (value/total_value)*100
    print(f"That is {perct}%")
except:
    print("Error")
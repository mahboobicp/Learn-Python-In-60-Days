date = input("Enter Date : ")
thought = input("Enter your thoughts : \n")
path = r"D:\Learn Python in 60 Days\Day 08 To Do App"

with open(f"{path}\{date}.txt", 'w') as file:
    file.write(thought)



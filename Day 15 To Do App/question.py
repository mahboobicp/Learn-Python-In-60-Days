import json
FILEPATH = r"D:\Python\Learn-Python-In-60-Days\Day 15 To Do App\q.json"
with open(FILEPATH,'r') as file:
    content = file.read()

data = json.loads(content)
#print(data)
score = 0
for qu in data:
    print(qu["question"])
    for index,ch in enumerate(qu["choice"]):
        print(f"{index + 1} - {ch}")
    uch = int(input("Enter answer : "))
    qu["uans"] = uch
    if qu["correct"] == qu["uans"]:
        score += 1

print(f"Your Score is : {score}/{len(data)}")
    

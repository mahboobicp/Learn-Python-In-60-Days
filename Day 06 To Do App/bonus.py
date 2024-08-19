""" in this section we will create a creat file and 
write conents to the files from LIST
 """
contents = ['A quick brown' , 'Fox jumps']
docs = ['test1.txt' , 'test2.txt']
path = r"D:\Python\Learn-Python-In-60-Days\Day 06 To Do App"  # Absolut path is required r is used for raw string

for content,doc in zip(contents,docs):                        # zip is like enumerate but it return values not indexs
    file = open(f"{path}\{doc}",'w')
    file.writelines(content)
    file.close()


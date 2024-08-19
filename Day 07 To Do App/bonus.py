lists = ['1.Doc' , '2.Book' , '3.Game']
# To transform this we will use list comprehension
new_list = [list.replace('.','-') + '.txt' for list in lists]
print(new_list)
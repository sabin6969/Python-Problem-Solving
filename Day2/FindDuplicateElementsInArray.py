original_list =[10,20,20,30,40,50,"hello","Ram","bikash","hello","hello","Ram"]
duplicate_elements =[]
for i in original_list:
    if(original_list.count(i)>1 and i not in duplicate_elements):
        duplicate_elements.append(i)
print(duplicate_elements)
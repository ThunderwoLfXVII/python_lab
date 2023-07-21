list_of_strings = []
while(True):
    st = input("Enter the string to add to list(Enter 0 to stop) : ")
    if st == '0':
        break
    list_of_strings.append(st)

count = 0 
result = []
for string in list_of_strings:
    if len(string) >= 2 and string[0]==string[-1]:
        count+=1
        result.append(string)

print(f"There are {count} string whose length is 2 or more and first and last letter is same.")
print(result)
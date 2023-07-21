def str_len(s):
    if len(s) == 0:
        return 0
    return 1 + str_len(s[1:])

string = input("Enter a string : ")
print(f"Length of string : {str_len(string)}")



def min_element(l,min_value):
    if len(l) == 1:
        return min_value if min_value < l[0] else l[0]
    return min_element(l[1:],l[0] if l[0] < min_value else min_value)

num = []
while(True):
    n = int(input("Enter the number(Enter 0 to stop) : "))
    if n == 0 :
        break
    num.append(n)

print(f"Minimum element in a list is {min_element(num[1:] , num[0])}")
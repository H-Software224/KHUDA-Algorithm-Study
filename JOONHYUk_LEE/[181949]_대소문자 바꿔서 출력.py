str = input()
str_list = list(str)

for i in range(len(str_list)):
    if str_list[i].isupper()  == True:
        str_list[i] = str_list[i].lower()
    else:
        str_list[i] = str_list[i].upper()

result = ''.join(str_list)
print(result)
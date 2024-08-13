# add your code here
upper_list = []
lower_list = []
for i in range(65,91):
    upper_list.append(i)
for i in range(97,123):
    lower_list.append(i)
c_cipher = input('Enter message:')
coded_message = ''
for char in c_cipher:
    new_val = ''
    if ord(char) in upper_list:
        new_val = chr(upper_list[upper_list.index(ord(char)) + 5 - len(upper_list)])
    elif ord(char) in lower_list:
        new_val = chr(lower_list[lower_list.index(ord(char)) + 5 - len(lower_list)])
    else:
        new_val = char
    coded_message = coded_message + new_val
print(coded_message)
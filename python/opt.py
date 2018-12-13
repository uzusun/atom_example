user_data1 = input()
user_data2 = input()
user_data_opt = input()

if user_data_opt == '+':
    user_data_total = int(user_data1) + int(user_data2)
elif user_data_opt == '-':
    user_data_total = int(user_data1) - int(user_data2)
elif user_data_opt == '*':
    user_data_total = int(user_data1) * int(user_data2)
elif user_data_opt == '/':
    user_data_total = int(user_data1) / int(user_data2)
elif user_data_opt == '%':
    user_data_total = int(user_data1) % int(user_data2)
else:
    print("%s is not supported symbol" % user_data_opt)
    exit()

print("결과값 : ",user_data_total)

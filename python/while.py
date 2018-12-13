user_data1 = input()
user_data2 = input()
user_data_opt = input()

while user_data_opt == '+' or user_data_opt == '-' or user_data_opt == '*' or user_data_opt == '/':
    if user_data_opt == '+':
        user_data_total = int(user_data1) + int(user_data2)
    elif user_data_opt == '-':
        user_data_total = int(user_data1) - int(user_data2)
    elif user_data_opt == '*':
        user_data_total = int(user_data1) * int(user_data2)
    elif user_data_opt == '/':
        user_data_total = int(user_data1) / int(user_data2)

    print("결과값 : ",user_data_total)

    user_data1 = input()
    user_data2 = input()
    user_data_opt = input()

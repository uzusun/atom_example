for temp_data in range(1,10):
    user_data1 = input("%d 번째 첫번째 값 : " % temp_data)
    user_data2 = input("%d 번째 두번째 값 : " % temp_data)
    user_data_opt = input("연산자 입력 : ")
    if user_data_opt == '+':
        user_data_total = int(user_data1) + int(user_data2)
    elif user_data_opt == '-':
        user_data_total = int(user_data1) - int(user_data2)
    elif user_data_opt == '*':
        user_data_total = int(user_data1) * int(user_data2)
    elif user_data_opt == '/':
        user_data_total = int(user_data1) / int(user_data2)

    print("두 수의 %s 결과값 : %d" % (user_data_opt,user_data_total))

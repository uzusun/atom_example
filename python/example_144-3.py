def caculate (product,money):
    return money - drink_data[product]

def print_list():
    print("<Drink List>")
    for item in drink_data.keys():
        print(str(item) + ":" + str(drink_data[item]))

drink_data = {"cola":1000, "milk":1500, "juice":2000, "water":900, "sprite":1000}

product = input("Input drink name?(Drink name or LIST) ")
while(1):
    if product.lower() == "list":
        print_list()
        product = input("what do you want?(Drink name) ")
    elif product.lower() not in drink_data.keys():
        print("Not provided")
        print_list()
        product = input("what do you want?(Drink name) ")
    else:
        break

money = input("Input price? ")

calc = caculate(product.lower(), int(money))

if (calc == 0):
    print("get a %s" % product.lower())
elif (calc > 0):
    print("change : %d" % calc)
    print("get a %s" % product.lower())
else:
    print("%s is %d, but you paid %d" % (product.lower(), int(drink_data[product.lower()]), int(money)))
    print("please pay %d (Do you agree? Y/N) " % abs(calc))
    answer = input()
    if answer == "Y":
        print("get a %s" % product.lower())
    else:
        print("return %d" % int(money))

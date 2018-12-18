#한글 깨짐 보정
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

drink_data = {"cola":1000, "milk":1500, "juice":2000, "water":900, "sprite":1000}

def vending_machine(product,money):
    if product in drink_data.keys():
        calc = int(money) - int(drink_data[product])
        if calc == 0:
            print("get a %s" % product)
        elif calc > 0:
            print("change : %d" % calc)
            print("get a %s" % product)
        else:
            print("%s is %d, but you paid %d" % (product, int(drink_data[product]), int(money)))
            print("please pay %d (Do you agree? Y/N) " % abs(calc))
            answer = input()
            if answer == "Y" or answer == "y":
                print("get a %s" % product)
            else:
                print("return %d" % money)
    else:
        print("없는 상품입니다! 상품명을 확인해주세요!!")
        exit()

print("<Drink List>")
for item in drink_data.keys():
    print(item, drink_data[item])

product = input("Input drink name? ")
money = input("Input price? ")

vending_machine(product,money)

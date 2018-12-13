drink_data = {"cola":1000, "milk":1500, "juice":2000, "water":900, "sprite":1000}

print("== Product list ==")
for key in drink_data.keys():
    print(key)

select_product = input("상품을 선택하세요 : ")

if select_product in drink_data.keys():
    #price = drink_data[select_product]
    print("%s 의 가격은 %d 원 입니다." % (select_product, drink_data[select_product]))
else:
    print("없는상품입니다.")

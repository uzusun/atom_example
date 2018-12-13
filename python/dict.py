drink = {"cola":1000,"milk":1500,"juice":2000,"water":900}
print(drink)
a = print(drink["cola"])
print(drink.keys())
for key in drink.keys():
    print(key)

print(list(drink.keys()))
print(drink.values())
print(drink.items())
#drink.clear()
print(drink)
b = print(drink.get("cola"))
print(type(a))
print(type(b))
print("orange juice" in drink)
print("juice" in drink)

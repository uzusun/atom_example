class vending:
    location = ""
    drink_data = {}
    def calculation(self, selected_drink_name, payment):
        return payment - self.drink_data[selected_drink_name]

vending1 = vending()
vending2 = vending()
vending3 = vending()

vending1.location = "seoul"
vending2.location = "incheon"
vending3.location = "suwon"

vending1.drink_data["cola"] = 1000
vending1.drink_data["juice"] = 1500
vending2.drink_data["water"] = 900
vending2.drink_data["sprite"] = 1100
vending3.drink_data["milk"] = 500

vending_name = input("vending name:")
selected_drink_name = input("drink name:")
payment = input("payment:")
if vending_name == vending1.location:
    calc = vending1.calculation(selected_drink_name, int(payment))
    print("selected drink name is %s" % selected_drink_name)
    if calc > 0:
        print("change: %d" % calc)
    elif calc < 0:
        print("required: %d" % calc)
    else:
        print("provied")
elif vending_name == vending2.location:
    calc = vending1.calculation(selected_drink_name, int(payment))
    print("selected drink name is %s" % selected_drink_name)
    if calc > 0:
        print("change: %d" % calc)
    elif calc < 0:
        print("required: %d" % calc)
    else:
        print("provied")
elif vending_name == vending3.location:
    calc = vending1.calculation(selected_drink_name, int(payment))
    print("selected drink name is %s" % selected_drink_name)
    if calc > 0:
        print("change: %d" % calc)
    elif calc < 0:
        print("required: %d" % calc)
    else:
        print("provied")
else:
    print("Not provided")

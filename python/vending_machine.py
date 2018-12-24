class vending:
    location = ""
    drink_data = {}
    def calculation(self, selected_drink_name, payment):
        print(payment - self.drink_data[selected_drink_name])

vending1 = vending()
vending2 = vending()

vending1.location = "seoul"
vending2.location = "incheon"

vending1.drink_data["cola"] = 1000
vending1.drink_data["juice"] = 1500
vending2.drink_data["water"] = 900
vending2.drink_data["sprite"] = 1100

vending_name = input("vending name:")
selected_drink_name = input("drink name:")
payment = input("payment:")
if vending_name == vending1.location:
    calc = vending1.calculation(selected_drink_name, int(payment))
elif vending_name == vending2.location:
    vending2.calculation(selected_drink_name, int(payment))

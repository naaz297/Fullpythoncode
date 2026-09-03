class Chef:

    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("The chef makes salad")

    def make_special_dish(self):
        print("The chef makes a special dish")


class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The Chinese chef makes fried rice")

    def make_noodles(self):
        print("The Chinese chef makes noodles")

    def make_special_dish(self):
        print("The Chinese chef makes orange chicken")


myChef = Chef()

myChef.make_chicken()
myChef.make_salad()
myChef.make_special_dish()

myChineseChef = ChineseChef()

myChineseChef.make_chicken()
myChineseChef.make_salad()
myChineseChef.make_fried_rice()
myChineseChef.make_noodles()
myChineseChef.make_special_dish()

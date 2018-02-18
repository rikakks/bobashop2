fruit_tea = {
    'Mango Green Tea': 3.75,
    'Grapefruit Green Tea': 3.75,
    'Honey Lemon with Aloe Vera': 3.75,
    'Wintermelon with Lemon Juice': 3.75,
    'Strawberry Black Tea': 4.00,
    'Pineapple Green Tea with Aiyu jelly': 4.00,
    'Hawaii Fruit Tea': 4.25,
    'Kiwi Fruit Tea with Aiyu Jelly': 4.25,
    'Mango and Passion Fruit Green Tea': 4.25,
    'Whole Lemon Black Tea': 4.25,
    'Passion Fruit, Orange and Grapefruit Tea': 4.25,
}

brewed_tea = {
    'Classic Black Tea': 3.25,
    'Classic Green Tea': 3.25,
    'Classic Oolong Tea': 3.25,
    'Wintermelon Tea': 3.00,
    'Honey Black Tea': 3.25,
    'Ginger Tea': 3.50,
}

creama = {
    'Creama Tea': 4.00,
    'Wintermelon Tea Creama': 4.00,
    'Coffee Creama': 4.00,
    'Cocoa Creama': 4.25,
    'Mango Green Tea Creama': 4.25,
    'Matcha Green Tea Creama': 4.25,
}

fresh_milk = {
    'Fresh Milk Tea': 3.75,
    'Wintermelon with Fresh Milk': 3.75,
    'Cocoa Lover': 4.00,
    'Boba Fresh Milk': 4.00,
    'Match with Fresh Milk': 4.00,
    'Handmade Taro with Fresh Milk': 4.25,
}

milk_tea = {
    'Classic Milk Tea': 3.50,
    'Honey Milk Tea': 3.50,
    'Classic Coffee': 3.75,
    'Ginger Milk Tea': 3.75,
    'Coffee Milk Tea': 3.75,
    'Hokkaido Pearl Milk Tea': 4.00,
    'Okinawa Pearl Milk Tea': 4.00,
    'Classic Pearl Milk Tea': 4.00,
    'Taro Pearl Milk Tea': 4.00,
    'Mango Green Milk Tea': 4.25,
    'QQ Happy Family Milk Tea': 4.25,
    'Match Red Bean Milk Tea': 4.25,
}

ice_blended = {
    'Oreo Ice Blended with Pearl': 4.75,
    'Taro Ice Blended with Pudding': 4.75,
    'Milk tea Ice Blended with Pearl': 4.75,
    'Matcha Red Bean with Ice Cream': 4.75,
    'Coffee Ice Blended with Ice Cream': 4.75,
    'Mango Ice Blended with Ice Cream': 4.75,
    'Strawberry Ice Blended': 4.75,
}

type_of_tea = {
    'Fruit Tea': fruit_tea,
    'Brewed Tea': brewed_tea,
    'Creama': creama,
    'Fresh Milk': fresh_milk,
    'Milk Tea': milk_tea,
    'Ice Blended': ice_blended,
}

toppings = {
    'Pearl': 0.50,
    'Mini Pearl': 0.50,
    'Red Bean': 0.50,
    'Herb Jelly': 0.50,
    'Aloe Jelly': 0.50,
    'Pudding': 0.50,
    'Aloe Vera': 0.50,
    'Lychee Jelly': 0.50,
    'Ice Cream': 0.50,
}

sugar_levels = {
    0: '100%',
    1: '80%',
    2: '50%',
    3: '30%',
    4: '0%',
}

ice_levels = {
    0: 'Regular Ice',
    1: 'Less Ice',
    2: 'No Ice',
}


class Boba:
    def name(self):
        name = 0
        while name == False:
            name = input("Enter your name: ")
        self.name = name

    def item_selected(self):
        print("Here is a list of the types of tea we offer: ")
        for tea in type_of_tea:
            print(tea)
        type_of_tea_input = 0
        while type_of_tea_input not in type_of_tea:
            type_of_tea_input = input("""What kind of tea would you like?
Enter name of menu: """)
        type_of_tea_selected = type_of_tea[type_of_tea_input]
        print("Here is a list of tea we offer for " + type_of_tea_input + ": ")
        for tea, price in type_of_tea_selected.items():
            print(tea, price)
        tea_input = 0
        while tea_input not in type_of_tea_selected:
            tea_input = input("Which tea would you like? Enter name of tea: ")
        self.tea_input = tea_input
        self.item_selected = type_of_tea_selected[tea_input]

    def toppings(self):
        self.toppings = []
        print("Here is a list of toppings we offer: ")
        for topping, price in toppings.items():
            print(topping, price)
        topping_input = ''
        while topping_input.lower() != 'n':
            topping_input = input("""Would you like to add any further
toppings? Enter the name of topping. Otherwise, enter 'n': """)
            if topping_input in toppings:
                self.toppings.append(topping_input)

    def sugar_levels(self):
        print("You have the following options for the sweetness level:")
        for number, percentage in sugar_levels.items():
            print(number, percentage)
        sugar_levels_selected = 5
        while sugar_levels_selected not in range(5):
            sugar_levels_selected = int(input("Enter a number from 0~4: "))
        self.sugar_levels = sugar_levels[sugar_levels_selected]

    def ice_levels(self):
        print("You have the following options for the ice level:")
        for number, percentage in ice_levels.items():
            print(number, percentage)
        ice_levels_selected = 3
        while ice_levels_selected not in range(3):
            ice_levels_selected = int(input("Enter a number from 0~2: "))
        self.ice_levels = ice_levels[ice_levels_selected]

    def bill(self):
        print("You have ordered: " + self.tea_input)
        if self.toppings != []:
            for topping in self.toppings:
                print('with ' + topping)
        print("Sugar Levels: " + self.sugar_levels)
        print("Ice Levels: " + self.ice_levels)
        total = self.item_selected
        for topping in self.toppings:
            total += toppings[topping]
        print("Your total for today is: $" + ('%.2f' % total) + '.')
        print("Thank you for getting boba with us!")


boba = Boba()
boba.name()
boba.item_selected()
boba.toppings()
boba.sugar_levels()
boba.ice_levels()
boba.bill()

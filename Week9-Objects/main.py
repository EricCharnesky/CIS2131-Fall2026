import random


class CoffeeCup:

    # init or constructor gives default values
    def __init__(self, max_size_in_milliliters):

        # attributes starting with _ are considered private
        self._color = "blue"
        self._max_size_in_milliliters = max_size_in_milliliters
        self._current_volume_of_contents_in_milliliters = 0
        self._has_lid = False

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_has_lid(self):
        return self._has_lid

    def set_has_lid(self, has_lid):
        self._has_lid = has_lid

    def get_current_volume_of_contents_in_milliliters(self):
        return self._current_volume_of_contents_in_milliliters

    def set_current_volume_of_contents_in_milliliters(self, current_volume_of_contents_in_milliliters):
        if current_volume_of_contents_in_milliliters < 0 \
                or current_volume_of_contents_in_milliliters > self._max_size_in_milliliters:
            # don't put print statements here
            raise ValueError("Invalid volume")  # no need for else, code will stop here
        self._current_volume_of_contents_in_milliliters = current_volume_of_contents_in_milliliters

    def get_max_size_in_milliliters(self):
        return self._max_size_in_milliliters

    def fill(self, amount_to_fill_in_milliliters):
        if amount_to_fill_in_milliliters < 0 or \
                self._current_volume_of_contents_in_milliliters + amount_to_fill_in_milliliters > self._max_size_in_milliliters:
            raise ValueError("Invalid amount to fill")
        self._current_volume_of_contents_in_milliliters += amount_to_fill_in_milliliters

    def drink(self, amount_to_drink_in_milliliters):
        if amount_to_drink_in_milliliters < 0 or \
                amount_to_drink_in_milliliters > self._current_volume_of_contents_in_milliliters:
            raise ValueError("Invalid amount to drink")
        self._current_volume_of_contents_in_milliliters -= amount_to_drink_in_milliliters


erics_cup = CoffeeCup(350)
erics_cup.set_color("Wood pattern")

while True:
    current_volume = int(input("How much coffee is in your mug in milliliters?"))
    try:
        erics_cup.set_current_volume_of_contents_in_milliliters(current_volume)
        break
    except ValueError as e:
        print(e)

# usual way
print(erics_cup.get_color())

# weird way
print(CoffeeCup.get_color(erics_cup))

erics_desk = []
erics_desk.append(CoffeeCup(350))
erics_desk.append(CoffeeCup(250))
erics_desk.append(CoffeeCup(500))

erics_desk[0].set_color("brown")
erics_desk[1].set_color("black")

erics_desk[0].fill(random.randint(1, 350))
erics_desk[1].fill(random.randint(1, 250))
erics_desk[2].fill(random.randint(1, 500))

for cup in erics_desk:
    print(f'{cup.get_color()} mug has {cup.get_current_volume_of_contents_in_milliliters()} left')
    drink = input("Do you want to drink from it? y/n").lower()
    if drink == 'y':
        how_much = int(input("How many milliliters do you want to drink?"))
        cup.drink(how_much)


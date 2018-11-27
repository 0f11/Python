"""Bakery.py."""


class Baker:
    def __init__(self, name: str, experience_level: int, money: int):
        """
        Constructor.

        :param name:
        :param experience_level:
        :param money:
        """
        self.name = name
        self.experience_level = experience_level
        self.money = money

    def __repr__(self):
        """
        Helper.
        :return:
        """
        return f"Baker: {self.name}({self.experience_level})"


class Pastry:
    def __init__(self, name: str, complexity_level: int):
        """
        Constructor.

        :param name:
        :param complexity_level:
        """
        self.name = name
        self.complexity_level = complexity_level

    def __repr__(self):
        """
        Helper.

        :return:
        """
        return self.name


class Recipe:
    def __init__(self, name, complexity_level):
        """
        Constructor.

        :param name:
        :param complexity_level:
        """
        self.name = name
        self.complexity_level = complexity_level

    def __repr__(self):
        """
        Helper.

        :return:
        """
        return self.name


class Bakery:
    def __init__(self, name: str, min_experience_level: int, budget: int):
        """
        Constructor.

        :param name:
        :param min_experience_level:
        :param budget:
        """
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.bakers = []
        self.recipe = {}
        self.pastries = []

    def add_baker(self, baker: Baker):
        """
        Adding baker to the bakery.

        :param baker:
        :return:
        """
        if isinstance(baker, Baker):
            if self.min_experience_level <= baker.experience_level:
                self.bakers.append(baker)
                return Baker

    def remove_baker(self, baker: Baker):
        """
        Removing baker from the bakery.

        :param baker:
        :return:
        """
        if baker in self.bakers:
            self.bakers.remove(baker)

    def add_recipe(self, name: str):
        """
        Adding recipe to the bakery.

        :param name:
        :return:
        """
        price = len(name)
        exp_level_baker = [bakers.experience_level for bakers in self.bakers]
        if price < self.budget and name not in self.recipe and (len(self.bakers)) > 0:
            complexity_level = abs((len(name) * len(self.bakers)) - min(exp_level_baker))
            recipe = Recipe(name, complexity_level)
            self.recipe[name] = recipe
            self.budget -= price

    def make_order(self, name: str):
        """
        Making the order.

        :param name:
        :return:
        """
        exp_level_baker = [bakers.experience_level for bakers in self.bakers]

        if name in self.recipe.keys() and len(self.bakers) > 0:
            for exp in exp_level_baker:
                if exp:
                    price = len(name) * 4
                    self.budget += price // 2
                    self.min_experience_level += 1

                    return Pastry

    def get_recipes(self) -> dict:
        """
        Get the recipes.

        :return:
        """
        d = {}
        for name, recipe in self.recipe:
            d[name] = recipe.complexity_level
        return d

    def get_pastries(self) -> list:
        """
        Get the pastries.

        :return:
        """
        return sorted(self.pastries, key=lambda p: p.complexity_level, reverse=True)

    def get_bakers(self) -> list:
        """
        Get list of bakers.

        :return:
        """
        return sorted(self.bakers, key=lambda b: b.experience_level, reverse=True)

    def __repr__(self):
        """
        Helper.

        :return:
        """
        return f"Bakery {self.name}: {len(self.bakers)} baker(s)"

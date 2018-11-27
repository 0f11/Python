"""Gym.py."""


class Gym:

    def __init__(self, name, max_members_number):
        self.name = name
        self.max_memebers_number = max_members_number
        self.members = {}

    def add_member(self, member):
        """Add member to the gym."""
        if self.max_memebers_number > len(self.members.keys()) and self.can_add_member(member):
            self.members[member] = self.name
            member.gyms.append(self.name)
        else:
            stamina = self.lowest_stamina()
            members = dict(self.members)
            for i in members:
                if i.trainers.stamina == stamina:
                    del self.members[i]
                self.members[member] = self.name
                member.gym.append(self.name)

    def lowest_stamina(self, member):
        return

    def can_add_member(self, member):
        pass

    def remove_member(self, member):
        pass

    def get_total_stamina(self):
        pass

    def get_members_number(self):
        pass

    def get_all_members(self):
        pass

    def get_average_age(self):
        pass

    def __repr__(self):
        return f""


class Member:
    def __init__(self, name, age, trainers):
        self.name = name
        self.age = age
        self.trainers = trainers

    def get_all_gyms(self):
        pass
        # all_gyms =

    def get_gyms(self):
        pass

    def __repr__(self):
        return f"{self.name}, {self.age}: {self.trainers}."


class Trainers:
    def __init__(self, stamina, color):
        self.stamina = stamina
        self.color = color

    def __str__(self):
        return f"Trainers: [{self.stamina}, {self.color}]."


class City:
    def __init__(self, max_gym_number):
        self.max_gym_number = max_gym_number
        self.number_of_gyms = 0
        self.gyms = []

    def build_gym(self, gym):
        if self.can_build_gym():
            self.gyms.append(gym)

    def can_build_gym(self):
        if self.number_of_gyms < self.max_gym_number:
            return True


    def destroy_gym(self):
        min_members_count = min(len(gym.members) for gym in self.gyms)
        min_members_count = min(self.gyms, key=lambda gym: len(gym.members))
        min_gyms = [gym for gym in self.gyms if len(gym.members) == min_members_count]

        min_members_count = len(self.gyms[0].members)
        gyms_to_destroy = []
        for gym in self.gyms:
            if len(gym.members) < min_members_count:
                min_members_count = len(gym.members)
                gyms_to_destroy = [gym]
            elif len(gym.members) == min_members_count:
                gyms_to_destroy.append(gym)
        for gym in gyms_to_destroy:
            pass

    def get_max_members_gym(self):
        pass

    def get_max_stamina_gyms(self):
        pass

    def get_max_average_ages(self):
        pass

    def get_min_average_ages(self):
        pass

    def get_gyms_by_trainers_color(self, color):
        pass

    def get_gyms_by_name(self, name):
        pass

    def get_all_gyms(self):
        pass

    def __repr__(self):
        return f""

if __name__ == "__main__":

    city1 = City(100)
    gym = Gym("TTÜ Sport", 50)
    city1.build_gym(gym)

    trainers1 = Trainers(50, "blue")
    trainers2 = Trainers(50, "grey")

    member = Member("Ago Luberg", 35, trainers1)
    member2 = Member("Ahti Lohk", 35, trainers2)

    gym.add_member(member)
    gym.add_member(member2)

    print(gym.get_members_number())  # 2

    print(gym.get_all_members())  # [Ago Luberg, 35: Trainers: [50, blue], Ahti Lohk, 35: Trainers: [50, grey]]

    gym.add_member(member)  # Trying to add Ago again
    print(gym.get_members_number())  # 2 //We can't...

    for i in range(48):
        gym.add_member(Member("Tudeng Tudeng", 20, Trainers(49, "blue")))

    print(gym.get_members_number())  # 50

    trainers3 = Trainers(60, "blue")
    member_new = Member("Megane", 19, trainers3)
    gym.add_member(member_new)

    print(
        gym.get_members_number())  # 3 -> Ago, Ahti and Megan, all others were removed because of the lowest trainers' stamina

    city2 = City(10)
    city2.build_gym(Gym("MyFitness", 100))
    city2.destroy_gym()

    for i in range(9):
        city2.build_gym(Gym("Super Gym", 10))

    print(city2.can_build_gym())  # False -> Cannot build gym, city is full of them

    # #######################################################################################
    #
    # city3 = City(100)
    #
    # gym4 = Gym("Sparta", 50)
    # gym5 = Gym("People Fitness", 30)
    # gym6 = Gym("Gym Eesti", 100)
    #
    # city3.build_gym(gym4)
    # city3.build_gym(gym5)
    # city3.build_gym(gym6)
    #
    # gym4.add_member(Member("Bob", 18, Trainers(50, "black")))
    # gym4.add_member(Member("Emma", 20, Trainers(70, "red")))
    # gym4.add_member(Member("Ken", 25, Trainers(40, "grey")))
    #
    # gym5.add_member(Member("Merili", 18, Trainers(100, "pink")))
    # gym5.add_member(Member("Richard", 20, Trainers(70, "green")))
    #
    # gym6.add_member(Member("Bella", 40, Trainers(15, "green")))
    # gym6.add_member(Member("Bob", 50, Trainers(70, "green")))
    # gym6.add_member(Member("Sandra", 25, Trainers(30, "pink")))
    # gym6.add_member(Member("Bob", 35, Trainers(50, "black")))
    #
    # city3.get_max_members_gym()  # [Gym Gym Eesti : 4 member(s)]
    # city3.get_max_stamina_clubs()  # [Gym People Fitness : 2 member(s)]
    # city3.get_max_average_ages()  # [Gym Gym Eesti : 4 member(s)] => average age 37,5
    # city3.get_min_average_ages()  # [Gym People Fitness : 2 member(s)] => average age 19
    # city3.get_gyms_by_trainers_color(
    #     "green")  # [Gym Gym Eesti : 4 member(s), Gym People Fitness : 2 member(s)] => Gym Eesti has 2 members with green trainers, People Fitness has 1.
    # city3.get_gyms_by_name(
    #     "Bob")  # [Gym Gym Eesti : 4 member(s), Gym Sparta : 2 member(s)] => Gym Eesti has 2 members with name Bob, Sparta has 1.
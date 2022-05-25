class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Targaryen(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Targaryen"
        self.house_words = "Fire and Blood"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

# Daenerys = Targaryen("Daenerys")
# Daenerys.print_house_words()
# print(Daenerys.__dict__)
# print(Daenerys.is_alive)
# Daenerys.die()
# print(Daenerys.is_alive)

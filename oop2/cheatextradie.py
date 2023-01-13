# add an extra dice roll
class Cheat_Extra_Die(Player):
    def cheat(self):
        self.dice.append(random.randint(1,6))


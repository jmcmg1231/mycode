# if total dice is under 9, get a re-roll
class Cheat_Mulligan(Player):
    def cheat(self):
       if sum(self.dice) <= 9:
           self.dice = []
           for i in range(3):
              self.dice.append(random.randint(1,6))


# first die roll is lucky and can't roll under a 3
class Cheat_Lucky_Die(Player):
    def cheat(self):
        if self.dice[0] < 3:
           self.dice[0]= random.randint(3,6)


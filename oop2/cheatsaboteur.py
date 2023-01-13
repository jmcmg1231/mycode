# switch other player's dice with dice that can't roll above a 3
class Cheat_Saboteur(Player):
  def cheat(self, other_player):
    other_player.dice = [random.randint(1,3) for i in range(3)]
                        # ^ this is a list comprehension;
                        # a handy way to generate list contents
                        # in one line of code


import random

class Dice:
    """Creates a dice class that takes a number of sides and rolls randomly within that number"""
    """The only dice we need is a six sided, so it's mostly conceptual"""

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Player:
    """Player creator"""
    """Took some work to make the turns come out ok, had them in the pig function for a long time"""

    def __init__(self, number):
        self.number = number
        self.score = 0
        self.turn_score = 0

    def pig_roll(self):
        return Dice(6).roll()

    def take_turn(self):
            self.turn_score = 0
            can_roll = True
            print(f'It\'s Player {self.number}\'s turn! They have {self.score} points!')
            while can_roll:
                output = input('r to roll, h to hold ')
                if output not in ['h', 'r']:
                    print('Try to keep it to h or r ')
                elif output == 'h':
                    self.score += self.turn_score
                    print(f'Holding at {self.turn_score}. Player {self.number} currently has {self.score}')
                    can_roll = False
                    break

                elif output == 'r':
                    outcome = self.pig_roll()
                    if outcome == 1:
                        print(f'Sorry, turn is over! Back to {self.score} points.')
                        self.turn_score = 0
                        break
                    else:
                        self.turn_score += outcome
                        print(f'Rolled a {outcome}. The score so far is {self.turn_score}.')


def Pig_game():
    """Simplified game function, with most of the code in the classes"""
    """The winner checks could probably have been written more elegantly"""

    winner = False
    current_turn = 1
    player1 = Player(1)
    player2 = Player(2)
    turn_score = 0

    while not winner:
        if player1.score >= 100:
            print('Player 1 has won the game!')
            break
        elif player2.score >= 100:
            print('Player 2 has won the game!')
            break
        else:
            player1.take_turn()
            player2.take_turn()

if __name__ == '__main__':
    Pig_game()
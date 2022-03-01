import random

from Player import *


class Game:
    def __init__(self, players: list[Player]):
        self.players = players
        print(list(self.players))
        i = 1
        for player in players:
            player.team = i
            i += 1

    def start(self):
        plateau = Plateau()
        is_finished = False
        last_x, last_y = 0, 0
        n = 0
        plateau.show(True)
        while not plateau.est_gagnant(last_x, last_y, (n-1) % len(self.players) + 1) and not plateau.est_nulle():
            coord = self.players[n % len(self.players)].joue(plateau)
            while not coord:
                coord = self.players[n % len(self.players)].joue(plateau)
            last_x, last_y = coord
            plateau.show(True)
            n += 1

        if not plateau.est_nulle():
            print(f"Partie terminée: {plateau.case(last_x, last_y)} a gagné!")
        else:
            print("Partie nulle.")


if __name__ == '__main__':
    human = Player(is_human=True)
    robot = Player(is_human=True)
    joueurs = [human, robot]
    g = Game(players=joueurs)
    g.start()

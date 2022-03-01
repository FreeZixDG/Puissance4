from random import shuffle
from typing import Tuple

from Plateau import Plateau


class Player:
    def __init__(self, is_human: bool = False):
        self.is_human = is_human
        self.team = None
        self.score = 0

    def ajoute_piece(self, plateau: Plateau, colonne: int) -> tuple[int, int] | bool:
        """
        Ajoute un pion d'une equipe e dans la grille dans les regles du Puissance 4.
        :param plateau: Plateau
        :param colonne: colonne
        :param e: equipe
        :return: True si le mouvement est valide, False sinon
        """
        for i in range(plateau.ligne - 1, -1, -1):
            if not plateau.case(colonne, i):
                plateau.add(colonne, i, self.team)
                return colonne, i
        return False

    def joue_aleatoire(self, plateau: Plateau):
        """
        Joue un coup aléatoire
        :param plateau: Plateau
        :return: True si le coup est validé, False sinon
        """
        coup_possibles = list(range(0, plateau.colonne))
        shuffle(coup_possibles)
        coup = coup_possibles[-1]
        coord = self.ajoute_piece(plateau, coup)
        while not coord:
            coup_possibles.pop()
            if not coup_possibles:
                return False
            coup = coup_possibles[-1]
            coord = self.ajoute_piece(plateau, coup)
        return coord

    def joue(self, plateau):
        if self.is_human:
            while True:
                try:
                    col = int(input("choose col: "))
                    if not 0 <= col <= plateau.colonne:
                        raise ValueError
                except ValueError:
                    continue
                break

            return self.ajoute_piece(plateau, col)

        return self.joue_aleatoire(plateau)

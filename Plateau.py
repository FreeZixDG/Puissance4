

class Plateau:
    def __init__(self, colonne: int = 7, ligne: int = 6):
        if colonne <= 0 or ligne <= 0: raise AttributeError('Must be positive lenght.')
        self._colonne = colonne
        self._ligne = ligne
        self.grille = bytearray(ligne * colonne)

    def case(self, x: int, y: int) -> int:
        """
        Renvoie la valeur d'une case de coord (x, y)
        :param x: abscisse
        :param y: ordonnee
        :return: la valeur
        """
        # return self.grille[(self._ligne - y) * self._colonne + x - 1]
        return self.grille[y * self._colonne + x]

    def show(self, indication_coord: bool = None) -> None:
        """
        Affiche la grille de jeu
        :param indication_coord: si on veut les coordonnee sur les côtés
        """
        res = ''
        if indication_coord:
            res += '   '
            for i in range(self._colonne):
                res += f'{i} '
            res += '\n'

        for j in range(self._ligne):
            res += f"{j if indication_coord else ''} |"
            for i in range(self._colonne):
                res += f'{self.case(i, j)}|'
            res += f" {j if indication_coord else ''}\n"

        if indication_coord:
            res += '   '
            for i in range(self._colonne):
                res += f'{i} '
            res += '\n'

        print(res, end='')

    def add(self, x: int, y: int, val: int) -> None:
        """
        Modifie la valeur de la grille au coordonnee (x, y)
        :param x: abscisse
        :param y: ordonnee
        :param val: valeur
        """
        self.grille[y * self._colonne + x] = val

    def est_gagnant(self, x: int, y: int, e: int) -> int:
        """
        Renvoie si le plateau est gagnant autour la position (x, y) pour un joueur d'une equipe e.
            0: partie non gagnante
            1: rouge gagnant
            2: jaune gagnant

        :param e: equipe
        :param x: colonne
        :param y: ligne
        :return: 0, 1 ou 2 comme dit plus haut
        """
        # ligne
        k = -1
        for i in range(x, -1, -1):
            if self.case(i, y) != e: break
            k += 1
        for i in range(x, self._colonne):
            if self.case(i, y) != e: break
            k += 1
        if k >= 4: return e
        # colonne
        k = -1
        for i in range(y, -1, -1):
            if self.case(x, i) != e: break
            k += 1
        for i in range(y, self._ligne):
            if self.case(x, i) != e: break
            k += 1
        if k >= 4: return e

        # diagonale y = x
        k = -1
        for i, j in zip(range(x, -1, -1), range(y, self._ligne)):
            if self.case(i, j) != e: break
            k += 1
        for i, j in zip(range(x, self._colonne), range(y, -1, -1)):
            if self.case(i, j) != e: break
            k += 1
        if k >= 4: return e

        # diagonale y = -x
        k = -1
        for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
            if self.case(i, j) != e: break
            k += 1
        for i, j in zip(range(x, self._colonne), range(y, self._ligne)):
            if self.case(i, j) != e: break
            k += 1
        if k >= 4: return e

        return 0

    def est_nulle(self):
        for i in self.grille:
            if i == 0: return False
        return True

    @property
    def ligne(self):
        return self._ligne

    @property
    def colonne(self):
        return self._colonne


if __name__ == '__main__':
    p = Plateau(7, 5)
    p.show(indication_coord=True)
    print(p.est_gagnant(4, 1, 1))

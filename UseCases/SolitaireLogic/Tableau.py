from UseCases.SolitaireLogic.columnOfTableau import ColumnOfTableau


class Tableau:
    def __init__(self):
        self.columns = [ColumnOfTableau() for i in range(7)]


from UseCases.SolitaireLogic.columnOfTableau import ColumnOfTableau


class Tableau:
    def __init__(self):
        self.columns = [ColumnOfTableau() for i in range(7)]

    def __str__(self):
        result = ""
        for i in range(len(self.columns)):
            result += f"Column {i}: \n {str(self.columns[i])}\n"
        return result

    def popCardFrom(self, column, index):
        self.columns[column].pop(index)


from enum import Enum


class Marks(Enum):
    Clovers = 0
    Diamonds = 1
    Spades = 2
    Hearts = 3

    @staticmethod
    def getAllValues():
        return f"{Marks.Clovers.value}, {Marks.Diamonds.value}, {Marks.Spades.value}, {Marks.Hearts.value}"


Ranks = ["A"] + [str(i) for i in range(2,11,1)] + ["J", "Q", "K"]

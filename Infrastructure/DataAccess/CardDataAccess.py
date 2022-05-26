from Data.CardData import Ranks, Marks
from copy import deepcopy


class CardInfo:
    ranks = Ranks
    reverseRanksSequence = deepcopy(Ranks)[::-1]
    marks = Marks

from copy import deepcopy
class Card:
    def __init__(self, rank, mark, isStatsVisible=True):
        self.rank = rank
        self.mark = mark
        self.isStatsVisible = isStatsVisible

    def flip(self):
        self.isStatsVisible = not self.isStatsVisible

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        self._mark = value

    def __str__(self):
        return f"{self.rank} | {str(self.mark)}"

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result
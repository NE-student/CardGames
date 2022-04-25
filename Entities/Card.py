class Card:
    def __init__(self, rank, mark):
        self.rank = rank
        self.mark = mark
        self.isStatsVisible = True

    def flip(self):
        self.isStatsVisible = not self.StatsVisible

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

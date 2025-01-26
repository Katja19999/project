class Result:

    def __init__(self, stats=('enemies killed', )):

        self.statistics = dict(zip(stats, [0] * len(stats)))

    def get(self, item):
        return str(self.statistics[item])

    def update(self, stat, value):
        self.statistics[stat] += value

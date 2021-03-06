from datetime import date


class ContributionsMap:
    width = 9
    heartmap = [
        [0, 0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0],
    ]

    startdate = date(year=2020, month=1, day=26)

    def get_count_by_date(self, date):
        delta = date - self.startdate
        row = delta.days % 7
        column = int(delta.days / 7) % self.width

        return self.heartmap[row][column]

class User:

    def __init__(self, rank: int = 8):
        self.rank = rank
        self.progress = 0

    def inc_progress(self, task_level):
        incr: int = task_level - self.rank
        self.progress += 10 * (incr * incr)


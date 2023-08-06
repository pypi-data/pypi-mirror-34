class DBConnectionRecorder(object):
    def __init__(self):
        self.total = 0
        self.active = 0

    def up_total(self):
        self.total += 1

    def down_total(self):
        self.total -= 1

    def up_active(self):
        self.active += 1

    def down_active(self):
        self.active -= 1

    def record(self):
        return (
            self.total,
            self.active,
        )

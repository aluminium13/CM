count = 0

class Task:
    def __init__(self):
        global count
        count += 1
        self.id = count
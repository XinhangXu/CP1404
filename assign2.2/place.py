"""

"""

class Place:
    def __init__(self, name, country, priority, status):
        self.name = name
        self.country = country
        self.priority = priority
        self.status = status

    def mark_place(self, status):
        self.status = status

    def __str__(self):
        return "{} in {}, priority {}, {}".format(self.name, self.country, self.priority, self.status)



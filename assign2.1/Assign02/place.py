# Create Place class in this file


class Place:
    def __init__(self, city="", country="", priority=0, status=""):
        self.title = city
        self.author = country
        self.pages = priority
        self.status = status


def mark_as_visited(self, status):
    # marks place as visited
    if status == "n":
        self.status = "n"
        return True
    elif status == "v":
        return False


def __str__(self):
    """Outputs in the format mentioned in the document"""
    return "{} in {}, priority {}.".format(self.city, self.country, self.priority)
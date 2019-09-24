class Place:
    def __init__(self, city="", country="", priority=0, status=""):
                self.city = city
                self.country = country
                self.priority = priority
                self.status = status

    def mark_as_complete(self,status):
        # marks place as completed
        if status == "n":
            self.status = "v"
            return True
        elif status == "v":
            return False


    def __str__(self):
        # format
        return "{} in {}, priority {}.".format(self.city, self.country, self.priority)